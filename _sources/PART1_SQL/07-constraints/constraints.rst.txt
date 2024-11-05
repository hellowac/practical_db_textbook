.. _constraints-chapter:

====================
键和约束
====================

**Keys and constraints**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中,我们将探讨约束数据的不同方法,以帮助保持数据的正确性。

    .. md-tab-item:: 英文

        In this chapter, we explore the different ways in which data may be constrained in order to help preserve the correctness of our data.

本章中使用的表
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        本章中的一些示例将使用 **books** 表及相关表(有关这些表的完整描述,请参见 :ref:`Appendix A <appendix-a>`)。其他示例将使用仅为示例创建的表,然后丢弃。

    .. md-tab-item:: 英文

        Some examples in this chapter will use the **books** table and related tables (see :ref:`Appendix A <appendix-a>` for a full description of these tables).  Other examples will use tables created just for the example, then discarded.

.. index:: constraint, constraint; domain

约束
:::::::::::

**Constraints**

.. md-tab-set::

    .. md-tab-item:: 中文

        由于数据对许多组织和应用程序至关重要,因此值得尽一切努力确保数据库中数据的正确性和一致性。这可以通过多种方式实现：应用软件可以进行检查,以确保数据的输入和维护正确,单独的程序可以测试和报告数据一致性,数据库可以通过约束和触发器来强制执行正确性。(触发器是在某些事件发生时(例如,对行的更新)数据库可以执行的操作;在某些数据库中,操作甚至可以是使用特定实现的编程语言编写的小程序。本书不涵盖触发器。)我们在本章中专注于数据库约束。

        约束是限制数据库中数据的各种属性。最简单的约束类型之一是*域*约束：输入到列中的数据被限制为该列定义的类型。(在 SQLite 中不强制执行域约束,因此我们无法使用本书的数据库进行演示。)下面我们讨论强制整个表的数据属性的约束——主键和外键约束——以及适用于单个行的约束：非空、唯一性和检查约束。

    .. md-tab-item:: 英文

        As data is critical to so many organizations and applications, it is worth doing everything possible to ensure the correctness and consistency of the data in databases.  This can be achieved in many ways: application software can do checks to ensure data is entered and maintained correctly, separate programs can test and report on data consistency, and databases can enforce correctness using constraints and triggers.  (Triggers are actions the database can perform when certain events, such as an update to a row, occur; in some databases, the actions can even be complete small programs using implementation-specific programming languages.  This book does not cover triggers.)  We focus in this chapter on database constraints.

        Constraints are properties of the database that restrict data in various ways.  One of the simplest types of constraints are *domain* constraints: data entered into a column is constrained to be of the type defined for the column.  (Domain constraints are not enforced in SQLite, so we cannot demonstrate using the book's database.)  Below we discuss constraints that enforce data properties for entire tables - primary and foreign key constraints - and those that apply to individual rows: not null, uniqueness, and check constraints.

.. index:: primary key - SQL, key - SQL; primary, constraint; primary key

主键
::::::::::::

**Primary keys**

.. md-tab-set::

    .. md-tab-item:: 中文

        *主键*是表中一列或多列,要求每行存储的值必须是唯一的。控制唯一性确保我们能够通过在另一个表中存储键值,将特定的单个数据项与另一个表中的数据关联起来。它还防止了不必要的数据重复,这可能导致错误的统计(例如,在进行计数或求和时)。在 :numref:`Chapter {number} <joins-chapter>` 中讨论的 id 列——专门用于确保每行可以唯一标识的特殊列——通常用作主键。一个表只能有一个主键。

        我们在书籍数据库中可以找到一些例子。例如,表 **authors** 将 **author_id** 作为主键。数据库将通过防止任何会导致主键重复的数据修改查询来强制执行 **author_id** 列的唯一性属性。删除行永远不会违反主键约束,但插入和更新可能会。以下任一查询都会导致错误,因为数据库中已经存在 **author_id** = 1 的行：

        .. activecode:: constraints_example_primary_key
            :language: sql
            :dburl: /_static/textbook.sqlite3

            INSERT INTO authors (author_id, name)
            VALUES (1, 'Charles Dickens');

            UPDATE authors SET author_id = 1 WHERE author_id = 2;

        由于我们需要比较主键值以确保唯一性,因此禁止在主键列中插入 ``NULL`` 值。(然而,SQLite 在这方面的行为有所不同。如果在整数主键列中插入 ``NULL``,SQLite 会为你生成一个唯一值。对于其他类型的主键列或多列主键,SQLite 允许插入 ``NULL`` 值。)

        在表 **authors_awards** 中可以找到多列主键的例子。对于此表,主键是(**author_id**,**award_id**)这对值。这并不意味着每一列都是主键,例如,每一列都是独立唯一的。相反,必须是这对值唯一。也就是说,你不能两次插入配对 ``(4, 10)``,但可以插入所有的 ``(4, 10)``, ``(4, 11)``, 和 ``(5, 10)``(假设这些配对在表中还不存在)。

    .. md-tab-item:: 英文

        A *primary key* is a column or set of columns of a table which are required to contain unique values for each row stored in the table.  Controlling for uniqueness ensures that we can associate a specific, single item of data with data in another table by storing the key value in the other table. It also prevents unnecessary duplication of data that could result in incorrect statistics (for example, when taking counts or sums).  The id columns discussed in :numref:`Chapter {number} <joins-chapter>` - special columns used specifically to ensure each row can be uniquely identified - are commonly used as primary keys.  A table can have only one primary key.

        Some examples can be found in our books database.  The table **authors**, for example, has **author_id** as a primary key.  The database will enforce the uniqueness property of the **author_id** column by preventing any data modification queries which would result in a duplicate primary key.  Deleting rows can never violate a primary key constraint, but inserts and updates can.  Either of the following queries will result in an error because there already exists a row in the database with **author_id** = 1:

        .. activecode:: constraints_example_primary_key
            :language: sql
            :dburl: /_static/textbook.sqlite3

            INSERT INTO authors (author_id, name)
            VALUES (1, 'Charles Dickens');

            UPDATE authors SET author_id = 1 WHERE author_id = 2;

        Because we need to compare primary key values to ensure uniqueness, it is also forbidden to insert ``NULL`` values into a primary key column.  (SQLite varies from this standard behavior, though. If you insert a ``NULL`` into an integer primary key column, SQLite will generate a unique value for you.  For other primary key column types, or multi-column primary keys, ``NULL`` values are permitted in SQLite.)

        An example of a multi-column primary key can be found in the table **authors_awards**.  For this table, the primary key is the pair (**author_id**, **award_id**).  This does not mean that each column is a primary key, e.g., that each column is independently unique.  Instead, it is the pair of values which must be unique.  That is, you may not insert the pair ``(4, 10)`` twice, but you may insert all of ``(4, 10)``, ``(4, 11)``, and ``(5, 10)`` (assuming none of those pairs is already in the table).

.. index:: PRIMARY KEY, ALTER TABLE

创建主键
-----------------------

**Creating a primary key**

.. md-tab-set::

    .. md-tab-item:: 中文

        在表上创建主键有几种方法。创建表时创建主键是最简单的。如果主键是单列,则可以简单地将 **PRIMARY KEY** 短语放在列定义的末尾：

        .. code:: sql

              DROP TABLE IF EXISTS test;
              CREATE TABLE test (
                x VARCHAR(10) PRIMARY KEY
              );

        你也可以将主键作为表定义中的单独条目创建;在创建多列主键时,必须使用这种形式。下面的第一个定义与上面的定义等价,而第二个定义则创建了一个多列主键：

        .. code:: sql

            DROP TABLE IF EXISTS test2;
            DROP TABLE IF EXISTS test3;

            CREATE TABLE test2 (
              x VARCHAR(10),
              PRIMARY KEY (x)
            );

            CREATE TABLE test3 (
              x INTEGER,
              y INTEGER,
              PRIMARY KEY (x, y)
            );

        某些数据库系统还允许使用 **ALTER TABLE** 命令将主键添加到现有表,只要现有数据符合该约束。**ALTER TABLE** 也可用于从表中移除(删除)约束。(SQLite 不支持此用法。)

    .. md-tab-item:: 英文

        There are a few ways to create a primary key on a table.  It is easiest to create a primary key when creating the table.  If the primary key is a single column, then you may simply put the phrase **PRIMARY KEY** at the end of the column definition:

        .. code:: sql

              DROP TABLE IF EXISTS test;
              CREATE TABLE test (
                x VARCHAR(10) PRIMARY KEY
              );

        You can also create the primary key as a separate entry in the table definition; you must use this form when creating a multi-column primary key.  The first definition below is equivalent to the one above, while the second creates a multi-column primary key:

        .. code:: sql

            DROP TABLE IF EXISTS test2;
            DROP TABLE IF EXISTS test3;

            CREATE TABLE test2 (
              x VARCHAR(10),
              PRIMARY KEY (x)
            );

            CREATE TABLE test3 (
              x INTEGER,
              y INTEGER,
              PRIMARY KEY (x, y)
            );

        Some database systems also allow the addition of a primary key to an existing table using the **ALTER TABLE** command, as long as the existing data would conform to the constraint.  **ALTER TABLE** can also be used to remove (drop) constraints from a table.  (SQLite does not support this usage.)

.. index:: foreign key, key - SQL; foreign, constraint; foreign key - SQL, constraint; referential integrity, referential integrity constraint, table; referencing, table; referenced


外键
::::::::::::

**Foreign keys**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们还对不同表之间的数据关系感兴趣。例如,**books** 表中的每一行都有一个 **author_id** 值,这让我们可以在 **authors** 表中查找作者信息。我们如何确保 **author_id** 值是有效的,即它始终有对应的 **authors** 表中的行呢？对于关系数据库,解决方案是 *外键* 约束。

        外键约束适用于一个表中的列或列列表(*引用* 表),并引用另一个表中的列或列列表(*被引用* 表)。该约束要求以下两种情况之一为真：

        - 引用表中的列或列列表中的值存在于被引用的列或列列表中
        - 引用表中的列或列列表中的值为 ``NULL``

        被引用表中的列或列列表必须约束为唯一,通常通过将它们设为主键,或通过唯一性约束(见下文)。

        我们的数据库在 **books** 和 **authors** 之间定义了一个外键。外键约束位于 **books** 的 **author_id** 列上,引用 **authors** 的 **author_id** 列。如果我们想要向 **books** 中添加一本新书,我们必须使用一个 **author_id** 值,这个值必须是 **authors** 表中的有效 **author_id**。外键本身允许 ``NULL`` 的 **author_id** 值,但我们进一步约束了 **author_id** 列,使其不能为 null(使用稍后定义的 **NOT NULL** 约束)。

        例如,下面的代码将因 **books** 中的外键约束引用 **authors** 而失败。(注意,与其他数据库系统不同,SQLite 不会强制执行外键,除非你特别告诉它这样做——下面以 **PRAGMA** 关键字开头的代码就是在执行这个操作。**PRAGMA** 关键字不是 SQL 标准的一部分,仅在 SQLite 中需要。)

        .. activecode:: constraints_example_foreign_key
            :language: sql
            :dburl: /_static/textbook.sqlite3

            PRAGMA foreign_keys = ON;

            INSERT INTO books (author_id, title)
            VALUES (99, 'Unknown');   -- 99 不是有效的作者 ID

        我们同样不能进行会破坏现有关系的操作。例如,**books** 表中存在 **author_id** = 1 的记录。如果我们删除具有该 ID 值的作者,将违反 **books** 表上的外键约束。我们也会违反 **authors_awards** 上的类似外键约束。因此,这段代码会产生错误：

        .. code:: sql

            PRAGMA foreign_keys = ON;

            DELETE FROM authors WHERE author_id = 1;

        然而,如果我们首先删除该作者的所有书籍和奖项,就可以成功删除该作者：

        .. code:: sql

            PRAGMA foreign_keys = ON;

            DELETE FROM books WHERE author_id = 1;
            DELETE FROM authors_awards WHERE author_id = 1;
            DELETE FROM authors WHERE author_id = 1;

        我们同样不能在不先删除任何引用表的情况下删除 **authors** 表。

        **books** 和 **authors** 的示例展示了一个常见模式,即外键约束将我们可能希望在联接查询中使用的列联系起来(见 :numref:`Chapter {number} <joins-chapter>`)。这并不意味着外键是联接的必要条件;关系数据库的一大优势是数据之间的关系不必是预先确定的。然而,外键的存在表明引用表和被引用表中的数据之间存在自然关系。

        外键约束也被称为 *参照完整性约束*。

    .. md-tab-item:: 英文

        We are also interested in the relationships between data in different tables.  For example, every row in the **books** table has an **author_id** value which lets us look up author information in the **authors** table.  How can we ensure that the **author_id** value is valid, that is, that it always has a corresponding row in the **authors** table?  For a relational database, the solution is a *foreign key* constraint.

        A foreign key constraint applies to a column or list of columns in one table (the *referencing* table), and references a column or list of columns in another table (the *referenced* table).  The constraint requires that one of two things be true:

        - The values in the column or columns in the referencing table exist in the referenced column or columns
        - The values in the column or columns in the referencing table are ``NULL``

        The column or columns in the referenced table must be constrained to be unique, either by making them the primary key (the usual case), or through a uniqueness constraint (see below).

        Our database defines a foreign key between **books** and **authors**.  The foreign key constraint is on the **author_id** column of **books** and references the **author_id** column of **authors**.  If we want to add a new book to **books**, we must add it with an **author_id** value, which must be a valid **author_id** from the **authors** table.  The foreign key by itself would allow a ``NULL`` **author_id** value, but we have further constrained the **author_id** column to not be null (using the **NOT NULL** constraint defined later on).

        For example, the code below will fail due to the foreign key constraint on **books** referencing **authors**.  (Note that, unlike other database systems, SQLite will not enforce foreign keys unless you specifically tell it to - that is what the line of code below starting with the keyword **PRAGMA** is doing.  The **PRAGMA** keyword is not part of the SQL standard, and is only needed in SQLite.)

        .. activecode:: constraints_example_foreign_key
            :language: sql
            :dburl: /_static/textbook.sqlite3

            PRAGMA foreign_keys = ON;

            INSERT INTO books (author_id, title)
            VALUES (99, 'Unknown');   -- 99 is not a valid author id

        We also cannot do operations which would destroy existing relationships.  For example, there exist records in the **books** table for which the **author_id** = 1.  If we were to delete the author with this id value, we would violate the foreign key constraint on the **books** table.  We would also violate a similar foreign key constraint on **authors_awards**.  This code therefore produces an error:

        .. code:: sql

            PRAGMA foreign_keys = ON;

            DELETE FROM authors WHERE author_id = 1;

        However, if we first remove all books and awards for this author, we can successfully remove the author:

        .. code:: sql

            PRAGMA foreign_keys = ON;

            DELETE FROM books WHERE author_id = 1;
            DELETE FROM authors_awards WHERE author_id = 1;
            DELETE FROM authors WHERE author_id = 1;

        We similarly cannot drop the **authors** table without first dropping any referencing tables.

        The **books** and **authors** examples demonstrate a common pattern, which is that foreign key constraints relate columns that we are likely to want to use in a join query (:numref:`Chapter {number} <joins-chapter>`).  This does not mean that a foreign key is a necessary condition for a join; one of the strengths of a relational database is that relationships between data do not have to be predetermined.  However, the presence of a foreign key is an indication that there exists a natural relationship between the data in the referencing and referenced tables.

        Foreign key constraints are also known as *referential integrity constraints*.

.. index:: REFERENCES, FOREIGN KEY

创建外键约束
---------------------------------

**Creating a foreign key constraint**

.. md-tab-set::

    .. md-tab-item:: 中文

        与主键一样,创建外键约束的方法有多种。如果外键约束限制了单个列,则可以在表的列定义中使用 **REFERENCES** 关键字添加它：

        .. code:: sql

            DROP TABLE IF EXISTS referencing;
            DROP TABLE IF EXISTS referenced;

            CREATE TABLE referenced (
              x INTEGER PRIMARY KEY
            );

            CREATE TABLE referencing (
              xx INTEGER REFERENCES referenced (x)
            );

        请注意,尽管外键约束只出现在引用表的定义中,但该约束影响两个表。上述代码确保 **referencing** 中的 **xx** 列的值要么是 ``NULL``,要么包含在 **referenced** 的 **x** 列中。

        (针对 MySQL 用户：MySQL 不识别用于创建外键的单列语法。请改用下面的显式约束语法。)

        我们还可以通过在表定义中添加单独的 **FOREIGN KEY** 条目来创建外键约束。这种形式必须用于多列外键：

        .. code:: sql

            DROP TABLE IF EXISTS referencing2;
            DROP TABLE IF EXISTS referenced2;

            CREATE TABLE referenced2 (
              a VARCHAR(10),
              b VARCHAR(20),
              PRIMARY KEY (a, b)
            );

            CREATE TABLE referencing2 (
              c INTEGER PRIMARY KEY,
              aa VARCHAR(10),
              bb VARCHAR(10),
              FOREIGN KEY (aa, bb) REFERENCES referenced2 (a, b)
            );

        在上述示例中,**referencing2** 中的 *对* (**aa**, **bb**) 必须与 **referenced2** 中的对应 (**a**, **b**) 对匹配;这些列不是独立约束的。

        请注意,可以(有时有用)创建一个外键约束,其中引用表和被引用表是同一表。例如,一家公司可能有一个引用自身的员工表：

        .. code:: sql

            CREATE TABLE employees (
              id INTEGER PRIMARY KEY,
              name VARCHAR(100),
              supervisor_id INTEGER REFERENCES employees (id)
            );

        与主键一样,一些数据库系统允许使用 **ALTER TABLE** 命令添加或删除外键约束。(SQLite 不支持这种用法。)

    .. md-tab-item:: 英文

        As with primary keys, there are multiple ways to create a foreign key constraint.  If the foreign key constrains a single column, then we can add it in the column definition for a table using the **REFERENCES** keyword:

        .. code:: sql

            DROP TABLE IF EXISTS referencing;
            DROP TABLE IF EXISTS referenced;

            CREATE TABLE referenced (
              x INTEGER PRIMARY KEY
            );

            CREATE TABLE referencing (
              xx INTEGER REFERENCES referenced (x)
            );

        Note that although the foreign key constraint only appears in the referencing table definition, the constraint affects both tables.  The code above ensures that values in the **xx** column of **referencing** are either ``NULL`` or contained in the **x** column of **referenced**.

        (Note for MySQL users: MySQL does not recognize the single column syntax for creating foreign keys.  Use instead the explicit constraint syntax below.)

        We can also create a foreign key constraint with a separate **FOREIGN KEY** entry in the table definition.  This form must be used for multi-column foreign keys:

        .. code:: sql

            DROP TABLE IF EXISTS referencing2;
            DROP TABLE IF EXISTS referenced2;

            CREATE TABLE referenced2 (
              a VARCHAR(10),
              b VARCHAR(20),
              PRIMARY KEY (a, b)
            );

            CREATE TABLE referencing2 (
              c INTEGER PRIMARY KEY,
              aa VARCHAR(10),
              bb VARCHAR(10),
              FOREIGN KEY (aa, bb) REFERENCES referenced2 (a, b)
            );

        In the above example, the *pair* (**aa**, **bb**) in **referencing2** must match a corresponding (**a**, **b**) pair in **referenced2**; the columns are not constrained independently.

        Note that it is possible (and sometimes useful) to create a foreign key constraint in which the referencing and referenced tables are the same table.  For example, a company might have a table of employees that references itself:

        .. code:: sql

            CREATE TABLE employees (
              id INTEGER PRIMARY KEY,
              name VARCHAR(100),
              supervisor_id INTEGER REFERENCES employees (id)
            );

        As with primary keys, some database systems allow the addition or removal of foreign key constraints using the **ALTER TABLE** command.  (This usage is not supported by SQLite.)

.. index:: constraint; violation, ON [UPDATE|DELETE] CASCADE, ON [UPDATE|DELETE] SET NULL, ON [UPDATE|DELETE] RESTRICT

执行机制
----------------------

**Enforcement mechanisms**

.. md-tab-set::

    .. md-tab-item:: 中文

        外键约束的默认行为是拒绝任何可能违反该约束的数据修改尝试。然而,SQL 提供了可应用于 **DELETE** 或 **UPDATE** 查询的附加选项。在外键约束中添加短语 **ON DELETE SET NULL** 表示如果引用表的行被删除,则相应的引用键值应设置为 ``NULL``(如果允许)。短语 **ON DELETE CASCADE** 表示引用行应与被引用行一同删除。类似地,**ON UPDATE SET NULL** 在被引用键值更改时将引用键值设置为 ``NULL``;**ON UPDATE CASCADE** 则将引用键值更改为匹配被更改的引用键值。最后,如果您想明确使用默认行为,可以使用 **ON DELETE RESTRICT** 和 **ON UPDATE RESTRICT**。

        这里是一个示例,使用 **CASCADE** 处理删除和更新(可以修改以尝试不同设置)：

        .. code:: sql

            PRAGMA foreign_keys = ON;

            DROP TABLE IF EXISTS works;
            DROP TABLE IF EXISTS composers;

            CREATE TABLE composers (
              id INTEGER PRIMARY KEY,
              name VARCHAR(30)
            );

            INSERT INTO composers VALUES
              (1, 'Beethoven'),
              (2, 'Mozart')
            ;

            CREATE TABLE works (
              title VARCHAR(50),
              composer_id INTEGER REFERENCES composers (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
            );

            INSERT INTO works VALUES
              ('Symphony No. 1', 1),
              ('Symphony No. 2', 1),
              ('String Quartet No. 1', 2)
            ;

            DELETE FROM composers WHERE name = 'Beethoven';

            UPDATE composers SET id = 4 WHERE name = 'Mozart';

            SELECT * FROM composers;
            SELECT * FROM works;

    .. md-tab-item:: 英文

        The default behavior for a foreign key constraint is to reject any attempt to modify data in a way that would violate the constraint.  However, SQL provides additional options that can be applied for **DELETE** or **UPDATE** queries.  Adding the phrase **ON DELETE SET NULL** to the foreign key constraint indicates that a deletion of a referenced table row should result in setting corresponding referencing key values to ``NULL`` (if permitted).  The phrase **ON DELETE CASCADE** indicates that referencing rows should be deleted along with the referenced row.  Similarly, **ON UPDATE SET NULL** results in setting referencing key values to ``NULL`` if the referenced key value is changed; **ON UPDATE CASCADE** changes the referencing key values to match the changed referenced key value.  Finally, if you want to use the default behavior explicitly, you can use **ON DELETE RESTRICT** and **ON UPDATE RESTRICT**.

        Here is an example to try, using **CASCADE** for both deletions and updates (modify to try different settings):

        .. code:: sql

            PRAGMA foreign_keys = ON;

            DROP TABLE IF EXISTS works;
            DROP TABLE IF EXISTS composers;

            CREATE TABLE composers (
              id INTEGER PRIMARY KEY,
              name VARCHAR(30)
            );

            INSERT INTO composers VALUES
              (1, 'Beethoven'),
              (2, 'Mozart')
            ;

            CREATE TABLE works (
              title VARCHAR(50),
              composer_id INTEGER REFERENCES composers (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
            );

            INSERT INTO works VALUES
              ('Symphony No. 1', 1),
              ('Symphony No. 2', 1),
              ('String Quartet No. 1', 2)
            ;

            DELETE FROM composers WHERE name = 'Beethoven';

            UPDATE composers SET id = 4 WHERE name = 'Mozart';

            SELECT * FROM composers;
            SELECT * FROM works;


其他约束
:::::::::::::::::

**Other constraints**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 提供了一些您可能会觉得有用的附加约束,本节将对此进行描述。

    .. md-tab-item:: 英文

        SQL provides some additional constraints you may find useful, which are described in this section.

.. index:: constraint; uniqueness, UNIQUE

UNIQUE
------

**UNIQUE**

.. md-tab-set::

    .. md-tab-item:: 中文

        偶尔,您可能需要确保某一列或一组列包含唯一值,但您不想将该列或列组设置为主键(例如,当其他某组列已经是主键时)。可以使用 **UNIQUE** 约束来实现此目的;只需在列定义中添加 **UNIQUE** 关键字。**UNIQUE** 约束和主键约束之间的一个区别是,**UNIQUE** 约束不阻止 ``NULL`` 值。然而,数据库对唯一列中的 ``NULL`` 值的处理方式不同;一些数据库允许多行包含 ``NULL``,而其他数据库则仅允许一行 ``NULL``(有效地将 ``NULL`` 视为可比较值)。请注意,下面的最后一条语句将因违反列 **x** 上的 **UNIQUE** 约束而失败。

        .. activecode:: constraints_example_other
            :language: sql
            :dburl: /_static/textbook.sqlite3

            DROP TABLE IF EXISTS test4;
            CREATE TABLE test4 (
              x INTEGER UNIQUE
            );

            INSERT INTO test4 VALUES (1);
            INSERT INTO test4 VALUES (2);
            INSERT INTO test4 VALUES (1);

        您还可以将 **UNIQUE** 约束作为表定义中的单独条目创建(对于多列约束这是必需的)：

        .. code:: sql

              DROP TABLE IF EXISTS test5;
              CREATE TABLE test5 (
                x INTEGER,
                y INTEGER,
                UNIQUE (x, y)
              );

        请注意,针对一组列的主键约束已经隐含了比 **UNIQUE** 更强的含义,因此如果 **PRIMARY KEY** 已经存在,则无需指定 **UNIQUE**。

    .. md-tab-item:: 英文

        Occasionally you may need to ensure that a column or set of columns contains unique values, but you do not want to set the column or columns as a primary key (for example, when some other set of columns is already the primary key).  The **UNIQUE** constraint can be used for this purpose; simply add the **UNIQUE** keyword as part of the column definition.  One difference between a **UNIQUE** constraint and a primary key constraint is that the **UNIQUE** constraint does not prevent ``NULL`` values. However, databases deal with ``NULL`` values in a unique column in different ways; some allow multiple rows to contain ``NULL``, and others allow only a single ``NULL`` row (effectively treating ``NULL`` as a comparable value).  Note that the final statement below will fail due to a violation of the **UNIQUE** constraint on column **x**.

        .. activecode:: constraints_example_other
            :language: sql
            :dburl: /_static/textbook.sqlite3

            DROP TABLE IF EXISTS test4;
            CREATE TABLE test4 (
              x INTEGER UNIQUE
            );

            INSERT INTO test4 VALUES (1);
            INSERT INTO test4 VALUES (2);
            INSERT INTO test4 VALUES (1);

        You can also create a **UNIQUE** constraint as a separate entry in the table definition (this is required for a multi-column constraint):

        .. code:: sql

              DROP TABLE IF EXISTS test5;
              CREATE TABLE test5 (
                x INTEGER,
                y INTEGER,
                UNIQUE (x, y)
              );

        Note that a primary key constraint on a set of columns already implies something stronger than **UNIQUE**, thus there is no need to specify **UNIQUE** if **PRIMARY KEY** is already in place.

.. index:: constraint; not null, NOT NULL

NOT NULL
--------

**NOT NULL**

.. md-tab-set::

    .. md-tab-item:: 中文

        ``NULL`` 值可能是许多数据错误的源头。如果您的软件中的某个错误错误地将 ``NULL`` 值插入数据库,数据将变得不完整,对数据的查询可能会产生错误的结果。此外,由于 ``NULL`` 值不可比较,因此在查询时它们往往是“不可见”的,除非专门使用 **IS NULL** 进行查找。这些因素的结合可能导致您花费大量时间来解决您认为真实的内容与查询结果之间的差异。

        因此,使用 **NOT NULL** 约束限制列不允许 ``NULL`` 值是非常有价值的。在我们的数据库中,一个例子是 **authors** 表,其中 **name** 列有一个 **NOT NULL** 约束——我们始终希望 **name** 列中有一个值 [#]_ . 您可以在与书籍相关的其他表中找到其他示例。

        请注意,主键中的所有列隐含地具有 **NOT NULL**,因此不需要为这些列指定 **NOT NULL**。

    .. md-tab-item:: 英文

        ``NULL`` values can be a source of many data errors.  If some bug in your software incorrectly inserts ``NULL`` values into your database, the data becomes corrupt, and queries against the data may produce wrong answers. Also, since ``NULL`` values are not comparable, they tend to be "invisible" when querying, unless looked for specifically using **IS NULL**.   This combination of factors can result in many lost hours of work trying to resolve differences between what you believe is true and what your queries are telling you.

        It can be valuable, then, to constrain columns to not allow ``NULL`` values at all, using the **NOT NULL** constraint.  In our database, one example is the **authors** table, which has a **NOT NULL** constraint on the **name** column - we always want a value in the **name** column [#]_.  You can find other examples in the books-related tables.

        Note that **NOT NULL** is implied on all columns in a primary key, so there is no need to specify **NOT NULL** for those columns.

.. index:: constraint; check, CHECK

CHECK
-----

**CHECK**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 提供了一种通用的约束形式,您可以用来对数据应用简单的布尔条件。**CHECK** 约束可以是涉及表中单个列或多个列的表达式。这个表达式通常在其他方面的使用上有限制;例如,通常不允许子查询,并且某些数据库不允许调用函数(实现因数据库而异)。

        下面是一个示例,展示了单列和表约束形式：

        .. code:: sql

            DROP TABLE IF EXISTS test6;
            CREATE TABLE test6 (
              a INTEGER CHECK (a BETWEEN 0 AND 100),
              b INTEGER,
              CHECK (b > a)
            );

            INSERT INTO test6 VALUES (42, 200);
            INSERT INTO test6 VALUES (-1, 6);   -- 错误
            INSERT INTO test6 VALUES (10, 5);   -- 错误

    .. md-tab-item:: 英文

        SQL provides a general constraint form that you can use to apply simple Boolean conditions on your data.  The **CHECK** constraint can be an expression involving a single column or multiple columns of the table.  This expression is typically limited in what else it can incorporate; for example subqueries are typically not allowed, and some databases do not allow function calls (implementations vary).

        Here is an example, showing both single column and table constraint forms:

        .. code:: sql

            DROP TABLE IF EXISTS test6;
            CREATE TABLE test6 (
              a INTEGER CHECK (a BETWEEN 0 AND 100),
              b INTEGER,
              CHECK (b > a)
            );

            INSERT INTO test6 VALUES (42, 200);
            INSERT INTO test6 VALUES (-1, 6);   -- error
            INSERT INTO test6 VALUES (10, 5);   -- error


..
  Behind the scenes
  :::::::::::::::::

  While **NOT NULL** and **CHECK** constraints affect single rows of data and can easily be verified when an **INSERT** or **UPDATE** is performed, key constraints and **UNIQUE** constraints require checks against entire tables.  In these cases, the constraint test fails (primary keys and **UNIQUE**) or succeeds (foreign keys) if a set of values matches some row in some table.  You might wonder how these checks can be performed efficiently in situations where the table to be tested contains very many rows.

  A full answer will have to wait until chapter XXX, but the short answer is that the data values we need to search to test our constraint are *indexed* - stored in a special data structure that allows us to find a particular value very fast, without having to examine every row.  Primary keys and columns constrained to be unique are automatically indexed by the database.  Using the index, the database can quickly detect if a duplicate value is about to be created.  To test a foreign key constraint, the database has to determine whether the data we are putting into the referencing table exists in the referenced table.  Since the referenced columns must either form a primary key or be constrained with **UNIQUE**, the data to be searched is indexed once again.

  Indexes are also very important in speeding up queries and statements of all kinds.  We can add additional indexes to the ones implied by our constraints in order to speed up specific searches or modifications.  We will discuss how to use indexes to improve the performance of queries and statements in chapter XXX.

  虽然 **NOT NULL** 和 **CHECK** 约束影响单行数据,并且在执行 **INSERT** 或 **UPDATE** 时可以轻松验证,但主键约束和 **UNIQUE** 约束则需要对整个表进行检查。在这些情况下,约束测试会失败(主键和 **UNIQUE**)或成功(外键),如果一组值与某个表中的某一行匹配。您可能会想知道如何在待测试的表中包含大量行的情况下有效地执行这些检查。

  完整的答案将留到 XXX 章,但简短的回答是,我们需要搜索以测试约束的数据值是 *索引* 的——存储在一种特殊的数据结构中,允许我们非常快速地找到特定值,而无需检查每一行。主键和受约束为唯一的列会自动由数据库建立索引。使用索引,数据库可以快速检测是否即将创建重复值。为了测试外键约束,数据库必须确定我们放入引用表中的数据是否存在于被引用表中。由于被引用的列必须形成主键或受 **UNIQUE** 约束,因此待搜索的数据再次被索引。

  索引在加速各种查询和语句方面也非常重要。我们可以在约束所隐含的索引之外添加额外的索引,以加速特定的搜索或修改。我们将在 XXX 章中讨论如何使用索引来改善查询和语句的性能。



----

**Notes**

.. [#] 我们可能希望记录一些作者未知(或匿名)的书籍,这似乎是一个想要使用 ``NULL`` 的实例;毕竟,``NULL`` 的一个可能含义是“未知”。然而,未知作者在 **authors** 表中有条目意味着什么？如果有的话,我们该如何解释 ``NULL`` 作者的出生和死亡日期字段？如果与该作者记录相关的多本书籍又意味着什么？它们都是同一个未知作者的作品,还是不同作者的作品,而这些作者都是未知的？对于没有已知作者的书籍,允许 **books** 表中 **author_id** 列的 ``NULL`` 值可能是一个稍好的选择——这更接近所需的含义。然而,这也引入了自身的问题,例如 **books** 和 **authors** 的内连接将会排除任何未知作者的书籍,因此我们在编写查询时需要非常小心。所有这些并不是说 ``NULL`` 从来不是正确的选择,而是它引入了复杂性,因此更有可能导致软件错误和数据损坏。请仔细考虑您的选择。

.. [#] It is possible that we might wish to record some book for whom the author is unknown (or anonymous), which might seem like an instance in which we would want ``NULL``; after all, one possible meaning of ``NULL`` is "unknown".  However, what does it mean for an unknown author to have an entry in the **authors** table in the first place?   What meaning would we give, if any, to the birth and death date fields for the ``NULL`` author?  And what does it mean if multiple books relate to that author record?  Are they all by the same, unknown author, or by different authors, all of whom are unknown?  A slightly better choice for a book with no known author may be to allow ``NULL`` values in the **author_id** column in **books** - this is closer to the desired meaning.  However, this introduces problems of its own, such as the fact that an inner join of **books** and **authors** will now leave out any books with unknown authors, so we would need to be very careful in writing our queries.  None of this is to say that ``NULL`` is never the right choice, only that it introduces complexity and therefore more opportunity for software bugs and data corruption.  Consider your options carefully.



