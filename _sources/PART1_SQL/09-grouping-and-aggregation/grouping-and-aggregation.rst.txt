.. _grouping-chapter:

========================
分组和聚合
========================

**Grouping and aggregation**

.. md-tab-set::

    .. md-tab-item:: 中文

        前面的章节集中于数据的存储和检索机制。SQL 还提供了对数据进行简单分析的功能。在本章中，我们将讨论数据分区的方法以及对分区进行简单统计计算的方法。

    .. md-tab-item:: 英文

        Previous chapters have focused on mechanisms for storing and retrieving data.  SQL also provides facilities for simple analyses of the data.  In this chapter, we discuss methods of partitioning data and computing simple statistics on the partitions.


本章中使用的表格
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中，我们将主要使用 **bookstore_inventory** 和 **bookstore_sales** 表，这些表模拟了一个二手书商可能参考的简单数据库。**bookstore_inventory** 表列出了书店库存的印刷书籍或最近销售的书籍，包括书籍的状态和标价。当书店销售一本书时，会在 **bookstore_sales** 表中添加一条记录。该表列出了所售书籍的 **stock_number**、销售日期和付款方式。**stock_number** 列是库存中每本书的唯一标识符，可用于连接这两个表。

        我们还将使用 **authors** 表来说明 ``NULL`` 与聚合函数的交互。

        有关这些表的完整描述，请参见 :ref:`Appendix A <appendix-a>`。

    .. md-tab-item:: 英文

        For this chapter, we will primarily work with the tables **bookstore_inventory** and **bookstore_sales**, which simulate a simple database that a seller of used books might reference.  The **bookstore_inventory** table lists printed books that the bookstore either has in stock or has sold recently, along with the condition of the book and the asking price.  When the bookstore sells a book, a record is added to the **bookstore_sales** table.  This table lists the **stock_number** of the book sold, the date sold, and the type of payment.  The column **stock_number** is a unique identifier for each book in the inventory, and can be used to join the tables.

        We will also use the **authors** table to illustrate the interaction of ``NULL`` with aggregate functions.

        A full description of these tables can be found in :ref:`Appendix A <appendix-a>`.

.. index:: aggregate statistic, aggregate function, COUNT, SUM, AVG, MIN, MAX

聚合统计数据
::::::::::::::::::::

**Aggregate statistics**

.. md-tab-set::

    .. md-tab-item:: 中文

        *聚合统计* 是在整个数据集上计算的值。计数、总和和平均值是聚合统计的示例。SQL 提供了多个聚合函数来计算这些统计值。本节将涵盖一些最常用的函数；有关 SQL 定义的所有聚合函数的文档，请参见附录 B - :ref:`appendix-b-aggregate-functions`。

        我们首先使用 **COUNT** 聚合函数来说明聚合函数的基本规则。在最简单的情况下，**COUNT** 可用于返回表中的行数：

        .. activecode:: grouping_example_aggregate
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT COUNT(*) FROM bookstore_sales;

        如果添加 **WHERE** 子句，**COUNT** 只会考虑符合 **WHERE** 子句的行：

        .. code:: sql

            SELECT COUNT(*)
            FROM bookstore_sales
            WHERE payment = 'cash';

        在聚合函数中使用 **\*** 是 **COUNT** 特有的；它仅表示我们希望计算行数，而不是特定的列。其他聚合函数需要应用于某一列或表达式。当应用于某一列或表达式时，**COUNT** 和其他聚合函数会忽略 ``NULL`` 值。例如，观察在 **authors** 表的不同列上应用 **COUNT** 时的结果：

        .. code:: sql

            SELECT COUNT(*), COUNT(author_id), COUNT(birth), COUNT(death)
            FROM authors;

        在上述每个结果中，我们为 **SELECT** 子句中的每个函数获得一个数字。只返回一行，因为我们（此时）将聚合函数应用于与（可选）**WHERE** 子句匹配的所有行。这一行代表数据的 *摘要*。作为摘要，数据的细节无法包含；当使用任何聚合函数时，尝试检索任何非聚合列的表达式都是错误的。以下查询在除了 SQLite 的所有数据库中都会导致错误：

        .. code:: sql

            SELECT title, COUNT(*) FROM bookstore_inventory;

        虽然 SQLite 不会给我们错误，但返回的数据表明了为什么在大多数数据库中这是一个错误；返回的 **title** 值仅代表表中的一行，而 **COUNT(\*)** 值是整个表的摘要。这两者不匹配。

        除了 **COUNT**，SQLite 实现的最常见聚合函数还有 **SUM**、**AVG**、**MIN** 和 **MAX**。SQL 还定义了许多其他聚合函数，包括方差和标准差等统计函数。与 **COUNT** 一样，该函数的参数是一个列或表达式，会针对每一行进行评估；``NULL`` 值会被丢弃。对于所有聚合函数（除了 **COUNT**），如果参数在每一行上都评估为 ``NULL``，那么结果也是 ``NULL``（对于 **COUNT**，结果是零）。

        您可能能猜到这些聚合函数的含义：

        - **SUM** 计算总和，只能应用于数字
        - **AVG** 计算平均值，只能应用于数字
        - **MIN** 根据值类型的正常排序顺序查找最小值
        - **MAX** 根据值类型的正常排序顺序查找最大值

        我们可以将这些函数应用于 **bookstore_inventory** 的 **price** 列：

        .. code:: sql

            SELECT COUNT(price), SUM(price), AVG(price), MIN(price), MAX(price)
            FROM bookstore_inventory;

        除了忽略 ``NULL`` 值外，可以通过在聚合函数的参数前加上 **DISTINCT** 关键字来指示应忽略重复值。这在与 **COUNT** 结合使用时特别有用。例如，如果我们想知道库存中的书籍总数与唯一书名的数量，我们可以写：

        .. code:: sql

            SELECT COUNT(title), COUNT(DISTINCT title) FROM bookstore_inventory;

    .. md-tab-item:: 英文

        *Aggregate statistics* are values computed on entire sets of data.  Counts, sums, and averages are examples of aggregate statistics.  SQL provides a number of aggregate functions for computing such statistics.  This section will cover some of the most commonly used functions; for documentation on all of the aggregate functions defined by SQL, see Appendix B - :ref:`appendix-b-aggregate-functions`.

        We start by using the **COUNT** aggregate function to illustrate the basic rules for aggregate functions.  At its simplest, **COUNT** can be used to return the number of rows in a table:

        .. activecode:: grouping_example_aggregate
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT COUNT(*) FROM bookstore_sales;

        If you add a **WHERE** clause, **COUNT** will only consider rows matching the **WHERE** clause:

        .. code:: sql

            SELECT COUNT(*)
            FROM bookstore_sales
            WHERE payment = 'cash';

        The use of **\*** within the aggregate function is unique to **COUNT**; it simply means that we want to count rows, rather than any particular column.  Other aggregate functions require application to a column or expression.  When applied to a column or expression, **COUNT** and the other aggregate functions ignore ``NULL`` values.  For example, observe the result when applying **COUNT** to different columns of the **authors** table:

        .. code:: sql

            SELECT COUNT(*), COUNT(author_id), COUNT(birth), COUNT(death)
            FROM authors;

        In each of the results above, we obtain a single number for each function in the **SELECT** clause.  Only one row is returned, because we are (at the moment) applying the aggregate function to all rows matching the (optional) **WHERE** clause.  This row represents a *summary* of the data.  As a summary, details of the data cannot be included; it is an error to try to retrieve any expressions on the columns other than aggregates, when any aggregate function is used.  The following query will result in an error in every database except SQLite:

        .. code:: sql

            SELECT title, COUNT(*) FROM bookstore_inventory;

        While SQLite does not give us an error, the data returned demonstrates why this is an error in most databases; the returned **title** value represents just one row of the table, while the **COUNT(\*)** value is a summary of the whole table.  These two things do not match.

        In addition to **COUNT**, the most common aggregate functions implemented by SQLite are **SUM**, **AVG**, **MIN**, and **MAX**.  SQL defines a number of other aggregate functions as well, including statistical functions such as variance and standard deviation.  As with **COUNT**, the argument of the function is a column or expression, which is evaluated for every row; ``NULL`` values are discarded.  For all aggregates except **COUNT**, if the argument evaluates to ``NULL`` for every row, then the result is ``NULL`` (for **COUNT** the result is zero).

        You can probably guess the meaning of these aggregate functions:

        - **SUM** computes the sum, and can only be applied to numbers
        - **AVG** computes the average, and can only be applied to numbers
        - **MIN** finds the minimum value according to the normal sort order for the value type
        - **MAX** finds the maximum value according to the normal sort order for the value type

        We can apply all of these to the **price** column of **bookstore_inventory**:

        .. code:: sql

            SELECT COUNT(price), SUM(price), AVG(price), MIN(price), MAX(price)
            FROM bookstore_inventory;

        In addition to ignoring ``NULL`` values, it is possible to indicate that duplicate values should be ignored by putting the **DISTINCT** keyword before the argument of the aggregate function.  This is mostly useful when combined with **COUNT**.  For example, if we want to know the total number of books versus the number of unique titles in our inventory, we could write:

        .. code:: sql

            SELECT COUNT(title), COUNT(DISTINCT title) FROM bookstore_inventory;

.. index:: grouping, GROUP BY

分组
::::::::

**Grouping**

.. md-tab-set::

    .. md-tab-item:: 中文

        聚合在应用于整个表或与 **WHERE** 子句匹配的一组行时非常有用。然而，有时我们希望从一个表中获取多个计数、总和或平均值；我们可能希望对某些行的子集进行这些统计，并按某个公共属性进行组织。例如，我们的 **bookstore_inventory** 表包含不同状态的书籍；我们可能想分别了解我们对“良好”状态书籍和“一般”状态书籍的平均定价，等等。

        SQL 为此提供了 **GROUP BY** 子句。**GROUP BY** 允许我们指定一个属性，例如书籍的状态，以将表组织成 *组*。特定组的成员资格基于 **GROUP BY** 表达式；每组的所有成员在该表达式上具有相同的值。这些组形成数据的 *分区*；每一行（如果使用，则匹配可选的 **WHERE** 子句）都被分配到一个组中，并且没有行被分配到多个组。

        在 **GROUP BY** 生效的情况下，我们现在可以检索关于每个组的整体信息；我们输出的每一行将代表一个组的信息。如果我们在 **SELECT** 子句中放入聚合函数表达式，则聚合会单独应用于每个组的行。除了聚合之外，我们还可以 **SELECT** **GROUP BY** 表达式——这是被允许的（并且是有意义的），因为每组中的所有行对于该表达式将具有相同的值。您通常希望包括分组表达式作为组的标签——否则，您将不知道每个聚合表达式属于哪个组！

        **GROUP BY** 子句紧接在 **WHERE** 子句之后，或在没有 **WHERE** 子句时紧接在 **FROM** 之后。以下是按书籍状态对我们的书店库存进行分组的示例：

        .. activecode:: grouping_example_grouping
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT condition, COUNT(*), AVG(price)
            FROM bookstore_inventory
            GROUP BY condition;

        如果我们想排除已售出的书籍，可以添加 **WHERE** 子句（在这里我们使用一个子查询，如 :numref:`Chapter {number} <subqueries-chapter>` 中讨论的那样）：

        .. code:: sql

            SELECT condition, COUNT(*), AVG(price)
            FROM bookstore_inventory
            WHERE stock_number NOT IN
            (SELECT stock_number FROM bookstore_sales)
            GROUP BY condition;

        也可以按多个表达式进行分组，在这种情况下，每组由所有表达式的唯一设置定义。我们的 **bookstore_sales** 表包含书籍售出的日期信息以及购买时使用的付款类型。我们可能非常希望了解按月份或按付款类型的销售总额，或两者都了解。为了获取支付的价格，我们将需要连接 **bookstore_inventory** 表。

        首先，让我们按月份检索销售总额（在这里我们将使用 SQLite 的 substring() 函数提取两位数的月份；在其他数据库中，可能可以通过名称提取月份）：

        .. code:: sql

            SELECT
            substring(s.date_sold, 6, 2) AS month,
            SUM(i.price) AS total_sales
            FROM
            bookstore_sales AS s
            JOIN bookstore_inventory AS i ON s.stock_number = i.stock_number
            GROUP BY month;

        请注意，我们可以在 **GROUP BY** 子句中使用在 **SELECT** 子句中定义的别名“month”，而无需重写函数表达式。

        现在，让我们按月份 *和* 付款类型细分我们的销售总额：

        .. code:: sql

            SELECT
            substring(s.date_sold, 6, 2) AS month,
            s.payment,
            SUM(i.price) AS total_sales
            FROM
            bookstore_sales AS s
            JOIN bookstore_inventory AS i ON s.stock_number = i.stock_number
            GROUP BY month, s.payment
            ORDER BY month, s.payment;

        在这里，我们还按分组表达式进行了排序，以确保我们的组以一致的方式出现。

    .. md-tab-item:: 英文

        Aggregates can be very useful when applied to an entire table or to a set of rows matching a **WHERE** clause.  Sometimes, though, we want more than one count, or sum, or average from a table; we may want these statistics over some subsets of rows, organized by some common attribute.  For example, our **bookstore_inventory** table includes books in different conditions; we might be interested in the average price we are charging for books in "good" condition separately from books in "fair" condition, and so forth.

        SQL provides the **GROUP BY** clause for this purpose.  **GROUP BY** lets us specify an attribute, such as the condition of a book, by which to organize a table into *groups*.  Membership in a specific group is based on the **GROUP BY** expression; all members of a group share the same value for the expression.  The groups form a *partition* of the data; every row (matching the optional **WHERE** clause, if used) is assigned to a group, and no row is assigned to more than one group.

        With **GROUP BY** in effect, we can now retrieve information about each group as a whole; each row of our output will represent information about one group.  If we put an aggregate function expression in our **SELECT** clause, the aggregate is applied to each group's rows separately.  In addition to aggregates, we can **SELECT** the **GROUP BY** expression - this is allowed (and makes sense) because all of the rows in each group will have the same value for the expression. You usually want to include the grouping expression as a label for the group - otherwise you will not know what group each aggregate expression belongs to!

        The **GROUP BY** clause comes immediately after the **WHERE** clause, or after **FROM** if there is no **WHERE** clause.  Here is an example of grouping on our bookstore inventory by book condition:

        .. activecode:: grouping_example_grouping
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT condition, COUNT(*), AVG(price)
            FROM bookstore_inventory
            GROUP BY condition;

        If we want to exclude books that have already been sold, we could add a **WHERE** clause (here we use a subquery as discussed in :numref:`Chapter {number} <subqueries-chapter>`):

        .. code:: sql

            SELECT condition, COUNT(*), AVG(price)
            FROM bookstore_inventory
            WHERE stock_number NOT IN
            (SELECT stock_number FROM bookstore_sales)
            GROUP BY condition;

        It is also possible to group by more than one expression, in which case each group is defined by a unique setting for all of the expressions.  Our **bookstore_sales** table contains information about the date in which a book was sold, as well as the type of payment used in the purchase.  We might be very interested in knowing sales totals by month, or by type of payment, or both.  To get the price that was paid, we will have to join in the **bookstore_inventory** table.

        To start with, let's retrieve sales totals by month (here we will use SQLite's substring() function to extract the 2-digit month number; in other databases it may be possible to extract a month by name):

        .. code:: sql

            SELECT
            substring(s.date_sold, 6, 2) AS month,
            SUM(i.price) AS total_sales
            FROM
            bookstore_sales AS s
            JOIN bookstore_inventory AS i ON s.stock_number = i.stock_number
            GROUP BY month;

        Note that we can use the alias "month" defined in our **SELECT** clause in our **GROUP BY** clause without having to rewrite the function expression.

        Now, let's break down our total sales by type of month *and* type of payment:

        .. code:: sql

            SELECT
            substring(s.date_sold, 6, 2) AS month,
            s.payment,
            SUM(i.price) AS total_sales
            FROM
            bookstore_sales AS s
            JOIN bookstore_inventory AS i ON s.stock_number = i.stock_number
            GROUP BY month, s.payment
            ORDER BY month, s.payment;

        Here we have sorted by our grouping expressions as well, just to ensure that our groups come out in a consistent fashion.

.. index:: HAVING

过滤分组数据
----------------------

**Filtering grouped data**

.. md-tab-set::

    .. md-tab-item:: 中文

        当我们进行分组时，我们生成了一组新的行，代表数据中存在的组。如果在查询中包含 **WHERE** 子句，它将应用于 *分组之前* 的数据。因此，**WHERE** 子句不能用于过滤由分组生成的行集。如果我们想过滤分组后的数据，必须使用 **HAVING** 子句。

        **HAVING** 子句的工作方式与 **WHERE** 子句类似，但适用于由分组生成的行集。使用 **HAVING**，我们可以按分组后可用的表达式进行过滤：任何我们分组的表达式（我们的组标签）或对组的聚合函数。**HAVING** 子句位于 **GROUP BY** 子句之后。

        在这里，我们使用 **HAVING** 列出我们书店库存中有多于一本副本的书籍，并按副本数量排序：

        .. code:: sql

            SELECT author, title, COUNT(*)
            FROM bookstore_inventory
            GROUP BY author, title
            HAVING COUNT(*) > 1
            ORDER BY COUNT(*) DESC;

        当然，我们可以在同一查询中同时使用 **WHERE** 和 **HAVING**——在这里，我们按作者和书名对尚未售出的书籍进行分组；然后我们报告有多本副本的书名（组）：

        .. code:: sql

            SELECT author, title, COUNT(*)
            FROM bookstore_inventory
            WHERE stock_number NOT IN
            (SELECT stock_number FROM bookstore_sales)
            GROUP BY author, title
            HAVING COUNT(*) > 1;

    .. md-tab-item:: 英文

        When we group, we are generating a new set of rows representing the groups present in our data.  If we include a **WHERE** clause in our query, it is applied to the data *before* grouping.  The **WHERE** clause, then, cannot be used to filter the set of rows produced by grouping.  If we want to filter the grouped data, we must do so using a **HAVING** clause.

        The **HAVING** clause works just like the **WHERE** clause, but applies to the set of rows generated by grouping.  Using **HAVING**, we can filter by expressions available to us after grouping: any expressions that we grouped by (our group labels), or aggregate functions on the groups.  The **HAVING** clause comes after the **GROUP BY** clause.

        Here we use **HAVING** to list books for which we have more than one copy in our bookstore inventory, in order by the number of copies:

        .. code:: sql

            SELECT author, title, COUNT(*)
            FROM bookstore_inventory
            GROUP BY author, title
            HAVING COUNT(*) > 1
            ORDER BY COUNT(*) DESC;

        We can, of course, use both **WHERE** and **HAVING** in the same query - here we group books that have not been sold by author and title; then we report  the titles (groups) with multiple copies:

        .. code:: sql

            SELECT author, title, COUNT(*)
            FROM bookstore_inventory
            WHERE stock_number NOT IN
            (SELECT stock_number FROM bookstore_sales)
            GROUP BY author, title
            HAVING COUNT(*) > 1;


自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含关于分组和聚合的练习，使用 **bookstore_inventory** 和 **bookstore_sales** 表。如果你遇到困难，可以点击练习下方的“显示答案”按钮查看正确答案。

        - 写一个查询，计算我们库存中作者 Toni Morrison 的书籍数量。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT COUNT(*) FROM bookstore_inventory WHERE author = 'Toni Morrison';


        - 写一个查询，查找 'good' 状态书籍的最低、最高和平均价格。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT MIN(price), MAX(price), AVG(price)
                FROM bookstore_inventory
                WHERE condition = 'good';


        - 写一个查询，找出在我们库存中写书的不同作者数量。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT COUNT(DISTINCT author) FROM bookstore_inventory;


        - 写一个查询，按作者获取书籍的平均价格；按最高平均价格排序。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT author, AVG(price)
                FROM bookstore_inventory
                GROUP BY author
                ORDER BY AVG(price) DESC;


        - 写一个查询，按作者和状态获取书籍的平均价格；按作者和状态排序。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT author, condition, AVG(price)
                FROM bookstore_inventory
                GROUP BY author, condition
                ORDER BY author, condition;


        - 写一个查询，给出按状态分组的已售书籍数量和这些书籍的总销售额。排除支付类型为 'trade in' 的书籍。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT i.condition, COUNT(*) AS books_sold, SUM(i.price) AS sales
                FROM
                bookstore_inventory AS i
                JOIN bookstore_sales AS s ON s.stock_number = i.stock_number
                WHERE s.payment <> 'trade in'
                GROUP BY i.condition;


        - 写一个查询，找出哪些作者的书籍平均价格低于 3 个货币单位。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT author, AVG(price)
                FROM bookstore_inventory
                GROUP BY author
                HAVING AVG(price) < 3;


        - 写一个查询，获取每种可能的书籍状态的最大价格和最小价格之间的差。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT condition, MAX(price) - MIN(price)
                FROM bookstore_inventory
                GROUP BY condition;


        - 写一个查询，找出我们库存中任何书籍的最高价格，并列出该价格的书籍。*提示*：你需要为这个查询使用子查询。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT * FROM bookstore_inventory WHERE price =
                (SELECT MAX(price) FROM bookstore_inventory);

    .. md-tab-item:: 英文

        This section contains exercises on grouping and aggregation, using the **bookstore_inventory** and **bookstore_sales** tables.  If you get stuck, click on the "Show answer" button below the exercise to see a correct answer.

        - Write a query to count the number of books in our inventory by the author Toni Morrison.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT COUNT(*) FROM bookstore_inventory WHERE author = 'Toni Morrison';


        - Write a query to find the minimum, maximum, and average price of a book in 'good' condition.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT MIN(price), MAX(price), AVG(price)
                FROM bookstore_inventory
                WHERE condition = 'good';


        - Write a query to find out how many different authors have written books in our inventory.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT COUNT(DISTINCT author) FROM bookstore_inventory;


        - Write a query to get the average price of a book, by author; sort by highest average price first.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT author, AVG(price)
                FROM bookstore_inventory
                GROUP BY author
                ORDER BY AVG(price) DESC;


        - Write a query to get the average price of a book, by author and condition; sort by author and condition.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT author, condition, AVG(price)
                FROM bookstore_inventory
                GROUP BY author, condition
                ORDER BY author, condition;


        - Write a query to give the number of books sold and the total sales from those books, grouped by condition.  Exclude books for the payment type 'trade in'.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT i.condition, COUNT(*) AS books_sold, SUM(i.price) AS sales
                FROM
                bookstore_inventory AS i
                JOIN bookstore_sales AS s ON s.stock_number = i.stock_number
                WHERE s.payment <> 'trade in'
                GROUP BY i.condition;


        - Write a query to find which authors' books have an average price less than 3 units of currency.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT author, AVG(price)
                FROM bookstore_inventory
                GROUP BY author
                HAVING AVG(price) < 3;


        - Write a query to get the difference between the maximum and minimum price of a book for each possible book condition.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT condition, MAX(price) - MIN(price)
                FROM bookstore_inventory
                GROUP BY condition;


        - Write a query to find the maximum price of any book in our inventory and list the books with that price.  *Hint*: you will need to use a subquery for this one.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM bookstore_inventory WHERE price =
                (SELECT MAX(price) FROM bookstore_inventory);








