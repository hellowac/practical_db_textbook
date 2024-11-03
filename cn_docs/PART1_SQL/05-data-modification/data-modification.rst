.. _data-modification-chapter:

==============
修改数据
==============

**Modifying data**

.. md-tab-set::

    .. md-tab-item:: 中文

        本章将解释向表中添加数据、从表中删除数据以及修改数据的基本机制。

    .. md-tab-item:: 英文

        This chapter will explain the basic mechanisms for adding data to tables, removing data from tables, and modifying data.

本章中使用的表
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        对于本章,我们将使用 **bookstore_inventory** 和 **bookstore_sales** 表,这些表模拟了一家二手书商可能使用的简单数据库。 **bookstore_inventory** 表列出了书店库存中或最近出售的印刷书籍,以及书籍的状态和标价。 列 **stock_number** 是每本书的唯一标识符。

        当书店出售一本书时,会在 **bookstore_sales** 表中添加一条记录。 该表列出了所售书籍的 **stock_number**、出售日期和支付方式。 列 **receipt_number** 是销售的唯一标识符。 (这可能不是一个很好的数据库设计;它假设我们一次只出售一本书！)

        有关这些表的完整描述,请参见 :ref:`Appendix A <appendix-a>`。

    .. md-tab-item:: 英文


        For this chapter, we will work with the tables **bookstore_inventory** and **bookstore_sales**, which simulate a simple database that a seller of used books might use.  The **bookstore_inventory** table lists printed books that the bookstore either has in stock or has sold recently, along with the condition of the book and the asking price.  The column **stock_number** is a unique identifier for each book.

        When the bookstore sells a book, a record is added to the **bookstore_sales** table.  This table lists the **stock_number** of the book sold, the date sold, and the type of payment.  The column **receipt_number** is a unique identifier for the sale.  (This may not be a very good database design; it assumes we only sell one book at a time!)

        A full description of these tables can be found in :ref:`Appendix A <appendix-a>`.

.. index:: INSERT INTO, INSERT, data; adding

使用 INSERT 添加数据
::::::::::::::::::::::::

**Adding data using INSERT**

.. md-tab-set::

    .. md-tab-item:: 中文

        要向数据库中的表添加行,我们使用以关键字 **INSERT** 开头的语句。 在其最简单的形式中, **INSERT** 允许您通过为表中定义的每一列提供一个值来向表中添加一行。 例如,假设我们书店的客户购买了加夫列尔·加西亚·马尔克斯的《百年孤独》。 这本书在我们的库存中列出的库存编号为 1455。 客户于 2021 年 8 月 14 日购买了这本书并以现金支付。 最后,我们向客户提供了收据,收据编号为 970。

        在数据库中,**bookstore_sales** 表定义了以下列： **receipt_number**、**stock_number**、**date_sold** 和 **payment**。

        我们可以使用以下语句记录这笔销售：

        .. activecode:: data_modification_example_insert
            :language: sql
            :dburl: /_static/textbook.sqlite3

            INSERT INTO bookstore_sales
            VALUES (970, 1455, '2021-08-14', 'cash');

        在交互式工具中尝试上述语句,然后使用 **SELECT** 查询验证新数据是否已添加。 请注意,值列出的顺序与 **bookstore_sales** 表中列的定义顺序相匹配。

    .. md-tab-item:: 英文


        To add rows to a table in the database, we use a statement starting with the keyword **INSERT**.  In its simplest form, **INSERT** lets you add a single row to a table by providing a value for each column in the table as defined.  As an example, suppose a customer at our bookstore purchases our copy of *One Hundred Years of Solitude* by Gabriel García Márquez.  This book is listed in our inventory with a stock number of 1455.  The customer purchases the book on August 14, 2021 and pays cash.  Finally, we provide a receipt to the customer with receipt number 970.

        In the database, the table **bookstore_sales** is defined with these columns:  **receipt_number**, **stock_number**, **date_sold**, and **payment**.

        We could record the sale using this statement:

        .. activecode:: data_modification_example_insert
            :language: sql
            :dburl: /_static/textbook.sqlite3

            INSERT INTO bookstore_sales
            VALUES (970, 1455, '2021-08-14', 'cash');

        Try the above statement in the interactive tool, then use a **SELECT** query to verify that the new data has been added.  Note that the order in which the values are listed matches the order in which columns are defined for the **bookstore_sales** table.


指定列
------------------

**Specifying columns**

.. md-tab-set::

    .. md-tab-item:: 中文

        执行如上所述的插入操作在我们确切知道数据库中表的定义时工作良好。 然而,实际中表会随着时间的推移而变化,这可能导致列的顺序不同,或表中添加更多列。 如果发生这种情况,旧的 SQL 代码如果假设了表的结构将会失效。 因此,提供不仅是数据,还有我们希望放入数据的列名是一种更好的实践。 为此,我们只需在表名后用括号列出列名：

        .. code:: sql

            INSERT INTO bookstore_sales (receipt_number, stock_number, date_sold, payment)
            VALUES (971, 1429, '2021-08-15', 'trade in');

        如 :numref:`Chapter {number} <table-creation-chapter>` 中所述,我们的一些列可以由数据库自动生成。 例如,如果我们向库存中添加一本新书,我们希望生成一个新的、唯一的库存编号。 **bookstore_inventory** 表已设置为执行此操作。 当数据库为我们生成这样的值时,我们不应为生成的列提供值。 指定列名使我们能够仅插入非生成列的数据。

        **bookstore_sales** 表同样设置为生成唯一的 **receipt_number** 值;上面我们为收据编号提供了值,这只有在我们提供的值尚未被使用时才有效。 **bookstore_sales** 表的 **date_sold** 列还有一个默认设置——如果您不提供该列的值,它将为您输入今天的日期。 下面是 **bookstore_sales** 表在实际中可能如何使用的示例：

        .. code:: sql

            INSERT INTO bookstore_sales (stock_number, payment)
            VALUES (1460, 'cash');

    .. md-tab-item:: 英文


        Performing the insert as we did above works fine when we know for certain how a table has been defined in a database.  However, tables change over time in practice, which may result in columns appearing in a different order, or in more columns being added to the table.  If this happens, old SQL code that makes assumptions about the table structure will break.  So it is a better practice to provide not only the data, but the names of the columns in which we want to put the data.  To do this, we simply list the column names in parentheses after the table name:

        .. code:: sql

            INSERT INTO bookstore_sales (receipt_number, stock_number, date_sold, payment)
            VALUES (971, 1429, '2021-08-15', 'trade in');

        As described in :numref:`Chapter {number} <table-creation-chapter>`, it is possible to have some of our columns be automatically generated by the database.  For example, if we add a new book to our inventory, we want to generate a new, unique stock number.  The **bookstore_inventory** table is set up to do this.  When the database generates values like this for us, we should not provide a value for the generated column.  Specifying column names lets us insert data for only the non-generated columns.

        The **bookstore_sales** table is likewise set up to generate unique **receipt_number** values; above we provided values for the receipt number, which only works as long as the values we provide are not already used.  The **bookstore_sales** table also has a default setting for the **date_sold** column - it will put in today's date for you if you do not provide a value for the column.  Here is how the **bookstore_sales** table might be used in practice:

        .. code:: sql

            INSERT INTO bookstore_sales (stock_number, payment)
            VALUES (1460, 'cash');

插入多行
-----------------------

**Inserting multiple rows**

.. md-tab-set::

    .. md-tab-item:: 中文

        虽然使用多个 **INSERT** 语句添加多行数据是完全有效的,但 SQL 也允许您在单个 **INSERT** 语句中提供多行。 也许我们希望在一个语句中输入一天的所有销售记录。 我们可以输入以下查询：

        .. code:: sql

            INSERT INTO bookstore_sales (stock_number, payment)
            VALUES
            (1444, 'credit card'),
            (1435, 'cash'),
            (1453, 'credit card')
            ;

        (对于 Oracle 用户的说明：Oracle 不允许在 **INSERT** 中使用多行。)

    .. md-tab-item:: 英文


        While it is perfectly valid to do multiple **INSERT** statements to add multiple rows of data, SQL also lets you provide multiple rows in a single **INSERT** statement.  Perhaps we wish to enter all of a day's sales in one statement.  We can enter this query:

        .. code:: sql

            INSERT INTO bookstore_sales (stock_number, payment)
            VALUES
            (1444, 'credit card'),
            (1435, 'cash'),
            (1453, 'credit card')
            ;

        (Note for Oracle users: Oracle does not permit multiple rows in an **INSERT**.)

.. index:: INSERT INTO ... SELECT

插入查询结果
-----------------------

**Inserting query results**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 还提供通过 **SELECT** 查询提供值的功能。 作为一个稍显牵强的例子,假设我们创建另一个名为 **bookstore_recent_sales** 的表,列名为 **author** 和 **title**。 我们将在此表中存储有关我们最近售出的书籍的数据(也许是为了查看哪些书籍和作者受欢迎,以指导我们的采购)。 我们可能想用过去一个月内售出的独特书籍填充此表。

        语法与常规的 **INSERT** 相同,但 **VALUES** 子句被 **SELECT** 查询替代(该查询必须返回与我们要插入的列相同类型且顺序相同的列)。 尝试下面的语句,看看它是如何工作的。

        .. code:: sql

            CREATE TABLE bookstore_recent_sales (author TEXT, title TEXT);

            INSERT INTO bookstore_recent_sales (author, title)
            SELECT DISTINCT i.author, i.title
            FROM
            bookstore_inventory AS i
            JOIN bookstore_sales AS s ON s.stock_number = i.stock_number
            WHERE s.date_sold BETWEEN '2021-08-01' AND '2021-08-31';

    .. md-tab-item:: 英文


        SQL also provides the capability of providing values via a **SELECT** query.  As a somewhat contrived example, suppose we create another table named **bookstore_recent_sales** with columns named **author** and **title**. We will store data in this table about books we sold recently (perhaps to see what books and authors are popular, to inform our purchasing).  We might want to fill this table with the unique books that have been sold in the past month.

        The syntax is the same as a regular **INSERT**, but with the **VALUES** clause replaced by a **SELECT** query (which must return columns of the same type and in the same order as the columns we are inserting into).  Try the statements below to see this in action.

        .. code:: sql

            CREATE TABLE bookstore_recent_sales (author TEXT, title TEXT);

            INSERT INTO bookstore_recent_sales (author, title)
            SELECT DISTINCT i.author, i.title
            FROM
            bookstore_inventory AS i
            JOIN bookstore_sales AS s ON s.stock_number = i.stock_number
            WHERE s.date_sold BETWEEN '2021-08-01' AND '2021-08-31';

.. index:: DELETE, data; removing

使用 DELETE 删除数据
:::::::::::::::::::::::::

**Removing data with DELETE**

.. md-tab-set::

    .. md-tab-item:: 中文

        从表中删除行是通过 **DELETE** 语句实现的。 **DELETE** 语句通常非常简单,仅需要一个 **FROM** 子句,并可选地包含一个 **WHERE** 子句。 您一次只能从一个表中删除数据。 例如,如果我们想删除 **bookstore_sales** 中 2021 年 8 月 1 日之前的所有销售记录,可以写成：

        .. activecode:: data_modification_example_delete
            :language: sql
            :dburl: /_static/textbook.sqlite3

            DELETE FROM bookstore_sales
            WHERE date_sold < '2021-08-01';

        除非我们先从 **bookstore_inventory** 中删除要删除的书籍的数据,否则这可能是个坏主意——否则我们可能会认为这些已售书籍仍然在库存中。 由于我们无法在一个查询中从多个表中删除数据(例如,使用连接),因此确定如何从 **bookstore_inventory** 中删除适当的行可能会有些棘手。 我们想要删除的行的信息实际上在 **bookstore_sales** 中(在 **date_sold** 列)。 我们需要的技术将在 :numref:`Chapter {number} <subqueries-chapter>` 中讨论——使用子查询。 这里是必要的查询,目前不作解释：

        .. code:: sql

            DELETE FROM bookstore_inventory
            WHERE stock_number IN
            (SELECT stock_number FROM bookstore_sales
            WHERE date_sold < '2021-08-01')
            ;

        在 :numref:`Chapter {number} <constraints-chapter>` 中,我们将讨论保持多个表之间一致性的其他技术。

        如果在 **DELETE** 查询中省略 **WHERE** 子句,则将从表中删除所有数据。

        与任何数据修改语句一样,**DELETE** 语句的效果是立即且永久的。 在某种程度上,如果您知道插入了哪些行,可以用 **DELETE** 来撤销 **INSERT** 的结果;然而,除非您有数据的备份,否则无法恢复已删除的行。 因此,确保您只删除所需内容非常重要。 在执行删除之前,测试这一点的简单方法是将语句中的 **DELETE** 替换为 **SELECT \***——这将准确显示您的语句将删除哪些行。

        请记住,在我们的交互式示例中,您对本书数据库所做的任何更改仅在当前浏览会话中有效,因此如果您希望恢复已删除的数据,可以通过刷新浏览器页面来实现。

    .. md-tab-item:: 英文


        Removing rows from a table is accomplished using **DELETE** statements.  **DELETE** statements are generally very simple, requiring only a **FROM** clause and optionally a **WHERE** clause.  You can delete data from only one table at a time.  As an example, if we want to remove all sales from **bookstore_sales** prior to August 1, 2021, we could write:

        .. activecode:: data_modification_example_delete
            :language: sql
            :dburl: /_static/textbook.sqlite3

            DELETE FROM bookstore_sales
            WHERE date_sold < '2021-08-01';

        This is probably a bad idea unless we first delete the data from **bookstore_inventory** for the books we are deleting - otherwise we might think that we still have those sold books.  Since we cannot delete data from multiple tables in one query (e.g., using a join) it may be tricky to see how to get rid of the appropriate rows from **bookstore_inventory**. The information about what rows we want to delete is actually in **bookstore_sales** (in the **date_sold** column).  The technique we need will be covered in :numref:`Chapter {number} <subqueries-chapter>` - using a subquery.  Here is the necessary query, given without explanation for now:

        .. code:: sql

            DELETE FROM bookstore_inventory
            WHERE stock_number IN
            (SELECT stock_number FROM bookstore_sales
            WHERE date_sold < '2021-08-01')
            ;

        In :numref:`Chapter {number} <constraints-chapter>` we will discuss other techniques for keeping multiple tables consistent with each other.

        If the **WHERE** clause is omitted in a **DELETE** query, then all data from the table is removed.

        As with any data modification statement, the effects of a **DELETE** statement are immediate and permanent.  To some extent, you can undo the result of an **INSERT** with a **DELETE** if you know which rows you inserted; however, it is impossible to restore deleted rows unless you have a backup of the data.  Thus, it is very important to be sure you are deleting only what you want to delete.  A simple way to test this before you perform a delete is to replace **DELETE** with **SELECT \*** in your statement - this will show you exactly the rows that your statement would delete.

        Remember that with our interactive examples, any changes you make to this book's database only last for the current viewing session, so if you wish to restore the deleted data, you may do so by refreshing the page in your browser.

.. index:: UPDATE, SET, data; modifying

使用 UPDATE 修改数据
::::::::::::::::::::::::::

**Modifying data with UPDATE**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 提供的最强大功能之一是使用 **UPDATE** 语句进行数据修改。 **UPDATE** 的形式为：

        .. code:: sql

            UPDATE tablename
            SET
            column1 = expression1,
            column2 = expression2,
            ...
            [WHERE expressions]
            ;

        通常,我们可能想要更新数据库中的单行。 例如,假设我们检查书店库存中的一本书,决定它的状态比我们最初认为的要好。 我们的《慢河》由尼古拉·格里菲斯著作(库存编号 1460)被列为状况良好,价格为 2(某种货币单位)。 我们希望将状况升级为“良好”,并同时将价格提高到 2.50：

        .. activecode:: data_modification_example_update
            :language: sql
            :dburl: /_static/textbook.sqlite3

            UPDATE bookstore_inventory
            SET
            condition = 'good',
            price = 2.50
            WHERE stock_number = 1460;

        我们也可以一次更新多行。 也许我们错误地将 2021 年 8 月 1 日的所有销售记录输入为 7 月 31 日。 我们可以在一个查询中修复这些错误：

        .. code:: sql

            UPDATE bookstore_sales
            SET date_sold = '2021-08-01'
            WHERE date_sold = '2021-07-31';

        当然,这只有在标记为 7 月 31 日的销售都不正确的情况下才有效;如果不是,我们可能需要在 **WHERE** 子句中更加聪明。

        然而,**UPDATE** 的真正强大之处在于 **SET** 子句中赋值的右侧可以是表达式,而这些表达式是基于正在更新的行。 因此,我们可以做如下操作：

        .. code:: sql

            UPDATE bookstore_inventory
            SET price = price + 0.25;

        这将使每本书的价格增加 0.25。

    .. md-tab-item:: 英文


        One of the most powerful capabilities SQL provides is data modification using **UPDATE** statements.  The form of an **UPDATE** is:

        .. code:: sql

            UPDATE tablename
            SET
            column1 = expression1,
            column2 = expression2,
            ...
            [WHERE expressions]
            ;

        Often, we may want to update a single row in our database.  For example, perhaps we examine one of the books in our bookstore inventory and decide that its condition is better than we initially thought.  Our copy of *Slow River* by Nicola Griffith (stock number 1460) is listed as in fair condition, with a price of 2 (in some unit of currency).  We want to upgrade the condition to "good" and raise the price to 2.50 at the same time:

        .. activecode:: data_modification_example_update
            :language: sql
            :dburl: /_static/textbook.sqlite3

            UPDATE bookstore_inventory
            SET
            condition = 'good',
            price = 2.50
            WHERE stock_number = 1460;

        We can also update multiple rows at a time.  Perhaps we mistakenly put in all sales for August 1, 2021 as July 31 instead.  We can fix these in one query:

        .. code:: sql

            UPDATE bookstore_sales
            SET date_sold = '2021-08-01'
            WHERE date_sold = '2021-07-31';

        Of course, this only works if none of the sales marked as July 31 were correct; we might have to be more clever with our **WHERE** clause if not.

        The real power of **UPDATE**, though, is that the right hand side of the assignments in the **SET** clause can be expressions, and these expressions are based on the row being updated.  Hence, we can do something like the following:

        .. code:: sql

            UPDATE bookstore_inventory
            SET price = price + 0.25;

        This would raise the price of every book by 0.25.

.. index:: TRUNCATE, MERGE

其他数据修改语句
::::::::::::::::::::::::::::::::::

**Other data modification statements**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 提供了一些其他数据修改语句类型,这些类型可能在您的数据库中支持,也可能不支持。 **TRUNCATE TABLE** 从表中删除所有行,通常比 **DELETE** 快(但只能用于删除 *所有* 行)。 **MERGE** 是一种较为复杂的操作,它结合了插入、更新和删除,允许将一个表与另一个表或表的连接进行同步。 这两种操作在严格意义上并不是必需的,因为可以通过 **INSERT**、 **UPDATE** 和 **DELETE** 实现相同的结果。 我们在本书中将不再进一步讨论它们。

    .. md-tab-item:: 英文


        SQL provides some other data modification statement types, which may or may not be supported in your database.  **TRUNCATE TABLE** removes all rows from a table, and is typically faster than **DELETE** (but can only be used to remove *all* rows).  **MERGE** is a somewhat complex operation that combines inserts, updates, and deletes, allowing synchronization of a table with another table or join of tables.  Neither of these operations is strictly necessary, given that the same results can be accomplished with **INSERT**, **UPDATE**, and **DELETE**.  We will not cover them further in this book.

自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含有关 **INSERT**、**UPDATE** 和 **DELETE** 的练习,使用 **bookstore_inventory** 和 **bookstore_sales** 表。 请记住,我们在这些练习中使用的数据库与上面的交互式示例共享,因此您在上面的交互式工具中应用的任何更改都反映在您下面使用的数据库中。 如果您获得的结果与预期不符,您可能需要在浏览器中重新加载此页面以获取数据库的新副本。

        如果您卡住了,可以点击练习下方的“显示答案”按钮查看正确答案。

        - 编写语句将 N. Scott Momaday 的书 *House Made of Dawn* 添加到 **bookstore_inventory** 表中。 使用 1471 作为库存编号,'like new' 作为状态,4.75 作为价格。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                INSERT INTO bookstore_inventory (stock_number, author, title, condition, price)
                VALUES (1471, 'N. Scott Momaday', 'House Made of Dawn', 'like new', 4.75);


        - 编写语句将 John Steinbeck 的所有书籍(来自我们的 **books** 表)以 'new' 状态和 4.00 的价格添加到 **bookstore_inventory** 中。 请注意,没有好的方法为这些书籍提供唯一的库存编号,但如果您完全省略 **stock_number** 列,**bookstore_inventory** 表已设置为自动提供唯一值。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                INSERT INTO bookstore_inventory (author, title, condition, price)
                SELECT a.name, b.title, 'new', 4.00
                FROM
                authors AS a
                JOIN books AS b ON a.author_id = b.author_id
                WHERE a.name = 'John Steinbeck';


        - 编写语句删除 **bookstore_inventory** 中所有状态为 'fair' 的书籍。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                DELETE FROM bookstore_inventory
                WHERE condition = 'fair';


        - 编写语句将收据编号为 963 的销售的支付方式更改为 'cash'。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                UPDATE bookstore_sales
                SET payment = 'cash'
                WHERE receipt_number = 963;


        - 编写语句将 Clifford Simak 的所有书籍在书店库存中的价格设置为特别销售价格 1.0。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                UPDATE bookstore_inventory
                SET price = 1.0
                WHERE author = 'Clifford Simak';


        - 编写语句将所有状态为 'new' 的书籍的价格翻倍。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                UPDATE bookstore_inventory
                SET price = price * 2
                WHERE condition = 'new';

    .. md-tab-item:: 英文


        This section contains exercises on **INSERT**, **UPDATE**, and **DELETE**, using the **bookstore_inventory** and **bookstore_sales** tables. Keep in mind that the database we are using for these exercises is shared with the interactive examples above, so any changes you have applied in an interactive tool above are reflected in the database you use below.  If the results you get are not what you are expecting, you may need to reload this page in your browser to get a fresh copy of the database.

        If you get stuck, click on the "Show answer" button below the exercise to see a correct answer.

        - Write a statement to add the book *House Made of Dawn* by N. Scott Momaday to the **bookstore_inventory** table.  Use 1471 for the stock number, 'like new' for the condition, and 4.75 for the price.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                INSERT INTO bookstore_inventory (stock_number, author, title, condition, price)
                VALUES (1471, 'N. Scott Momaday', 'House Made of Dawn', 'like new', 4.75);


        - Write a statement to add all books by John Steinbeck (from our **books** table) into **bookstore_inventory** with a condition of 'new' and a price of 4.00.  Note that there is no good way to provide unique stock numbers for each of these books, but if you omit the **stock_number** column entirely, the **bookstore_inventory** table is set up to provide unique values automatically.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                INSERT INTO bookstore_inventory (author, title, condition, price)
                SELECT a.name, b.title, 'new', 4.00
                FROM
                authors AS a
                JOIN books AS b ON a.author_id = b.author_id
                WHERE a.name = 'John Steinbeck';


        - Write a statement to remove all books from **bookstore_inventory** that are in 'fair' condition.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                DELETE FROM bookstore_inventory
                WHERE condition = 'fair';


        - Write a statement to change the payment type to 'cash' for the sale with receipt number 963.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                UPDATE bookstore_sales
                SET payment = 'cash'
                WHERE receipt_number = 963;


        - Write a statement to set the price (in our bookstore inventory) for all books by Clifford Simak to a special sale price of 1.0.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                UPDATE bookstore_inventory
                SET price = 1.0
                WHERE author = 'Clifford Simak';


        - Write a statement to double the price of all books in 'new' condition.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                UPDATE bookstore_inventory
                SET price = price * 2
                WHERE condition = 'new';







