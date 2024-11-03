.. _data-retrieval-chapter:

==============
数据检索
==============

**Data retrieval**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中,您将了解有关 **SELECT** 查询的更多信息,包括如何检索特定行以及如何对输出进行排序。

    .. md-tab-item:: 英文

        In this chapter, you will learn more about **SELECT** queries, including how to retrieve specific rows and how to sort the output.


本章中使用的表
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中,我们将使用 **simple_books** 和 **simple_authors** 表。顾名思义,这些是我们将在本书后面使用的其他表的小型简化版本,数据涉及书籍及其作者。您可以在 :ref:`附录 A <appendix-a>` 中阅读这些表的完整解释,但现在我们建议您仅使用 **SELECT** 查询来查看这两个表中的所有数据。以下是一个您可以用于此目的的互动工具：

        .. activecode:: data_retrieval_example_tables  
            :language: sql  
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books;

        请记住,在上一章中,您可以使用 **SELECT** \* 来检索所有列,或者可以指定您想要的列：

        .. code:: sql

            SELECT author, title FROM simple_books;

    .. md-tab-item:: 英文

        We will be working with the **simple_books** and **simple_authors** tables for this chapter.  As the names suggest, these are smaller, simplified versions of other tables we will work with later in the book, and the data concerns books and their authors.  You can read a full explanation of these tables in :ref:`Appendix A <appendix-a>`, but for now we recommend simply using a **SELECT** query to view all of the data in these two tables.  Here is an interactive tool you can use for that purpose:

        .. activecode:: data_retrieval_example_tables
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books;

        Remember from the previous chapter that you can **SELECT** \* to retrieve all columns, or you can specify the columns you want:

        .. code:: sql

            SELECT author, title FROM simple_books;


.. index:: WHERE

过滤行: WHERE 子句
::::::::::::::::::::::::::::::::

**Filtering rows: the WHERE clause**

.. md-tab-set::

    .. md-tab-item:: 中文

        从表中检索所有数据是有用的,但通常不是我们想要的,特别是如果表非常大(而且表可以变得非常非常大！)。要查看仅部分行,我们在查询中包含 **WHERE** 子句。**WHERE** 子句由关键字 **WHERE** 及其后跟的 *表达式* 组成,该表达式的值为真或假(布尔表达式) [#]_。**WHERE** 子句位于 **FROM** 子句之后。表达式将在 :numref:`第 {number} 章 <expressions-chapter>` 中更详细地讨论,但现在让我们看看一些简单的示例：

        .. activecode:: data_retrieval_example_where  
            :language: sql  
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books WHERE author = 'Isabel Allende';

            SELECT author, title, genre
            FROM simple_books
            WHERE publication_year > 1999;

            SELECT birth, death
            FROM simple_authors
            WHERE name = 'Ralph Ellison';

        请注意, SQL 中的字符串字面量用单引号括起来,而不是双引号。双引号在 SQL 中用于不同的目的,我们将在 :numref:`第 {number} 章 <joins-chapter>` 中看到。

        查询可以返回零、一或多行。如果没有行匹配 **WHERE** 条件,则返回零行(尝试将以下内容粘贴到上面的一个互动工具中)：

        .. code:: sql

            SELECT * FROM simple_books WHERE genre = 'romance';

    .. md-tab-item:: 英文

        Retrieving all of the data from a table is useful, but often not what we want, especially if the table is very large (and tables can get very, very large!)  To see just a subset of rows, we include a **WHERE** clause in our query.  The **WHERE** clause consists of the keyword **WHERE** followed by an *expression* that evaluates to true or false (a Boolean expression). [#]_  The **WHERE** clause is placed after the **FROM** clause.  Expressions are discussed more in :numref:`Chapter {number} <expressions-chapter>`, but for now, let's see some simple examples:

        .. activecode:: data_retrieval_example_where
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books WHERE author = 'Isabel Allende';

            SELECT author, title, genre
            FROM simple_books
            WHERE publication_year > 1999;

            SELECT birth, death
            FROM simple_authors
            WHERE name = 'Ralph Ellison';

        Note that character string literals in SQL are enclosed with single quotes - not double quotes.  Double quotes are used in SQL for a different purpose, which we'll see in :numref:`Chapter {number} <joins-chapter>`.

        Queries can return zero, one, or many rows.  If no rows match the **WHERE** condition, zero rows are returned (try pasting this in one of the interactive tools above):

        .. code:: sql

            SELECT * FROM simple_books WHERE genre = 'romance';


.. index:: ORDER BY, DESC, ASC

排序数据：ORDER BY 子句
::::::::::::::::::::::::::::::::::

**Ordering data: the ORDER BY clause**

.. md-tab-set::

    .. md-tab-item:: 中文

        关于关系数据库,有一个令人惊讶的事实是,表中的行不一定按任何特定的方式排序。实际上,关系数据库管理系统(RDBMS)可以以最方便或最高效的方式存储数据,并以最方便的方式检索数据。例如,在许多 RDBMS 中,数据可能最初按照添加到表中的顺序排列,但随后的数据修改语句会导致数据重新排序。

        SQL 提供了一种机制,可以根据我们希望的任何标准对行进行排序。这是通过 **ORDER BY** 子句实现的,该子句始终位于任何查询的最后。关键短语 **ORDER BY** 后跟一个以逗号分隔的表达式列表,这些表达式必须能够评估为某种可以排序的类型：数字、字符串、日期等。默认情况下,数字按从小到大的顺序排序,日期按从早到晚的顺序排序。字符字符串则稍微复杂,因为不同的数据库以不同的方式对其排序。[#]_ 我们使用的方言 SQLite 默认采用基于 `ASCII <https://en.wikipedia.org/wiki/ASCII>`_ 值的 `lexicographic ordering <https://en.wikipedia.org/wiki/Lexicographic_order>`_。

        以下是一些简单的查询供您尝试：

        .. activecode:: data_retrieval_example_order_by  
            :language: sql  
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books ORDER BY publication_year;

            SELECT * FROM simple_authors ORDER BY birth;

        排序最初是使用 **ORDER BY** 关键字后面的第一个表达式进行应用。如果根据第一个表达式有两个行相等,并且 **ORDER BY** 子句中有其他表达式,则下一个表达式会应用于具有第一个表达式相等值的行组,以此类推。例如,假设您正在为图书馆或书店组织书籍,其中书籍按类别分组,然后按标题字母排序。您可以编写以下查询来帮助完成此任务：

        .. code:: sql

            SELECT author, title, genre
            FROM simple_books
            ORDER BY genre, title;

        也可以使用 **DESC** (“降序”)关键字反转任何或所有标准的排序。 (您也可以使用 **ASC** 表示“升序”,但由于这是默认值,通常会省略。)如果我们想查看按时间从最近到最久的所有书籍,可以写：

        .. code:: sql

            SELECT * FROM simple_books ORDER BY publication_year DESC;

    .. md-tab-item:: 英文

        One surprising fact about relational databases is that the rows in a table are not necessarily ordered in any particular fashion.  In fact, relational DBMSes (RDBMSes) are permitted to store data in whatever fashion is most convenient or efficient, as well as to retrieve data however is most convenient.  For example, in many RDBMSes, data may be initially in the order in which it was added to the table, but a subsequent data modification statement results in the data being re-ordered.

        SQL provides a mechanism by which we can put rows in order by whatever criteria we wish.  This is accomplished via the **ORDER BY** clause, which always comes last in any query.  The key phrase **ORDER BY** is followed by a comma-separated list of expressions, which must evaluate to some type that can be put in order: numbers, character strings, dates, etc.  By default, numbers are sorted from smallest to largest, and dates from earliest to latest.  Character strings are a bit trickier, because different databases order them differently. [#]_ SQLite, the dialect we are using, defaults to `lexicographic ordering <https://en.wikipedia.org/wiki/Lexicographic_order>`_ based on `ASCII <https://en.wikipedia.org/wiki/ASCII>`_ values.

        Here are some simple queries to try:

        .. activecode:: data_retrieval_example_order_by
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books ORDER BY publication_year;

            SELECT * FROM simple_authors ORDER BY birth;


        Ordering is initially applied using the first expression after the **ORDER BY** keyword.  If any two rows are equal according to that first expression, and there are additional expressions in the **ORDER BY** clause, the next expression is then applied to groups of rows that have equal values for the first expression, and so forth.  For example, suppose you are organizing books for a library or bookstore where books are grouped by genre and then alphabetized by title.  You could write the following query to help with this task:

        .. code:: sql

            SELECT author, title, genre
            FROM simple_books
            ORDER BY genre, title;

        It is also possible to reverse the ordering for any or all of the criteria using the **DESC** ("descending") keyword.  (You can also use **ASC** for "ascending", but, as that is the default, it is usually omitted.)  If we want to see all books listed from most recent to least recent, we can write:

        .. code:: sql

            SELECT * FROM simple_books ORDER BY publication_year DESC;


.. index:: DISTINCT, uniqueness

检索唯一行：DISTINCT 关键字
::::::::::::::::::::::::::::::::::::::::::::

**Retrieving unique rows: the DISTINCT keyword**

.. md-tab-set::

    .. md-tab-item:: 中文

        正如我们将在后面的章节中看到的,通常的好做法是设置数据库表,使得表中的每条记录都是唯一的;也就是说,对于每一行,表中不会有其他行在每一列中包含完全相同的数据。

        然而,查询 **SELECT** 表的某些列时,结果很容易出现重复项;这可能是期望的,也可能不是。假设您想浏览我们数据库中某些特定类型的书籍,但您不确定数据库将书籍归入哪些类型——也就是说,您需要确定给定数据的有效选择。

        您可以简单地运行以下查询：

        .. activecode:: data_retrieval_example_distinct  
            :language: sql  
            :dburl: /_static/textbook.sqlite3

            SELECT genre FROM simple_books;

        对于这小部分书籍来说,这可能是可以的——虽然有重复值,但我们可以很快得出唯一的集合。然而,真正的书籍数据库可能包含成千上万本书。您不会想要浏览那么多行来发现可能的书籍类型！

        SQL 提供了一个关键字 **DISTINCT**,可以在 **SELECT** 关键字后添加,告诉 SQL 我们只想要唯一的结果,如果有重复项,则应将其丢弃。这将给我们所需的结果,即我们可以选择的唯一类型集合：

        .. code:: sql

            SELECT DISTINCT genre FROM simple_books;

    .. md-tab-item:: 英文

        As we will see in later chapters, it is usually good practice to set up database tables in such as way that each record in the table is unique; that is, for each row, there will be no other row in the table that contains exactly the same data in every column.

        However, queries that **SELECT** a subset of the columns of a table can easily end up with duplicate results; this may or may not be desired.  Suppose you were interested in browsing the books in our database for particular genres of books, but you weren't sure what genres the database puts books into - that is, you need to determine what would be valid choices given the data.

        You could simply run the query:

        .. activecode:: data_retrieval_example_distinct
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT genre FROM simple_books;

        For this small collection of books, that would probably be fine - there are duplicate values, but we can pretty quickly come up with a unique set.  However, a real database of books could contain many thousands of books.  You wouldn't want to browse that many rows to discover the possible genres!

        SQL provides a keyword, **DISTINCT**, that can be added after the **SELECT** keyword and tells SQL that we only want unique results, and if there are duplicates, it should discard them.  This will give us the desired result, a unique set of genres that we can choose from:

        .. code:: sql

            SELECT DISTINCT genre FROM simple_books;


自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含一些简单的练习,使用上文提到的 **simple_books** 和 **simple_authors** 表。如果您遇到困难,可以点击练习下方的“显示答案”按钮查看正确答案。

        - 修改下面的 SQL 语句,仅检索作者姓名。

          .. code:: sql

              SELECT * FROM simple_authors;

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT name FROM simple_authors;


        - 编写查询以查找所有科幻类书籍。

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books WHERE genre = 'science fiction';


        - 编写查询以查找书籍 *Bodega Dreams* 的出版年份和作者。

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT publication_year, author
                FROM simple_books
                WHERE title = 'Bodega Dreams';


        - 编写查询以查找所有在1950年前出版的书籍。

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books WHERE publication_year < 1950;

        - 编写查询以按书名排序获取书籍。

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books ORDER BY title;


        - 编写查询以获取自1980年以来出版的作者,按作者姓名排序。

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT author
                FROM simple_books
                WHERE publication_year > 1979
                ORDER BY author;


        - 编写查询以获取自1980年以来出版的书籍的唯一出版年份,按最新到最早排序。

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT DISTINCT publication_year
                FROM simple_books
                WHERE publication_year > 1979
                ORDER BY publication_year DESC;

    .. md-tab-item:: 英文

        This section contains some simple exercises using the **simple_books** and **simple_authors** tables used in the text above.  If you get stuck, click on the "Show answer" button below the exercise to see a correct answer.

        - Modify the SQL statement below to retrieve author names only.

          .. code:: sql

              SELECT * FROM simple_authors;

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name FROM simple_authors;


        - Write a query to find all books in the science fiction genre.
            ~~~~

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books WHERE genre = 'science fiction';


        - Write a query to find the publication year and author for the book *Bodega Dreams*.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT publication_year, author
                FROM simple_books
                WHERE title = 'Bodega Dreams';


        - Write a query to find all books published prior to 1950.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books WHERE publication_year < 1950;

        - Write a query to get books in order by title.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books ORDER BY title;


        - Write a query to get the authors publishing since 1980, in order by author name.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT author
                FROM simple_books
                WHERE publication_year > 1979
                ORDER BY author;


        - Write a query to get the unique publication years for the books in our database published since 1980, ordered latest to earliest.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT DISTINCT publication_year
                FROM simple_books
                WHERE publication_year > 1979
                ORDER BY publication_year DESC;




----

**Notes**

.. [#] 实际上,还有第三个可能的值 ``NULL``,它可能出现在查询的 **WHERE** 子句中使用的表达式中。 ``NULL`` 是一个复杂的话题,将在 :numref:`Chapter {number} <expressions-chapter>` 中讨论。现在,假设结果为正常的布尔值：真或假。

.. [#] There is actually a third possible value, ``NULL``, which may occur in expressions used in the **WHERE** clause of a query.  ``NULL`` is a complex topic which will be covered in :numref:`Chapter {number} <expressions-chapter>`.  For now, assume a normal Boolean result of true or false.

.. [#] 您可以通过应用 **COLLATE** 操作符来更改字符串的排序顺序。 **COLLATE** 超出了本教材的范围,并且在 SQL 的不同方言中有所不同。请查看您所使用的特定 DBMS 的文档。

.. [#] You can change the sort order for strings by applying the **COLLATE** operator. **COLLATE** is out of scope for this textbook, and varies with the dialect of SQL.  Please see the documentation for your particular DBMS.



