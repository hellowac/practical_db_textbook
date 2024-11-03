.. _advanced-sql-chapter:

===============
高级主题
===============

**Advanced topics**

.. md-tab-set::

    .. md-tab-item:: 中文

        本章简要介绍了一些未能很好融入前几章的高级 SQL 功能：视图、公共表表达式和窗口函数。这些主题并未被彻底涵盖（特别是公共表表达式和窗口函数）。希望这个介绍能够让您对 SQL 中的额外可能性有一些了解。

    .. md-tab-item:: 英文

        This chapter provides brief coverage of some advanced SQL capabilities that did not fit neatly into previous chapters: views, common table expressions, and window functions.  These topics are not thoroughly covered (particularly common table expressions and window functions).  It is hoped that this introduction will suffice to give you some understanding of the additional possibilities within SQL.

本章中使用的表
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中，我们将使用书籍数据集（包含表 **books**、 **authors** 等），其描述可在 :ref:`附录 A <appendix-a>` 中找到。

    .. md-tab-item:: 英文

        For this chapter we will be using the books dataset (with tables **books**, **authors**, etc.), a description of which can be found in :ref:`Appendix A <appendix-a>`.

.. index:: view, CREATE VIEW, DROP VIEW

视图
:::::

**Views**

.. md-tab-set::

    .. md-tab-item:: 中文

        *视图* 是一个数据库对象，充当已保存的 **SELECT** 查询，其结果可以直接像表一样被查询。数据本身并不存储；每次查询视图时，必须执行该视图所表示的查询，以确保返回最新的数据 [#]_. 视图特别适用于保存需要频繁执行的复杂查询，或者将被 SQL 技能较少的人使用的查询；查询的复杂部分可以编写一次、测试并保存，从而减少后续使用中的错误。

        要创建视图，请使用 **CREATE VIEW** 语句：

        .. activecode:: advanced_example_view
            :language: sql
            :dburl: /_static/textbook.sqlite3

            CREATE VIEW book_editions AS
            SELECT
              a.name AS author,
              b.title,
              e.publication_year,
              e.publisher,
              e.publisher_location,
              e.title AS published_title,
              e.pages,
              e.isbn10,
              e.isbn13
            FROM
              editions AS e
              JOIN books AS b ON b.book_id = e.book_id
              JOIN authors AS a ON a.author_id = b.author_id
            ;

            SELECT author, published_title, publication_year, publisher
            FROM book_editions
            WHERE title = 'The Two Towers';

        要删除视图，请使用 **DROP VIEW** 语句：

        .. code:: sql

            DROP VIEW book_editions;

    .. md-tab-item:: 英文

        A *view* is a database object that acts as a saved **SELECT** query, the result of which can be queried directly as if it were a table.  The data itself is not stored; the query that the view represents must be executed each time the view is queried, ensuring that up-to-date data is returned [#]_.  Views are particularly useful for saving complex queries that must be executed frequently, or that will be used by people with minimal SQL skills; the complex parts of the query can be written once, tested, and saved, reducing errors in later usage.

        To create a view, use the **CREATE VIEW** statement:

        .. activecode:: advanced_example_view
            :language: sql
            :dburl: /_static/textbook.sqlite3

            CREATE VIEW book_editions AS
            SELECT
              a.name AS author,
              b.title,
              e.publication_year,
              e.publisher,
              e.publisher_location,
              e.title AS published_title,
              e.pages,
              e.isbn10,
              e.isbn13
            FROM
              editions AS e
              JOIN books AS b ON b.book_id = e.book_id
              JOIN authors AS a ON a.author_id = b.author_id
            ;

            SELECT author, published_title, publication_year, publisher
            FROM book_editions
            WHERE title = 'The Two Towers';

        To remove a view, use the **DROP VIEW** statement:

        .. code:: sql

            DROP VIEW book_editions;

.. index:: common table expression, CTE, WITH

常用表表达式
::::::::::::::::::::::::

**Common table expressions**

.. md-tab-set::

    .. md-tab-item:: 中文

        与视图和子查询相关的 *公用表表达式*（CTE）允许我们定义一个 **SELECT** 查询，并为其分配一个名称以在更大 **SELECT** 查询的上下文中使用。在一个查询中可以使用多个 CTE。与视图不同，CTE 仅在其定义的查询的生命周期内存在。与子查询不同，CTE 不能与主查询相关联（除非在子查询中使用自身）。CTE 的一个常见用法是替代在主查询的 **FROM** 子句中使用的子查询；CTE 实际上将子查询移出主查询的主体，这使得阅读更容易。此外，一个 CTE 可以引用查询中之前定义的另一个 CTE，从而消除嵌套此类子查询的需要。

        CTE 在主 **SELECT** 子句之前定义，使用 **WITH** 子句：

        .. code:: sql

            WITH
              name1 AS
                (select query 1),
              name2 AS
                (select query 2),
              ...
            SELECT ...

        以下是一个示例，列出书籍及其一些附加信息：书籍获奖数量和印刷版数量（请注意，我们只有 J.R.R. 托尔金的书籍的版本信息）。我们可以简单地使用连接和分组聚合提供其中任意一条信息，但在同一查询中提供这两条信息将需要编写至少一个子查询或使用窗口函数（将在下一节讨论）。在这里，我们使用 CTE 分别完成分组和聚合步骤，然后在主查询中连接这些结果。

        .. activecode:: advanced_example_cte
            :language: sql
            :dburl: /_static/textbook.sqlite3

            WITH
              ec AS
                (SELECT book_id, COUNT(*) AS count
                FROM editions
                GROUP BY book_id),
              ac AS
                (SELECT b.book_id, COUNT(ba.book_id) AS count
                FROM
                  books AS b
                  LEFT JOIN books_awards AS ba ON b.book_id = ba.book_id
                GROUP BY b.book_id)
            SELECT
              au.name AS author,
              ac.count AS "awards won",
              ec.count AS "editions in print",
              b.title
            FROM
              authors AS au
              JOIN books AS b ON b.author_id = au.author_id
              JOIN ac ON ac.book_id = b.book_id
              LEFT JOIN ec ON ec.book_id = b.book_id
            ;

    .. md-tab-item:: 英文

        Related to both views and subqueries, *common table expressions* (CTEs) let us define a **SELECT** query and assign it a name for use within the context of a larger **SELECT** query.  Multiple CTEs may be used within a query.  Unlike views, CTEs only exist for the lifetime of the query in which they are defined.  Unlike subqueries, CTEs may not be correlated with the main query (unless used itself in a subquery).  A common use of CTEs is in place of subqueries used in the **FROM** clause of the main query; the CTE effectively moves the subquery out of the body of the main query, which makes it easier to read.  In addition, one CTE can refer to another CTE defined earlier in the query, which eliminates the need to nest subqueries of this type.

        CTEs are defined prior to the main **SELECT** clause, using a **WITH** clause:

        .. code:: sql

            WITH
              name1 AS
                (select query 1),
              name2 AS
                (select query 2),
              ...
            SELECT ...

        Here is an example listing books along with some additional pieces of information: the number of awards the book has won, and the number of printed editions of the book (keeping in mind that we only have edition information for books by J.R.R. Tolkien).  We could easily provide either one of these pieces of information simply using joins and grouping and aggregation, but providing both in the same query would require writing at least one subquery or using window functions (which are discussed in the next section).  Here we use CTEs to do our grouping and aggregation steps separately, then we join those results in the main query.

        .. activecode:: advanced_example_cte
            :language: sql
            :dburl: /_static/textbook.sqlite3

            WITH
              ec AS
                (SELECT book_id, COUNT(*) AS count
                FROM editions
                GROUP BY book_id),
              ac AS
                (SELECT b.book_id, COUNT(ba.book_id) AS count
                FROM
                  books AS b
                  LEFT JOIN books_awards AS ba ON b.book_id = ba.book_id
                GROUP BY b.book_id)
            SELECT
              au.name AS author,
              ac.count AS "awards won",
              ec.count AS "editions in print",
              b.title
            FROM
              authors AS au
              JOIN books AS b ON b.author_id = au.author_id
              JOIN ac ON ac.book_id = b.book_id
              LEFT JOIN ec ON ec.book_id = b.book_id
            ;

.. index:: window function, PARTITION BY

窗口函数
::::::::::::::::

**Window functions**

.. md-tab-set::

    .. md-tab-item:: 中文

        正如我们在 :numref:`Chapter {number} <grouping-chapter>` 中看到的，分组和聚合使我们能够报告有关数据组的聚合统计信息，以及与该组共同的属性（通常是我们用于分组的属性）。然而，组中的个别元素并不可见。*窗口函数* 提供了一种机制，可以在报告与某些数据分组相关的信息的同时列出所有个别行。一般而言，所有聚合函数都可作为窗口函数使用，还有一些额外的函数可以将行与其在组中的成员关系（例如，根据某种排序的组内排名）关联起来。

        作为一个例子，假设我们希望列出所有书籍，以及同一作者的书籍数量和该书在作者作品中的序号，并按出版年份排序（例如，这是作者的第一本、第二本还是第三本书？）。我们可以使用窗口函数实现这一点：

        .. activecode:: advanced_example_window
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
              a.name AS author,
              COUNT(*) OVER
                (PARTITION BY b.author_id)
                AS author_count,
              ROW_NUMBER() OVER
                (PARTITION BY b.author_id ORDER BY b.publication_year)
                AS book_rank,
              b.title,
              b.publication_year
            FROM
              authors AS a
              JOIN books AS b ON b.author_id = a.author_id
            ORDER BY a.name, book_rank;

        请注意，窗口计算发生在任何 **WHERE** 条件应用之后，甚至在分组和 **HAVING** 条件应用之后。这使得窗口函数在应用于已分组数据时非常有用，但这也意味着您不能对窗口函数的结果本身应用 **WHERE** 或 **HAVING** 条件。

        窗口函数还有许多额外选项，允许进行相当复杂的处理，但我们在这里不做详细讨论。

    .. md-tab-item:: 英文

        As we saw in :numref:`Chapter {number} <grouping-chapter>`, grouping and aggregation let us report aggregate statistics on groups of data, along with attributes common to the group (typically, attributes that we grouped by).  However, the individual elements of the group are not visible.  *Window functions* provide a mechanism for reporting information related to some grouping of data while also listing all individual rows.  In general, all aggregate functions are available as window functions, and there are additional functions that relate a row to its membership in the group (such as its rank within the group according to some ordering).

        As an example, suppose we wish to list all books, along with the number of books by the same author, and the ordinal number of the book as part of the author's body of work, in order by publication year (e.g., was this the author's first, second, or third book?).  We can do this with window functions:

        .. activecode:: advanced_example_window
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
              a.name AS author,
              COUNT(*) OVER
                (PARTITION BY b.author_id)
                AS author_count,
              ROW_NUMBER() OVER
                (PARTITION BY b.author_id ORDER BY b.publication_year)
                AS book_rank,
              b.title,
              b.publication_year
            FROM
              authors AS a
              JOIN books AS b ON b.author_id = a.author_id
            ORDER BY a.name, book_rank;

        Note that windowing occurs *after* application of any **WHERE** conditions, and even after grouping and application of **HAVING** conditions.  This makes window functions useful in application to already grouped data, for example, but it also means that you cannot apply **WHERE** or **HAVING** conditions to the window function result itself.

        Window functions have a number of additional options allowing for fairly complex processing, which we do not cover here.





----

**Notes**

.. [#] 一些数据库还提供 *物化视图*，它们存储实际数据；当执行视图查询所需时间过长时使用这种视图。这种视图会变得过时，必须定期刷新。

.. [#] Some databases also provide *materialized views*, which store actual data; these are used when executing the query for a view would take too long.  Such views do become out of date and must be refreshed periodically.


