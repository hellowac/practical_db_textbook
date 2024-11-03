.. _sets-chapter:

==============
集合运算
==============

**Set operations**

.. index:: set operation - SQL

.. md-tab-set::

    .. md-tab-item:: 中文

        关系数据库理论基于数学集合理论。尽管关系数据库的实现因某些重要方面偏离了理论，但集合的概念仍然很重要。在本章中，我们将探讨 SQL 中可用的三种集合操作。

    .. md-tab-item:: 英文

        Relational database theory is based on mathematical set theory.  Even though relational database implementations stray from the theory in some important regards, the notion of sets remains important.  In this chapter, we examine the three set operations available to us in SQL.

本章中使用的表
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中，我们将使用书籍数据集（表 **books**、**authors** 等），该数据集在 :ref:`附录 A <appendix-a>` 中进行了描述。

    .. md-tab-item:: 英文

        For this chapter we will be using the books dataset (tables **books**, **authors**, etc.), which is described in :ref:`Appendix A <appendix-a>`.

.. index:: set; defined

集合复习
::::::::::::::

**Sets refresher**

.. md-tab-set::

    .. md-tab-item:: 中文

        如果您已经熟悉集合及其基本运算（并集、交集和集合差），那么可以跳过本节。否则，请继续阅读一些非常基础的背景知识。

        *集合* 是一个数学对象，表示一组不同的值。对于给定的集合和任何值，我们可以询问该集合是否包含该值。集合可以通过某些共同属性来定义，或者简单地列出集合中的所有值。例如，在下图中，蓝色圆圈（包括重叠部分）表示一个包含数字 0、2、4、6、8 和 10 的集合。更简洁地说，这个集合包含 0 到 10 之间的 2 的倍数。该图还包含一个黄色圆圈，包含 0 到 10 之间的 3 的倍数。

        .. figure:: venn_diagram.svg

            说明集合运算的维恩图。左侧（蓝色）圆圈包含范围 [0, 10] 内的 2 的倍数。右侧（黄色）圆圈包含相同范围内的 3 的倍数。

        这种类型的图称为维恩图，常用于说明集合及其运算。我们将用它来讨论集合上的三种二元运算：*并集*、*交集* 和 *集合差*。

        两个集合的 **并集** 是另一个集合： **该集合包含在任一集合中的所有值**。在上面的图中，两个集合的并集包含值 0、2、3、4、6、8、9 和 10。在图中，这些是包含在任一圆圈中的所有数字。注意，我们不重复值；即使 6 在两个集合中，并集也不会包含两次 6。一个数字要么在集合中出现一次，要么根本不在集合中。值的并集与布尔 **OR** 运算符有关：这两个集合的并集包含 0 到 10 之间的整数，它们是 2 的倍数 或 3 的倍数。

        两个集合的 **交集** 也是一个集合，这次只 **包含在两个原始集合中都出现的值** 。在上面的图中，交集由两个圆圈之间的重叠部分表示，包含值 0 和 6。交集与布尔 **AND** 操作有关；这两个集合的交集包含 0 到 10 之间的整数，它们是 2 的倍数 并且 是 3 的倍数。

        虽然并集和交集是交换的——参与运算的集合可以互换，结果相同——但 **集合差** 却不是。在集合差中，您是 **将一个集合“减去”另一个集合** ，以获得一个新集合。结果是第一个集合中的所有值，排除第二个集合中也包含的任何值。上图显示了我们可以使用这两个集合获得的两种可能的集合差。这是圆圈中位于交集外的部分。例如，如果我们将 3 的倍数集合从 2 的倍数集合中减去，我们会得到左侧圆圈中不在右侧圆圈中的数字，即值 2、4、8 和 10。集合差并不直接对应于基本布尔运算，但我们可以使用 **NOT** 和 **AND** 来近似集合差：上面的集合差（2 的倍数减去 3 的倍数）是 0 到 10（含）之间的整数集合，它们是 2 的倍数 并且 不是 3 的倍数。

        从这个简单的例子中，想象集合在数学和计算机科学中所有令人惊叹的应用可能会很困难。然而，集合理论是一个非常强大的工具。正如我们将在 :numref:`Part {number} <relational-theory-part>` 中讨论的那样，关系数据库是将集合理论应用于数据管理问题的结果。

    .. md-tab-item:: 英文

        If you are already familiar with sets, and with basic operations on sets (union, intersection, and set difference), then you can skip this section.  Otherwise, please continue reading for some very basic background.

        A *set* is a mathematical object that represents a collection of distinct values.  For a given set and any value, we can ask whether or not the set contains the value.  Sets can be defined by some property that values have in common, or simply by listing all of the values in the set.  For example, in the figure below, the blue circle (including the overlapping portion) represents a set containing the numbers 0, 2, 4, 6, 8, and 10.  More succinctly, this set contains the multiples of 2 between 0 and 10.  The figure also contains a yellow circle containing the multiples of 3 between 0 and 10.

        .. figure:: venn_diagram.svg

            A Venn diagram illustrating set operations.  The left (blue) circle contains multiples of 2 in the range [0, 10].  The right (yellow) circle contains multiples of 3 in the same range.

        This type of diagram is known as a Venn diagram, and it is frequently used to illustrate sets and operations on them.  We will use it to discuss three binary operations on sets: *union*, *intersection*, and *set difference*.

        The union of two sets is another set: the set containing all values that are in either set.  In the diagram above, the union of the two sets contains the values 0, 2, 3, 4, 6, 8, 9, and 10.  In the diagram, this is every number that is contained in either circle.  Note that we do not duplicate values; even though 6 is in both sets, the union of the sets does not contain 6 twice.  A number is either in the set once, or it is not in the set at all.  A union of values is related to the Boolean **OR** operator: the union of these two sets contains integers between 0 and 10 which are multiples of 2 OR multiples of 3.

        The intersection of two sets is again a set, this time containing only values which appear in both of the original sets.  In the diagram above, the intersection is represented by the overlap between the two circles, containing the values 0 and 6.  Intersection is related to the Boolean **AND** operation; the intersection of these two sets contains integers between 0 and 10 which are multiples of 2 AND multiples of 3.

        While union and intersection are commutative - the sets involved in an operation can be exchanged and get the same result - set difference is not.  In set difference, you are "subtracting" one set from another to obtain a new set.  The result is all values in the first set excluding any values also in the second set.  The diagram above shows the two possible set differences we can obtain using our two sets.  These are the portions of the circles that are outside the intersection.  For example, if we subtract the set of multiples of 3 from the set of multiples of 2, we get the numbers in the left circle which are not in the right circle, that is, the values 2, 4, 8, and 10.  Set difference does not correspond directly to a basic Boolean operation, but we can approximate set difference using **NOT** and **AND**:  the set difference above (multiples of 2 minus multiples of 3) is the set of integers between 0 and 10 inclusive which are multiples of 2 AND NOT multiples of 3.

        It may be difficult to imagine all of the amazing applications of sets in both mathematics and computer science from this simple example.  However, set theory is a very powerful tool.  As we will discuss in :numref:`Part {number} <relational-theory-part>`, relational databases resulted from the application of set theory to the problems of data management.

.. index:: multiset

表作为集合
::::::::::::::

**Tables as sets**

.. md-tab-set::

    .. md-tab-item:: 中文

        在数学上，集合是不同值的集合。在关系数据库的最初构思中，表和数据检索查询的结果被视为真实的集合；也就是说，行的集合中没有两行是完全相同的。出于性能考虑，SQL 数据库允许在表中以及查询结果中存在重复行。例如，如果我们运行以下查询，我们会得到一些重复的行。

        .. code:: sql

            SELECT publication_year FROM books;

        在 SQL 中，用来描述表和查询结果的术语是 *多重集合* （multiset）。多重集合是来自同一值域的值的集合，但值可以在集合中出现多次。这种实际关系数据库与理论之间的差异导致了一些复杂情况，正如我们将很快看到的那样。

        SQL 支持的三种基本集合操作是并集、交集和集合差。

    .. md-tab-item:: 英文

        Mathematically, sets are collections of distinct values.  In the original conception of relational databases, tables and the results of data retrieval queries were intended to be true sets; that is, collections of rows, with no two rows being exactly the same.  For performance reasons, SQL databases allow duplicate rows in both tables and in the results of queries.  For example, if we run the following query, we get some duplicate rows.

        .. code:: sql

            SELECT publication_year FROM books;

        The term used to describe tables and query results in SQL is *multiset*.  A multiset is a collection of values from the same domain of values, but values can appear more than once in the set.  This difference between relational databases in practice and in theory results in some complications, as we will soon see.

        The three basic set operations that SQL supports are union, intersection, and set difference.

.. index:: UNION, set operation - SQL; union

并集
-----

**Union**

.. md-tab-set::

    .. md-tab-item:: 中文

        集合并集在 SQL 中是对两个 **SELECT** 查询的操作。查询的写法是一个 **SELECT** 查询，后跟关键字 **UNION**，再后跟另一个 **SELECT** 查询。这两个查询的结果必须在列数上兼容，并且列的数据类型应该兼容。查询的并集包含从任一查询返回的每个不同的行。作为一个非常简单的例子，我们可以用 **UNION** 查询来代替布尔 **OR** 条件。比较以下两个查询：

        .. activecode:: sets_example_aggregate
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM books WHERE title LIKE 'W%'
            UNION
            SELECT * FROM books WHERE publication_year = 1995;

            SELECT *
            FROM books
            WHERE title LIKE 'W%'
            OR publication_year = 1995;

        在这种情况下，两个查询返回相同的结果。然而，它们之间有一个细微的区别。当我们使用 **UNION** 时，SQL 将其视为真正的集合操作，并返回一组不同的行——任何重复的行都会被移除。为了完全等价，我们应该在第二个查询中使用 **DISTINCT** 关键字。

        在这种情况下，没有特别的理由选择并集查询而不是 **OR** 表达式；这仅仅是用于说明。在其他场景中，例如涉及复杂条件逻辑时，**UNION** 可能是更可取的替代方案。作为一个简单的例子，考虑提供一个列来标记作者为“活着”、“已故”（给出死亡日期）或“未知”（出生和死亡日期未知）。我们可以使用 **CASE** 表达式，或者使用三个查询的 **UNION**（可以想象为前两个查询的并集，然后将结果与第三个查询进行并集）：

        .. code:: sql

            SELECT name, 'living' AS status
            FROM authors
            WHERE death IS NULL AND birth IS NOT NULL
            UNION
            SELECT name, 'died ' || death
            FROM authors
            WHERE death IS NOT NULL AND birth IS NOT NULL
            UNION
            SELECT name, 'unknown'
            FROM authors
            WHERE birth IS NULL;

            SELECT
            name,
            CASE
                WHEN death IS NULL AND birth IS NOT NULL
                THEN 'living'
                WHEN death IS NOT NULL AND birth IS NOT NULL
                THEN 'died ' || death
                WHEN birth IS NULL
                THEN 'unknown'
            END AS status
            FROM authors;

        如果你运行上述并集查询，你会看到整个查询结果的列名来自第一个 **SELECT** 查询，使用集合操作时也是如此。

        在某些情况下，**UNION** 可能是你唯一的选择——例如当你要合并来自不同表的结果时。这种情况的一个例子可能是，当一家公司希望创建一个与公司相关的所有人的电子邮件列表时：公司的数据库可能包含一个员工表、一个客户表和一个供应商表。并集查询将轻松地从这三个表创建一个邮件列表，并消除重复（因为，例如，员工也可能是客户）。

    .. md-tab-item:: 英文

        Set union in SQL is an operation on two **SELECT** queries.  The query is written as one **SELECT** query, followed by the keyword **UNION**, followed by another **SELECT** query.  The two query results must be compatible in the sense that they must both return the same number of columns, and the columns should have compatible types.  The union of the queries contains every distinct row that is returned from either query.  As a very simple example, we can use a **UNION** query in place of a Boolean **OR** condition.  Compare these two queries:

        .. activecode:: sets_example_aggregate
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM books WHERE title LIKE 'W%'
            UNION
            SELECT * FROM books WHERE publication_year = 1995;

            SELECT *
            FROM books
            WHERE title LIKE 'W%'
            OR publication_year = 1995;

        In this case, the queries return the same results.  However, there is a subtle difference between them.  When we use **UNION**, SQL treats it as a true set operation and returns a set of distinct rows - any duplicates are removed.  To be completely equivalent, we should use the **DISTINCT** keyword in the second query.

        There is no particular reason to choose a union query over the **OR** expression in this case; it is merely used for illustration.  **UNION** may be a more preferable alternative in other scenarios, such as those involving complex conditional logic.  As a simple example, consider providing a column labeling authors as "living", "dead" (giving the date of death), or "unknown" (where the birth and death dates are unknown).  We could do this with a **CASE** expression, or with a **UNION** of three queries (think of a union of the first two queries, then a union of the result with the third query):

        .. code:: sql

            SELECT name, 'living' AS status
            FROM authors
            WHERE death IS NULL AND birth IS NOT NULL
            UNION
            SELECT name, 'died ' || death
            FROM authors
            WHERE death IS NOT NULL AND birth IS NOT NULL
            UNION
            SELECT name, 'unknown'
            FROM authors
            WHERE birth IS NULL;

            SELECT
            name,
            CASE
                WHEN death IS NULL AND birth IS NOT NULL
                THEN 'living'
                WHEN death IS NOT NULL AND birth IS NOT NULL
                THEN 'died ' || death
                WHEN birth IS NULL
                THEN 'unknown'
            END AS status
            FROM authors;

        If you run the union query above, you will see that column names for the result of the whole query come from the first **SELECT** query when using set operations.

        In some cases, **UNION** may be your only choice - such as when you are combining results from different tables.  One example of this might occur when a company wishes to create an email list for everyone related to the company in some way: the company's database might contain one table for employees, another for customers, and a third for vendors  A union query would easily create one mailing list from these three tables, and eliminate duplicates (since, for example, employees might also be customers).

.. index:: UNION ALL

多重集合复杂化
#####################

**Multiset complication**

.. md-tab-set::

    .. md-tab-item:: 中文

        单独使用 **UNION** 会导致从查询结果集中移除所有重复项。在某些情况下，这可能不是所期望的行为；如果你希望保留重复记录（保留任一查询返回的所有行），只需在 **UNION** 后添加关键字 **ALL**。下面的查询将返回重复记录：

        .. code:: sql

            SELECT * FROM books WHERE title LIKE 'W%'
            UNION ALL
            SELECT * FROM books WHERE publication_year = 1995;

    .. md-tab-item:: 英文

        Used by itself, **UNION** results in the removal of all duplicates from the result set of the query.  There may be occasions when this is not the desired behavior; if you wish to retain duplicate records (keeping all rows returned by either query), simply add the keyword **ALL** after **UNION**.  The query below will result in duplicate records:

        .. code:: sql

            SELECT * FROM books WHERE title LIKE 'W%'
            UNION ALL
            SELECT * FROM books WHERE publication_year = 1995;

.. index:: INTERSECT, set operation - SQL; intersection

交集
------------

**Intersection**

.. md-tab-set::

    .. md-tab-item:: 中文

        在 SQL 中，集合交集通过关键字 **INTERSECT** 实现。使用 **INTERSECT** 的规则与使用 **UNION** 相同，但其结果仅包含在 *两个* 查询结果中都存在的每个唯一行：

        .. code:: sql

            SELECT * FROM books WHERE title LIKE 'W%'
            INTERSECT
            SELECT * FROM books WHERE publication_year = 1995;

        这个结果类似于在单个查询的 **WHERE** 子句中使用 **AND** 表达式所实现的结果：

        .. code:: sql

            SELECT DISTINCT *
            FROM books
            WHERE title LIKE 'W%'
            AND publication_year = 1995;

        然而，与 **UNION** 一样，你可以使用 **INTERSECT** 对多个表进行查询。

        SQL 标准允许在 **INTERSECT** 后使用关键字 **ALL**，但大多数数据库（包括 SQLite）不支持这种用法。

        （针对 MySQL 用户：MySQL 不实现 **INTERSECT**。）

    .. md-tab-item:: 英文

        Set intersection in SQL is accomplished by the keyword **INTERSECT**.  The rules for using **INTERSECT** are the same as for using **UNION**, but its result contains only every distinct row that is contained in *both* query results:

        .. code:: sql

            SELECT * FROM books WHERE title LIKE 'W%'
            INTERSECT
            SELECT * FROM books WHERE publication_year = 1995;

        This result is similar to that achieved by using an **AND** expression in the **WHERE** clause of a single query:

        .. code:: sql

            SELECT DISTINCT *
            FROM books
            WHERE title LIKE 'W%'
            AND publication_year = 1995;

        However, as with **UNION**, you can use **INTERSECT** to perform queries against multiple tables.

        The SQL standard allows the keyword **ALL** after **INTERSECT**, but most databases (including SQLite) do not support this usage.

        (Note for MySQL users: MySQL does not implement **INTERSECT**.)

.. index:: EXCEPT, set operation - SQL; difference

集合差集
--------------

**Set difference**

.. md-tab-set::

    .. md-tab-item:: 中文

        在 SQL 中，集合差集通过关键字 **EXCEPT** 实现。使用 **EXCEPT** 的规则与 **UNION** 和 **INTERSECT** 相同，但请注意 **EXCEPT** 不是交换的——查询的顺序很重要。下面是我们之前相同的示例，使用 **EXCEPT**：

        .. code:: sql

            SELECT * FROM books WHERE title LIKE 'W%'
            EXCEPT
            SELECT * FROM books WHERE publication_year = 1995;

        这个结果类似于在单个查询的 **WHERE** 子句中要求一个条件 **AND NOT** 另一个条件所实现的结果：

        .. code:: sql

            SELECT DISTINCT *
            FROM books
            WHERE title LIKE 'W%'
            AND NOT publication_year = 1995;

        然而，与 **UNION** 和 **INTERSECT** 一样，你可以使用 **EXCEPT** 对多个表进行查询。

        SQL 标准允许在 **EXCEPT** 后使用关键字 **ALL**，但大多数数据库（包括 SQLite）不支持这种用法。

        **EXCEPT** 操作符的一个应用是确定两个查询结果是否相同；如果你进行双向的集合差集运算，当两个查询返回相同的唯一行时，结果应该为空（重复行的计数可能会有所不同）。另一种方法是查看两个查询的并集和交集是否包含相同数量的行。

        （针对 MySQL 用户：MySQL 不实现 **EXCEPT**。）

        （针对 Oracle 用户：Oracle 使用关键字 **MINUS** 而不是 **EXCEPT**。）

    .. md-tab-item:: 英文

        Set difference in SQL is accomplished by the keyword **EXCEPT**.  The rules for using **EXCEPT** are again the same as for **UNION** and **INTERSECT**, but note that **EXCEPT** is not commutative - the order of the queries matters.  Here is our same example again, using **EXCEPT**:

        .. code:: sql

            SELECT * FROM books WHERE title LIKE 'W%'
            EXCEPT
            SELECT * FROM books WHERE publication_year = 1995;

        This result is similar to that achieved by requiring one condition **AND NOT** the other condition in the **WHERE** clause of a single query:

        .. code:: sql

            SELECT DISTINCT *
            FROM books
            WHERE title LIKE 'W%'
            AND NOT publication_year = 1995;

        However, as with **UNION** and **INTERSECT**, you can use **EXCEPT** to perform queries against multiple tables.

        The SQL standard allows the keyword **ALL** after **EXCEPT**, but most databases (including SQLite) do not support this usage.

        One application of the **EXCEPT** operator is determining if two query results are identical; if you take the set difference in both directions, your result should be empty if the two queries return the same distinct rows (there could be a difference in the counts of duplicate rows).  An alternate approach is to see if the union and intersection of the two queries contain the same count of rows.

        (Note for MySQL users: MySQL does not implement **EXCEPT**.)

        (Note for Oracle users: Oracle uses the keyword **MINUS** rather than **EXCEPT**.)

链接运算
-------------------

**Chaining operations**

.. md-tab-set::

    .. md-tab-item:: 中文

        正如我们在 **UNION** 中看到的，可以在单个查询中执行多个集合操作。对于仅涉及 **UNION** 的查询，查询的顺序并不重要，因为 **UNION** 是既交换的又结合的。仅涉及 **INTERSECT** 的查询也是如此。然而，对于涉及 **EXCEPT** 的查询，或混合集合操作的查询，情况就复杂了。**EXCEPT** 既不是交换的也不是结合的。链式混合运算符的查询在所有数据库中的表现并不相同，因此在尝试此操作时要谨慎；某些数据库允许使用括号来强制指定希望执行操作的顺序。

    .. md-tab-item:: 英文

        As we saw with **UNION**, it is possible to do more than one set operation in a single query.  For queries just involving **UNION**, the order of queries does not matter, as **UNION** is both commutative and associative.  The same is true for a query just involving **INTERSECT**.  For queries involving **EXCEPT**, or queries mixing set operations, the situation is more complicated.  **EXCEPT** is neither commutative nor associative.  Queries that chain mixed operators do not behave the same in all databases, so be cautious when attempting this; some databases allow you to use parentheses to force the order in which you want operations to be performed.



自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含一些使用书籍数据集的练习（提醒：您可以在 :ref:`附录 A <appendix-a>` 中获取所有表的完整描述）。如果您遇到困难，请单击练习下方的“显示答案”按钮以查看正确答案。回答这些问题有多种方法；请尝试使用集合操作来解决每个问题。

        - 编写查询以查找诗人艾伦·金斯堡（Allen Ginsberg）作为作者或书籍所获的所有奖项。您的输出应包含三列：奖项名称、获奖年份，以及获奖理由——书籍奖的书名或作者奖的“作品集”。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT aw.name, ba.year, bo.title AS "Awarded For"
                FROM
                awards AS aw
                JOIN books_awards AS ba ON ba.award_id = aw.award_id
                JOIN books AS bo ON bo.book_id = ba.book_id
                JOIN authors AS au ON au.author_id = bo.author_id
                WHERE au.name = 'Allen Ginsberg'
                UNION
                SELECT aw.name, aa.year, 'body of work'
                FROM
                awards AS aw
                JOIN authors_awards AS aa ON aa.award_id = aw.award_id
                JOIN authors AS au ON au.author_id = aa.author_id
                WHERE au.name = 'Allen Ginsberg';


        - 编写查询以查找曾因书籍或作者作品集而获得的奖项列表（即，奖项应同时出现在 **authors_awards** 和 **books_awards** 中）。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT * FROM awards WHERE award_id IN
                (SELECT award_id FROM books_awards)
                INTERSECT
                SELECT * FROM awards WHERE award_id IN
                (SELECT award_id FROM authors_awards)
                ;


        - 编写查询以查找获得作者奖但未获得书籍奖的作者列表。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE author_id IN
                (SELECT author_id FROM authors_awards)
                EXCEPT
                SELECT name FROM authors WHERE author_id IN
                (SELECT author_id FROM books WHERE book_id IN
                    (SELECT book_id FROM books_awards))
                ;

    .. md-tab-item:: 英文

        This section contains some exercises using the books data set (reminder: you can get full descriptions of all tables in :ref:`Appendix A <appendix-a>`).  If you get stuck, click on the "Show answer" button below the exercise to see a correct answer.  There are many ways to answer these questions; try to use a set operation to solve each.

        - Write a query to find all of the awards won by poet Allen Ginsberg, either as an author or for a book.  Your output should have three columns: the name of the award, the year of the award, and what the award was won for - the book title for book awards, or "body of work" for author awards.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT aw.name, ba.year, bo.title AS "Awarded For"
                FROM
                awards AS aw
                JOIN books_awards AS ba ON ba.award_id = aw.award_id
                JOIN books AS bo ON bo.book_id = ba.book_id
                JOIN authors AS au ON au.author_id = bo.author_id
                WHERE au.name = 'Allen Ginsberg'
                UNION
                SELECT aw.name, aa.year, 'body of work'
                FROM
                awards AS aw
                JOIN authors_awards AS aa ON aa.award_id = aw.award_id
                JOIN authors AS au ON au.author_id = aa.author_id
                WHERE au.name = 'Allen Ginsberg';


        - Write a query to find a list of awards that have been given for either books or an author's body of work (i.e., the award(s) should show up in both **authors_awards** and **books_awards**).

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM awards WHERE award_id IN
                (SELECT award_id FROM books_awards)
                INTERSECT
                SELECT * FROM awards WHERE award_id IN
                (SELECT award_id FROM authors_awards)
                ;


        - Write a query to find a list of authors who won author awards but no book awards.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE author_id IN
                (SELECT author_id FROM authors_awards)
                EXCEPT
                SELECT name FROM authors WHERE author_id IN
                (SELECT author_id FROM books WHERE book_id IN
                    (SELECT book_id FROM books_awards))
                ;






