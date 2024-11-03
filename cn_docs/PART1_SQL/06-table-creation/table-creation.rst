.. _table-creation-chapter:

=============================
数据类型和创建表
=============================

.. index:: table; creation

.. md-tab-set::

    .. md-tab-item:: 中文

        本章将讨论基本的表创建,首先解释 SQL 数据类型。

    .. md-tab-item:: 英文


        This chapter will discuss basic table creation, starting with an explanation of SQL data types.

.. index:: data; types, data type

数据类型
::::::::::

**Data types**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 标准定义了几种基本数据类型,可以与列相关联。 虽然大多数基本类型在所有关系数据库系统中都存在,但这些类型的实际实现差异很大。 大多数数据库系统还定义了额外的非标准类型用于各种用途。 不同寻常的是,SQLite 是动态类型的,您可以在任何列中存储任何类型的值,无论该列如何定义。 由于以上所有原因,您需要查阅数据库系统的文档,以了解可用的类型。 在本节中,我们将概述主要数据类型,而不讨论数据库的兼容性;有关更多信息,请参见附录 B - :ref:`appendix-b-data-types`。

    .. md-tab-item:: 英文

        The SQL standard defines several basic data types with which columns can be associated.  While most of the basic types exist in all relational database systems, actual implementation of the types varies quite a bit.  Most database systems define additional, non-standard types for various uses.  Unusually, SQLite is dynamically typed, and you can store values of any type in any column no matter how the column is defined.  For all of these reasons, you will want to consult your database system's documentation to understand the types available to you.  In this section we survey the major data types, without discussion of database compatibility; for more information, see Appendix B - :ref:`appendix-b-data-types`.

数字
-------

**Numbers**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 支持几种不同类型的数字,每种都有不同的应用和限制。 然而,标准的实际实现差异很大;有关数字类型的详细讨论,请参见附录 B - :ref:`appendix-b-number-types`。

    .. md-tab-item:: 英文

        SQL provides support for several different types of numbers, each with different applications and limitations.  However, actual implementation of the standard varies quite a bit; see Appendix B - :ref:`appendix-b-number-types` for a full discussion of number types.

.. index:: data type; integer, INTEGER, INT, SMALLINT, BIGINT

整数
########

**Integers**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 定义了三种整数类型：**INTEGER**、**SMALLINT** 和 **BIGINT**。 这些类型的实现有所不同,但通常情况下,**INTEGER**(通常缩写为 **INT**)存储 32 位整数,**SMALLINT** 存储 16 位整数,而 **BIGINT** 存储 64 位整数。 并非所有数据库都识别所有这些类型,但 **INTEGER** 是本书考虑的所有数据库中都被识别的。 您的数据库系统可能还提供其他整数类型。

    .. md-tab-item:: 英文

        SQL defines three integer types: **INTEGER**, **SMALLINT**, and **BIGINT**.  Implementations of these types vary, but it is not uncommon for **INTEGER** (often abbreviated as **INT**) to store 32-bit integers, **SMALLINT** 16-bit integers, and **BIGINT** 64-bit integers.  Not all databases recognize all of these types, but **INTEGER** is recognized by all of the databases considered for this book.  Additional integer types may be available for your database system.

.. index:: data type; exact decimal number, NUMERIC, DECIMAL, precision, scale

精确十进制数
#####################

**Exact decimal numbers**

.. md-tab-set::

    .. md-tab-item:: 中文

        十进制数字类型允许精确存储在小数点右侧有数字的数字,例如 1234.56789。 这些数字是精确的(与下面描述的浮点类型不同),并允许在可能的情况下进行精确的数学运算(加法、减法和乘法)。 SQL 中定义的两种类型是 **NUMERIC** 和 **DECIMAL**,它们是彼此的同义词。 这些类型可以定义参数表示 *精度* 和 *规模*,其中精度是可以存储的有效数字的数量,规模是小数点后数字的数量。 如果给定了精度但没有给定规模,则规模默认为零。

        例如,在大多数实现中：

        - **NUMERIC(3, 2)** 定义了一种可以存储 -999.99 到 999.99 之间的值的类型,最大有 2 位小数。
        - **NUMERIC(4)** 定义了一种可以存储 -9999 到 9999 之间的整数的类型。
        - **NUMERIC** 定义了一种可以精确存储具有实现定义的精度和规模的十进制值的类型。

        在尝试存储的值超过指定的精度和规模允许的位数时,不同的实现会有不同的行为。 这可能导致错误,或者(在小数点右侧的位数过多的情况下)可能导致值的四舍五入或截断。

        十进制数字类型对于存储货币数据特别重要,因为在此情况下需要精确的加法、减法和乘法。

    .. md-tab-item:: 英文

        Decimal number types allow for exact storage of numbers that have digits to the right of the decimal point, e.g., 1234.56789.  These numbers are exact (unlike the floating point types described below) and permit exact mathematical operations where possible (addition, subtraction, and multiplication).  The two defined types for SQL are **NUMERIC** and **DECIMAL**, which are synonyms of each other.  These types may be defined with parameters representing *precision* and *scale*, where precision is the number of significant digits that can be stored, and scale is the number of digits following the decimal point.  If the precision is given, but not the scale, the scale defaults to zero.

        For example, in most implementations:

        - **NUMERIC(3, 2)** defines a type that can store the values between -999.99 and 999.99, with a maximum of 2 digits past the decimal point.
        - **NUMERIC(4)** defines a type that can store integers between -9999 and 9999.
        - **NUMERIC** defines a type that can exactly store decimal values with implementation-defined precision and scale.

        Different implementations behave differently when an attempt is made to store values with more digits than are allowed by the specified precision and scale.  This may result in an error, or (in the case of too many digits to the right of the decimal point), it may result in rounding or truncation of the value.

        Decimal number types are particularly important for the storage of monetary data, where exact addition, subtraction, and multiplication is necessary.

.. index:: data type; floating point number, FLOAT, REAL, DOUBLE, DOUBLE PRECISION

浮点数
######################

**Floating point numbers**

.. md-tab-set::

    .. md-tab-item:: 中文

        浮点数字类型允许对实数进行可能不精确的存储,类似(或有时相同于)`IEEE 754`_ 规范。 SQL 标准定义了 **FLOAT**、**REAL** 和 **DOUBLE PRECISION**(通常缩写为 **DOUBLE**)类型,但这些类型的实现有所不同。 这些类型可以支持极大和极小的数字,并在科学和数学应用中最为有用。

    .. md-tab-item:: 英文

        Floating point number types allow for a possibly inexact storage of real numbers, similar (or sometimes identical to) the `IEEE 754`_ specification.  The SQL standard defines the types **FLOAT**, **REAL**, and **DOUBLE PRECISION** (often abbreviated **DOUBLE**), but implementation of these types vary.  These types can support extremely large and extremely small numbers, and are most useful in scientific and mathematical applications.

.. _`IEEE 754`: https://en.wikipedia.org/wiki/IEEE_754

.. index:: data type; character string, CHARACTER, CHAR, CHARACTER VARYING, VARCHAR, TEXT

字符串类型
----------------------

**Character string types**

.. md-tab-set::

    .. md-tab-item:: 中文

        在 SQL 中有几种用于存储字符数据的数据类型;同样,实际实现各不相同。有关字符字符串类型的详细讨论,请参见附录 B - :ref:`appendix-b-string-types`。

        类型 **CHARACTER**,通常缩写为 **CHAR**,用于固定长度字符串。类型 **CHAR** 后面跟着括号,括号内包含字符串的长度。例如,类型为 **CHAR(4)** 的列中的所有值必须恰好包含 4 个字符。 在实践中,许多数据库放宽了定义中的“恰好”部分,允许存储较短的字符串,尽管它们可能会用尾随空格填充值。 尝试存储长度超过 *n* 的字符串通常会导致错误。

        **CHARACTER VARYING** 通常缩写为 **VARCHAR**,用于长度可变的字符串,最多到某个最大值,该最大值必须与 **CHAR** 类型一样指定。 尝试存储超过最大长度的字符串通常会导致错误。 (对于 Oracle 用户：Oracle 强烈建议使用他们的 **VARCHAR2** 类型,而不是 **VARCHAR**,尽管两者都被识别。)

        示例：

        - **CHAR(5)** 可以存储字符串 ``'apple'``、``'1 2 3'`` 或 ``'x    '``(带有四个尾随空格),但不能存储 ``'x'`` 或 ``'this is too long'``。
        - **VARCHAR(5)** 可以存储字符串 ``'hello'``、``'a b'`` 或 ``'y'``,但不能存储 ``'also too long'``。

        **VARCHAR** 的一个缺点是需要预测您可能需要存储的字符串的最大长度。 现在许多数据库实现某种类型的任意长度字符字符串类型,通常称为 **TEXT**。 某些数据库对该类型施加限制(例如,不允许其用于索引列)。 在使用 **TEXT** 之前,请确保阅读数据库实现的文档,以了解这些限制;如果您需要在数据库之间实现可移植性,最好使用 **VARCHAR** 并分配充足的大小。

    .. md-tab-item:: 英文

        There are several data types for storing character data in SQL; again, actual implementations vary.  See Appendix B - :ref:`appendix-b-string-types` for a full discussion of character string types.

        The type **CHARACTER**, usually abbreviated as **CHAR**, is used for fixed-length strings.  The type **CHAR** is followed by parentheses enclosing the length of the string.  All values in a column of type **CHAR(4)**, for example, must contain exactly 4 characters.  In practice, many databases relax the "exactly" part of the definition and allow for shorter strings to be stored, although they may pad the value with trailing space characters.  Attempting to store strings longer than *n* usually results in an error.

        **CHARACTER VARYING** is usually abbreviated as **VARCHAR**, and is used for strings of varying length up to some maximum, which must be specified just as with the **CHAR** type.  It is usually an error to attempt to store strings longer than the maximum.  (Note for Oracle users: Oracle strongly recommends using their **VARCHAR2** type rather than **VARCHAR**, although both types are recognized.)

        Examples:

        - **CHAR(5)** can store the strings ``'apple'``, ``'1 2 3'``, or ``'x    '`` (with four trailing spaces), but not ``'x'`` or ``'this is too long'``.
        - **VARCHAR(5)** can store the strings ``'hello'``, ``'a b'`` or ``'y'``, but not ``'also too long'``.

        One disadvantage to **VARCHAR** is the need to predict the maximum length of string that you might need to store.  Many databases now implement some type of arbitrary-length character string type, often named **TEXT**.  Some databases impose limitations on this type (such as not allowing its use for indexed columns).  Be sure to read your database implementation's documentation to understand these limitations before using **TEXT**; if you need portability between databases, it may be best to use **VARCHAR** with a generous size allocation.

.. index:: data type; date, data type; time, data type; timestamp

日期和时间类型
-------------------

**Date and time types**

.. md-tab-set::

    .. md-tab-item:: 中文

        日期和时间数据的管理非常复杂。 日历随着时间变化并在不同文化中有所不同,时区在地理上也有所差异,而对日历和时钟的“闰”调整是不规律的。 SQL 提供了非常强大的日期和时间类型以及对这些类型的操作,这些操作允许对这些值进行非常精确的存储和管理。 然而,实施细节各不相同,您应阅读数据库系统的文档以了解细节。 有关完整讨论,请参见附录 B - :ref:`appendix-b-datetime-types`。

        SQL 中没有标准的日期和时间字面量语法。 在大多数情况下,使用某种实现定义格式的字符串来表示日期和时间。 在内部,这些值可能以十进制数字的形式存储——即从某个固定参考点的偏移量。 在本书中,我们将简单地使用符合 `ISO 8601`_ 标准的字符字符串。 使用这种格式,可以有效地比较日期——``'2001-04-10'`` 确实小于 ``'2014-01-22'``——这也意味着我们可以按日期列对数据进行排序。 时间值可能更棘手,因为可能会包含时区,但我们将通过简单地忽略它们来避免这些复杂性(我们的数据库中没有时间值的示例)。

    .. md-tab-item:: 英文

        Management of date and time data is a very complicated affair.  Calendars change over time and differ among cultures, time zones vary geographically, and "leap" adjustments to the calendar and clock occur irregularly.  SQL provides very robust date and time types along with operations on these types that allow for very precise storage and management of these values.  However, here again implementations vary, and you should read your database system's documentation to understand the fine points.  See Appendix B - :ref:`appendix-b-datetime-types` for a full discussion.

        There is no standard syntax for date and time literals in SQL.  In most cases, strings in some implementation-defined format(s) are used to represent dates and times.  Internally, the values may be stored as decimal numbers - offsets from some fixed reference.  In this book we will simply use character strings conforming to the `ISO 8601`_ standard.  Using this format, dates can be usefully compared - ``'2001-04-10'`` is correctly less than ``'2014-01-22'`` - which also means we can put data in order by date columns.  Time values can be trickier due to the possible inclusion of time zones, but we will avoid these complications by simply ignoring them (there are no examples of time values in our database).

.. _`ISO 8601`: https://en.wikipedia.org/wiki/ISO_8601

.. index:: data type; Boolean, BOOLEAN, True, False

其他数据类型
---------------------

**Additional data types**

.. md-tab-set::

    .. md-tab-item:: 中文

        以下是您在 SQL 环境中可能遇到或希望使用的一些其他数据类型的列表。这些类型并不是所有数据库实现都支持的。

        - SQL 定义了一种布尔数据类型 (**BOOLEAN**),可以存储字面值 **True** 和 **False**,但是并非所有数据库都支持此类型。
        - SQL 还定义了用于存储二进制数据的类型。这在某些情况下可能很有用,尽管像图像或音乐文件这样的二进制数据占用大量空间。因此,通常更可取的是将它们存储在外部,只在数据库中记录检索文件所需的信息(例如,文件路径或 URL)。
        - SQL 提供用户定义类型;即数据库用户为特定应用程序创建的自定义数据类型。
        - 许多数据库支持未在 SQL 标准中定义的类型,或定义为可选扩展,例如用于存储和处理 JSON 和 XML 文档、几何对象、地理或空间坐标、数组等的类型。

    .. md-tab-item:: 英文

        Below is a list of some other data types you might encounter or wish to use in a SQL setting.  These are not supported by all database implementations.

        - SQL defines a Boolean data type (**BOOLEAN**) which can store the literal values **True** and **False**, however, not all databases support this type.
        - SQL also defines types designed to hold binary data.  This can sometimes be useful, although binary data such as images or music files take up a great deal of space. Thus, it is often preferable to store them externally, and only record the information needed to retrieve the files in the database  (e.g., a file path or URL).
        - SQL provides for user-defined types; that is, custom data types created by the database user for specific applications.
        - Many databases support types not defined in the SQL standard, or defined as optional extensions, such as types for storing and working with JSON and XML documents, geometric objects, geographical or spatial coordinates, arrays, and more.


SQLite 中的类型
---------------

**Types in SQLite**

.. md-tab-set::

    .. md-tab-item:: 中文

        正如前面提到的,SQLite(在本书的交互示例中使用)允许将任意类型的数据存储到任何列中;不进行类型检查。 实质上,SQLite 中的一个值可以是 ``NULL``、整数、浮点数或字符字符串。 然而,SQLite 支持用于表创建的标准 SQL 语法,包括为列指定数据类型;这种类型信息可以视为对数据库用户的提示,指示应该存储哪种类型的数据。 我们将在示例中始终使用您可能在其他数据库中找到的类型,并存储与这些类型相适应的数据。

    .. md-tab-item:: 英文

        As mentioned earlier, SQLite (used in the interactive examples in this book) allows the storage of arbitrary types of data into any column; no type checking is performed.  Essentially, a value in SQLite can be ``NULL``, an integer, a floating point number, or a character string.  However, SQLite supports standard SQL syntax for table creation, including specifying data types for columns; this type information can be viewed as a hint to the database user as to what kind of data should be stored.  We will consistently use types that you might find in other databases, and store data appropriate to those types in our examples.

.. index:: CREATE TABLE

创建表
:::::::::::::::

**Creating tables**

.. md-tab-set::

    .. md-tab-item:: 中文

        一旦我们选择了列的类型,就可以使用 **CREATE TABLE** 语句创建一个表。 在我们的第一个示例中,我们将创建一个简单的表,仅用于演示目的。 您不需要担心我们正在更改数据库 - 我们只是使用每次您将教科书加载到浏览器时创建的数据库副本。 您可以随时重新加载此页面以开始新的一轮！

    .. md-tab-item:: 英文

        Once we have chosen the types for our columns, we can create a table using a **CREATE TABLE** statement.  For our first example, we will create something simple just for demonstration purposes.  You do not need to worry that we are changing the database - we are only working with a copy of the database that is created each time you load the textbook into your browser.  You can reload this page anytime you want to start fresh!

从头开始创建表
-----------------------------

**Creating a table from scratch**

.. md-tab-set::

    .. md-tab-item:: 中文

        使用 **CREATE TABLE** 命令来创建一个表。 现在,我们将通过定义表中的列来创建一个简单的表。 之后,我们将以 *约束* 和 *默认值* 的形式向表中添加更多细节。 **CREATE TABLE** 命令的格式如下：

        .. code:: sql

            CREATE TABLE (
            column1 type1,
            column2 type2,
            ...
            );

        其中 "column*n*" 是列的名称,"type*n*" 是您的数据库支持的数据类型。 下面是一些代码供您尝试：

        .. activecode:: table_creation_example_create
            :language: sql
            :dburl: /_static/textbook.sqlite3

            CREATE TABLE test (
            id INTEGER,
            x  VARCHAR(20),
            y  DATE,
            z  NUMERIC(10,2)
            );

            INSERT INTO test VALUES
            (0, 'this is a test', '2021-06-14', 1234.56),
            (1, 'apple', '2021-01-01', 10.10)
            ;

            SELECT * FROM test;

        所有数据库工具都提供某种机制以查看数据库中表的定义。 在 SQLite 中,您可以通过查询特殊表 **sqlite_master** 来查看表的定义：

        .. code:: sql

            SELECT sql FROM sqlite_master WHERE name = 'test';

    .. md-tab-item:: 英文

        Use the **CREATE TABLE** command to create a table.  For now, we will create a simple table by defining the columns in the table.  Later, we will add additional details to the table in the form of *constraints* and *defaults*.  The **CREATE TABLE** command looks like this:

        .. code:: sql

            CREATE TABLE (
            column1 type1,
            column2 type2,
            ...
            );

        Where "column*n*" is the name of a column, and "type*n*" is a data type that your database supports.  Here is some code to try out:

        .. activecode:: table_creation_example_create
            :language: sql
            :dburl: /_static/textbook.sqlite3

            CREATE TABLE test (
            id INTEGER,
            x  VARCHAR(20),
            y  DATE,
            z  NUMERIC(10,2)
            );

            INSERT INTO test VALUES
            (0, 'this is a test', '2021-06-14', 1234.56),
            (1, 'apple', '2021-01-01', 10.10)
            ;

            SELECT * FROM test;

        All database tools provide some mechanism for seeing the definition of tables in the database.  In SQLite, you can see the definition of tables by querying the special table **sqlite_master**:

        .. code:: sql

            SELECT sql FROM sqlite_master WHERE name = 'test';

.. index:: table; removal, DROP TABLE

删除表
---------------

**Dropping tables**

.. md-tab-set::

    .. md-tab-item:: 中文

        当表已经存在时,我们无法 **CREATE** 一个表,因此如果您尝试多次运行上面的示例(而不在浏览器中重新加载此页面),您将收到错误消息。在重新创建之前,我们需要先删除该对象。从数据库中移除对象称为 *删除* 对象,可以通过 **DROP** 语句来完成：

        .. code:: sql

            DROP TABLE test;

        如果在没有名为 **test** 的表时执行此语句,将会导致错误。这可能会造成不便,因为在开发数据库修改程序或 *脚本* 时,我们可能希望多次删除并重新创建表,但不一定总能知道数据库的当前状态。幸运的是,大多数数据库实现了 **DROP** 的扩展,使我们可以仅在表存在时删除它,如果不存在则不会出现错误：

        .. code:: sql

            DROP TABLE IF EXISTS test;

        (注意：对于 Oracle 用户,Oracle 不支持此语法。)

        请注意,删除表还会销毁存储在表中的所有数据,这个操作是不可逆的(没有“撤销”操作)。这也是数据库修改程序通常在使用“真实”数据库之前,先使用数据库的副本进行开发和全面测试的原因之一。

    .. md-tab-item:: 英文

        We cannot **CREATE** a table when it already exists, so if you try to run the above example more than once (without reloading this page in your browser), you will get an error message.  We need to remove the object before re-creating it.  Removing an object from the database is called *dropping* the object, and is accomplished with a **DROP** statement:

        .. code:: sql

            DROP TABLE test;

        This statement will cause an error if you do it when there is no table named **test**, however.  This can be inconvenient, because we might want to drop and recreate the table many times when we are developing a database-modifying program, or *script*, but we may not always know the current state of the database.  Fortunately, most databases implement an extension to **DROP** that lets us remove the table if and only if it exists, without an error if it does not exist:

        .. code:: sql

            DROP TABLE IF EXISTS test;

        (Note for Oracle users: Oracle does not recognize this syntax.)

        Note that dropping a table also destroys all data stored in the table, and this action is irrevocable (there is no "undo" operation).  This is one reason that database-modifying programs are usually developed and thoroughly tested by using a copy of a database before they are ever used on the "real" database.

.. index:: CREATE TABLE ... AS SELECT

通过查询创建表
-----------------------------

**Creating a table from a query**

.. md-tab-set::

    .. md-tab-item:: 中文

        从 SQL 的角度来看,**SELECT** 查询的结果在本质上与表是相同的。不同之处在于,**SELECT** 结果没有名称且仅存在于临时状态。SQL 提供了一种方法,让我们可以将查询的结果保存为一个命名的表,表的列根据结果列隐式定义。任何 **SELECT** 查询都可以使用。下面是一个从我们的 **books** 和 **authors** 表创建表的示例：

        .. activecode:: table_creation_example_create_as_select
            :language: sql
            :dburl: /_static/textbook.sqlite3

            -- 良好的实践是总是以此开始
            DROP TABLE IF EXISTS recent_books;

            CREATE TABLE recent_books AS
            SELECT
                a.name AS author,
                b.title,
                b.publication_year
            FROM
                authors AS a
                JOIN books AS b ON a.author_id = b.author_id
            WHERE b.publication_year >= 2010
            ;

            SELECT sql FROM sqlite_master WHERE name = 'recent_books';

            SELECT * FROM recent_books;

        (注意：对于 SQL Server 用户,SQL Server 不支持上述语法。 SQL Server 中等效的语句如下：``SELECT ... INTO new_table FROM ... WHERE ...;``。)

    .. md-tab-item:: 英文

        From the perspective of SQL, the result of a **SELECT** query is essentially the same thing as a table.  The difference is that the **SELECT** result is not named and exists only temporarily.  SQL provides a way for us to save the result of a query as a named table, with the table columns defined implicitly based on the result columns.  Any **SELECT** query can be used.  Here is an example making a table from our **books** and **authors** tables:

        .. activecode:: table_creation_example_create_as_select
            :language: sql
            :dburl: /_static/textbook.sqlite3

            -- good practice to always start with this
            DROP TABLE IF EXISTS recent_books;

            CREATE TABLE recent_books AS
            SELECT
                a.name AS author,
                b.title,
                b.publication_year
            FROM
                authors AS a
                JOIN books AS b ON a.author_id = b.author_id
            WHERE b.publication_year >= 2010
            ;

            SELECT sql FROM sqlite_master WHERE name = 'recent_books';

            SELECT * FROM recent_books;

        (Note for SQL server users: SQL server does not support the above syntax.  The equivalent statement in SQL server looks like: ``SELECT ... INTO new_table FROM ... WHERE ...;``.)

.. index:: default, auto increment, sequence, DEFAULT, GENERATED ... AS IDENTITY

默认值和自动增量
----------------------------

**Defaults and auto increments**

.. md-tab-set::

    .. md-tab-item:: 中文

        表的列可以定义额外的属性,这些属性可以以不同方式增强数据库的使用。在 :numref:`Chapter {number} <constraints-chapter>` 中,我们将讨论各种 *约束*,它们可以用来限制数据,从而帮助确保数据库整体的有效性。我们可以添加到列的另一个属性是 *默认* 表达式——一个在我们未提供值时由数据库提供的值的表达式。

        以下是一个使用 **DEFAULT** 关键字的示例：

        .. activecode:: table_creation_example_default
            :language: sql
            :dburl: /_static/textbook.sqlite3

            DROP TABLE IF EXISTS test2;

            CREATE TABLE test2 (
            id INTEGER,
            greeting VARCHAR(15) DEFAULT 'Hello'
            );

            INSERT INTO test2 (id, greeting) VALUES (1, 'Good morning');
            INSERT INTO test2 (id, greeting) VALUES (2, NULL);
            INSERT INTO test2 (id) VALUES (3);

            SELECT * FROM test2;

        如你所见,当我们为 **greeting** 列提供了一个值(或 ``NULL``)时,所提供的值被存储。当我们未提供值时,默认值 ``'Hello'`` 被使用。

        在最简单的情况下,如上所示,我们可以为列提供一个文字值。更常见的是,我们将使用一个表达式,通常是调用某种函数。一个常见的用法是记录添加记录到数据库时的日期和时间。我们将在这里使用 **CURRENT_TIMESTAMP** 函数来实现这一目的：

        .. code:: sql

            DROP TABLE IF EXISTS test3;

            CREATE TABLE test3 (
            purchase VARCHAR(10),
            created_at VARCHAR(20) DEFAULT CURRENT_TIMESTAMP
            );

            INSERT INTO test3 (purchase) VALUES ('apple');

            SELECT * FROM test3;

        默认列通常也与一种称为 *序列* 的特殊数据库对象结合使用,序列可以简单地生成顺序整数。这可以用于创建每一行的唯一标识符。例如,这种用法非常常见,以至于 SQL 标准提供了创建必要序列并为表设置默认值的语法;并非所有数据库都支持此语法,但大多数提供某种机制用于生成列的顺序值。 SQL 标准语法在 SQLite 中无法使用,因此你无法在本书的交互工具中进行测试,但使用此语法的列定义如下：

        .. code:: sql

            column_name type GENERATED BY DEFAULT AS IDENTITY

        或者

        .. code:: sql

            column_name type GENERATED ALWAYS AS IDENTITY

        第一种形式允许用户在插入行时提供值,就像常规值一样。第二种形式要求值始终由数据库提供——用户无法覆盖。

        (注意：在本书考虑的数据库中,只有 PostgreSQL 和 Oracle 支持标准语法;它们还提供使用不同语法的等效机制。对于 MySQL,请参阅关于 INTEGER 数据类型的 AUTO_INCREMENT 属性的文档,对于 SQL Server,请查看 CREATE TABLE 下的 IDENTITY 选项。对于 SQLite,请见下文。)

        SQLite 提供了一种与标准类似但不同的机制。在 SQLite 中,我们可以创建一个整数列,该列使用 **AUTOINCREMENT** 关键字自动提供新值。如果用户未提供值,数据库将提供一个值为 1(如果表为空)或大于已存储最大值的 1。要创建这种类型的列,该列还必须声明为主键,相关内容在 :numref:`Chapter {number} <constraints-chapter>` 中讨论。以下是一个示例：

        .. code:: sql

            DROP TABLE IF EXISTS test4;

            CREATE TABLE test4 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            greeting VARCHAR(15)
            );

            INSERT INTO test4 (greeting) VALUES ('Hello');
            INSERT INTO test4 (id, greeting) VALUES (4, 'Good day');
            INSERT INTO test4 (greeting) VALUES ('Good afternoon');

            SELECT * FROM test4;

        在我们的数据库中,表 **bookstore_inventory** 和 **bookstore_sales** 使用自动增量列;**bookstore_sales** 也使用 **DEFAULT** 属性。

    .. md-tab-item:: 英文

        Table columns can be defined with additional properties that can enhance usage of the database in different ways.  In :numref:`Chapter {number} <constraints-chapter>`, we will talk about various *constraints* that can be used to restrict data to help ensure the validity of the database as a whole.  Another property we can add to a column is a *default* expression - an expression producing a value that will be provided by the database only when we do not provide a value.

        Here is an example, showing the usage of the **DEFAULT** keyword:

        .. activecode:: table_creation_example_default
            :language: sql
            :dburl: /_static/textbook.sqlite3

            DROP TABLE IF EXISTS test2;

            CREATE TABLE test2 (
            id INTEGER,
            greeting VARCHAR(15) DEFAULT 'Hello'
            );

            INSERT INTO test2 (id, greeting) VALUES (1, 'Good morning');
            INSERT INTO test2 (id, greeting) VALUES (2, NULL);
            INSERT INTO test2 (id) VALUES (3);

            SELECT * FROM test2;

        As you can see, when we provided a value (or ``NULL``) for the column **greeting**, what we provided was stored.  When we did not provide the value, the default ``'Hello'`` was used.

        In the simplest case, as above, we can provide a literal value for a column.  More commonly, we will use an expression, typically calling a function of some sort.  A common usage for this is to record the date and time when a record is added to the database.  Here we will use the **CURRENT_TIMESTAMP** function for this purpose:

        .. code:: sql

            DROP TABLE IF EXISTS test3;

            CREATE TABLE test3 (
            purchase VARCHAR(10),
            created_at VARCHAR(20) DEFAULT CURRENT_TIMESTAMP
            );

            INSERT INTO test3 (purchase) VALUES ('apple');

            SELECT * FROM test3;

        Default columns are also commonly used in combination with a special kind of database object called a *sequence*, which simply generates sequential integers.  This can be used, for example, to create unique identifiers for every row in a table.  This usage is so common that the SQL standard provides syntax that both creates the necessary sequence and sets up the default for the table; not all databases support this syntax, but most provide some mechanism for the generation of sequential values for a column.  The SQL standard syntax does not work in SQLite, so you will not be able to test it in an interactive tool in this book, but the column definition using this syntax is

        .. code:: sql

            column_name type GENERATED BY DEFAULT AS IDENTITY

        or

        .. code:: sql

            column_name type GENERATED ALWAYS AS IDENTITY

        The first form allows values to be provided by the user when inserting a row, just like a regular value.  The second form requires that the value always be provided by the database - it cannot be overridden by the user.

        (Note: of the databases considered for this book, only PostgreSQL and Oracle support the standard syntax; they also provide equivalent mechanisms using different syntax.  For MySQL, see documentation on the AUTO_INCREMENT property of the INTEGER data type, and for SQL Server, see the IDENTITY option under CREATE TABLE.  For SQLite, see below.)

        SQLite provides a mechanism which is similar to, but different from the standard.  In SQLite, we can create an integer column that automatically provides a new value using the **AUTOINCREMENT** keyword. If the user does not provide a value, the database supplies a value of 1 (if the table is empty) or 1 greater than the maximum value already stored.  To create a column of this type, the column must also be declared to be a primary key, a topic covered in :numref:`Chapter {number} <constraints-chapter>`.  Here is an example to try out:

        .. code:: sql

            DROP TABLE IF EXISTS test4;

            CREATE TABLE test4 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            greeting VARCHAR(15)
            );

            INSERT INTO test4 (greeting) VALUES ('Hello');
            INSERT INTO test4 (id, greeting) VALUES (4, 'Good day');
            INSERT INTO test4 (greeting) VALUES ('Good afternoon');

            SELECT * FROM test4;

        In our database, the tables **bookstore_inventory** and **bookstore_sales** use auto increment columns; **bookstore_sales** also uses the **DEFAULT** property.

自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含有关创建表的练习。如果遇到困难,请点击练习下方的“显示答案”按钮以查看正确答案。

        - 写一个语句创建一个名为 **my_table** 的表,包含列 **a**、**b**、**c** 和 **d**。列 **a** 将包含最多 100 个字符的字符串; **b** 将包含日期; **c** 将包含最多 15 位数字,其中有 3 位在小数点后; **d** 将包含恰好两个字符的字符串。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                CREATE TABLE my_table (
                a VARCHAR(100),
                b DATE,
                c NUMERIC(15,3),
                d CHAR(2)
                );

        - 写一个语句以删除 **my_table**。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                DROP TABLE my_table;

            或

            .. code:: sql

                DROP TABLE IF EXISTS my_table;

        - 写一个语句创建一个名为 **a_authors** 的表,只包含名字以字母 'A' 开头的作者。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                CREATE TABLE a_authors AS
                SELECT * FROM authors
                WHERE name LIKE 'A%'
                ;

    .. md-tab-item:: 英文

        This section contains exercises on table creation.  If you get stuck, click on the "Show answer" button below the exercise to see a correct answer.

        - Write a statement to create a table named **my_table** with columns **a**, **b**, **c**, and **d**.  Column **a** will contain strings of at most 100 characters; **b** will contain dates; **c** will contain numbers with at most 15 digits, three of which come after the decimal point; and **d** will contain strings of exactly two characters.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                CREATE TABLE my_table (
                a VARCHAR(100),
                b DATE,
                c NUMERIC(15,3),
                d CHAR(2)
                );

        - Write a statement to remove **my_table**.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                DROP TABLE my_table;

            or

            .. code:: sql

                DROP TABLE IF EXISTS my_table;

        - Write a statement to create a table named **a_authors** containing just authors whose names start with the letter 'A'.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                CREATE TABLE a_authors AS
                SELECT * FROM authors
                WHERE name LIKE 'A%'
                ;




----

..
 **Notes**

 .. [#] Relational databases allow operations to be wrapped in something called a *transaction*, which does provide a way to undo work.  We will study transactions more in chapter XXX.



