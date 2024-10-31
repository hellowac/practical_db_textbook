.. _joins-chapter:

==========================
多个表上的查询
==========================

**Queries on multiple tables**

.. md-tab-set::

    .. md-tab-item:: 中文

        在前面的章节中，我们看到了如何从单个表中检索数据、根据不同标准过滤数据、对数据进行排序，以及使用各种表达式格式化数据。现在，我们将讨论如何在单个查询中从多个表中检索数据。例如，使用 **simple_books** 和 **simple_authors** 表，我们可能希望查看书名以及作者的姓名和出生日期。作者的姓名在两个表中都有，但书名在 **simple_books** 中，而作者的出生日期在 **simple_authors** 中。我们如何才能将这些信息汇总到一个结果中呢？本章将解释如何使用 *joins* 从多个表中检索数据，并探讨在处理多个表时出现的各种问题。

    .. md-tab-item:: 英文

        In past chapters, we saw how to retrieve data from individual tables, filter data on different criteria, order the data, and format the data with various expressions.  Now we turn to the question of how to retrieve data from more than one table in a single query.  For example, using the tables **simple_books** and **simple_authors**, we might like to see book titles together with author's name and birth date. The author's name is in both tables, but book titles are in **simple_books**, while author birth dates are in **simple_authors**.  How can we get these together in one result?  This chapter will explain how to retrieve data from multiple tables using *joins*, and explore various issues that arise when working with multiple tables.


本章中使用的表
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中，我们将使用几个表的集合，首先是一些用于说明连接的抽象表。这些抽象表在下面进行了说明，同时也可以在数据库中进行自己的实验。本章还引入了一个合成数据集，模拟二手书店的数据库，以及一个关于书籍和作者的更复杂的表集合。我们将继续使用前面章节中的 **simple_books** 和 **simple_authors** 表。新引入的表的简要说明可以在下方找到，所有数据集的完整说明可以在 :ref:`Appendix A <appendix-a>` 中找到。

        在每个新表引入时，您可能希望花一些时间对其进行 **SELECT** 查询，以了解数据的外观。理解您的数据库是关键！

    .. md-tab-item:: 英文

        We will use several collections of tables in this chapter, starting with some abstract tables used to illustrate joins.  These abstract tables are illustrated below, but are also available in the database for your own experimentation.  Also new to this chapter is a synthetic dataset simulating the database for a used book store, as well as a more complex set of tables about books and authors.  We will also continue to use the **simple_books** and **simple_authors** tables from previous chapters.  Brief explanations of newly introduced tables can be found below, and a full explanation of all of the datasets can be found in :ref:`Appendix A <appendix-a>`.

        You may wish to spend some time doing **SELECT** queries on each new table as it is introduced, to get a sense of what the data looks like.  Understanding your database is key!


.. index:: join - SQL, JOIN, join - sql; inner, join condition

简单连接
::::::::::::

**Simple joins**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们将从一个抽象示例开始，该示例包含少量数据。具体而言，我们将使用如下所示的两个表，分别命名为 **s** 和 **t**: 

        .. image:: joins1.svg
            :alt: Tables s and t

        这些数据没有实际意义，但您可能会注意到表数据暗示了一种关系:表 **s** 有一列 **sy**，包含小整数，而表 **t** 有一列 **ty**，同样包含小整数。我们希望实现的是当 **sy** 和 **ty** 列的值相同时，将表 **s** 的行与表 **t** 的行连接在一起。期望的结果如下所示:

        .. image:: joins1_result.svg
            :alt: The desired result of connecting s and t

        当一个表中的行与另一个表中的行配对时，我们称结果为表的 *连接*。以下是一个连接 **s** 和 **t** 的查询，以生成上面所示的结果:

        .. activecode:: joins_example_simple_join
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT *
            FROM
              s
              JOIN t ON sy = ty
            ;

        我们从 **FROM** 子句开始，首先是表 **s**，然后使用 **JOIN** 关键字引入表 **t**，接着是 **ON** 关键字，最后是一个布尔条件，向 SQL 解释哪些 **s** 的行与哪些 **t** 的行相匹配。 **ON** 之后的布尔条件称为 *连接条件*。连接条件总是将一个表上的表达式与另一个表上的表达式进行比较。

        要理解运行此查询时会发生什么，依次考虑 **s** 中的每一行。对于 **s** 中的每一行，查看 **t** 中的每一行并应用连接条件。如果连接条件评估为 ``True``，则通过将 **s** 的行与 **t** 的行连接起来，生成一新行，并将其添加到结果中。(这可以类比于在 Python 或 Java 等编程语言中执行嵌套的 **for** 循环；外层循环遍历 **s** 中的行，内层循环遍历 **t** 中的行。)

        例如，我们从 **s** 中的第一行开始，表示为 ``('one', 1)``。该行中 **sy** 的值为 1。现在，我们查看 **t** 中的每一行，以查找 **ty** 也等于 1 的行。 **t** 中的第一行是 ``(1, 'green')``，其 **ty** 值为 1，因此我们生成行 ``('one', 1, 1, 'green')`` 并将其添加到输出中。 **t** 中没有其他行匹配，因此我们继续查看 **s** 中的下一行 ``('two', 2)``。同样，我们考虑 **t** 中的每一行，这次寻找 **ty** 值等于 2；这次我们匹配到行 ``(2, 'blue')``，并将 ``('two', 2, 2, 'blue')`` 添加到输出中。这个过程一直持续到我们处理完 **s** 中的每一行。

        在第一个示例中，**s** 中的每一行恰好与 **t** 中的一行匹配，而 **t** 中的每一行也恰好与 **s** 中的一行匹配。如果情况并非如此，会发生什么呢？首先，考虑下面的表 **s2** 和 **t2**，其中每个表中有一行未能匹配到另一个表中的任何行:

        .. image:: joins2.svg
            :alt: Tables s2 and t2

        使用相同的等式条件连接 **s2** 和 **t2**，现在我们得到:

        .. image:: joins2_result.svg
            :alt: The join of s2 and t2

        这个结果可以通过检查 **s2** 的每一行并寻找 **t2** 中的匹配项来理解。如果没有匹配，则不会输出任何行。

        我们还可以遇到一个情况，即一个表中的多行匹配到另一个表中的某一行。这里有两个表供考虑:

        .. image:: joins3.svg
            :alt: Tables s3 and t3

        这次，**s3** 中的行 ``('two', 2)`` 匹配 **t3** 中的 *两个* 不同的行，因此我们将生成两行组合行，其中 **sy** 和 **ty** 均等于 2:

        .. image:: joins3_result.svg
            :alt: The join of s3 and t3

        表 **s2**、**t2**、**s3** 和 **t3** 也可以在上面的交互工具中访问。

        两个表可以通过多个列而不仅仅是一个列相关联。要连接它们，您可以使用复合连接条件，使用 **AND**。实际上，连接条件不必是等式(尽管通常是)；可以使用任何将一个表中的行与另一个表中的行关联的逻辑表达式。检查第一个表中的每一行并与第二个表中的每一行进行比较的概念模型依然适用。看看您能否找出以下查询将产生什么(然后在上面的交互工具中尝试):

        .. code:: sql

            SELECT *
            FROM
              s
              JOIN t ON sy = ty OR sy > ty
            ;

        **JOIN** 子句被视为 **FROM** 子句的子子句。当然，我们可以像往常一样向查询添加其他子句，例如 **WHERE** 子句:

        .. code:: sql

            SELECT *
            FROM
              s
              JOIN t ON sy = ty
            WHERE tz = 'blue';

        将 **FROM** 子句视为数据库处理查询的第一部分。结果是一些行的集合，我们可以用 **WHERE** 子句对其进行过滤，或用 **ORDER BY** 子句对其进行特定顺序排列，等等。

        关于连接还有很多内容要讨论，但在继续之前，让我们看看如何回答之前提出的问题，即希望在一个查询结果中同时获取书名和作者出生日期，使用 **simple_books** 和 **simple_authors**。解决方案如下:

        .. code:: sql

            SELECT title, author, birth
            FROM
              simple_books
              JOIN simple_authors ON author = name
            ;

        请注意，我们在 **SELECT** 子句中选择特定的列作为结果的一部分。连接条件中使用的列 **name** 是 **simple_authors** 表中包含作者名称的列。我们将此列与 **simple_books** 中的 **author** 列进行比较以进行连接，但在检索的列中不包含它；否则，我们将有相同的作者名称在两个不同的列中显示。

    .. md-tab-item:: 英文

        To start with, we will consider an abstract example with a small amount of data.  Specifically, we will work with the two tables shown below, named **s** and **t**:

        .. image:: joins1.svg
            :alt: Tables s and t

        There is no real meaning to this data, but you might notice that the table data suggests a relationship: table **s** has a column **sy** containing small integers and table **t** has a column **ty** similarly containing small integers.  What we want to accomplish is to connect rows from table **s** with rows from table **t** when the values in the **sy** and **ty** columns are the same.  The desired result looks like this:

        .. image:: joins1_result.svg
            :alt: The desired result of connecting s and t

        When rows from one table are paired with rows from another table, we call the result a *join* of the tables.  Here is a query that joins **s** and **t** to produce the result shown above:

        .. activecode:: joins_example_simple_join
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT *
            FROM
              s
              JOIN t ON sy = ty
            ;

        We start our **FROM** clause with table **s**, then use the **JOIN** keyword to bring in table **t**, followed by the **ON** keyword, and finally a Boolean condition explaining to SQL which rows from **s** go with which rows from **t**.  The Boolean condition after **ON** is known as a *join condition*.  Join conditions always compare an expression on one table with an expression on another table.

        To understand what happens when you run this query, consider each row in **s** in turn.  For each row in **s**, look at each row in **t** and apply the join condition.  If the join condition evaluates to ``True``, then make a new row by concatenating the row from **s** with the row from **t**, and add it to the result.  (This can be likened to performing nested **for** loops in a programming language like Python or Java; the outer loop is over the rows in **s**, and the inner loop is over the rows in **t**.)

        So, for example, we start by looking at the first row in **s**, which we can write as ``('one', 1)``.  The value of **sy** in this row is 1.  Now, we look at each row in **t** to see which ones have **ty** also equal to 1.  The first row in **t** is ``(1, 'green')``, which has a **ty** value of 1, so we make the row ``('one', 1, 1, 'green')`` and add it to the output.  No other rows in **t** match, so we move on to the next row in **s**, ``('two', 2)``.  Again, we consider each row in **t**, this time looking for a **ty** value equal to 2; this time we match the row ``(2, 'blue')``, and we add ``('two', 2, 2, 'blue')`` to the output.  This process continues until we have processed every row in **s**.

        In the first example, each row in **s** matched exactly one row in **t**, and each row in **t** matched exactly one row in **s**.  What happens if this is not the case?  First, consider tables **s2** and **t2** below, in which one row in each table fails to match any rows in the other table:

        .. image:: joins2.svg
            :alt: Tables s2 and t2

        Joining **s2** and **t2** using the same equality condition on columns **sy** and **ty** now gives us:

        .. image:: joins2_result.svg
            :alt: The join of s2 and t2

        This result can again be understood by examining each row of **s2** and looking for matches in **t2**.  If there is no match, no row gets output.

        We can also have the case where more than one row in one table matches some row in the other table.  Here are two more tables to consider:

        .. image:: joins3.svg
            :alt: Tables s3 and t3

        This time, the **s3** row ``('two', 2)`` matches *two* different rows in **t3**, so we will produce two combined rows where **sy** and **ty** both equal 2:

        .. image:: joins3_result.svg
            :alt: The join of s3 and t3


        Tables **s2**, **t2**, **s3** and **t3** are also in the database accessible in the interactive tool above.

        Two tables can be related via multiple columns rather than just one in each table.  To join them, you would use a compound join condition using **AND**.  In fact, join conditions do not have to be equality (although they usually are); any logical expression relating rows in one table with rows in another can be used.  The conceptual model of examining each row in the first table and comparing with each row in the second table still works.  See if you can figure out what this query will produce (and then try it in the interactive tool above):

        .. code:: sql

            SELECT *
            FROM
              s
              JOIN t ON sy = ty OR sy > ty
            ;

        **JOIN** clauses are considered to be sub-clauses of the **FROM** clause.  We are, of course, free to add other clauses as normal to the query, such as a **WHERE** clause:

        .. code:: sql

            SELECT *
            FROM
              s
              JOIN t ON sy = ty
            WHERE tz = 'blue';

        Think of the **FROM** clause as being the first part of the query processed by the database.  The result is some collection of rows, which we can then filter with a **WHERE** clause, or put in a particular order with an **ORDER BY** clause, and so forth.

        We have a lot more to talk about with joins, but before moving on, let us see how to answer the question raised earlier, where we would like to obtain both book titles and author birth dates in one query result using **simple_books** and **simple_authors**.  Here is the solution:

        .. code:: sql

            SELECT title, author, birth
            FROM
              simple_books
              JOIN simple_authors ON author = name
            ;

        Note here that we are choosing specific columns to return as part of our result, using our **SELECT** clause.  The column **name**, used in the join condition, is the column containing author names in the **simple_authors** table.  We compare this column to the **author** column in **simple_books** for our join, but we don't include it in the columns we retrieve; otherwise we would have the same author name showing in two different columns.


事物的名称
:::::::::::::::

**Names of things**

.. md-tab-set::

    .. md-tab-item:: 中文

        到目前为止，我们(主要)并没有担心事物的 *名称*。我们已经说过，可以使用列名作为表达式，表示正在考虑的某一行中列的值，但现在我们需要考虑一些情况下，仅凭列名并不够具体的情境。我们还给出了一些示例，其中我们重命名了 **SELECT** 查询的输出列，但我们推迟了对此技术的讨论。本节将更详细地探讨这两个主题以及更多内容。

    .. md-tab-item:: 英文

        We have (mostly) not worried about the *names* of things in our discussion so far.  We have said that we can use a column name as an expression representing the value in the column for some row under consideration, but we now need to consider some scenarios in which a column's name by itself is not sufficiently specific.  We have also given some examples where we renamed the output columns for a **SELECT** query, but we deferred discussion of that technique.  This section will go into more detail regarding both of these topics and more.

.. index:: name; collision, ambiguity

名称冲突和歧义
-----------------------------

**Name collisions and ambiguity**

.. md-tab-set::

    .. md-tab-item:: 中文

        到目前为止，我们的所有示例中，被查询的表中的所有列都有唯一的名称。例如，**s** 和 **t** 的连接包含名为 **sx**、**sy**、**ty** 和 **tz** 的列。然而，在处理多个表时，我们通常不会如此幸运，能够拥有不同的列名。当参与连接的两个表中的列具有相同名称时，我们称这些列名 *冲突*。当发生命名冲突时，我们无法单独使用列名作为查询中任何部分的表达式，因为数据库无法知道您指的是哪个表的列；数据库将给出列名 *模糊* 的错误消息。

    .. md-tab-item:: 英文

        In all of our examples so far, all of the columns in the tables we queried had unique names.  For example, the join of **s** and **t** contained columns named **sx**, **sy**, **ty**, and **tz**.  However, we will often not be so lucky as to have distinct column names when working with multiple tables.  When two columns from tables involved in a join have the same name, we say that the column names *collide*.  When a naming collision occurs, we cannot use the column name by itself as an expression in any part of our query, because the database will not know which table's column you mean; the database will give an error message that the column name is *ambiguous*.

.. index:: name; qualified

限定名称
---------------

**Qualified names**

.. md-tab-set::

    .. md-tab-item:: 中文

        幸运的是，有一种简单的方法可以指定特定表中的特定列:只需先给出表名，然后加一个句点(".")再加上列名。即使名称没有歧义，也可以这样做。例如，上述最后的查询可以表示为:

        .. activecode:: joins_example_qualified_names
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
              simple_books.title,
              simple_books.author,
              simple_authors.birth
            FROM
              simple_books
              JOIN simple_authors
                ON simple_books.author = simple_authors.name
            ;

        这样做还有一个附加好处，就是可以清楚地表明每一列的来源，方便任何不熟悉数据库的读者。

        您还可以使用星号快捷方式，通过在前面加上表名和句点，表示特定表中的所有列:

        .. code:: sql

            SELECT simple_books.*, simple_authors.birth
            FROM
              simple_books
              JOIN simple_authors ON simple_books.author = simple_authors.name
            ;

        使用表名和列名的这种表达方式称为 *合格* 列名，可以与任何数据库一起使用。在某些数据库实现中，表可以被分组到更大的容器中；在这些数据库中，可能会有多个同名表(在不同的容器中)，这时必须使用容器名进行合格化。每个数据库实现都是不同的，因此您需要了解您特定数据库系统的命名合格化规则。

        在进行连接时，最好对所有列名进行合格化。这将使任何阅读或维护您代码的人更容易理解您的查询在做什么。

    .. md-tab-item:: 英文

        Fortunately, there is an easy way to specify a particular column in a particular table: simply give the table name first, followed by a period, or dot (".") and then the column name.  You can do this even if names are not ambiguous. For example, the last query above could be expressed as:

        .. activecode:: joins_example_qualified_names
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
              simple_books.title,
              simple_books.author,
              simple_authors.birth
            FROM
              simple_books
              JOIN simple_authors
                ON simple_books.author = simple_authors.name
            ;

        This has the added benefit of making clear where each column is coming from for anyone reading the query who is not familiar with the database.

        You can also use the asterisk shortcut to mean all columns in a specific table by prefixing with the table name and a dot:

        .. code:: sql

            SELECT simple_books.*, simple_authors.birth
            FROM
              simple_books
              JOIN simple_authors ON simple_books.author = simple_authors.name
            ;

        Such expressions using both the table name and the column name are known as *qualified* column names, and can be used with any database.  In some database implementations, tables can be grouped together into larger containers; in those databases, it is possible to have multiple tables of the same name (in different containers), which now must be qualified using the container name.  Each database implementation is different, so you will need to learn about your particular database system's rules for qualifying names.

        When doing a join, it is good practice to qualify all of your column names.  This will make it easier for anyone reading or maintaining your code to understand what your query is doing.

.. index:: aliasing, AS

别名
--------

**Aliasing**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 提供了在单个查询上下文中更改表和列名称的功能。这在某些情况下非常有用，甚至是必要的。在前面的章节中，我们使用列重命名来获得更漂亮的输出列标题。例如，考虑以下查询:

        .. code:: sql

            SELECT
              title,
              floor((publication_year + 99) / 100) AS century
            FROM simple_books;

        我们为第二个输出列提供了名称 "century"(否则其标题将看起来像我们计算的数学表达式)。这种技术称为 *别名*，使用 **AS** 关键字实现。列别名通常用于为输出中的列提供有用的名称，尽管它也可以用于其他原因，稍后我们会看到。

        别名也可以用于表。这通常用于缩短表名，以保持合格名称简短且可读。在 **FROM** 子句中使用 **AS** 关键字，对每个应重命名的表进行处理。然后，可以在 **SELECT**、**WHERE** 和其他子句中使用别名代替表名。以下是使用表别名重写的早期查询:

        .. code:: sql

            SELECT b.title, b.author, a.birth
            FROM
              simple_books AS b
              JOIN simple_authors AS a ON b.author = a.name
            ;

        在处理使用许多表的大型查询时，别名可以显著缩小查询并提高可读性。

        表别名 *要求* 的一个情况是将表与其自身连接。这在同一表内的行之间存在某种关系时可以实现，这种情况比您想象的更为常见。作为一个示例，考虑我们可能用简单书籍和作者数据执行的查询:“哪些书是在与《三体》相同的年份出版的？”以下是一种用查询回答该问题的方法:

        .. code:: sql

            SELECT b2.*
            FROM
              simple_books AS b1
              JOIN simple_books AS b2
                ON b1.publication_year = b2.publication_year
            WHERE
              b1.title = 'The Three-Body Problem';

        如果这让您感到困惑，可以将其视为使用两个表，**b1** 和 **b2**，每个表都包含与 **simple_books** 相同的数据。考虑将 **b1** 和 **b2** 连接，应用连接条件 ``b1.publication_year = b2.publication_year``；然后，用条件 ``b1.title = 'The Three-Body Problem'`` 过滤该结果；最后，仅输出 **b2** 的列。如果您在每个步骤中都难以想象结果应该是什么，请记住您可以使用上面的交互工具查询数据库。

        在使用表别名时，应该使用别名对所有列名进行合格化，这是一种良好的风格。一些数据库允许您使用原始表名而不是别名，但混合使用别名和原始表名是不一致和混乱的，在某些情况下可能导致难以调试的错误代码。

        只需记住，别名仅影响进行重命名的查询；新查询不会了解之前对表或列应用的任何别名。

        最后需要注意的是，**AS** 关键字在 SQL 中实际上是可选的——您可以在省略此关键字的情况下创建别名。只需在表名或列表达式后放置一个有效的标识符字符串:

        .. code:: sql

          SELECT b.title, b.author, a.birth
          FROM
            simple_books b
            JOIN simple_authors a ON b.author = a.name
          ;

        省略关键字可能会显得奇怪，但您可能会在某个时候看到使用这种形式的别名的代码，因此要有所了解。没有关于哪种风格更好的共识；在本教科书中，我们将始终使用 **AS** 来增加清晰度。

        (Oracle 用户注意:**AS** 关键字对于列是可选的，但不支持表别名——在 Oracle 查询中对表进行别名时，必须省略 **AS**。)

    .. md-tab-item:: 英文

        SQL provides facilities to change the names of tables and columns within the context of a single query.  This can be useful, and at times, necessary.  In a previous chapter, we used column renaming to get nicer column headers in our output.  For example, consider this query:

        .. code:: sql

            SELECT
              title,
              floor((publication_year + 99) / 100) AS century
            FROM simple_books;

        We supplied the name "century" for the second output column (which otherwise would have a header that looked like the mathematical expression we computed).  This technique is known as *aliasing*, and is accomplished with the **AS** keyword.  Aliasing for columns is most often used for the purpose of giving a helpful name for the column in the output, although it can be applied for other reasons that we shall see.

        Aliasing can also be used with tables.  This is often used to shorten table names to keep qualified names short and readable.  Here, the **AS** keyword is used in the **FROM** clause after each table that should be renamed.  The alias can then be used in the **SELECT**, **WHERE**, and other clauses in place of the table name.  Here is an earlier query, rewritten using table aliasing:

        .. code:: sql

            SELECT b.title, b.author, a.birth
            FROM
              simple_books AS b
              JOIN simple_authors AS a ON b.author = a.name
            ;

        When working with large queries using many tables, aliasing can make the query significantly smaller and more readable.

        One instance where table aliasing is *required* is when joining a table to itself.  This can be done when there is some kind of relationship between rows within the same table, which happens more often than you might guess.  As an example of a query we might do with our simple books and authors data, consider the question, "What books were published in the same year as *The Three-Body Problem*?".  Here is one way to answer that question with a query:

        .. code:: sql

            SELECT b2.*
            FROM
              simple_books AS b1
              JOIN simple_books AS b2
                ON b1.publication_year = b2.publication_year
            WHERE
              b1.title = 'The Three-Body Problem';

        If this seems confusing, think about it as using two tables, **b1** and **b2**, each containing the same data as **simple_books**.  Work through what happens if you join **b1** and **b2** applying the join condition ``b1.publication_year = b2.publication_year``; then, filter that result with the condition ``b1.title = 'The Three-Body Problem'``; finally, output just the columns from **b2**.  If you have trouble visualizing what the result should be at each step, remember that you can query the database using the interactive tool above.

        When using table aliasing, you should qualify all of your column names using the aliases as a matter of good style.  Some databases allow you to use original table names instead of aliases, but mixing aliases with original table names is inconsistent and confusing, and in some cases that can result in incorrect code that is difficult to debug.

        Just remember, aliasing only affects the query in which the renaming occurs; a new query will know nothing about any previous aliasing applied to tables or columns.

        As a final note, the **AS** keyword is actually optional in SQL - you can create an alias with this keyword omitted.  Simply put a valid identifier string after the name of a table or after a column expression:

        .. code:: sql

          SELECT b.title, b.author, a.birth
          FROM
            simple_books b
            JOIN simple_authors a ON b.author = a.name
          ;

        Leaving out a keyword may seem strange, but you are likely to read code at some point using this form of aliasing, so be aware.  There is no consensus on which style is better; for this textbook, we will consistently use **AS** for additional clarity.

        (Note for Oracle users: the **AS** keyword is optional for columns, but is not supported for table aliases - you must omit the **AS** in Oracle queries when aliasing a table.)

.. index:: double quotes

保留名称、带空格的名称或大小写混合的名称mixed-case names
-------------------------------------------------------

**Reserved names, names with spaces, or **

.. md-tab-set::

    .. md-tab-item:: 中文

        通常，事物的名称是不区分大小写的，并且不包含空格。此外，查询输出标题的显示大小写可能是全大写或全小写，这取决于数据库(在本教科书中，小写是常规)。然而，确实可以使用区分大小写且包含空格的名称。要做到这一点，只需将名称放在双引号内。例如，以下查询输出列的标题将是混合大小写并包含空格:

        .. code:: sql

            SELECT 42 AS "The Answer";

        保留名称(如 SQL 关键字)在用作列或表名称时也可能需要放在双引号内。

        很少情况下，您可能会遇到表或列名称是混合大小写或包含空格的数据库。这可能发生在数据库创建者在创建表时使用了双引号的 SQL 代码中。一般来说，这并不是一个好习惯，因为它迫使在任何未来的查询中使用双引号。保留字通常也应避免，尽管在处理多个数据库时这可能很困难，因为一个数据库中允许的词在另一个数据库中可能是保留字。

        (MySQL 用户注意:使用反引号而不是双引号。反引号字符看起来像撇号，但倾斜方向相反。)

    .. md-tab-item:: 英文

        Usually, names of things are case-insensitive and do not contain spaces.  Also, the case used when displaying the output headers for a query may be all uppercase or all lowercase, depending on the database (for this textbook, lowercase is the norm).  It is possible, however, to use names which are case-sensitive and which contain spaces.  To do this, put the name within double quotes.  For example, the header for the output column of in the following query will be mixed-case as well as having spaces:

        .. code:: sql

            SELECT 42 AS "The Answer";

        Reserved names (such as SQL keywords) may also need to be put inside double quotes when used as column or table names.

        Very rarely, you may encounter a database where table or column names are mixed-case or contain spaces.  This can occur if the database creator used double quotes in the SQL code when creating the tables.  In general, this is not a good practice, as it forces the use of double quotes for any future queries using the table.  Reserved words should also be avoided in general, although this can be difficult when working with multiple databases, as an allowed word in one database may be a reserved word in another database.

        (Note for MySQL users: use backticks instead of double quotes.  The backtick character looks like an apostrophe, but slanting in the opposite direction.)


.. index::
    single: column; identity
    single: id column
    single: universally unique identifier
    single: UUID

标识列
::::::::::::::::

**Identity columns**

.. md-tab-set::

    .. md-tab-item:: 中文

        如果我们想要通过连接在一个表中的数据与另一个表中的数据建立联系，我们需要这些表共享一些共同的数据元素。在我们的简单书籍数据集中，共同元素是作者的名字，它在 **simple_books** 和 **simple_authors** 表中都存在；这使我们能够通过连接条件 ``simple_books.author = simple_authors.name`` 将两个表连接起来。我们可以对结果有信心，因为我们知道作者的名字在我们的简单数据库中唯一地标识了作者。但是，如果作者的名字不是唯一的呢？那么我们可能会将作者与他们实际上没有写的书连接起来！

        对于某些类型的数据，某些数据元素对于每个可能的数据项都是唯一的，并可以用作数据库中数据的标识符。例如，国际旅行到许多国家要求旅行者持有护照，而签发国家加上护照号码唯一地标识任何旅行者。然而，这仅适用于国际旅行；大多数国家在国内旅行时不要求护照，因此有很多人根本没有护照。因此，试图跟踪国内旅行者的数据库不能将护照信息作为唯一标识符。

        作者的名字可能看起来是作者的一个好标识符，但事实上，我们也必须小心，因为有多个作者共享同一个名字。例如，有两位小说家名为 Richard Wright，还有一位小说家和一位诗人名为 David Diop。我们可以通过他们的出生日期进一步区分这些作者，或者我们可以考虑他们的出生地或其他属性。当然，前提是我们 *知道* 数据库中每位作者的出生日期等信息。在任何情况下，由于必须存储关于每位作者的如此多信息，以便于任何我们想要与作者表连接的表，这开始变得令人不满意。

        这种类型的问题经常出现。我们将采用的解决方案在实践中被广泛使用，即为数据库中的每位作者创建一个人工唯一标识符，或 *id*。唯一标识符可以有不同的形式。最常见的方案是在数据库中保持一个计数器，每次向表中添加行时递增该计数器。然后将此计数器值用作新行的 id 值(我们将在 :numref:`Chapter {number} <table-creation-chapter>` 中讨论如何做到这一点)。

        另一个流行的方案是使用随机生成的非常大的整数——*通用唯一标识符*，或 UUID。在这个方案中，由于可能的 UUID 数量非常大，每个新的 id 值很可能与表中之前的任何其他 id 不同。如果存在重复项，也很容易检测到，在这种情况下可以生成另一个值。

        在我们的数据库中，有一个名为 **authors** 的表，其中有一个 **author_id** 列，存储每行的唯一值。还有一个 **books** 表，里面没有存储作者名字的列。相反，它也有 **author_id** 列。**books** 中的每个唯一 **author_id** 都等于 **authors** 中的某个 **author_id** 值。

        为了将作者的名字与他们的书籍一起获取，我们需要通过公共 id 值将 **books** 与 **authors** 连接起来:

        .. activecode:: joins_example_books_join
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT authors.name, books.title
            FROM
              books
              JOIN authors ON authors.author_id = books.author_id
            ;

        请注意，这个查询需要使用合格的列名，至少对于两个 **author_id** 列——如果我们简单地尝试以下查询:

        .. code:: sql

            SELECT name, title
            FROM
              books
              JOIN authors ON author_id = author_id
            ;

        我们将收到一个错误消息，提示 **author_id** 名称是模糊的。

    .. md-tab-item:: 英文

        If we want to make a connection between data in one table and data in another using a join, we need the tables to share some data elements in common.  In our simple books dataset, the common element was the author's name, which was present in both the **simple_books** and **simple_authors** tables; this let us join the two tables with the join condition ``simple_books.author = simple_authors.name``.  We can be confident in our result because we know the author's name uniquely identifies the authors in our simple database.  But what if author names were not unique?  Then we might join authors to books they did not actually write!

        For some types of data, some element of the data is unique for every possible data item and can be used as an identifier for the data in a database.  For example, international travel to many countries requires the traveler to have a passport, and the issuing country together with the passport number uniquely identifies any traveler.  However, this only works for international travel; most countries do not require passports for travel within the country's own borders, and therefore there are many people who have no passport at all.  A database trying to track domestic travelers, then, cannot use passport information as a unique identifier.

        Author names might seem like a good identifier for authors, but, in fact, we have to be careful here as well due to multiple authors sharing the same name.  For example, there are two novelists named Richard Wright, and both a novelist and a poet named David Diop.  We could further distinguish between these authors using their birth dates, or perhaps we could consider their birthplace or other attributes.  That only works, of course, if we *know* the birth date and so forth of each author in our database. In any case it begins to be an unsatisfactory solution due to the complexity of having to store so many pieces of information about each author for any tables we want to join to our table of authors.

        This type of problem comes up a lot.  The solution we will adopt, which is widely used in practice, is to create an artificial unique identifier, or *id*, for each author in our database.  Unique identifiers can take different forms.  The most common scheme is to keep a counter in the database and increment it each time a row is added to a table.  This counter value is then used as the id value for the new row (we will discuss how to do this in :numref:`Chapter {number} <table-creation-chapter>`).

        Another popular scheme is to use a very large integer generated at random - a *universally unique identifier*, or UUID.  In this scheme, due to the large number of possible UUIDs, each new id value is very likely to be different from any other previously id in the table. It is also easy to detect if there is a duplicate, in which case another value can be generated.

        In our database, there is a table named **authors** which has an **author_id** column holding a unique value for each row.  There is also a **books** table, which does not have a column to store the author's name.  Instead, it also has the column **author_id**.  Each unique **author_id** in **books** is equal to some **author_id** value in **authors**.

        To get the author's name together with their books, we will need to join **books** to **authors** using the common id value:

        .. activecode:: joins_example_books_join
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT authors.name, books.title
            FROM
              books
              JOIN authors ON authors.author_id = books.author_id
            ;

        Note that this query requires the use of qualified column names, at least for the two **author_id** columns - if we simply try the query

        .. code:: sql

            SELECT name, title
            FROM
              books
              JOIN authors ON author_id = author_id
            ;

        we will get an error message that the **author_id** name is ambiguous.


表关系
:::::::::::::::::::

**Table relationships**

.. md-tab-set::

    .. md-tab-item:: 中文

        与早期数据库系统相比，关系数据库的一大优势是关系并不是在数据库中显式存储的。这在数据库设计和软件复杂性方面提供了许多优点，这些优点大多超出了本书的范围。关系方法的一个重要优势是，您可以轻松表达关于关系的查询，而这些关系并没有被数据库设计者预见到；例如，我们之前查询寻找与另一本书在同一年出版的书籍。然而，这种灵活性也意味着，当您遇到一个新的关系数据库时，您可能无法立即理解数据库中的结构和关系，或如何(或为什么)将两个表连接在一起。

        一个结构良好的数据库通常会提供一些可能的表连接位置的指示。一个指示可能在列的名称中——例如，表中的 **book_id** 强烈暗示与 **books** 表的标识列链接的列。另一个指示可以以 *外键约束* 的形式出现，这是我们将在 :numref:`Chapter {number} <constraints-chapter>` 中讨论的主题。探索数据库以发现这些隐含关系是学习任何新数据库的重要第一步。

        您的数据库也可能附带数据模型图，在本书的 :numref:`Part {number} <data-modeling-part>` 中讨论过。(我们数据库中数据集的数据模型可以在 :ref:`Appendix A <appendix-a>` 中找到。)数据模型通常会明确表之间的关系。虽然数据可以以非常复杂的方式相互关联，但有一些基本的关系类型捕捉到大多数关系的重要方面。这些关系通常称为“一对一”、“一对多”和“多对多”。下面，我们将讨论这些常见关系及其在我们数据库中的出现位置。

    .. md-tab-item:: 英文

        One of the strengths of relational databases compared to earlier database systems is that relationships are not explicitly stored in the database.  This provides a number of advantages regarding database design and software complexity, which are mostly beyond the scope of this book.  One important advantage of the relational approach is that you can easily express queries concerning relationships which were not anticipated by the designer of the database; for example, our earlier query looking for books published in the same year as another book.  However, this flexibility also means that when you encounter a new relational database, you may not immediately understand the structure and relationships in the database, or how (or why) you should join two tables together.

        A well structured database usually gives some indication of likely places to join tables together.  One indication may be in the names of columns - e.g., **book_id** in a table strongly suggests a column that links to the identity column of the **books** table.  Another indication can come in the form of *foreign key constraints*, a topic we will discuss in :numref:`Chapter {number} <constraints-chapter>`.  Exploring the database to find these implicit relationships is an important first step in learning any new database.

        Your database might also come with a data model diagram, discussed in :numref:`Part {number} <data-modeling-part>` of this book.  (Data models for the data sets in our database can be found in :ref:`Appendix A <appendix-a>`.)  The data model will typically make the relationships between tables explicit.  While data can be related to each other in very complex ways, there are some basic relationship types that capture the important aspects of most relationships.  These relationships are commonly called "one-to-one", "one-to-many", and "many-to-many".  Below, we discuss these common relationships and where they appear in our database.

.. index::
    single: relationship - tables; one-to-one
    single: one-to-one relationship - tables

一对一
----------

**One-to-one**

.. md-tab-set::

    .. md-tab-item:: 中文

      *一对一* 描述了两种数据之间的关系。如果我们将每种数据类型视为拥有自己的表，那么一个表中的每一行与另一个表中的 *至多* 一行之间有明确定义的关系，反之亦然。有时，一个表中的每一行在另一个表中都有一个对应的行，反之亦然；而其他时候，某些行在一个或两个表中可能没有在另一个表中的对应行。当表之间存在真正的一对一对应关系时，有时将这些表合并为一个更大的表是可取的(是否这样做是一个设计决策)。

      一对一关系的一个例子可能出现在二手书销售商的数据库中。在我们数据库中的 **bookstore_inventory** 和 **bookstore_sales** 表中可以找到一些这个虚构书店的示例数据。每本书的作者、标题、状况和当前价格都记录在 **bookstore_inventory** 中。表 **bookstore_sales** 记录了书籍的销售情况，包括销售日期、付款方式和收据编号。这两个表可以通过共同列 **stock_number** 连接，后者作为 **bookstore_inventory** 的 ID 列。 **bookstore_sales** 表中的每一条记录对应于 **bookstore_inventory** 表中的一条记录；然而，任何尚未售出的书籍仍在卖家的手中，将不会有对应的 **bookstore_sales** 记录。

      以下是每个表的一些示例行。

      .. figure:: one_to_one.svg

          **bookstore_inventory** 和 **bookstore_sales** 表中的一些示例行:两个库存项目有对应的销售记录，但第三个尚未售出。

    .. md-tab-item:: 英文

      *One-to-one* describes a relationship between two types of data.  If we think of each data type as having its own table, then each row in one table has a well-defined relationship with *at most* one row in the other table, and vice versa.  Sometimes each row in a table has exactly one corresponding row in the other table, and vice versa; other times, some rows in one or both tables may not have corresponding rows in the other table.  When there is a true one-to-one correspondence between tables, it is sometimes desirable to combine the tables into one larger table (whether or not to do this is a design decision).

      An example of a one-to-one relationship might appear in a database for a seller of used books.  Some example data for this fictional bookstore can be found in our database in the tables **bookstore_inventory** and **bookstore_sales**.  Each of the seller's books is recorded in **bookstore_inventory**, listing the book's author, title, condition, and current price.  The table **bookstore_sales** records the sale of a book, the date it was sold, the payment type, and a receipt number.  These two tables can be joined by the common column **stock_number**, which functions as the id column for **bookstore_inventory**.  Every record in the **bookstore_sales** table corresponds to exactly one record in the **bookstore_inventory** table; however, any unsold books still in the seller's possession will not have a corresponding **bookstore_sales** record.

      A few rows from each table are illustrated below.

      .. figure:: one_to_one.svg

          Some example rows from the **bookstore_inventory** and **bookstore_sales** tables: two inventory items have corresponding sales records, but the third has not been sold yet.

.. index::
    single: relationship - tables; one-to-many
    single: one-to-many relationship - tables
    single: relationship - tables; many-to-one
    single: many-to-one relationship - tables

一对多
-----------

**One-to-many**

.. md-tab-set::

    .. md-tab-item:: 中文

        *一对多* 指的是一个表中的行对应于另一个表中的多行，而第二个表中的行最多只对应于第一个表中的一行。在某些情况下，第一个表中的行总是至少有一行对应；而在其他情况下，行可以有零行或多行对应。

        在我们的数据库中，**authors** 和 **books** 之间存在一对多关系——每位作者有一本或多本书，但每本书只有一位作者。(这并不反映现实世界——许多书籍是由两位或多位作者共同创作的！但为了简单起见，我们的数据库只包含单作者的书籍。)请注意，我们也可以谈论 *多对一* 关系，这正是与一对多的对称关系；我们可以说 **authors** 表与 **books** 表之间存在一对多关系，或者说 **books** 表与 **authors** 表之间存在多对一关系。

        要将一个表的行与另一个表的行连接起来，其中存在一对多关系，最简单的方法是在“多”侧包含一个存储来自“一”侧的 ID 值的列。如上所述，这种策略在 **books** 和 **authors** 中得到了应用；**authors** 表具有唯一的 **author_id** 列，而 **books** 表则具有对应的 **author_id** 列。

        .. figure:: one_to_many.svg

            **authors** 和 **books** 表中的一些示例行(未显示所有列):每本书有一个作者，一些作者写了多本书。

        同样，**books** 表与我们数据库中的 **editions** 表也存在一对多关系。在这种情况下，**editions** 表有一个 **book_id** 列，正如你所猜测的，包含来自 **books** 的 **book_id** 列的值。(**editions** 表包含关于书籍印刷版的信息:出版商信息、印刷标题、印刷年份等。[#]_ )

    .. md-tab-item:: 英文

        *One-to-many* refers to the case when rows in one table correspond to some number of rows in another table, but rows in the second table only correspond to at most one row in the first table.  In some cases, rows in the first table always have at least one corresponding row; other times, rows can have zero or more corresponding rows.

        In our database, we have a one-to-many relationship between **authors** and **books** - each author has one or more books, but each book has exactly one author.  (This is not reflective of the real world - many books exist that were written by two or more authors working together!  However, for simplicity our database only contains single-author books.)  Note that we can also talk of *many-to-one* relationships, which are just the symmetric equivalent of one-to-many; we can say that the **authors** table is in a one-to-many relationship with **books**, or that the **books** table is in a many-to-one relationship with **authors**.

        To connect rows from one table to rows in another table where a one-to-many relationship exists between them, the simplest approach is to include a column on the "many" side that stores id values from the "one" side.  As we saw above, this strategy is used with **books** and **authors**; the **authors** table has the **author_id** column, which is unique for every row, and the **books** table has the corresponding column **author_id**.

        .. figure:: one_to_many.svg

            Some example rows from the **authors** and **books** tables (not all columns shown): each book has one author, some authors have written multiple books.

        Similarly, the **books** table has a one-to-many relationship with the **editions** table in our database.  In this case, the **editions** table has a **book_id** column, which, as you might guess, contains values from the **book_id** column of **books**.  (The **editions** table contains information about the printed editions of books: publisher information, title as printed, year printed, and so forth. [#]_)

.. index::
    single: relationship - tables; many-to-many
    single: many-to-many relationship - tables
    single: table; cross-reference
    single: cross-reference table

多对多
------------

**Many-to-many**

.. md-tab-set::

    .. md-tab-item:: 中文

        *多对多* 关系意味着一个表中的行可能对应于另一个表中的多行，反之亦然。在我们的数据库中，多对多关系的示例将涉及书籍和作者的奖项。例如，雨果奖每年颁发给一本科幻类书籍。在我们的数据库中，许多书籍获得了雨果奖；因此，**awards** 表中雨果奖的行与 **books** 表中的多行相关联。尤其优秀的科幻书籍可能会同时获得雨果奖和星云奖；因此，**books** 表中的行可以对应多个 **awards** 行。

        当存在多对多关系时，如何将一个表的行连接到另一个表的行？如果你尝试使用我们在一对多关系中使用的技巧，你会很快遇到问题。例如，假设我们试图在 **awards** 表中存储来自 **books** 的 ID 值；由于许多书籍获得了雨果奖，我们需要存储多个书籍 ID，因此会有许多雨果奖的行，所有行都相同，除了书籍 ID。另一方面，如果我们试图在 **books** 表中存储奖项 ID，获得多个奖项的书籍将需要多行，所有行都相同，除了奖项 ID。[#]_  具有多个几乎相同的行会产生许多问题，其中一些我们将在 :numref:`Chapter {number} <normalization-chapter>` 中探讨。

        解决方案是使用一个称为 *交叉引用* 表的第三个表作为连接器。至少，交叉引用表将为被连接的两个表中的每个唯一 ID 列有一列。例如，我们数据库中的 **books_awards** 表具有一个 **book_id** 列，指向 **books** 的 **book_id** 列，以及一个 **award_id** 列，指向 **awards** 的 **award_id** 列。在 **books_awards** 表中存在的 (book id, award id) 对表示给定书籍获得了指定的奖项。

        我们还可以在交叉引用表中存储其他信息。在 **books_awards** 的情况下，我们还具有一个 **year** 列，用于存储颁发给书籍的奖项年份。请注意，交叉引用表实际上是存储该信息的唯一地方；年份并不“属于”奖项，因为奖项可以在多个年份颁发；而它也不真正属于书籍，因为书籍可以在不同年份获得奖项。

        .. figure:: many_to_many.svg

            **books**、**books_awards** 和 **awards** 表中的一些示例行(未显示所有列)。每行在 **books_awards** 中将书籍与书籍获得的奖项连接起来。奖项年份也存储在 **books_awards** 中。

        要使用交叉引用表，我们需要将 *三个* 表连接在一起。连接三个表的基本原则与连接两个表相同；首先连接两个表，然后将该结果与第三个表连接。完成的查询如下所示:

        .. activecode:: joins_example_many_to_many
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT b.title, a.name AS award, ba.year
            FROM
              books AS b
              JOIN books_awards AS ba ON b.book_id = ba.book_id
              JOIN awards AS a ON a.award_id = ba.award_id
            ;

        查看上述查询，将第一个连接视为将交叉引用表中的奖项 ID 添加到书籍表的行中，并将第二个连接视为引入与这些奖项 ID 匹配的奖项信息。(同样，你可以将此查询拆分为更小的部分，并在交互工具中尝试它们，以帮助你理解 SQL 的工作方式。)

        除了为特定书籍获奖外，作者还可以因其整个作品而获奖。这类奖项也存储在 **awards** 表中；然而，我们需要另一个表将作者与这些奖项连接起来(因为 **books_awards** 表仅连接特定书籍)。为此目的存在交叉引用表 **authors_awards**。

    .. md-tab-item:: 英文

        *Many-to-many*, you can probably guess, implies that rows in one table may correspond to multiple rows in the other table, and vice versa.  In our database, our examples of many-to-many relationships will involve book and author awards.  For example, the Hugo Award is given out each year to a book in the science fiction genre.  In our database, there are many books that have won a Hugo Award; therefore the row for the Hugo Award in the **awards** table relates to multiple rows in the **books** table.  Especially good science fiction books might win both a Hugo Award and a Nebula Award; so rows in the **books** table can correspond to multiple **awards** rows.

        How do you connect rows from one table to rows in another table when there is a many-to-many relationship?  If you try the trick we used with one-to-many relationships, you quickly run into trouble.  For example, suppose we try to store id values from **books** in the **awards** table; since many books have won the Hugo Award, we need to store many book ids, so we would have many rows for the Hugo Award, all identical except for the book id. On the other hand, if we try to store award ids in the **books** table, books that have won multiple awards will need multiple rows, all identical except for the award ids. [#]_  Having multiple nearly identical rows creates a number of problems, some of which we will explore in :numref:`Chapter {number} <normalization-chapter>`.

        The solution is to use a third table, known as a *cross-reference* table, as a connector.  At minimum, a cross-reference table will have one column for each of the unique id columns in the two tables being connected.  For example, the **books_awards** table in our database has a column **book_id** referring to the **book_id** column of **books** and an **award_id** column referring to the **award_id** column of **awards**.  The existence of a (book id, award id) pair in the **books_awards** table means that the given book has won the stated award.

        We can store other information in the cross-reference table as well.  In the case of **books_awards**, we also have a **year** column storing the year in which the award was given to the book.  Note that the cross-reference table is really the only place we can store this information; the year doesn't properly "belong" to the award, as an award is given out in many years; and it doesn't properly belong to the book, as books can win awards in different years.

        .. figure:: many_to_many.svg

            Some example rows from **books**, **books_awards**, and **awards** (not all columns shown).  Each row in **books_awards** connects a book to an award that the book has won.  The year of the award is stored in **books_awards** as well.

        To use the cross-reference table, we will need to join together *three* tables.  The basic principles for joining three tables are the same as for two; start by joining two tables, then join that result with the third table.  The finished query looks like this:

        .. activecode:: joins_example_many_to_many
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT b.title, a.name AS award, ba.year
            FROM
              books AS b
              JOIN books_awards AS ba ON b.book_id = ba.book_id
              JOIN awards AS a ON a.award_id = ba.award_id
            ;

        Looking at the query above, think of the first join as adding award ids from the cross-reference table to the rows from the books table, and think of the second join as then bringing in the award information matching those award ids.  (Again, you can break this query down into smaller pieces and try them in the interactive tool to help build your intuition about how SQL works.)

        In addition to winning awards for specific books, an author can win awards for their entire body of work.  Awards of this type are also stored in the **awards** table; however, we need another table to connect authors with these awards (since the **books_awards** table connects to specific books only).  The cross-reference table **authors_awards** exists for this purpose.

.. index:: join - SQL; outer, outer join, INNER JOIN, RIGHT [OUTER] JOIN, LEFT [OUTER] JOIN, FULL [OUTER] JOIN

内连接和外连接
:::::::::::::::::::::

**Inner and outer joins**

.. md-tab-set::

    .. md-tab-item:: 中文

        当关系数据库程序员使用“连接”("join")这个词而不加任何限定时，他们几乎总是指我们上面描述的类型，即结果仅包含在连接两侧匹配的行。这种类型的连接更正式地称为 *内连接*(*inner join*)。实际上，如果你想明确你正在进行的连接类型，可以在 **JOIN** 前可选地使用关键字 **INNER**；然而，**INNER** 通常被省略，因为没有 **INNER** 的默认连接仍然是内连接。

        如果你想从一个表中检索 *所有* 行，即使在连接的另一侧没有匹配的行呢？例如，我们可能想要获取书籍的列表，以及这些书籍获得的任何奖项。由于并非所有书籍都获得了奖项，上面显示的 **books**、**books_awards** 和 **awards** 的内连接仅返回我们数据库中的部分书籍。为了获取所有书籍以及相应的奖项，我们需要使用 *外连接*(*outer join*)。

        外连接有三种类型:*左外连接*(*left*)、*右外连接*(*right*)和 *全外连接*(*full*)。这些通过关键短语 **LEFT [OUTER] JOIN**、**RIGHT [OUTER] JOIN** 和 **FULL [OUTER] JOIN** 实现。(方括号表示 **OUTER** 关键字是可选的；也就是说，**LEFT JOIN** 与 **LEFT OUTER JOIN** 意思相同。)在外连接中，根据外连接的类型，将返回一个或两个表中的所有行。在左外连接中，将返回 **LEFT JOIN** 关键短语左侧表的所有行，但仅返回右侧表中匹配的行。**RIGHT JOIN** 则相反，而 **FULL JOIN** 则返回参与连接的两个表中的所有行。

        当连接指定应该返回一个表中的所有行时，如果某行在另一个表中没有匹配，该行应包含什么来表示缺失的数据？一个合乎逻辑的选择是用 ``NULL`` 值填充这些列，这正是发生的情况。以下是一个查询，用于检索所有书籍以及相关的奖项:

        .. activecode:: joins_example_outer_join
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT b.title, a.name AS award, ba.year
            FROM
              books AS b
              LEFT JOIN books_awards AS ba ON b.book_id = ba.book_id
              LEFT JOIN awards AS a ON a.award_id = ba.award_id
            ;

        注意，在上面的查询中，我们必须进行两个外连接。**books** 和 **books_awards** 之间的第一个外连接是必要的，因为没有奖项的书籍在 **books_awards** 交叉引用表中将没有匹配记录。因此，该连接的结果将有来自 **books_awards** 表的 **award_id** 列的 ``NULL`` 值。所以，当我们与 **awards** 连接时，我们再次需要一个外连接，因为 ``NULL`` **award_id** 值将不会与 **awards** 表中的任何行匹配。

        在大多数数据库中，我们可以使用一个右外连接来改写该查询。(注意:在本书撰写时，SQLite 尚不支持右外连接或全外连接，因此该查询在上面的交互工具中可能无法正常工作):

        .. code:: sql

            SELECT b.title, a.name AS award, ba.year
            FROM
              awards AS a
              JOIN books_awards AS ba
                ON a.id = ba.award_id
              RIGHT JOIN books AS b
                ON b.id = ba.book_id
            ;

        在这里，**awards** 和 **books_awards** 表可以使用常规连接，因为我们只关心在 **books_awards** 表中引用的奖项，并且 **books_awards** 表中的所有行已经在 **awards** 表中有匹配的条目。然而，右外连接也能同样有效——如果所有行匹配，则外连接等同于内连接。

        上述查询确实展示了一种可能不想要的行为，即我们对于获得多个奖项的书籍有多行。某些数据库提供了一种生成书籍后列出奖项的列表的方法，而不是多行；请参见附录 B - :ref:`appendix-b-aggregate-functions` 中的 **LISTAGG** 聚合函数(我们将在 :numref:`Chapter {number} <grouping-chapter>` 中讨论聚合函数的使用)。

        这是另一个使用外连接的示例，这次使用我们的书店表——看看你能否弄清楚这个查询在做什么:

        .. code:: sql

            SELECT
              inv.*,
              CASE WHEN sales.stock_number IS NULL THEN 'in stock'
                  ELSE 'sold'
              END
                AS status
            FROM
              bookstore_inventory AS inv
              LEFT JOIN bookstore_sales AS sales
                ON inv.stock_number = sales.stock_number
            ;

    .. md-tab-item:: 英文

        When relational database programmers use the word "join" without any qualifiers, they almost always mean the type of join we have been describing above, in which the result only contains rows that match on both sides of the join.  This type of join is more formally known as an *inner join*.  In fact, you can optionally use the keyword **INNER** in front of **JOIN** if you want to make clear what type of join you are doing; however, **INNER** is commonly dropped simply because the default without **INNER** is still an inner join.

        What if you want to retrieve *all* rows from one table in a join, even if there are no matching rows on the other side of the join?  For example, we might want a list of books, together with any awards the books have won.  Since not all books have won awards, the inner join of the **books**, **books_awards**, and **awards** shown above only returns some of the books in our database.  To get all books, and awards where present, we want an *outer join*.

        There are three types of outer join: *left*, *right*, and *full*.  These are implemented with the key phrases **LEFT [OUTER] JOIN**, **RIGHT [OUTER] JOIN**, and **FULL [OUTER] JOIN**.  (The square brackets mean that the **OUTER** keyword is optional; that is, **LEFT JOIN** means the same thing as **LEFT OUTER JOIN**.)  In an outer join, all rows from one or both tables are returned, depending on the type of outer join.  In a left outer join, all of the rows from the table on the left-hand side of the **LEFT JOIN** key phrase are returned, but only matching rows are returned from the right-hand side table.  **RIGHT JOIN** does the opposite, while **FULL JOIN** returns all rows from both tables involved in the join.

        When the join specifies that all rows from a table should be returned, and a row has no match in the other table, what should the row contain for the missing data from the other table?  A logical choice is to fill in those columns with ``NULL`` values, which is exactly what happens.  Here is one query to retrieve all books, as well as awards where relevant:

        .. activecode:: joins_example_outer_join
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT b.title, a.name AS award, ba.year
            FROM
              books AS b
              LEFT JOIN books_awards AS ba ON b.book_id = ba.book_id
              LEFT JOIN awards AS a ON a.award_id = ba.award_id
            ;

        Note that we have to do two outer joins in the above query.  The first outer join between **books** and **books_awards** is necessary because books without awards will have no matching records in the **books_awards** cross reference table.  The result of that join, then, will have ``NULL`` values for the **award_id** column coming from the **books_awards** table.  So, when we join with **awards** we again need an outer join, because the ``NULL`` **award_id** values will not match any rows in the **awards** table.

        In most databases, we could instead write the query using one right outer join. (Note: at the time this book was written, SQLite did not yet support right or full outer joins, so this query may not work in the interactive tool above):

        .. code:: sql

            SELECT b.title, a.name AS award, ba.year
            FROM
              awards AS a
              JOIN books_awards AS ba
                ON a.id = ba.award_id
              RIGHT JOIN books AS b
                ON b.id = ba.book_id
            ;

        Here, the **awards** and **books_awards** tables can use a regular join, as we only care about awards that are referenced in the **books_awards** table, and all rows in the **books_awards** table have a matching entry already in the **awards** table.  However, a right outer join would have worked equally well - an outer join is equivalent to an inner join if all rows match.

        The above queries do exhibit one behavior which may be unwanted, which is that we have multiple rows for books that have won multiple awards.  Some databases provide a way to produce a list of awards after each book, rather than multiple rows; see the **LISTAGG** aggregate function in Appendix B - :ref:`appendix-b-aggregate-functions` (we discuss the use of aggregate functions in :numref:`Chapter {number} <grouping-chapter>`).

        Here is one more example of the use of an outer join, this time using our bookstore tables - see if you can figure out what this query is doing:

        .. code:: sql

            SELECT
              inv.*,
              CASE WHEN sales.stock_number IS NULL THEN 'in stock'
                  ELSE 'sold'
              END
                AS status
            FROM
              bookstore_inventory AS inv
              LEFT JOIN bookstore_sales AS sales
                ON inv.stock_number = sales.stock_number
            ;

.. index:: join - SQL; implicit, cross product - SQL, CROSS JOIN

隐式连接语法
::::::::::::::::::::

**Implicit join syntax**

.. md-tab-set::

    .. md-tab-item:: 中文

        在 SQL 中，内连接的能力早于 **JOIN** 关键字和相关短语的引入。 在引入这种 *显式* 连接语法之前，连接使用的是 *隐式* 连接语法，本节将对此进行描述。 你可能更喜欢上面的显式语法，许多实践者认为使用它是最佳实践，因为它提供了清晰性。 然而，隐式语法受到所有数据库的支持，你在实践中很可能会遇到它。此外，大多数数据库内部将显式语法简化为隐式语法，这对理解数据库如何处理连接查询有影响。 基于这些原因，理解隐式连接语法非常重要。

        回到本章开始时的抽象示例:

        .. image:: joins1.svg
            :alt: Tables s and t

        在隐式连接语法中，第一步是在 **FROM** 子句后简单列出所有参与连接的表。 在 SQL 中，这意味着表的 *笛卡尔积*。 在两个表的笛卡尔积中，*每* 行都与 *每* 行配对。 你可以在下面的查询中看到这一点:

        .. activecode:: joins_example_implicit_join
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM s, t;

        鉴于此结果，我们如何应用连接条件以获取实际需要的行？ 我们只需将连接条件放入 **WHERE** 子句中:

        .. code:: sql

            SELECT * FROM s, t
            WHERE sy = ty;

        这在各方面等同于:

        .. code:: sql

            SELECT *
            FROM
              s
              JOIN t ON sy = ty
            ;

        也就是说，所有通常应放在 **JOIN** 子句中 **ON** 关键字之后的条件都应放在使用隐式连接语法时的 **WHERE** 子句中。 如果你考虑 **s** 和 **t** 的笛卡尔积，就很容易看出如何应用连接条件来过滤笛卡尔积以产生所需结果。 [#]_

        使用隐式连接语法的一个危险在于，它将连接条件与实际连接表的查询部分分开，这使得很容易意外遗漏连接条件。 连接条件被放入 **WHERE** 子句中，连同任何其他单表条件一起。

        如果你使用隐式语法连接 *n* 个表，则始终记住需要 *n - 1* 个连接条件，以确保所有表都连接在一起。 所有表之间必须直接连接或通过其他表的路径连接(如果你熟悉数据结构，表必须是 *连通图* 的节点，通常呈现 *自由树* 的形状，边由连接条件表示)。 请记住，如果任何连接条件是复合的，*n - 1* 个连接条件可能意味着超过 *n - 1* 个 **WHERE** 子句条件。 如果你在编写查询时为每个添加到 **FROM** 子句的新表添加一个连接条件到 **WHERE** 子句中，你可以系统地创建正确的连接结构。

        一个很好的线索，表明你遗漏了连接条件，就是如果你突然得到了比预期更多的行。 如果你更仔细地查看数据(可能需要在 **SELECT** 子句中包含更多列以便查看)，你会发现你创建了一个笛卡尔积。 考虑一个 **books**、**books_awards** 和 **awards** 的隐式连接，其中缺少连接条件:

        .. activecode:: joins_example_missing_join_condition
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT b.title, a.name AS award, ba.year
            FROM books AS b, awards AS a, books_awards AS ba
            WHERE b.book_id = ba.book_id
            -- missing: AND a.award_id = ba.award_id
            ;

        看起来每本获得奖项的书籍都赢得了 *每一个* 奖项！ 这是由于缺失的连接条件导致的笛卡尔积。

        隐式连接语法仅适用于内连接。 一些数据库实现确实提供了使用隐式形式进行外连接的非标准方法，你可能会看到使用这些方法的旧查询。 由于符号有所不同，我们在此不包含任何示例。

        最后要提到的是，笛卡尔积本身通常不是期望的结果。 但是，如果你确实需要笛卡尔积并希望对此进行显式说明，SQL 提供了 **CROSS JOIN** 关键短语用于此目的:

        .. code:: sql

            SELECT * FROM s CROSS JOIN t;

    .. md-tab-item:: 英文

        The ability to do inner joins existed in SQL long before the **JOIN** keyword and related key phrases.  Prior to the introduction of this *explicit* join syntax, joins used an *implicit* join syntax, which is described in this section.  You may prefer the explicit syntax above, and it is considered by many practitioners to be best practice to use it for the clarity it provides.  However, the implicit syntax is supported by all databases and you are very likely to encounter it in practice. Additionally, most databases reduce the explicit syntax to the implicit syntax internally, which has implications for understanding how the database processes join queries.  For these reasons, it is important that you understand the implicit join syntax.

        Returning to our abstract examples from the start of this chapter:

        .. image:: joins1.svg
            :alt: Tables s and t

        In the implicit join syntax, the first step is to simply list all tables involved in the join after the **FROM** clause.  In SQL, this implies a *cross product* of the tables.  In a cross product of two tables, *every* row in one table is paired with *every* row from the other table.  You can see this in action in the query below:

        .. activecode:: joins_example_implicit_join
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM s, t;

        Given this result, how do we apply join conditions to get the rows we actually want?  We simply put our join conditions into the **WHERE** clause:

        .. code:: sql

            SELECT * FROM s, t
            WHERE sy = ty;

        This is equivalent in all respects to:

        .. code:: sql

            SELECT *
            FROM
              s
              JOIN t ON sy = ty
            ;

        That is, all conditions that would normally be put after the **ON** keyword in a **JOIN** clause should be put into the **WHERE** clause when using the implicit join syntax.  If you consider the cross product of **s** and **t**, it is easy to see how applying the join condition to filter the cross product produces the desired result. [#]_

        One danger in using the implicit join syntax is that it separates join conditions from the part of the query that actually joins the tables, making it easy to accidentally leave out a join condition.  The join conditions instead are put into the **WHERE** clause together with any other single-table conditions needed.

        If you are joining together *n* tables using the implicit syntax, then always remember that you need *n - 1* join conditions to ensure that all of the tables are linked in.  It is important that all of the tables connect to each other either directly or through a path of other tables (if you are familiar with data structures, the tables must be the nodes of a *connected graph*, generally in the shape of a *free tree*, with the edges represented by join conditions).  Remember that *n - 1* join conditions may mean more than *n - 1* **WHERE** clause conditions, if any of the join conditions are compound.  If you add a join condition to your **WHERE** clause for each new table you add to the **FROM** clause as you are writing your query, you can systematically create the proper join structure.

        A good clue that you have omitted a join condition is if you suddenly get many more rows than you expected.  If you look more closely at the data (you may need to include more columns in your **SELECT** clause to see it), you can see that you have created a cross product.  Consider an implicit join of **books**, **books_awards**, and **awards** with a missing join condition:

        .. activecode:: joins_example_missing_join_condition
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT b.title, a.name AS award, ba.year
            FROM books AS b, awards AS a, books_awards AS ba
            WHERE b.book_id = ba.book_id
            -- missing: AND a.award_id = ba.award_id
            ;

        It looks like every book that has won an award has won *every* award!  That is due to the cross product resulting from the missing join condition.

        Implicit join syntax is standard only for inner joins.  Some database implementations do provide non-standard ways of doing outer joins using the implicit form, and you may see older queries using these.  Since notations vary, we will not include any examples here.

        As a final note, cross products are seldom a desired result on their own.  However, if you actually need a cross product and wish to be explicit about it, SQL provides the **CROSS JOIN** key phrase for the purpose:

        .. code:: sql

            SELECT * FROM s CROSS JOIN t;


自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含一些使用图书数据集的练习(提醒:你可以在 :ref:`附录 A <appendix-a>` 中获得所有表的完整描述)。 如果你卡住了，请点击练习下方的“显示答案”按钮以查看正确答案。 对于每个练习，首先尝试使用显式连接语法编写答案，然后使用隐式语法(如果可能的话)。

        - 编写查询，列出标题为“The Hobbit”的书籍的所有版本(出版商、年份和出版标题)，

        .. admonition:: 显示答案
            :class: dropdown

            显式:

            .. code:: sql

                SELECT e.publisher, e.publication_year, e.title
                FROM
                  books AS b
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE b.title = 'The Hobbit';

            隐式:

            .. code:: sql

                SELECT e.publisher, e.publication_year, e.title
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title = 'The Hobbit';

        - 编写查询，列出书籍 'The Fellowship of the Ring' 出版的不同标题。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT DISTINCT e.title
                FROM
                  books AS b
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE b.title = 'The Fellowship of the Ring';

                SELECT DISTINCT e.title
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title = 'The Fellowship of the Ring';

        - 编写查询，列出自2005年以来以不同名称出版的版本(标题、对应书籍标题、出版商和出版商位置)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT e.title, b.title, e.publisher, e.publisher_location
                FROM
                  books AS b
                  JOIN editions AS e
                    ON b.book_id = e.book_id AND b.title <> e.title
                WHERE e.publication_year > 2005;

                SELECT e.title, b.title, e.publisher, e.publisher_location
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title <> e.title
                AND   e.publication_year > 2005;

        - 编写查询，列出自2010年以来出版的作者、书籍标题、版本标题和出版商。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT a.name, b.title, e.title, e.publisher
                FROM
                  authors AS a
                  JOIN books AS b ON a.author_id = b.author_id
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE e.publication_year > 2010;

                SELECT a.name, b.title, e.title, e.publisher
                FROM authors AS a, books AS b, editions AS e
                WHERE a.author_id = b.author_id
                AND   b.book_id = e.book_id
                AND   e.publication_year > 2010;

        - 编写查询，返回1996年获得诺斯塔特国际文学奖的作者。 注意:这是 *作者* 奖，而不是 *书籍* 奖。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name
                FROM
                  authors AS au
                  JOIN authors_awards AS aa ON aa.author_id = au.author_id
                  JOIN awards AS aw ON aa.award_id = aw.award_id
                WHERE aw.name = 'Neustadt International Prize for Literature'
                AND   aa.year = 1996;

                SELECT au.name
                FROM authors AS au, authors_awards AS aa, awards AS aw
                WHERE aa.author_id = au.author_id
                AND   aa.award_id = aw.award_id
                AND   aw.name = 'Neustadt International Prize for Literature'
                AND   aa.year = 1996;

        - 编写查询，列出获得作者奖项的作者及其奖项和获奖年份。 给输出描述性标题(而不仅仅是“name”和“name”)。 按作者姓名排序。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name AS author, aw.name AS award, aa.year
                FROM
                  authors AS au
                  JOIN authors_awards AS aa ON aa.author_id = au.author_id
                  JOIN awards AS aw ON aa.award_id = aw.award_id
                ORDER BY au.name;

                SELECT au.name AS author, aw.name AS award, aa.year
                FROM authors AS au, authors_awards AS aa, awards AS aw
                WHERE aa.author_id = au.author_id
                AND   aa.award_id = aw.award_id
                ORDER BY au.name;

        - 编写查询，列出所有作者及其(作者)奖项(如果有)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name AS author, aw.name AS award, aa.year
                FROM
                  authors AS au
                  LEFT JOIN authors_awards AS aa ON aa.author_id = au.author_id
                  LEFT JOIN awards AS aw ON aa.award_id = aw.award_id
                ORDER BY au.name;

        - 编写查询，列出未获得我们数据库中列出的任何作者奖项的作者。 提示:你如何在上面的查询中检测奖项的缺失？

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name
                FROM
                  authors AS au
                  LEFT JOIN authors_awards AS aa ON aa.author_id = au.author_id
                WHERE aa.author_id IS NULL;

        - 编写查询，列出“Interpreter of Maladies”的作者的所有书籍。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT b1.title
                FROM
                  books AS b1
                  JOIN books AS b2 ON b2.author_id = b1.author_id
                WHERE b2.title = 'Interpreter of Maladies';

                SELECT b1.title
                FROM books AS b1, books AS b2
                WHERE b1.author_id = b2.author_id
                AND   b2.title = 'Interpreter of Maladies';

        - 与上面相同，但显示作者的名字。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT b1.title, a.name
                FROM
                  books AS b1
                  JOIN authors AS a ON b1.author_id = a.author_id
                  JOIN books AS b2 ON b2.author_id = a.author_id
                WHERE b2.title = 'Interpreter of Maladies';

                SELECT b1.title, a.name
                FROM books AS b1, books AS b2, authors AS a
                WHERE b1.author_id = a.author_id
                AND   b2.author_id = a.author_id
                AND   b2.title = 'Interpreter of Maladies';

        - 使用 **books** 和 **authors** 表，查找与 *The Three-Body Problem* 同年出版的所有书籍(作者和标题)，排除 *The Three-Body Problem* 本身。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT a.name, b2.title
                FROM
                  books AS b1
                  JOIN books AS b2
                    ON
                      b1.publication_year = b2.publication_year
                      AND b2.book_id <> b1.book_id
                  JOIN authors AS a ON a.author_id = b2.author_id
                WHERE b1.title = 'The Three-Body Problem';

                SELECT a.name, b2.title
                FROM books AS b1, books AS b2, authors AS a
                WHERE b1.publication_year = b2.publication_year
                AND   b2.book_id <> b1.book_id
                AND   a.author_id = b2.author_id
                AND   b1.title = 'The Three-Body Problem';

        - 编写查询，列出获得星云奖的书籍(作者、名称和标题)。 显示获奖年份，并首先列出最近的奖项。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name AS author, b.title, ba.year
                FROM
                  authors AS au
                  JOIN books AS b ON au.author_id = b.author_id
                  JOIN books_awards AS ba ON b.book_id = ba.book_id
                  JOIN awards AS aw ON aw.award_id = ba.award_id
                WHERE aw.name = 'Nebula Award'
                ORDER BY ba.year DESC;

                SELECT au.name AS author, b.title, ba.year
                FROM authors AS au, books AS b, books_awards AS ba, awards AS aw
                WHERE au.author_id = b.author_id
                AND   b.book_id = ba.book_id
                AND   aw.award_id = ba.award_id
                AND   aw.name = 'Nebula Award'
                ORDER BY ba.year DESC;

        - 编写查询，给出获得诺贝尔文学奖(作者奖)的作者赢得的书籍奖项的不同列表。

        .. admonition:: 显本节包含一些使用图书数据集的练习(提醒:你可以在 :ref:`附录 A <appendix-a>` 中获得所有表的完整描述)。 如果你卡住了，请点击练习下方的“显示答案”按钮以查看正确答案。 对于每个练习，首先尝试使用显式连接语法编写答案，然后使用隐式语法(如果可能的话)。

        - 编写查询，列出标题为“The Hobbit”的书籍的所有版本(出版商、年份和出版标题)，

        .. admonition:: 显示答案
            :class: dropdown

            显式:

            .. code:: sql

                SELECT e.publisher, e.publication_year, e.title
                FROM
                  books AS b
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE b.title = 'The Hobbit';

            隐式:

            .. code:: sql

                SELECT e.publisher, e.publication_year, e.title
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title = 'The Hobbit';

        - 编写查询，列出书籍 'The Fellowship of the Ring' 出版的不同标题。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT DISTINCT e.title
                FROM
                  books AS b
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE b.title = 'The Fellowship of the Ring';

                SELECT DISTINCT e.title
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title = 'The Fellowship of the Ring';

        - 编写查询，列出自2005年以来以不同名称出版的版本(标题、对应书籍标题、出版商和出版商位置)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT e.title, b.title, e.publisher, e.publisher_location
                FROM
                  books AS b
                  JOIN editions AS e
                    ON b.book_id = e.book_id AND b.title <> e.title
                WHERE e.publication_year > 2005;

                SELECT e.title, b.title, e.publisher, e.publisher_location
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title <> e.title
                AND   e.publication_year > 2005;

        - 编写查询，列出自2010年以来出版的作者、书籍标题、版本标题和出版商。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT a.name, b.title, e.title, e.publisher
                FROM
                  authors AS a
                  JOIN books AS b ON a.author_id = b.author_id
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE e.publication_year > 2010;

                SELECT a.name, b.title, e.title, e.publisher
                FROM authors AS a, books AS b, editions AS e
                WHERE a.author_id = b.author_id
                AND   b.book_id = e.book_id
                AND   e.publication_year > 2010;

        - 编写查询，返回1996年获得诺斯塔特国际文学奖的作者。 注意:这是 *作者* 奖，而不是 *书籍* 奖。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name
                FROM
                  authors AS au
                  JOIN authors_awards AS aa ON aa.author_id = au.author_id
                  JOIN awards AS aw ON aa.award_id = aw.award_id
                WHERE aw.name = 'Neustadt International Prize for Literature'
                AND   aa.year = 1996;

                SELECT au.name
                FROM authors AS au, authors_awards AS aa, awards AS aw
                WHERE aa.author_id = au.author_id
                AND   aa.award_id = aw.award_id
                AND   aw.name = 'Neustadt International Prize for Literature'
                AND   aa.year = 1996;

        - 编写查询，列出获得作者奖项的作者及其奖项和获奖年份。 给输出描述性标题(而不仅仅是“name”和“name”)。 按作者姓名排序。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name AS author, aw.name AS award, aa.year
                FROM
                  authors AS au
                  JOIN authors_awards AS aa ON aa.author_id = au.author_id
                  JOIN awards AS aw ON aa.award_id = aw.award_id
                ORDER BY au.name;

                SELECT au.name AS author, aw.name AS award, aa.year
                FROM authors AS au, authors_awards AS aa, awards AS aw
                WHERE aa.author_id = au.author_id
                AND   aa.award_id = aw.award_id
                ORDER BY au.name;

        - 编写查询，列出所有作者及其(作者)奖项(如果有)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name AS author, aw.name AS award, aa.year
                FROM
                  authors AS au
                  LEFT JOIN authors_awards AS aa ON aa.author_id = au.author_id
                  LEFT JOIN awards AS aw ON aa.award_id = aw.award_id
                ORDER BY au.name;

        - 编写查询，列出未获得我们数据库中列出的任何作者奖项的作者。 提示:你如何在上面的查询中检测奖项的缺失？

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name
                FROM
                  authors AS au
                  LEFT JOIN authors_awards AS aa ON aa.author_id = au.author_id
                WHERE aa.author_id IS NULL;

        - 编写查询，列出“Interpreter of Maladies”的作者的所有书籍。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT b1.title
                FROM
                  books AS b1
                  JOIN books AS b2 ON b2.author_id = b1.author_id
                WHERE b2.title = 'Interpreter of Maladies';

                SELECT b1.title
                FROM books AS b1, books AS b2
                WHERE b1.author_id = b2.author_id
                AND   b2.title = 'Interpreter of Maladies';

        - 与上面相同，但显示作者的名字。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT b1.title, a.name
                FROM
                  books AS b1
                  JOIN authors AS a ON b1.author_id = a.author_id
                  JOIN books AS b2 ON b2.author_id = a.author_id
                WHERE b2.title = 'Interpreter of Maladies';

                SELECT b1.title, a.name
                FROM books AS b1, books AS b2, authors AS a
                WHERE b1.author_id = a.author_id
                AND   b2.author_id = a.author_id
                AND   b2.title = 'Interpreter of Maladies';

        - 使用 **books** 和 **authors** 表，查找与 *The Three-Body Problem* 同年出版的所有书籍(作者和标题)，排除 *The Three-Body Problem* 本身。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT a.name, b2.title
                FROM
                  books AS b1
                  JOIN books AS b2
                    ON
                      b1.publication_year = b2.publication_year
                      AND b2.book_id <> b1.book_id
                  JOIN authors AS a ON a.author_id = b2.author_id
                WHERE b1.title = 'The Three-Body Problem';

                SELECT a.name, b2.title
                FROM books AS b1, books AS b2, authors AS a
                WHERE b1.publication_year = b2.publication_year
                AND   b2.book_id <> b1.book_id
                AND   a.author_id = b2.author_id
                AND   b1.title = 'The Three-Body Problem';

        - 编写查询，列出获得星云奖的书籍(作者、名称和标题)。 显示获奖年份，并首先列出最近的奖项。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT au.name AS author, b.title, ba.year
                FROM
                  authors AS au
                  JOIN books AS b ON au.author_id = b.author_id
                  JOIN books_awards AS ba ON b.book_id = ba.book_id
                  JOIN awards AS aw ON aw.award_id = ba.award_id
                WHERE aw.name = 'Nebula Award'
                ORDER BY ba.year DESC;

                SELECT au.name AS author, b.title, ba.year
                FROM authors AS au, books AS b, books_awards AS ba, awards AS aw
                WHERE au.author_id = b.author_id
                AND   b.book_id = ba.book_id
                AND   aw.award_id = ba.award_id
                AND   aw.name = 'Nebula Award'
                ORDER BY ba.year DESC;

        - 编写查询，给出获得诺贝尔文学奖(作者奖)的作者赢得的书籍奖项的不同列表。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT DISTINCT aw1.name
                FROM
                  books AS b
                  JOIN books_awards AS ba ON b.book_id = ba.book_id
                  JOIN awards AS aw1 ON aw1.award_id = ba.award_id  -- 书籍奖项
                  JOIN authors_awards AS aa ON b.author_id = aa.author_id
                  JOIN awards AS aw2 ON aw2.award_id = aa.award_id  -- 作者奖项
                WHERE aw2.name = 'Nobel Prize in Literature';

                SELECT DISTINCT aw1.name
                FROM
                  books AS b,
                  books_awards AS ba,
                  awards AS aw1,         -- 书籍奖项
                  authors_awards AS aa,
                  awards AS aw2          -- 作者奖项
                WHERE b.book_id = ba.book_id
                AND   aw1.award_id = ba.award_id
                AND   b.author_id = aa.author_id
                AND   aw2.award_id = aa.award_id
                AND   aw2.name = 'Nobel Prize in Literature';

    .. md-tab-item:: 英文

        This section contains some exercises using the books data set (reminder: you can get full descriptions of all tables in :ref:`Appendix A <appendix-a>`).  If you get stuck, click on the "Show answer" button below the exercise to see a correct answer.  For each of these, try writing the answer using explicit join syntax first, and then using the implicit syntax (where possible).

        - Write a query listing all of the editions (publisher, year, and published title) for the book titled "The Hobbit",

        .. admonition:: Show answer
            :class: dropdown

            Explicit:

            .. code:: sql

                SELECT e.publisher, e.publication_year, e.title
                FROM
                  books AS b
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE b.title = 'The Hobbit';

            Implicit:

            .. code:: sql

                SELECT e.publisher, e.publication_year, e.title
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title = 'The Hobbit';

        - Write a query listing the distinct titles under which the book 'The Fellowship of the Ring' was published.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT DISTINCT e.title
                FROM
                  books AS b
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE b.title = 'The Fellowship of the Ring';

                SELECT DISTINCT e.title
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title = 'The Fellowship of the Ring';

        - Write a query listing editions (title, corresponding book title, publisher, and publisher location) that were published since 2005 under a different name than the book.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT e.title, b.title, e.publisher, e.publisher_location
                FROM
                  books AS b
                  JOIN editions AS e
                    ON b.book_id = e.book_id AND b.title <> e.title
                WHERE e.publication_year > 2005;

                SELECT e.title, b.title, e.publisher, e.publisher_location
                FROM books AS b, editions AS e
                WHERE b.book_id = e.book_id
                AND   b.title <> e.title
                AND   e.publication_year > 2005;

        - Write a query listing author, book title, edition title, and publisher for editions published since 2010.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT a.name, b.title, e.title, e.publisher
                FROM
                  authors AS a
                  JOIN books AS b ON a.author_id = b.author_id
                  JOIN editions AS e ON b.book_id = e.book_id
                WHERE e.publication_year > 2010;

                SELECT a.name, b.title, e.title, e.publisher
                FROM authors AS a, books AS b, editions AS e
                WHERE a.author_id = b.author_id
                AND   b.book_id = e.book_id
                AND   e.publication_year > 2010;

        - Write a query returning the author who won the Neustadt International Prize for Literature in 1996. Note: this is an *author* award, not a *book* award.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT au.name
                FROM
                  authors AS au
                  JOIN authors_awards AS aa ON aa.author_id = au.author_id
                  JOIN awards AS aw ON aa.award_id = aw.award_id
                WHERE aw.name = 'Neustadt International Prize for Literature'
                AND   aa.year = 1996;

                SELECT au.name
                FROM authors AS au, authors_awards AS aa, awards AS aw
                WHERE aa.author_id = au.author_id
                AND   aa.award_id = aw.award_id
                AND   aw.name = 'Neustadt International Prize for Literature'
                AND   aa.year = 1996;

        - Write a query to list the authors who have won author awards, together with their awards and the year of the award. Give the output descriptive headers (not just "name" and "name").  Order by author name.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT au.name AS author, aw.name AS award, aa.year
                FROM
                  authors AS au
                  JOIN authors_awards AS aa ON aa.author_id = au.author_id
                  JOIN awards AS aw ON aa.award_id = aw.award_id
                ORDER BY au.name;

                SELECT au.name AS author, aw.name AS award, aa.year
                FROM authors AS au, authors_awards AS aa, awards AS aw
                WHERE aa.author_id = au.author_id
                AND   aa.award_id = aw.award_id
                ORDER BY au.name;

        - Write a query listing all authors, together with their (author) awards, if any.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

              SELECT au.name AS author, aw.name AS award, aa.year
              FROM
                authors AS au
                LEFT JOIN authors_awards AS aa ON aa.author_id = au.author_id
                LEFT JOIN awards AS aw ON aa.award_id = aw.award_id
              ORDER BY au.name;

        - Write a query listing authors who have *not* won any of the author awards listed in our database. Hint: how might you detect the absence of an award in the query above?

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT au.name
                FROM
                  authors AS au
                  LEFT JOIN authors_awards AS aa ON aa.author_id = au.author_id
                WHERE aa.author_id IS NULL;


        - Write a query listing all the books by the author of "Interpreter of Maladies".

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT b1.title
                FROM
                  books AS b1
                  JOIN books AS b2 ON b2.author_id = b1.author_id
                WHERE b2.title = 'Interpreter of Maladies';

                SELECT b1.title
                FROM books AS b1, books AS b2
                WHERE b1.author_id = b2.author_id
                AND   b2.title = 'Interpreter of Maladies';


        - Same as above, but show the author's name as well.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT b1.title, a.name
                FROM
                  books AS b1
                  JOIN authors AS a ON b1.author_id = a.author_id
                  JOIN books AS b2 ON b2.author_id = a.author_id
                WHERE b2.title = 'Interpreter of Maladies';

                SELECT b1.title, a.name
                FROM books AS b1, books AS b2, authors AS a
                WHERE b1.author_id = a.author_id
                AND   b2.author_id = a.author_id
                AND   b2.title = 'Interpreter of Maladies';


        - Using the **books** and **authors** tables, find all books (author and title) published in the same year as *The Three-Body Problem*, excluding *The Three-Body Problem* itself.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT a.name, b2.title
                FROM
                  books AS b1
                  JOIN books AS b2
                    ON
                      b1.publication_year = b2.publication_year
                      AND b2.book_id <> b1.book_id
                  JOIN authors AS a ON a.author_id = b2.author_id
                WHERE b1.title = 'The Three-Body Problem';

                SELECT a.name, b2.title
                FROM books AS b1, books AS b2, authors AS a
                WHERE b1.publication_year = b2.publication_year
                AND   b2.book_id <> b1.book_id
                AND   a.author_id = b2.author_id
                AND   b1.title = 'The Three-Body Problem';


        - Write a query to list books (author, name, and title) that have won the Nebula Award. Show the year of the award and list the most recent awards first.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT au.name AS author, b.title, ba.year
                FROM
                  authors AS au
                  JOIN books AS b ON au.author_id = b.author_id
                  JOIN books_awards AS ba ON b.book_id = ba.book_id
                  JOIN awards AS aw ON aw.award_id = ba.award_id
                WHERE aw.name = 'Nebula Award'
                ORDER BY ba.year DESC;

                SELECT au.name AS author, b.title, ba.year
                FROM authors AS au, books AS b, books_awards AS ba, awards AS aw
                WHERE au.author_id = b.author_id
                AND   b.book_id = ba.book_id
                AND   aw.award_id = ba.award_id
                AND   aw.name = 'Nebula Award'
                ORDER BY ba.year DESC;

        - Write a query giving a distinct list of book awards won by authors who have also won the Nobel Prize in Literature (an author award).

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT DISTINCT aw1.name
                FROM
                  books AS b
                  JOIN books_awards AS ba ON b.book_id = ba.book_id
                  JOIN awards AS aw1 ON aw1.award_id = ba.award_id  -- book awards
                  JOIN authors_awards AS aa ON b.author_id = aa.author_id
                  JOIN awards AS aw2 ON aw2.award_id = aa.award_id  -- author awards
                WHERE aw2.name = 'Nobel Prize in Literature';

                SELECT DISTINCT aw1.name
                FROM
                  books AS b,
                  books_awards AS ba,
                  awards AS aw1,         -- book awards
                  authors_awards AS aa,
                  awards AS aw2          -- author awards
                WHERE b.book_id = ba.book_id
                AND   aw1.award_id = ba.award_id
                AND   b.author_id = aa.author_id
                AND   aw2.award_id = aa.award_id
                AND   aw2.name = 'Nobel Prize in Literature';




----

**Notes**

.. [#] 由于如果我们在数据库中包含所有书籍的所有已知版本，数据库将会相当庞大(用于你的网页浏览器)，因此 **editions** 表仅包含作者 J.R.R. Tolkien 的书籍的版本。 **editions** 数据尤其“脏”，因为有许多信息缺失，数据的准确性和完整性存疑。你可以在 :ref:`附录 A <appendix-a>` 中阅读有关数据及其收集方式的更多信息。

.. [#] Because the database would be rather large (for use in your web browser) if we included all the known editions of all of the books in our database, the **editions** table only contains editions for books by author J.R.R. Tolkien.  The **editions** data is particularly "dirty", in the sense that there are many missing pieces of information, and the accuracy and completeness of the data are questionable. You can read more about the data and how it was collected in :ref:`Appendix A <appendix-a>`.

.. [#] 你可以认为 **books** 表应该存储一个 *数组* 的奖项 ID，而不是仅仅一个奖项 ID，这样就解决了这个困境。这在一些支持数组值列的数据库实现中是可行的。然而，使用这样的列并非没有争议。在本教科书中，我们将采用使用交叉引用表的更常见的方法。

.. [#] You could argue that the **books** table should store an *array* of award ids, instead of just a single award id, thus solving the dilemma.  This is actually possible in a few database implementations that support array-valued columns.  However, the use of such columns is not without controversy.  For this textbook, we will take the more common approach of using cross-reference tables.

.. [#] 由于交叉积的行数等于一个表中的行数乘以另一个表中的行数，当涉及的表很大时，乘积会非常庞大。尽管数据库通常会将显式连接在内部转换为隐式连接，但在处理连接时，数据库系统通常不会创建交叉积，然后应用 **WHERE** 子句条件，因为那样会非常慢，并且需要大量内存或临时存储。然而，这一概念模型有助于理解最终结果。

.. [#] Because a cross product has a number of rows equal to the number of rows in one table times the number of rows in the other table, the product is very large when the tables involved are large.  Even though databases typically convert explicit joins to their implicit equivalents internally, when database systems process joins they generally do not create the cross product and then apply the **WHERE** clause conditions, as that would be very slow and require a lot of memory or temporary storage.  However, the conceptual model is helpful in understanding the end result.


