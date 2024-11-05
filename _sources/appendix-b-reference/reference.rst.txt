.. _appendix-b:

=========================
附录 B: SQL 参考
=========================

**Appendix B: SQL Reference**

.. md-tab-set::

    .. md-tab-item:: 中文

        本附录包含有关 SQL 标准（2016年）各个方面的文档。这并不是标准的详尽指南。在可能的情况下，文档中会展示各种数据库实现（SQLite、PostgreSQL、MySQL、Oracle、Microsoft SQL Server）与标准的差异。请注意，这类文档是动态变化的，因此您阅读时以下信息可能已经过时。请查阅您的数据库供应商的文档以获取最新信息。

        在下面的文档中，选项可能用方括号表示。例如， **SUBSTRING** 函数的用法文档如下所示：

        .. code:: sql

            SUBSTRING(*s* FROM *start* [FOR *length*])

        这意味着以下两个表达式都是有效的：

        .. code:: sql

            SUBSTRING('hello, world' FROM 1 FOR 5)
            SUBSTRING('hello, world' FROM 8)

        （第一个表达式的结果为 ``'hello'``，第二个表达式的结果为 ``'world'``。）

    .. md-tab-item:: 英文

        This appendix contains documentation on various aspects of the SQL standard (2016).  This is not an exhaustive guide to the standard.  Where possible, variations from the standard by various database implementations (SQLite, PostgreSQL, MySQL, Oracle, Microsoft SQL Server) are shown.  Note that documentation of this sort is a moving target, so the information below may be out-of-date when you read it.  Consult your database vendor's documentation for current information.

        In the documentation below, options may be indicated using square brackets.  For example, usage of the **SUBSTRING** function is documented as

        .. code:: sql

            SUBSTRING(*s* FROM *start* [FOR *length*])

        meaning both of the following expressions are valid:

        .. code:: sql

            SUBSTRING('hello, world' FROM 1 FOR 5)
            SUBSTRING('hello, world' FROM 8)

        (The first expression evaluates to ``'hello'``, and the second to ``'world'``.)

.. _appendix-b-data-types:
.. _Data types:

数据类型
::::::::::

**Data types**

.. _appendix-b-number-types:

数字类型
------------

**Number types**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 标准同时支持精确（整数和定点十进制）和不精确（浮点）数字。这些类型的详细信息（例如，数字表示中使用的位数）由各个实现决定，因此请查阅您的数据库文档以充分了解其功能。

    .. md-tab-item:: 英文

        The SQL standard provides for both exact (integers and fixed-precision decimal) and inexact (floating point) numbers.  Details of these types (e.g., the number of bits used in the number representation) are left up to individual implementations, so consult your database's documentation to fully understand its capabilities.

整数
########

**Integers**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 定义了三种整数类型： **INTEGER** 、 **SMALLINT** 和 **BIGINT**。这些类型的实现有所不同，但通常情况下， **INTEGER**（通常缩写为 **INT**）存储 32 位整数， **SMALLINT** 存储 16 位整数， **BIGINT** 存储 64 位整数。并非所有数据库都识别所有这些类型，但本书考虑的所有数据库都识别 **INTEGER**。您的数据库系统可能还提供其他整数类型。

    .. md-tab-item:: 英文

        SQL defines three integer types: **INTEGER**, **SMALLINT**, and **BIGINT**.  Implementations of these types vary, but it is not uncommon for **INTEGER** (often abbreviated as **INT**) to store 32-bit integers, **SMALLINT** 16-bit integers, and **BIGINT** 64-bit integers.  Not all databases recognize all of these types, but **INTEGER** is recognized by all of the databases considered for this book.  Additional integer types may be available for your database system.

精确十进制数
#####################

**Exact decimal numbers**

.. md-tab-set::

    .. md-tab-item:: 中文

        十进制数字类型允许精确存储在小数点右侧有数字的数字，例如 1234.56789。这些数字是精确的（与下面的浮点类型相比），并允许在可能的情况下进行精确的数学运算（加法、减法和乘法）。 SQL 中定义的两种类型是 **NUMERIC** 和 **DECIMAL**，它们是彼此的同义词。这些类型可以定义参数来表示 *精度(precision)* 和 *小数位数(scale)*，其中精度是可以存储的有效数字的数量，小数位数是小数点后面的数字数量。如果给定了精度，但没有给出小数位数，则小数位数默认为零。

        例如，在大多数实现中：

        - **NUMERIC(3, 2)** 定义了一种可以存储值范围在 -999.99 到 999.99 之间的类型，最大小数位数为 2。
        - **NUMERIC(4)** 定义了一种可以存储范围在 -9999 到 9999 之间的整数类型。
        - **NUMERIC** 定义了一种可以精确存储具有实现定义的精度和小数位数的十进制值的类型。

        不同的实现对尝试存储超过指定精度和小数位数所允许的数字时的行为不同。这可能会导致错误，或者（在小数点后数字过多的情况下）可能会导致值的四舍五入或截断。

    .. md-tab-item:: 英文

        Decimal number types allow for exact storage of numbers that have digits to the right of the decimal point, e.g., 1234.56789.  These numbers are exact (compare to the floating point types below), and permit exact mathematical operations where possible (addition, subtraction, and multiplication).  The two defined types for SQL are **NUMERIC** and **DECIMAL**, which are synonyms of each other.  These types may be defined with parameters representing *precision* and *scale*, where precision is the number of significant digits that can be stored, and scale is the number of digits following the decimal point.  If the precision is given, but not the scale, the scale defaults to zero.

        For example, in most implementations:

        - **NUMERIC(3, 2)** defines a type that can store the values between -999.99 and 999.99, with a maximum of 2 digits past the decimal point.
        - **NUMERIC(4)** defines a type that can store integers between -9999 and 9999.
        - **NUMERIC** defines a type that can exactly store decimal values with implementation-defined precision and scale.

        Different implementations behave differently when an attempt is made to store values with more digits than are allowed by the specified precision and scale.  This may result in an error, or (in the case of too many digits to the right of the decimal point), it may result in rounding or truncation of the value.

浮点数
######################

**Floating point numbers**

.. _`IEEE 754`: https://en.wikipedia.org/wiki/IEEE_754

.. md-tab-set::

    .. md-tab-item:: 中文

        浮点数字类型允许（可能是不精确的）实数存储，类似（或有时与） `IEEE 754`_ 规范相同。 SQL 标准定义了 **FLOAT** 、 **REAL** 和 **DOUBLE PRECISION**（通常缩写为 **DOUBLE**）这几种类型，但这些类型的实现各不相同。

    .. md-tab-item:: 英文

        Floating point number types allow for (possibly inexact) storage of real numbers, similar (or sometimes identical to) the `IEEE 754`_ specification.  The SQL standard defines the types **FLOAT**, **REAL**, and **DOUBLE PRECISION** (often abbreviated **DOUBLE**), but implementation of these types vary.

数据库对数字类型的支持
#################################

**Database support for number types**

.. md-tab-set::

    .. md-tab-item:: 中文

        数据库对数字类型支持的摘要如下（适用于本教材尝试涵盖的五个数据库）：

        ================  ===================== ============================== ======== ================================== ================
        类型              SQLite                PostgreSQL                     MySQL    Oracle                             SQL Server
        ================  ===================== ============================== ======== ================================== ================
        INTEGER           是                     是                              是        使用 NUMBER                        是
        SMALLINT          相当于 INTEGER                是                     是                 使用 NUMBER                          是
        BIGINT            相当于 INTEGER                是                      是                使用 NUMBER                          是
        NUMERIC/DECIMAL   是                     是                              是        使用 NUMBER                         是
        FLOAT             相当于 REAL                  相当于 DOUBLE PRECISION      是       是；但推荐使用 BINARY_DOUBLE      是
        REAL              是                     是                             是       是；但推荐使用 BINARY_DOUBLE      是
        DOUBLE PRECISION  相当于 REAL           是                             是       是； 但推荐使用 BINARY_DOUBLE      使用 FLOAT
        ================  ===================== ============================== ======== ================================== ================

    .. md-tab-item:: 英文

        A summary of database support for number types is shown below (for the five databases this textbook attempts to cover):

        ================  ===================== ============================== ======== ================================== ================
        Type              SQLite                PostgreSQL                     MySQL    Oracle                             SQL Server
        ================  ===================== ============================== ======== ================================== ================
        INTEGER           yes                   yes                            yes      use NUMBER                         yes
        SMALLINT          equivalent to INTEGER yes                            yes      use NUMBER                         yes
        BIGINT            equivalent to INTEGER yes                            yes      use NUMBER                         yes
        NUMERIC/DECIMAL   yes                   yes                            yes      use NUMBER                         yes
        FLOAT             equivalent to REAL    equivalent to DOUBLE PRECISION yes      yes; but BINARY_DOUBLE recommended yes
        REAL              yes                   yes                            yes      yes; but BINARY_DOUBLE recommended yes
        DOUBLE PRECISION  equivalent to REAL    yes                            yes      yes; but BINARY_DOUBLE recommended use FLOAT
        ================  ===================== ============================== ======== ================================== ================


.. _appendix-b-string-types:

字符串类型
----------------------

**Character string types**

.. md-tab-set::

    .. md-tab-item:: 中文

        在 SQL 中存储字符数据有三种主要数据类型。官方名称为 **CHARACTER**、 **CHARACTER VARYING** 和 **CHARACTER LARGE OBJECT** 。此外，修饰符 **NATIONAL** 可用于指示包含来自区域相关字符集的数据的字符串。这些名称相对较长且不够简洁，因此数据库通常使用缩写或甚至完全不同的名称来表示相同的概念。

        类型 **CHARACTER**，通常缩写为 **CHAR**，用于固定长度的字符串。类型 **CHAR** 后面跟着括号，括号内包含字符串的长度。例如，类型为 **CHAR(4)** 的列中所有值必须恰好包含 4 个字符。实际上，许多数据库放宽了定义中“恰好”的部分，允许存储较短的字符串，尽管它们可能会用尾随的空格字符对值进行“填充”。尝试存储超过 *n* 长度的字符串通常会导致错误。

        **CHARACTER VARYING** 通常缩写为 **VARCHAR**，用于可变长度的字符串，长度上限必须指定，与 **CHAR** 类型一样。尝试存储超过最大长度的字符串通常会导致错误。

        **CHARACTER LARGE OBJECT** 有许多名称，用于存储任意长度的字符串，长度上限由实现定义（例如，Oracle 的 **CLOB** 类型在某些情况下允许最大字符串长度为 128TB）。在许多实现中，此类型在可以使用的操作或函数上受到限制，并且可能不允许索引。

        数据库对字符字符串支持的摘要如下：

        =======================  ===================== ========== ======== =============== ================
        Type                     SQLite                PostgreSQL MySQL    Oracle          SQL Server
        =======================  ===================== ========== ======== =============== ================
        CHARACTER(n)             equivalent to TEXT    yes        yes      yes             yes
        CHARACTER VARYING(n)     equivalent to TEXT    yes        yes      use VARCHAR2(n) yes
        CHARACTER LARGE OBJECT   equivalent to TEXT    use TEXT   use TEXT use CLOB        use VARCHAR(MAX)
        =======================  ===================== ========== ======== =============== ================

    .. md-tab-item:: 英文

        There are three main data types for storing character data in SQL.  Officially, these are named **CHARACTER**, **CHARACTER VARYING**, and **CHARACTER LARGE OBJECT**.  In addition, the modifier **NATIONAL** may be used to indicate strings containing data from locale-dependent character sets.  These names are fairly long and clunky, so databases typically use abbreviations or even completely different names for the same concepts.

        The type **CHARACTER**, usually abbreviated as **CHAR**, is used for fixed-length strings.  The type **CHAR** is followed by parentheses enclosing the length of the string.  All values in a column of type **CHAR(4)**, for example, must contain exactly 4 characters.  In practice, many databases relax the "exactly" part of the definition and allow for shorter strings to be stored, although they may "pad" the value with trailing space characters.  Attempting to store strings longer than *n* usually results in an error.

        **CHARACTER VARYING** is usually abbreviated as **VARCHAR**, and is used for strings of varying length up to some maximum, which must be specified just as with the **CHAR** type.  It is usually an error to attempt to store strings longer than the maximum.

        **CHARACTER LARGE OBJECT** goes by many names, and is used to store strings of arbitrary length, up to some implementation-defined maximum (for example, Oracle's **CLOB** type allows strings of up to 128TB in some cases).  In many implementations, this type is limited in the operations or functions that may be used, and may not allow indexing.

        A summary of database support for character strings is shown below:

        =======================  ===================== ========== ======== =============== ================
        Type                     SQLite                PostgreSQL MySQL    Oracle          SQL Server
        =======================  ===================== ========== ======== =============== ================
        CHARACTER(n)             equivalent to TEXT    yes        yes      yes             yes
        CHARACTER VARYING(n)     equivalent to TEXT    yes        yes      use VARCHAR2(n) yes
        CHARACTER LARGE OBJECT   equivalent to TEXT    use TEXT   use TEXT use CLOB        use VARCHAR(MAX)
        =======================  ===================== ========== ======== =============== ================


.. _appendix-b-datetime-types:

日期和时间类型
-------------------

**Date and time types**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 标准定义了三种或五种主要类型，这取决于如何计数。这些类型是 **DATE**、**TIME**（有时区或无时区）和 **TIMESTAMP**（有时区或无时区）。如果您仅指定 **TIME** 或 **TIMESTAMP**，则会获得不带时区的版本；附加 **WITH TIME ZONE** 以存储时区信息。

        - **DATE** 值以一种方式存储日期，使得历史上任何特定的日期都可以被准确记录。通常支持公历，但某些实现会转换为儒略历或其他日历。
        - **TIME** 表示一天中的某个时间，而不参考日期。**TIME WITH TIME ZONE** 包括指定相对于哪个时区评估时间的信息。
        - **TIMESTAMP** 表示一个精确的时间点，包含日期和一天中的时间（有时区或无时区）。

        数据库对日期和时间类型支持的摘要如下：

        ========================  ========================== ========== ======== ================================ ================
        Type                      SQLite                     PostgreSQL MySQL    Oracle                           SQL Server
        ========================  ========================== ========== ======== ================================ ================
        DATE                      use TEXT, REAL, or INTEGER yes        yes      yes                              yes
        TIME                      use TEXT, REAL, or INTEGER yes        yes      no, use TIMESTAMP                yes
        TIME WITH TIME ZONE       use TEXT, REAL, or INTEGER yes        no       no, use TIMESTAMP WITH TIME ZONE no
        TIMESTAMP                 use TEXT, REAL, or INTEGER yes        yes      yes                              use DATETIME2
        TIMESTAMP WITH TIME ZONE  use TEXT, REAL, or INTEGER yes        no       yes                              no
        ========================  ========================== ========== ======== ================================ ================

        除了日期和时间类型，SQL 还定义了一组称为 *interval* 的类型，其中间隔表示两个日期或时间值之间的天数或时间跨度。本书不涵盖间隔类型。

    .. md-tab-item:: 英文

        The SQL standard defines three or five principal types, depending on how you count.  The types are **DATE**, **TIME** (with or without time zone), and **TIMESTAMP** (with or without time zone).  If you specify simply **TIME** or **TIMESTAMP**, you get the version without time zones; append **WITH TIME ZONE** to additionally store time zone information.

        - **DATE** values store dates in such a way that any particular day in history can be accurately recorded.  Typically the Gregorian calendar is supported, but some implementations will convert to and from Julian dates or other calendars.
        - **TIME** represents a time of day, without reference to the date.  **TIME WITH TIME ZONE** includes information specifying the time zone relative to which the time should be evaluated.
        - **TIMESTAMP** represents a precise moment in time, incorporating both the date and the time of day (with or without time zone).

        A summary of database support for date and time types is shown below:

        ========================  ========================== ========== ======== ================================ ================
        Type                      SQLite                     PostgreSQL MySQL    Oracle                           SQL Server
        ========================  ========================== ========== ======== ================================ ================
        DATE                      use TEXT, REAL, or INTEGER yes        yes      yes                              yes
        TIME                      use TEXT, REAL, or INTEGER yes        yes      no, use TIMESTAMP                yes
        TIME WITH TIME ZONE       use TEXT, REAL, or INTEGER yes        no       no, use TIMESTAMP WITH TIME ZONE no
        TIMESTAMP                 use TEXT, REAL, or INTEGER yes        yes      yes                              use DATETIME2
        TIMESTAMP WITH TIME ZONE  use TEXT, REAL, or INTEGER yes        no       yes                              no
        ========================  ========================== ========== ======== ================================ ================

        In addition to the date and time types, SQL defines a set of types known as *interval* types, where an interval represents a span of days or time between two date or time values.  Intervals are not covered in this book.


运算和函数
:::::::::::::::::::::::

**Operators and functions**

.. _appendix-b-comparison-operators:

比较运算符
--------------------

**Comparison operators**

.. md-tab-set::

    .. md-tab-item:: 中文

        一般来说，同类型的两个非 NULL 值可以进行比较，结果为布尔值。在某些情况下，可以比较不同类型的值，例如当两个值都是数字时。数字值根据它们的代数值进行比较。日期、时间和时间戳值按时间顺序比较。布尔值 ``True`` 大于 ``False``。

        字符字符串比较相对复杂，因为比较结果依赖于对值有效的 *排序规则*；排序可能依赖于许多因素，包括：DBMS 实现、DBMS 配置参数（如 *区域设置*）、操作系统参数，以及给定数据库表的任何显式排序设置。排序可以用于在特定语言环境中实现正确的排序。例如，通常如果字符串 *s* 在排序（升序）中排在字符串 *t* 之前，则 *s* \< *t*。

        将任何值与 ``NULL`` 进行比较时，使用下表中的任何运算符都会导致结果为 ``NULL`` [#]_。

        =========== ========================= =========================== =============================================
        operator    meaning                   usage                       notes
        =========== ========================= =========================== =============================================
        \=          equal to                  *x* \= *y*
        \<\>        not equal to              *x* \<\> *y*                can also use != in most DBMSes (nonstandard)
        \<          less than                 *x* \< *y*
        \>          greater than              *x* \> *y*
        \<=         less than or equal to     *x* \<= *y*
        \>=         greater than or equal to  *x* \>= *y*
        BETWEEN     range comparison          *x* BETWEEN *y* AND *z*     equivalent to *x* \>= *y* AND *x* \<= *z*
        NOT BETWEEN exterior range comparison *x* NOT BETWEEN *y* AND *z* equivalent to NOT(*x* BETWEEN *y* AND *z*)
        =========== ========================= =========================== =============================================

        比较 ``NULL`` 值需要特殊处理；表达式 ``NULL = NULL`` 的结果为 ``NULL``，而不是 ``True``，因此在测试 ``NULL`` 时并不有用。为此提供了 **IS NULL** 运算符。**IS NULL**（以及其反向，**IS NOT NULL**）表达式始终返回 ``True`` 或 ``False``。

        另一个在存在 ``NULL`` 值时有用的标准 SQL 运算符是二元运算符 **IS DISTINCT FROM** 和 **IS NOT DISTINCT FROM**。这些运算符比较两个值，将 ``NULL`` 视为一个特殊的、不同的值，并始终返回 ``True`` 或 ``False``。因此，表达式 ``x IS NOT DISTINCT FROM y`` 在 ``x = y`` 为真，或当 *x* 和 *y* 都为 ``NULL`` 时返回 ``True``。在本书考虑的数据库中，只有 PostgreSQL 实现了 **IS DISTINCT FROM** 和 **IS NOT DISTINCT FROM**。

        下表总结了这些运算符。

        ==================== ============================ =========================================================== ================
        operator             usage                        result                                                      notes
        ==================== ============================ =========================================================== ================
        IS NULL              *x* IS NULL                  True if and only if *x* evaluates to NULL
        IS NOT NULL          *x* IS NOT NULL              equivalent to NOT (*x* IS NULL)
        IS DISTINCT FROM     *x* IS DISTINCT FROM *y*     equivalent to NOT (*x* IS NOT DISTINCT FROM *y*)            PostgreSQL only
        IS NOT DISTINCT FROM *x* IS NOT DISTINCT FROM *y* True if *x* = *y* is true, or if *x* and *y* are both NULL  PostgreSQL only
        ==================== ============================ =========================================================== ================

        另见下面的 `布尔运算符`_ 部分，了解仅适用于布尔值的比较运算符。

    .. md-tab-item:: 英文

        Generally speaking, two non-NULL values of the same type can be compared, resulting in a Boolean value.  In certain cases, comparisons can made between different types, e.g., when both are numbers.  Numeric values are compared according to their algebraic values.  Date, time, and timestamp values are compared chronologically.  The Boolean value ``True`` is greater than ``False``.

        Character string comparison is somewhat complex, as the comparison done depends on the *collation* rules in effect for the values; collation may depend on many factors including: the DBMS implementation, DBMS configuration parameters (such as the *locale*), operating system parameters, and any explicit collation settings for a given database table.  Collations may be used to implement proper sorting, for example, in a particular language context.  In general, if string *s* would appear in sorted (ascending) order prior to string *t*, then *s* \< *t*.

        A comparison of any value with ``NULL`` results in ``NULL`` [#]_ when using any of the operators in the table below.

        =========== ========================= =========================== =============================================
        operator    meaning                   usage                       notes
        =========== ========================= =========================== =============================================
        \=          equal to                  *x* \= *y*
        \<\>        not equal to              *x* \<\> *y*                can also use != in most DBMSes (nonstandard)
        \<          less than                 *x* \< *y*
        \>          greater than              *x* \> *y*
        \<=         less than or equal to     *x* \<= *y*
        \>=         greater than or equal to  *x* \>= *y*
        BETWEEN     range comparison          *x* BETWEEN *y* AND *z*     equivalent to *x* \>= *y* AND *x* \<= *z*
        NOT BETWEEN exterior range comparison *x* NOT BETWEEN *y* AND *z* equivalent to NOT(*x* BETWEEN *y* AND *z*)
        =========== ========================= =========================== =============================================

        Comparison of ``NULL`` values requires special treatment; the expression ``NULL = NULL`` results in ``NULL``, not ``True``, and thus is not useful in testing for ``NULL``.  The **IS NULL** operator is provided for this purpose.  **IS NULL** (and the inverse, **IS NOT NULL**) expressions always result in ``True`` or ``False``.

        Another standard SQL operator that has utility in the presence of ``NULL`` values are the binary operators **IS DISTINCT FROM** and **IS NOT DISTINCT FROM**.  These operators compare two values, treating ``NULL`` as if it were a special, distinct value, and always return ``True`` or ``False``.  Thus, the expression ``x IS NOT DISTINCT FROM y`` returns ``True`` if ``x = y`` evaluates to ``True`` or if *x* and *y* are both ``NULL``.  Of the databases considered for this book, only PostgreSQL implements **IS DISTINCT FROM** and **IS NOT DISTINCT FROM**.

        The table below summarizes these operators.

        ==================== ============================ =========================================================== ================
        operator             usage                        result                                                      notes
        ==================== ============================ =========================================================== ================
        IS NULL              *x* IS NULL                  True if and only if *x* evaluates to NULL
        IS NOT NULL          *x* IS NOT NULL              equivalent to NOT (*x* IS NULL)
        IS DISTINCT FROM     *x* IS DISTINCT FROM *y*     equivalent to NOT (*x* IS NOT DISTINCT FROM *y*)            PostgreSQL only
        IS NOT DISTINCT FROM *x* IS NOT DISTINCT FROM *y* True if *x* = *y* is true, or if *x* and *y* are both NULL  PostgreSQL only
        ==================== ============================ =========================================================== ================

        Also see the `Boolean operators`_ section below for comparison operators that only apply to Boolean values.

.. _appendix-b-math-operators:

数学运算符和函数
------------------------------------

**Mathematical operators and functions**

.. md-tab-set::

    .. md-tab-item:: 中文

        除非另有说明，下面的操作数或参数可以是任何数字类型。

        ================== ===================== ================================ ===========================================
        运算符  / 函数     含义                  用法                             备注 
        ================== ===================== ================================ ===========================================
        \+                 加法                  *x* + *y*
        \-                 减法                  *x* - *y*
        \*                 乘法                  *x* * *y*
        \/                 除法sion              *x* / *y*
        ABS                绝对值                ABS(*x*)
        MOD                取模（余数）           MOD(*x*, *divisor*)              标准 SQL 中仅限整数          
        LOG                对数(logarithm)        LOG(*base*, *x*)                 在 SQL Server 中, 使用 LOG(*x*, *base*)
        LN                 自然对数              LN(*x*)                          在 SQL Server 中, 使用 LOG(*x*)
        LOG10              基于 10 的对数        LOG10(*x*)                       在 SQL Server 中, 使用 LOG(10, *x*)
        EXP                指数函数              EXP(*x*)
        POWER              幂运算                POWER(*base*, *exponent*)
        SQRT               平方根                SQRT(*x*)
        FLOOR              向下取整              FLOOR(*x*)
        CEILING            向上取整              CEILING(*x*) or CEIL(*x*)
        SIN                正弦函数              SIN(*x*)                         参数为弧 (radians) 
        COS                余弦函数              COS(*x*)
        TAN                正切函数              TAN(*x*)
        ASIN               反正弦                ASIN(*x*)
        ACOS               反余弦                ACOS(*x*)
        ATAN               反正切                ATAN(*x*)
        SINH               双曲正弦              SINH(*x*)
        COSH               双曲余弦              COSH(*x*)
        TANH               双曲正切              TANH(*x*)
        ================== ===================== ================================ ===========================================

        大多数数据库实现提供额外的非标准函数和运算符；例如，大多数包括生成随机数的某种机制。

        数学表达式中，如果一个或多个操作数或输入为 ``NULL``，则评估结果为 ``NULL``。

    .. md-tab-item:: 英文

        Unless otherwise noted, the operands or parameters below can be any numeric type.

        ================== ===================== ================================ ===========================================
        operator/ function meaning               usage                            notes
        ================== ===================== ================================ ===========================================
        \+                 addition              *x* + *y*
        \-                 subtraction           *x* - *y*
        \*                 multiplication        *x* * *y*
        \/                 division              *x* / *y*
        ABS                absolute value        ABS(*x*)
        MOD                modulus (remainder)   MOD(*x*, *divisor*)              integers only in standard SQL
        LOG                logarithm             LOG(*base*, *x*)                 in SQL Server, use LOG(*x*, *base*)
        LN                 natural logarithm     LN(*x*)                          in SQL Server, use LOG(*x*)
        LOG10              base-10 logarithm     LOG10(*x*)                       in Oracle, use LOG(10, *x*)
        EXP                exponential function  EXP(*x*)
        POWER              raise to power        POWER(*base*, *exponent*)
        SQRT               square root           SQRT(*x*)
        FLOOR              floor function        FLOOR(*x*)
        CEILING            ceiling function      CEILING(*x*) or CEIL(*x*)
        SIN                sine function         SIN(*x*)                         argument in radians
        COS                cosine function       COS(*x*)
        TAN                tangent function      TAN(*x*)
        ASIN               inverse sine          ASIN(*x*)
        ACOS               inverse cosine        ACOS(*x*)
        ATAN               inverse tangent       ATAN(*x*)
        SINH               hyperbolic sine       SINH(*x*)
        COSH               hyperbolic cosine     COSH(*x*)
        TANH               hyperbolic tangent    TANH(*x*)
        ================== ===================== ================================ ===========================================

        Most database implementations provide additional non-standard functions and operators; for example, most include some mechanism for generating random numbers.

        Mathematical expressions where one or more operands or inputs are ``NULL`` evaluate to ``NULL``.


.. _appendix-b-string-operators:

字符串运算符和函数
----------------------------------------

**Character string operators and functions**


.. _`Chapter 3`: ../PART1_SQL/03-expressions/expressions.html
.. _`第 3 章`: ../PART1_SQL/03-expressions/expressions.html

.. md-tab-set::

    .. md-tab-item:: 中文

        下面是对字符字符串操作的运算符和函数的部分列表，省略了一些不常实现的函数和不常用的可选参数。

        SQL 标准定义了几种运算符和函数，利用三种不同的模式匹配语言：一个用于运算符 **LIKE** （在 `第 3 章`_ 中讨论），以及两种不同的正则表达式（regex）语言；然而，本书考虑的数据库在这些运算符和函数方面大多不符合标准。许多实现提供类似效果的函数，但名称不同且使用不同的 regex 语言。因此，这些函数被省略，但建议您查阅您的数据库文档，以了解可用的选项。

        ================== ================================== ================================================== ===========================================
        operator/function  meaning                            usage                                              notes
        ================== ================================== ================================================== ===========================================
        \||                concatenation                      *s* || *t*                                         in MySQL, use CONCAT(*s*, *t*); in SQL Server, use *s* + *t*
        LIKE               pattern comparison                 *s* LIKE *pattern*                                 see :numref:`Chapter {number} <expressions-chapter>`
        NOT LIKE           inverse of LIKE                    *s* NOT LIKE *pattern*                             equivalent to NOT (*s* LIKE *pattern*)
        CHAR_LENGTH        length of string                   CHARACTER_LENGTH(*s*) or CHAR_LENGTH(*s*)          in SQLite and Oracle, use LENGTH(*s*); in SQL Server, use LEN(*s*)
        POSITION           index of substring                 POSITION(*t* IN *s*)                               in SQLite and Oracle, use INSTR(*s*, *t*)
        SUBSTRING          substring extraction               SUBSTRING(*s* FROM *start* [FOR *length*])         in SQLite and Oracle, use SUBSTR(*s*, *start*, *length*); in SQL Server, use SUBSTRING(*s*, *start*, *length*)
        UPPER              convert to uppercase               UPPER(*s*)
        LOWER              convert to lowercase               LOWER(*s*)
        TRIM               remove leading/trailing characters TRIM([[LEADING|TRAILING|BOTH] [*t*] FROM] *s*)     If *t* is omitted, whitespace is trimmed; BOTH is the default if LEADING etc. are omitted; in SQLite, Oracle, and SQL Server use LTRIM, RTRIM and TRIM (varying usage)
        OVERLAY            substring replacement              OVERLAY(*s* PLACING *t* FROM *start* FOR *length*) not in SQLite, Oracle, or SQL Server, but see REPLACE
        ================== ================================== ================================================== ===========================================

        大多数数据库实现提供额外的非标准函数和运算符。

        当运算符或函数的操作数或输入为 ``NULL`` 时，字符串运算符或函数表达式的结果为 ``NULL``。

    .. md-tab-item:: 英文

        Below is a partial listing of operators and functions acting on character strings, omitting some less frequently implemented functions and some less frequently used optional parameters.

        The SQL standard defines several operators and functions making use of three different pattern-matching languages: the one used by the operator **LIKE** (discussed in `Chapter 3`_), and two different regular expression (regex) languages; however the databases considered for this book mostly do not conform to the standard with respect to these operators and functions.  Many implementations provide functions with similar effect, but under different names and using different regex languages.  These functions are therefore omitted, but you are encouraged to read the documentation for your database to see what options are available to you.

        ================== ================================== ================================================== ===========================================
        operator/function  meaning                            usage                                              notes
        ================== ================================== ================================================== ===========================================
        \||                concatenation                      *s* || *t*                                         in MySQL, use CONCAT(*s*, *t*); in SQL Server, use *s* + *t*
        LIKE               pattern comparison                 *s* LIKE *pattern*                                 see :numref:`Chapter {number} <expressions-chapter>`
        NOT LIKE           inverse of LIKE                    *s* NOT LIKE *pattern*                             equivalent to NOT (*s* LIKE *pattern*)
        CHAR_LENGTH        length of string                   CHARACTER_LENGTH(*s*) or CHAR_LENGTH(*s*)          in SQLite and Oracle, use LENGTH(*s*); in SQL Server, use LEN(*s*)
        POSITION           index of substring                 POSITION(*t* IN *s*)                               in SQLite and Oracle, use INSTR(*s*, *t*)
        SUBSTRING          substring extraction               SUBSTRING(*s* FROM *start* [FOR *length*])         in SQLite and Oracle, use SUBSTR(*s*, *start*, *length*); in SQL Server, use SUBSTRING(*s*, *start*, *length*)
        UPPER              convert to uppercase               UPPER(*s*)
        LOWER              convert to lowercase               LOWER(*s*)
        TRIM               remove leading/trailing characters TRIM([[LEADING|TRAILING|BOTH] [*t*] FROM] *s*)     If *t* is omitted, whitespace is trimmed; BOTH is the default if LEADING etc. are omitted; in SQLite, Oracle, and SQL Server use LTRIM, RTRIM and TRIM (varying usage)
        OVERLAY            substring replacement              OVERLAY(*s* PLACING *t* FROM *start* FOR *length*) not in SQLite, Oracle, or SQL Server, but see REPLACE
        ================== ================================== ================================================== ===========================================

        Most database implementations provide additional non-standard functions and operators.

        String operator or function expressions where the operands or inputs are ``NULL`` result in ``NULL``.


.. _appendix-b-boolean-operators:
.. _Boolean operators:

布尔运算符
-----------------

**Boolean operators**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 中主要的布尔运算符是 **AND**、**OR** 和 **NOT**。在操作数严格为真值，即不为 ``NULL`` 的情况下，这些运算符的结果与其名称所表示的逻辑操作相符。即，``a AND b`` 当且仅当 ``a`` 和 ``b`` 均为 ``True`` 时，结果为 ``True``；``c OR d`` 当 ``c`` 或 ``d`` 任一为 ``True`` 时，结果为 ``True``；而 ``NOT e`` 则反转值 ``e``。

        然而，由于结果为布尔值的表达式也可能导致 NULL（例如，``4 > NULL``），因此 ``NULL`` 也是布尔运算符的有效操作数，我们可以认为 SQL 具有 3 值（而非真正的布尔）逻辑 [#]_。以下是 **AND**、**OR** 和 **NOT** 的真值表。将 ``NULL`` 视为布尔表达式中的“未知”，我们可以一般性地推断涉及 ``NULL`` 的布尔表达式的结果。例如，``True AND NULL`` 必须计算为 ``NULL``（表示未知），因为第二个操作数的真值未知。另一方面，``True OR NULL`` 必须计算为 ``True``，因为无论第二个操作数代表真值还是假值都无关紧要。

        ===== ===== =========== ==========
        *a*   *b*   *a* AND *b* *a* OR *b*
        ===== ===== =========== ==========
        True  True  True        True
        True  False False       True
        True  NULL  NULL        True
        False True  False       True
        False False False       False
        False NULL  False       NULL
        NULL  True  NULL        True
        NULL  False False       NULL
        NULL  NULL  NULL        NULL
        ===== ===== =========== ==========

        ===== =======
        *a*   NOT *a*
        ===== =======
        True  False
        False True
        NULL  NULL
        ===== =======

        SQL 标准定义了一些较少使用的布尔值一元运算符：**IS [NOT] TRUE**、**IS [NOT] FALSE** 和 **IS [NOT] UNKNOWN**，其中 **IS UNKNOWN** 等同于 **IS NULL**，但仅适用于布尔表达式的结果。因此，例如，SQL 允许我们写 ``NULL < 7 IS FALSE``，该表达式的结果为 ``False``。

        SQL Server 和 Oracle 不实现 **IS [NOT] TRUE**、**IS [NOT] FALSE** 和 **IS [NOT] UNKNOWN**。SQLite 不实现 **IS [NOT] UNKNOWN**。

        一些数据库实现提供额外的非标准运算符，例如 **XOR**、**&** 作为 **AND** 的替代等。

    .. md-tab-item:: 英文

        The principal Boolean operators in SQL are **AND**, **OR**, and **NOT**.  Given operands that are strictly truth valued, i.e., not ``NULL``, these operators result in the logic operations they are named for.  That is, ``a AND b`` evaluates to ``True`` if and only if ``a`` and ``b`` are both ``True``, ``c OR d`` evaluates to ``True`` if either ``c`` or ``d`` are ``True``, and ``NOT e`` inverts the value ``e``.

        However, since expressions resulting in Boolean values may also result in NULL (e.g., ``4 > NULL``), ``NULL`` is also a valid operand for the Boolean operators, and we can think of SQL as therefore having a 3-valued (rather than truly Boolean) logic [#]_.  The truth tables for **AND**, **OR**, and **NOT** are given below.  Treating ``NULL`` as meaning "unknown" in Boolean expressions, we can generally infer the result of a Boolean expression involving ``NULL``.  For example, ``True AND NULL`` must evaluate to ``NULL`` (meaning unknown), because the truth of the second operand is unknown.  On the other hand, ``True OR NULL`` must evaluate to ``True``, as it doesn't matter whether the second operand represents a true or a false value.

        ===== ===== =========== ==========
        *a*   *b*   *a* AND *b* *a* OR *b*
        ===== ===== =========== ==========
        True  True  True        True
        True  False False       True
        True  NULL  NULL        True
        False True  False       True
        False False False       False
        False NULL  False       NULL
        NULL  True  NULL        True
        NULL  False False       NULL
        NULL  NULL  NULL        NULL
        ===== ===== =========== ==========

        ===== =======
        *a*   NOT *a*
        ===== =======
        True  False
        False True
        NULL  NULL
        ===== =======

        The SQL standard defines some less frequently used unary operators on Boolean values:  **IS [NOT] TRUE**, **IS [NOT] FALSE**, and **IS [NOT] UNKNOWN**, with **IS UNKNOWN** equivalent to **IS NULL** except that it only applies to the result of a Boolean expression.  So for example, SQL allows us to write ``NULL < 7 IS FALSE``, which would evaluate to ``False``.

        SQL Server and Oracle do not implement **IS [NOT] TRUE**, **IS [NOT] FALSE**, and **IS [NOT] UNKNOWN**.  SQLite does not implement **IS [NOT] UNKNOWN**.

        Some database implementations provide additional non-standard operators, such as **XOR**, **&** as an alternative to **AND**, etc.


.. _appendix-b-datetime-operators:

日期和时间运算符和函数
-------------------------------------

**Date and time operators and functions**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 标准定义了与 **DATE**、**TIME**（带和不带时区）、**TIMESTAMP**（带和不带时区）以及 **INTERVAL** 数据类型相关的几种基本操作。（有关这些数据类型的描述，请参考上面的 `数据类型`_ 部分。）

        同类类型的比较使用之前记录的 `Comparison operators`_ 完成。例如，**DATE** 值可以与其他 **DATE** 值进行比较，但不能与 **TIME**、**TIMESTAMP** 或 **INTERVAL** 值进行比较。（不同数据库实现之间的行为差异很大——有些允许在 SQL 标准不允许的类型之间进行比较。然而，通常不建议比较不同类型，除非你确切知道比较是如何进行的。）

        此外，可以使用以下数学运算符 *+*、*-*、*\* 和 */*：

        ======== ========================= ======================== =====================
        operator left operand              right operand            result type
        ======== ========================= ======================== =====================
        \-       DATE, TIME, or TIMESTAMP  DATE, TIME, or TIMESTAMP INTERVAL
        \+ or \- DATE, TIME, or TIMESTAMP  INTERVAL                 DATE, TIME, or TIMESTAMP
        \+       INTERVAL                  DATE, TIME, or TIMESTAMP DATE, TIME, or TIMESTAMP
        \+ or \- INTERVAL                  INTERVAL                 INTERVAL
        \* or \/ INTERVAL                  number (INTEGER, etc.)   INTERVAL
        \*       number (INTEGER, etc.)    INTERVAL                 INTERVAL
        ======== ========================= ======================== =====================

        例如，从一个 **TIMESTAMP** 中减去另一个 **TIMESTAMP** 会得到一个表示天、小时、分钟和秒差的 **INTERVAL**。

        涉及日期和时间的其他运算符和函数：

        ===================== ============================================ ======================================
        operator or function  meaning                                      usage
        ===================== ============================================ ======================================
        CURRENT_DATE          evaluates to the current date                CURRENT_DATE
        CURRENT_TIME          evaluates to the current time                CURRENT_TIME
        CURRENT_TIMESTAMP     evaluates to the current date and time       CURRENT_TIMESTAMP
        EXTRACT               get a date or time field from a date or time EXTRACT(*field* FROM *date/time/interval*), where *field* is e.g., 'YEAR', 'HOUR', etc.
        OVERLAPS              test if one span of time overlaps another    *period1* OVERLAPS *period2*, where each *period* can be (*start date/time*, *end date/time*) or (*start date/time*, *interval*)
        ===================== ============================================ ======================================

        示例：

        ``EXTRACT('HOUR' FROM TIME '10:03:21')`` 结果为整数 ``10``。

        ``(DATE '2002-07-19', DATE '2003-01-31') OVERLAPS (DATE '2002-12-31', DATE '2005-05-05')`` 结果为 ``True``。

        在实际操作中，考虑到本书的数据库在实现 SQL 标准方面的差异很大，关于日期和时间类型及其操作的实现变异如此之多，以至于我们没有尝试在上述表中列出与标准的偏差。在大多数实现中，类似类型可以比较，日期和时间类型可以相减以产生间隔，间隔可以与日期和时间类型相加或相减以得到修改后的日期或时间。大多数数据库实现 **CURRENT_DATE**、**CURRENT_TIME** 和 **CURRENT_TIMESTAMP** 或类似功能。大多数实现提供一些函数，复制 **EXTRACT** 的某些功能。

    .. md-tab-item:: 英文

        The SQL standard defines several basic operations relating **DATE**, **TIME** (with and without timezone), **TIMESTAMP** (with and without timezone), and **INTERVAL** data types.  (For a description of these data types, consult the section on `Data types`_ above.)

        Comparison of like types is accomplished using the `Comparison operators`_ previously documented.  For example, **DATE** values can be compared with other **DATE** values, but not with **TIME**, **TIMESTAMP**, or **INTERVAL** values. (Behavior varies widely among the different database implementations - some do allow comparisons between types not allowed in the SQL standard.  However, it is generally inadvisable to compare different types, unless you know exactly how the comparison is being made.)

        In addition, the mathematical operators *+*, *-*, *\**, and */* may be used as follows:

        ======== ========================= ======================== =====================
        operator left operand              right operand            result type
        ======== ========================= ======================== =====================
        \-       DATE, TIME, or TIMESTAMP  DATE, TIME, or TIMESTAMP INTERVAL
        \+ or \- DATE, TIME, or TIMESTAMP  INTERVAL                 DATE, TIME, or TIMESTAMP
        \+       INTERVAL                  DATE, TIME, or TIMESTAMP DATE, TIME, or TIMESTAMP
        \+ or \- INTERVAL                  INTERVAL                 INTERVAL
        \* or \/ INTERVAL                  number (INTEGER, etc.)   INTERVAL
        \*       number (INTEGER, etc.)    INTERVAL                 INTERVAL
        ======== ========================= ======================== =====================

        So, for example, a subtraction of one **TIMESTAMP** from another yields an **INTERVAL** representing the difference in days, hours, minutes, and seconds.

        Other operators and functions involving dates and times:

        ===================== ============================================ ======================================
        operator or function  meaning                                      usage
        ===================== ============================================ ======================================
        CURRENT_DATE          evaluates to the current date                CURRENT_DATE
        CURRENT_TIME          evaluates to the current time                CURRENT_TIME
        CURRENT_TIMESTAMP     evaluates to the current date and time       CURRENT_TIMESTAMP
        EXTRACT               get a date or time field from a date or time EXTRACT(*field* FROM *date/time/interval*), where *field* is e.g., 'YEAR', 'HOUR', etc.
        OVERLAPS              test if one span of time overlaps another    *period1* OVERLAPS *period2*, where each *period* can be (*start date/time*, *end date/time*) or (*start date/time*, *interval*)
        ===================== ============================================ ======================================

        Examples:

        ``EXTRACT('HOUR' FROM TIME '10:03:21')`` results in the integer ``10``.

        ``(DATE '2002-07-19', DATE '2003-01-31') OVERLAPS (DATE '2002-12-31', DATE '2005-05-05')`` results in a ``True``.

        In actual practice, the databases considered for this book vary widely in their implementation of the SQL standard in regards to date and time types and operations on those types.  The variations are so great, we have not attempted to list departures from the standard in the above tables.  In most implementations, similar types can be compared, date and time types can be subtracted to yield intervals, and intervals can be added or subtracted to date and time types to yield a modified date or time.  Most databases implement **CURRENT_DATE**, **CURRENT_TIME**, and **CURRENT_TIMESTAMP**, or something similar.  Most implementations provide some function or functions replicating some of the functionality of **EXTRACT**.


其他运算符和函数
-------------------------------------

**Miscellaneous operators and functions**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节收集了一些不易归入上述类别的杂项 SQL 函数。

        ================== ====================================== ==================================================== ===========================================
        function           meaning                                usage                                                notes
        ================== ====================================== ==================================================== ===========================================
        NULLIF             ``NULL`` if *a* = *b*, else *a*        NULLIF(*a*, *b*)
        COALESCE           yield first non-``NULL`` argument      COALESCE(*a*, *b*, ...)
        CASE               general purpose conditional expression see :numref:`Chapter {number} <expressions-chapter>`
        CAST               explicit type conversion               CAST (*a* AS *type*)
        ================== ====================================== ==================================================== ===========================================

    .. md-tab-item:: 英文

        This section collects some miscellaneous SQL functions that do not fit neatly into the above categories.

        ================== ====================================== ==================================================== ===========================================
        function           meaning                                usage                                                notes
        ================== ====================================== ==================================================== ===========================================
        NULLIF             ``NULL`` if *a* = *b*, else *a*        NULLIF(*a*, *b*)
        COALESCE           yield first non-``NULL`` argument      COALESCE(*a*, *b*, ...)
        CASE               general purpose conditional expression see :numref:`Chapter {number} <expressions-chapter>`
        CAST               explicit type conversion               CAST (*a* AS *type*)
        ================== ====================================== ==================================================== ===========================================


.. _appendix-b-aggregate-functions:

聚合函数
:::::::::::::::::::

**Aggregate functions**

.. md-tab-set::

    .. md-tab-item:: 中文

        以下是一些 SQL 标准定义的更常用的聚合函数的参考。有关其使用的基本指南，请参见 :numref:`Chapter {number} <grouping-chapter>`。SQL 标准还定义了一些用于两个变量的统计函数；这些函数仅在 PostgreSQL 和 Oracle 中实现。大多数数据库实现提供了额外的非标准聚合函数。

        ================== ====================================== ==================================================== ===========================================
        function           meaning                                usage                                                notes
        ================== ====================================== ==================================================== ===========================================
        COUNT              count of rows or non-``NULL`` values   COUNT(\*) or COUNT([DISTINCT] *a*)
        AVG                average or mean                        AVG([DISTINCT] *a*)                                  *a* must be numeric
        MAX                maximum                                MAX([DISTINCT] *a*)
        MIN                minimum                                MIN([DISTINCT] *a*)
        SUM                sum                                    SUM([DISTINCT] *a*)                                  *a* must be numeric
        VAR_POP            population variance                    VAR_POP([DISTINCT] *a*)                              *a* must be numeric; not in SQLite; in SQL Server, use VARP(*a*)
        VAR_SAMP           sample variance                        VAR_SAMP([DISTINCT] *a*)                             *a* must be numeric; not in SQLite; in SQL Server, use VAR(*a*)
        STDDEV_POP         population standard deviation          STDDEV_POP([DISTINCT] *a*)                           *a* must be numeric; not in SQLite; in SQL Server, use STDEVP(*a*)
        STDDEV_SAMP        sample standard deviation              STDDEV_SAMP([DISTINCT] *a*)                          *a* must be numeric; not in SQLite; in SQL Server, use STDEV(*a*)
        LISTAGG            concatenate values into a string       LISTAGG(*a* [, *delim*])                             In SQLite and MySQL, use GROUP_CONCAT(*a*, *delim*); in PostgreSQL and SQL Server, use STRING_AGG(*a*, *delim*)
        ================== ====================================== ==================================================== ===========================================

        ================== ====================================== ==================================================== ===========================================
        function           meaning                                usage                                                notes
        ================== ====================================== ==================================================== ===========================================
        COUNT              计数行或非``NULL`` 值                   COUNT(\*) 或 COUNT([DISTINCT] *a*)
        AVG                平均值或算术平均数                    AVG([DISTINCT] *a*)                                  *a* 必须是数值类型
        MAX                最大值                                MAX([DISTINCT] *a*)
        MIN                最小值                                MIN([DISTINCT] *a*)
        SUM                总和                                   SUM([DISTINCT] *a*)                                  *a* 必须是数值类型
        VAR_POP            总体方差                             VAR_POP([DISTINCT] *a*)                              *a* 必须是数值类型；在 SQLite 中没有；在 SQL Server 中使用 VARP(*a*)
        VAR_SAMP           样本方差                             VAR_SAMP([DISTINCT] *a*)                             *a* 必须是数值类型；在 SQLite 中没有；在 SQL Server 中使用 VAR(*a*)
        STDDEV_POP         总体标准差                           STDDEV_POP([DISTINCT] *a*)                           *a* 必须是数值类型；在 SQLite 中没有；在 SQL Server 中使用 STDEVP(*a*)
        STDDEV_SAMP        样本标准差                           STDDEV_SAMP([DISTINCT] *a*)                          *a* 必须是数值类型；在 SQLite 中没有；在 SQL Server 中使用 STDEV(*a*)
        LISTAGG            将值连接成字符串                     LISTAGG(*a* [, *delim*])                             在 SQLite 和 MySQL 中使用 GROUP_CONCAT(*a*, *delim*)；在 PostgreSQL 和 SQL Server 中使用 STRING_AGG(*a*, *delim*)
        ================== ====================================== ==================================================== ===========================================

    .. md-tab-item:: 英文

        Below is a reference to some of the more commonly implemented aggregate functions defined by the SQL standard.  See :numref:`Chapter {number} <grouping-chapter>` for a basic guide to their use.  The SQL standard also defines a number of statistical functions on two variables; these are implemented in PostgreSQL and Oracle only.  Most database implementations provide additional non-standard aggregate functions.

        ================== ====================================== ==================================================== ===========================================
        function           meaning                                usage                                                notes
        ================== ====================================== ==================================================== ===========================================
        COUNT              count of rows or non-``NULL`` values   COUNT(\*) or COUNT([DISTINCT] *a*)
        AVG                average or mean                        AVG([DISTINCT] *a*)                                  *a* must be numeric
        MAX                maximum                                MAX([DISTINCT] *a*)
        MIN                minimum                                MIN([DISTINCT] *a*)
        SUM                sum                                    SUM([DISTINCT] *a*)                                  *a* must be numeric
        VAR_POP            population variance                    VAR_POP([DISTINCT] *a*)                              *a* must be numeric; not in SQLite; in SQL Server, use VARP(*a*)
        VAR_SAMP           sample variance                        VAR_SAMP([DISTINCT] *a*)                             *a* must be numeric; not in SQLite; in SQL Server, use VAR(*a*)
        STDDEV_POP         population standard deviation          STDDEV_POP([DISTINCT] *a*)                           *a* must be numeric; not in SQLite; in SQL Server, use STDEVP(*a*)
        STDDEV_SAMP        sample standard deviation              STDDEV_SAMP([DISTINCT] *a*)                          *a* must be numeric; not in SQLite; in SQL Server, use STDEV(*a*)
        LISTAGG            concatenate values into a string       LISTAGG(*a* [, *delim*])                             In SQLite and MySQL, use GROUP_CONCAT(*a*, *delim*); in PostgreSQL and SQL Server, use STRING_AGG(*a*, *delim*)
        ================== ====================================== ==================================================== ===========================================

----

**Notes**

.. [#] 从技术上讲，与 NULL 的比较结果是“未知”值。然而，在我们所知的所有数据库中，NULL 与“未知”不可区分，除非使用操作符 **IS [NOT] UNKNOWN**。

.. [#] Technically, a comparison with NULL results in the value "unknown".  However, in all databases that we are aware of, NULL is indistinguishable from "unknown" except when using the operator **IS [NOT] UNKNOWN**.

.. [#] 参见上面的注释。真值表在技术上应该在所有出现“NULL”的地方使用“未知”。

.. [#] See above note.  The truth table technically should use "unknown" everywhere "NULL" appears.


