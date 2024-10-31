.. _expressions-chapter:

===========
表达式
===========

**Expressions**

.. index:: expression

.. md-tab-set::

    .. md-tab-item:: 中文

        在 SQL 中，*表达式* 是可以被 *评估* 的事物——任何产生值的东西。一些例子包括文字值、运算符表达式和函数调用表达式。表达式在 SQL 查询的大多数子句中使用；例如，在 **SELECT** 子句中，表达式产生我们从查询中看到的返回值，而在 **WHERE** 子句中，表达式决定是否返回某一行。您还可以对表达式使用 **ORDER BY**，稍后我们将看到表达式的其他用法。本章将探讨一些最常见的表达式类型；在后面的章节中将介绍更多的表达式。

    .. md-tab-item:: 英文


        An *expression* in SQL is a thing that can be *evaluated* - anything that results in a value.  Some examples include literal values, operator expressions, and function call expressions.  Expressions are used in most clauses of a SQL query; for example, in the **SELECT** clause, expressions result in the values we see returned from the query, while in the **WHERE** clause, expressions determine whether or not a row is returned from the query.  You can also **ORDER BY** expressions, and later we will see other uses for expressions.  This chapter will explore some of the most common expression types; additional expressions will be introduced in later chapters.

本章中使用的表
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们将在本章中再次使用 **simple_books** 和 **simple_authors** 表。提醒:您可以在 :ref:`Appendix A <appendix-a>` 中阅读这些表的完整说明。

    .. md-tab-item:: 英文

        We will again be working with the **simple_books** and **simple_authors** tables for this chapter.  Reminder: you can read a full explanation of these tables in :ref:`Appendix A <appendix-a>`.


.. index:: column expression

列表达式
::::::::::::::::::

**Column expressions**

.. md-tab-set::

    .. md-tab-item:: 中文

        在 SQL 语句中使用列名会产生一个特殊的表达式，该表达式计算当前处理行中存储在该列中的值。因此，当我们运行

        .. activecode:: expressions_example_column
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT *
            FROM simple_books
            WHERE author = 'J.R.R. Tolkien';

        查询执行将逐行检查 **simple_books** 表，以评估表达式 ``author = 'J.R.R. Tolkien'``。这个表达式使用 **=** 运算符将 **author** 列的值与字面值 ``'J.R.R. Tolkien'`` 进行比较。如果两者相同，则整个表达式评估为 ``True``，该行将包含在输出中；否则，该行将被排除。

    .. md-tab-item:: 英文

        The use of a column name in a SQL statement produces a special expression which evaluates to the value stored in that column for the current row being processed.  So, when we run

        .. activecode:: expressions_example_column
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT *
            FROM simple_books
            WHERE author = 'J.R.R. Tolkien';

        the query execution examines each row of the table **simple_books** in turn to evaluate the expression ``author = 'J.R.R. Tolkien'``.  This expression compares the value of the **author** column to the literal value ``'J.R.R. Tolkien'`` using the **=** operator.  If the two are the same, the overall expression evaluates to ``True``, and the row is included in the output; otherwise, the row is excluded.


.. index:: literal; number, literal; character string, literal; Boolean

文字
::::::::

**Literals**

.. md-tab-set::

    .. md-tab-item:: 中文

        文字面量是以数据库可以识别和理解的形式表达的简单值。 SQL 中只有几种基本类型的文字面量，尽管这些可以在数据库中转换为许多不同的类型。我们将在 :numref:`Chapter {number} <table-creation-chapter>` 中进一步讨论 SQL 数据类型。您将遇到的主要文字面量包括:

        - 数字:这些以常规方式表示，例如 ``-1``、 ``3.14159``、 ``0.0008``。根据数据库的不同，您还可以使用科学记数法或其他格式的数字文字，例如 ``6.02e23`` (表示 :math:`6.02 \times 10^{23}`)。
        - 字符串:这些是用单引号括起来的字符字符串，例如 ``'apple'``。如果您需要表达包含单引号的文字字符串，只需将单引号写两次；这可能比较难以阅读，但会产生预期的结果。以下查询演示了这一点:

        .. activecode:: expressions_example_literal
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT author FROM simple_books
            WHERE title = 'The Handmaid''s Tale';

        - 布尔值: ``True`` 或 ``False``。 但请注意，并非所有 SQL 实现都支持布尔文字。
        - 日期和时间值。不同 SQL 实现对日期和时间的接受表示法差异很大。
        - 特殊值 ``NULL``。我们将在下面详细讨论 ``NULL``。

        您可以在 **SELECT** 子句中请求文字表达式——这在某些情况下是有用的。在这种情况下，文字在您查询的每一行中被评估为其自身。例如:

        .. code:: sql

            SELECT 42, 'hello', author FROM simple_books;

        如果您在上面的交互式工具中尝试此查询，请注意输出提供的列名基于所选的文字表达式。稍后我们将看到如何更改输出中列的名称，以使其更有意义。

    .. md-tab-item:: 英文

        Literals are simple values expressed in a form that the database recognizes and understands.  There are only a few basic types of literals in SQL, although these can be converted to many different types within a database.  We will discuss SQL data types further in :numref:`Chapter {number} <table-creation-chapter>`.  The main literals you will encounter are:

        - Numbers: these are expressed in the usual fashion, for example, ``-1``, ``3.14159``, ``0.0008``. Depending on the database, you may also be able to use numeric literals in scientific notation or other formats, for instance, ``6.02e23`` (which stands for :math:`6.02 \times 10^{23}`).
        - Character strings: these are strings of characters enclosed in single quotes, for example, ``'apple'``.  If you need to express a literal character string which contains a single quote, you simply write the single quote twice; this is tricky to read, but produces the desired result.  This is shown in the following query:

        .. activecode:: expressions_example_literal
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT author FROM simple_books
            WHERE title = 'The Handmaid''s Tale';

        - Boolean values: ``True`` or ``False``.  Note, however, that not all SQL implementations support Boolean literals.
        - Date and time values. The accepted notations for dates and times vary widely among different SQL implementations.
        - The special value ``NULL``. We will talk more about ``NULL`` below.

        You can ask for literal expressions in the **SELECT** clause - this is sometimes useful.  In this case, the literal is evaluated as itself for each row in the table you are querying.  For example:

        .. code:: sql

            SELECT 42, 'hello', author FROM simple_books;

        If you try this query in the interactive tool above, note that the output provides column names based on the literal expressions selected.  Later we will see how to change the names of columns in the output if we want to make them more meaningful.


运算符和函数
:::::::::::::::::::::::

**Operators and functions**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 定义了一些对其各种类型有用的操作。这些操作有些使用简单的运算符，类似于数学表达式，而其他则呈现为函数。:ref:`Appendix B <appendix-b>` 提供了 SQL 标准定义的运算符和函数的详细列表，但我们将在此讨论一些最常用的运算符和函数，以及它们的使用示例。

    .. md-tab-item:: 英文

        SQL defines a number of useful operations on its various types.  Some of these use simple operators, as in mathematical expressions, while others take the form of functions.  :ref:`Appendix B <appendix-b>` provides extensive lists of the operators and functions defined by the SQL standard, but we will discuss some of the most commonly used ones here, along with examples of their use.


.. index:: operator; comparison

比较运算符
--------------------

**Comparison operators**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们已经在查询的 **WHERE** 子句中看到使用等于运算符 (**=**) 来测试某列是否等于一个字面值。我们可以使用不等于运算符 (**<>**) 来测试不等式:

        .. activecode:: expressions_example_comparison
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books WHERE genre <> 'fantasy';

        尽管这并不是标准用法，但大多数数据库也识别 **!=** 作为不等式运算符。(请注意，SQL 不使用 **==**，这是许多编程语言中用于测试相等的运算符。虽然 SQLite 将其识别为相等比较运算符，但 **请不要使用它**，因为这会成为一个难以改掉的习惯。)

        我们还可以测试一个值是否小于 (**<**)、大于 (**>**)、小于或等于 (**<=**) 或大于或等于 (**>=**) 其他某个值。还有一个三元运算符 **BETWEEN**，用于测试一个值是否在两个其他值之间(详情见附录 B - :ref:`appendix-b-comparison-operators`)。

    .. md-tab-item:: 英文

        We've already seen the equality operator (**=**) used to test if some column is equal to a literal value in the **WHERE** clause of queries.  We could instead test for inequality using the (**<>**) operator:

        .. activecode:: expressions_example_comparison
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books WHERE genre <> 'fantasy';

        Though it is non-standard, most databases also recognize **!=** as an inequality operator.  (Note that SQL does not use **==**, which is used to test for equality in many programming languages.  While SQLite does recognize it as an equality comparison operator, **do not use it**, as it will be a difficult habit to break.)

        We can also test to see if a value is less than (**\<**), greater than (**\>**), less than or equal to (**\<=**), or greater than or equal to (**\>=**) some other value.  There is also a ternary operator, **BETWEEN**, that tests if a value is between two other values (see Appendix B - :ref:`appendix-b-comparison-operators` for details).


.. index:: operator; mathematics, function; mathematics

数学运算符
-----------

**Mathematics**

.. md-tab-set::

    .. md-tab-item:: 中文

        你可以期待基本的算术运算符能够处理任何数字值:加法 (**+**)、减法 (**-**)、乘法 (**\***) 和除法 (**/**) 是标准的。你的数据库可能实现了其他运算符，但确保你阅读了数据库的文档，以确认其他运算符的功能符合你的预期。你实际上可以将数据库用作简单的计算器！尝试运行以下查询:

        .. activecode:: expressions_example_math
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT 4 + 7;
            SELECT 302.78 * 14;

        (对于 Oracle 用户:Oracle 要求所有 **SELECT** 查询都必须有 **FROM** 子句，因此提供了一个特殊的表 **dual**，用于不使用列并返回一行的查询。因此，在 Oracle 中使用 ``SELECT 4 + 7 FROM dual;``。)

        SQL 标准还提供了许多有用的数学运算函数，例如对数 (**log**, **ln**, **log10**)、指数 (**exp**)、平方根 (**sqrt**)、模 (**mod**)、向下取整和向上取整 (**floor**, **ceiling** 或 **ceil**)、三角函数 (**sin**, **cos** 等) 等。以下是一些示例:

        .. code:: sql

            SELECT sqrt(3);
            SELECT log10(1e5);
            SELECT cos(0);

        如果你正在处理财务或科学记录等数字数据，你很可能会在 SQL 中使用数学运算符。在 :numref:`Chapter {number} <table-creation-chapter>` 中，我们将讨论用于存储数字的不同数据类型:整数、十进制数和浮点值。每种类型在不同问题中都有应用。

        作为一个有些牵强的示例，考虑找出一本书出版的世纪。在英语中，第一个世纪传统上被认为是编号为 1 到 100 的年份。每过 100 年，世纪数加 1，因此第 20 世纪包括 1901 到 2000 年。

        通过简单的数学，我们可以提取出数据库中每本书出版的世纪:

        .. code:: sql

            SELECT
            title,
            floor((publication_year + 99) / 100) AS century
            FROM simple_books;

        注意使用括号来强制操作顺序:加法运算在除法之前执行，然后除法的结果提供给 **floor()** 函数。我们还引入了一个新概念——重命名操作，以便给结果列一个更具信息性的名称。**AS** 关键字让我们能够在查询的输出中重命名列。我们将在 :numref:`Chapter {number} <joins-chapter>` 中学习更多关于使用 **AS** 的内容。

        有关标准运算符和函数的完整列表，请参见附录 B - :ref:`appendix-b-math-operators`。

    .. md-tab-item:: 英文

        You can expect the basic arithmetic operators to work with any numeric values: addition (**+**), subtraction (**-**), multiplication (**\***), and division (**/**) are standard.  Your database may implement others, but make sure you read the documentation for your database to ensure other operators do what you think they do.  You can actually use your database as a simple calculator!  Try running these:

        .. activecode:: expressions_example_math
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT 4 + 7;
            SELECT 302.78 * 14;

        (Note for Oracle users: Oracle requires all **SELECT** queries to have a **FROM** clause, so the special table **dual** is provided for queries that use no columns and return one row.  Thus, use ``SELECT 4 + 7 FROM dual;`` in Oracle.)

        The SQL standard additionally provides functions for many useful mathematical operations, such as logarithms (**log**, **ln**, **log10**), exponentials (**exp**), square root (**sqrt**), modulus (**mod**), floor and ceiling (**floor**, **ceiling** or **ceil**), trigonometric functions (**sin**, **cos**, etc.), and more.  Some examples:

        .. code:: sql

            SELECT sqrt(3);
            SELECT log10(1e5);
            SELECT cos(0);

        You will most likely find yourself using mathematical operators in SQL if you are working with numerical data such as financial or scientific records.  In :numref:`Chapter {number} <table-creation-chapter>` we will discuss some of the different data types available for storing numbers: integers, decimal numbers, and floating point values.  Each has applications to various problems.

        As a somewhat contrived example of applying mathematical operators to an actual table, consider the problem of finding out which century a book was published in.  In the English language, the 1st century is traditionally considered to be the years numbered 1 - 100.  Each subsequent 100 years adds 1 to the century, so the 20th century included the years 1901 - 2000.

        With a little math, we can extract the century in which each book in our database was published:

        .. code:: sql

            SELECT
            title,
            floor((publication_year + 99) / 100) AS century
            FROM simple_books;

        Note the use of parentheses to enforce an order of operations: the addition operation occurs before the division, and then the result of the division is provided to the **floor()** function.  We have also introduced something new - a renaming operation to give our result column a more informative name. The **AS** keyword lets us rename a column in the output of our query.  We will learn more about using **AS** in :numref:`Chapter {number} <joins-chapter>`.

        See Appendix B - :ref:`appendix-b-math-operators` for a complete list of standard operators and functions.


.. index:: operator; character string, function; character string, string concatenation, LIKE, pattern matching

字符串运算符和函数
----------------------------------------

**Character string operators and functions**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 提供了两个非常有用的字符串运算符。运算符 **||**(两个竖线)用于字符串连接。我们在许多情况下希望将一个字符串附加到另一个字符串上。例如，如果我们不喜欢 **simple_books** 表的多列输出，可以使用字符串连接生成更熟悉的数据表示:

        .. activecode:: expressions_example_string
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT title || ', by ' || author FROM simple_books;

        (关于实现的说明:在 SQL Server 中，你需要使用 **+** 而不是 **||**；在 MySQL 中，你需要使用 MySQL 的 **concat** 函数，例如 ``SELECT concat(title, ', by ', author) FROM simple_books;``。)

        **LIKE** 运算符是一个布尔运算符，几乎专门用于 **WHERE** 子句。**LIKE** 提供了非常简单的模式匹配功能。一个 *模式* 只是一个字符串，可以包含常规文本和特殊的 *通配符* 字符，这些字符可以匹配一个或多个未指定的字符。两个通配符是 **%**，可以匹配任意长度的字符串(包括零个字符)，和 **_**，可以匹配任意单个字符。常规文本则完全匹配自身。(如果你熟悉标准的 *正则表达式* 语法，**%** 通配符对应于正则表达式中的 ".*"，而 **_** 通配符对应于 "."。)

        考虑这样一种情况:我们记得一个作者的名字，但不记得全名，希望查找具有该名字的作者。**%** 通配符可以用于表示未知的名字部分:

        .. code:: sql

            SELECT name FROM simple_authors WHERE name LIKE 'Isabel %';

        由于 **%** 可以匹配任意字符串，模式 ``'Isabel %'`` 可以匹配 "Isabel Allende"、"Isabel Granada" 或 "Isabel del Puerto"(虽然这些中只有一个在我们的 **simple_authors** 表中)。

        同样，如果我们记得名字的最后部分，但不记得开始部分，我们可以再次使用 **%** 通配符:

        .. code:: sql

            SELECT name FROM simple_authors WHERE name LIKE '% Ginsberg';

        我们甚至可以多次使用通配符:

        .. code:: sql

            SELECT title FROM simple_books WHERE title LIKE '%Earth%';

        现在，假设我们对使用首字母而不是全名的作者感兴趣。首字母看起来像某个单个字符后跟一个句点——这两个都是必需的。以下是使用 **%** 和 **_** 通配符的查询示例:

        .. code:: sql

            SELECT name FROM simple_authors WHERE name LIKE '_.%';

        除了这些运算符外，SQL 还提供了一些对字符字符串操作的有用函数。函数 **upper** 和 **lower** 分别将字符串转换为全大写或全小写字符。当然，并不是所有语言都区分大写和小写，因此这些函数在某些地区可能不适用。你可以在想要返回全大写或全小写字符串时使用 **upper** 或 **lower**:

        .. code:: sql

            SELECT upper(title), author FROM simple_books;

        如果你不确定数据库中字符串的大小写，也可以在模式匹配时使用它们:

        .. code:: sql

            SELECT * FROM simple_books WHERE lower(title) LIKE '%love%';

        SQL 还提供了用于子字符串提取或替换、查找子字符串位置、修剪字符串前后空格(或其他字符)等任务的函数，还有更多功能。请参见附录 B - :ref:`appendix-b-string-operators` 以获取更多信息。

    .. md-tab-item:: 英文

        SQL provides two very useful string operators. The operator **||** (two vertical bars) is used for string concatenation.  There are many instances in which we want to append one string to another.  For example, if we do not like the multi-column output from our **simple_books** table, we could use string concatenation to produce a more familiar representation of the data:

        .. activecode:: expressions_example_string
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT title || ', by ' || author FROM simple_books;

        (Note about implementations: in SQL Server, you will need to use **+** instead of **||**; in MySQL, you will need to use the MySQL **concat** function, e.g. ``SELECT concat(title, ', by ', author) FROM simple_books;``.)

        The **LIKE** operator is a Boolean operator that is used almost exclusively in the **WHERE** clause.  **LIKE** provides very simple pattern matching capabilities in SQL.  A *pattern* is just a string that can contain regular text and special *wildcard* characters, which can match one or many unspecified characters.  The two wildcards are **%**, which can match any string of zero or more characters, and **_**, which can match exactly one of any character. Normal text matches itself exactly.  (If you are familiar with standard *regular expression* syntax, the **%** wildcard corresponds to ".*" as used in a regular expression, and the **_** wildcard corresponds to ".".)

        Consider the case in which we recall the first name of an author, but not the full name, and wish to look up authors with that first name.  The **%** wildcard can be used here to stand in for the unknown part of the name:

        .. code:: sql

            SELECT name FROM simple_authors WHERE name LIKE 'Isabel %';

        Since the **%** can match any string, the pattern ``'Isabel %'`` would match "Isabel Allende", "Isabel Granada", or "Isabel del Puerto" for example (only one of these is in our **simple_authors** table, though).

        Similarly, if we remember the last part of the name, but not the start, we can use the **%** wildcard again:

        .. code:: sql

            SELECT name FROM simple_authors WHERE name LIKE '% Ginsberg';

        We can even use the wildcard more than once:

        .. code:: sql

            SELECT title FROM simple_books WHERE title LIKE '%Earth%';

        Now, suppose we are interested in authors who use an initial instead of their full first name.  An initial looks like some single character followed by a period - both are required.  Here's what the query would look like, using both the **%** and **_** wildcards:

        .. code:: sql

            SELECT name FROM simple_authors WHERE name LIKE '_.%';

        In addition to these operators, SQL provides a number of useful functions that act on character strings.  The functions **upper** and **lower** convert strings to all uppercase or lowercase characters, respectively.  Not all languages distinguish between uppercase and lowercase, of course, so these functions may not be applicable in certain locales.  You can use **upper** or **lower** whenever you want to get back strings in all uppercase or lowercase:

        .. code:: sql

            SELECT upper(title), author FROM simple_books;

        You can also use them when pattern matching if you aren't sure of the capitalization of the strings in your database:

        .. code:: sql

            SELECT * FROM simple_books WHERE lower(title) LIKE '%love%';

        SQL also provides functions for tasks such as substring extraction or replacement, finding the location of a substring, trimming whitespace (or other characters) from the front and/or back of a string, and many more.  See Appendix B - :ref:`appendix-b-string-operators` for these.


.. index:: operator; Boolean, AND, OR, NOT

布尔运算符
-----------------

**Boolean operators**

.. md-tab-set::

    .. md-tab-item:: 中文

        如 :numref:`Chapter {number} <data-retrieval-chapter>` 中讨论的，**SELECT** 查询的 **WHERE** 子句在 **WHERE** 关键字后期望一个布尔表达式。SQL 中的一些布尔表达式包括使用比较运算符的表达式，或使用 **LIKE** 运算符的表达式。许多函数也会返回布尔值。

        SQL 提供了操作布尔值的逻辑运算符。这些运算符是 **AND**、**OR** 和 **NOT**，它们执行其名称所暗示的逻辑操作。例如，如果我们有一个形式为 ``expr1 AND expr2`` 的表达式，当且仅当 ``expr1`` 和 ``expr2`` 都评估为 ``True`` 时，结果才为 ``True``。类似地，``expr1 OR expr2`` 在 ``expr1`` 和 ``expr2`` 中至少有一个为 ``True`` 时评估为 ``True``。最后，``NOT`` 会反转真值:``NOT True`` 结果为 ``False``，而 ``NOT False`` 结果为 ``True``。

        这些逻辑运算符允许我们从更简单的布尔表达式构建复杂的布尔表达式，以表达我们希望在 **WHERE** 子句中使用的特定逻辑条件。例如，我们可能对自 2000 年以来出版的奇幻书籍感兴趣:

        .. activecode:: expressions_example_boolean
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT *
            FROM simple_books
            WHERE genre = 'fantasy' AND publication_year > 2000;

        或者，我们可能对奇幻或科幻类书籍感兴趣:

        .. code:: sql

            SELECT * FROM simple_books
            WHERE genre = 'fantasy' OR genre = 'science fiction';

        如果我们简单地讨厌科幻，我们可以写:

        .. code:: sql

            SELECT * FROM simple_books WHERE NOT genre = 'science fiction';

        这与以下查询结果相同:

        .. code:: sql

            SELECT * FROM simple_books WHERE genre <> 'science fiction';

        对于涉及 **AND**、**OR** 和 **NOT** 组合的更复杂表达式，我们可能需要使用括号来使我们的意思更清晰。在 SQL 中，**NOT** 在 **AND** 之前应用，**AND** 在 **OR** 之前应用。例如，或许我们对 2000 年后出版的除奇幻书籍以外的任何书籍感兴趣。我们可能会想写:

        .. code:: sql

            SELECT * FROM simple_books
            WHERE NOT genre = 'fantasy' AND publication_year > 2000;

        然而，这并不完全正确(试试吧！)。由于 **NOT** 首先应用，这个查询返回的书籍 a) 不是奇幻书籍且 b) 自 2000 年以来出版。表达式 ``NOT genre = 'fantasy' AND publication_year > 2000`` 相当于 ``(NOT genre = 'fantasy') AND (publication_year > 2000)``。要获得我们最初想要的结果，我们需要明确使用括号:

        .. code:: sql

            SELECT * FROM simple_books
            WHERE NOT (genre = 'fantasy' AND publication_year > 2000);

        你可以看到，上述查询只排除了书籍列表中的书籍:

        .. code:: sql

            SELECT * FROM simple_books
            WHERE genre = 'fantasy' AND publication_year > 2000;

        同样，我们可能对科幻或奇幻书籍感兴趣，但只有在它们是 2000 年后出版的情况下。比较以下两个查询:

        .. code:: sql

            SELECT *
            FROM simple_books
            WHERE genre = 'science fiction' OR genre = 'fantasy'
            AND publication_year > 2000;

            SELECT *
            FROM simple_books
            WHERE
                (genre = 'science fiction' OR genre = 'fantasy')
                AND publication_year > 2000;

        第一个查询返回 *任何* 科幻书籍，以及 2000 年后出版的奇幻书籍。第二个查询返回期望的结果: 2000 年后出版的奇幻或科幻类书籍。

        要更全面地讨论布尔运算符，我们需要了解更多关于 ``NULL`` 值的信息，这将在下面讨论。有关 SQL 布尔运算符的完整文档，请参见附录 B - :ref:`appendix-b-boolean-operators`。

    .. md-tab-item:: 英文

        As discussed in :numref:`Chapter {number} <data-retrieval-chapter>`, the **WHERE** clause of a **SELECT** query expects a Boolean expression after the **WHERE** keyword.  Some expressions that are Boolean in SQL include expressions using comparison operators, or an expression using the **LIKE** operator.  Many functions also result in a Boolean value.

        SQL provides logical operators that operate on Boolean values.  These operators are **AND**, **OR**, and **NOT**, which perform the logical operations that their names imply.  For example, if we have an expression of the form ``expr1 AND expr2``, the result is ``True`` if and only if both ``expr1`` and ``expr2`` evaluate to ``True``.  Similarly, ``expr1 OR expr2`` evaluates to ``True`` if at least one of ``expr1`` and ``expr2`` are ``True``.  Finally, ``NOT`` inverts the truth value:  ``NOT True`` results in ``False``, and ``NOT False`` results in ``True``.

        These logical operators allow us to build up complex Boolean expressions from simpler Boolean expressions to express the particular logical conditions we want for our **WHERE** clause.  So, for example, we might be interested in fantasy books published since the year 2000:

        .. activecode:: expressions_example_boolean
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT *
            FROM simple_books
            WHERE genre = 'fantasy' AND publication_year > 2000;

        Or, we might be interested in books in either the fantasy or science fiction genres:

        .. code:: sql

            SELECT * FROM simple_books
            WHERE genre = 'fantasy' OR genre = 'science fiction';

        If we simply hate science fiction, we might write

        .. code:: sql

            SELECT * FROM simple_books WHERE NOT genre = 'science fiction';

        which gives the same result as

        .. code:: sql

            SELECT * FROM simple_books WHERE genre <> 'science fiction';

        For more complex expressions involving combinations of **AND**, **OR**, and **NOT**, we may need to use parentheses to make our meaning clear.  In SQL, **NOT** is applied before **AND**, and **AND** is applied before **OR**. For example, perhaps we are interested in any books other than fantasy books published after the year 2000.  We might be tempted to write

        .. code:: sql

            SELECT * FROM simple_books
            WHERE NOT genre = 'fantasy' AND publication_year > 2000;

        However, this isn't quite right (try it!).  Since the **NOT** is applied first, this query returns books that a) are not fantasy and b) were published since the year 2000.  The expression ``NOT genre = 'fantasy' AND publication_year > 2000`` is equivalent to ``(NOT genre = 'fantasy') AND (publication_year > 2000)``.  To get what we originally wanted, we need to use parentheses explicitly:

        .. code:: sql

            SELECT * FROM simple_books
            WHERE NOT (genre = 'fantasy' AND publication_year > 2000);

        You can see that the above query only excludes books in the list:

        .. code:: sql

            SELECT * FROM simple_books
            WHERE genre = 'fantasy' AND publication_year > 2000;

        Similarly, we might be interested in either science fiction or fantasy books, but only if they were published after 2000.  Compare the two queries below:

        .. code:: sql

            SELECT *
            FROM simple_books
            WHERE genre = 'science fiction' OR genre = 'fantasy'
            AND publication_year > 2000;

            SELECT *
            FROM simple_books
            WHERE
                (genre = 'science fiction' OR genre = 'fantasy')
                AND publication_year > 2000;

        The first of these queries returns *any* science fiction books, along with fantasy books published after 2000.  The second returns the desired result: books published after 2000 in either the fantasy or science fiction genres.

        For a fuller discussion of Boolean operators, we need to know more about ``NULL`` values, which will be discussed below.  See Appendix B - :ref:`appendix-b-boolean-operators` for complete documentation on the SQL Boolean operators.


.. index:: operator; date and time, function; date and time, CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP

日期和时间运算符和函数
-------------------------------------

**Date and time operators and functions**

.. md-tab-set::

    .. md-tab-item:: 中文

        日期和时间数据在许多数据库应用中极为重要，例如支持政府或金融机构的应用。SQL 提供了广泛的功能来管理日期和时间。不幸的是，这是一个不同 SQL 实现之间在遵循 SQL 标准方面差异很大的领域。有关更全面的讨论，请参见附录 B - :ref:`appendix-b-datetime-operators`，并查阅您的数据库实现文档以了解其在日期和时间处理方面提供的功能。

        大多数数据库实现的一个有用 SQL 函数是 **CURRENT_DATE** 函数(还可以尝试 **CURRENT_TIME** 和 **CURRENT_TIMESTAMP**):

        .. activecode:: expressions_example_datetime
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT CURRENT_DATE;

        我们将在 :numref:`Chapter {number} <table-creation-chapter>` 中看到如何使用此函数在新创建的行中自动记录日期。

    .. md-tab-item:: 英文

        Date and time data are extremely important in many database applications, such as those supporting governmental or financial institutions.  SQL provides extensive functionality for managing dates and times.  Unfortunately, this is an area where different SQL implementations vary widely in their conformance to the SQL standard. See Appendix B - :ref:`appendix-b-datetime-operators` for a fuller discussion, and consult your database implementation's documentation to see what capabilities it offers with respect to date and time handling.

        One useful SQL function that most databases implement is the **CURRENT_DATE** function (also try **CURRENT_TIME** and **CURRENT_TIMESTAMP**):

        .. activecode:: expressions_example_datetime
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT CURRENT_DATE;

        We will see in :numref:`Chapter {number} <table-creation-chapter>` how this function can be used to automatically record the date in a newly created row.


.. index:: NULL - SQL, three value logic - SQL

NULL
::::

.. md-tab-set::

    .. md-tab-item:: 中文

        在许多数据库应用中，有时需要记录某个数据方面的 *缺失信息*。例如，在查询我们的 **authors** 表时，可以看到 **death** 列中的一些条目是空白的。这可能意味着该行的作者在数据输入时尚未去世，因此该列对该作者不适用；即没有死亡日期。此外，一些 **birth** 日期是空白的；在这种情况下，该列显然适用于作者——他们显然在某个时候出生！然而，输入数据的人并不知道这一信息，因此没有任何内容被输入。

        这些 *不适用* 或 *未知* 的数据条目概念在 SQL 中通过一个特殊值来表示: ``NULL``。 [#]_ ``NULL`` 值表示信息的缺失。当我们查询 **authors** 表时，结果中的空白并不表示数据库中存在空字符串。相反，``NULL`` 值代表缺失的信息。不幸的是，``NULL`` 并没有告诉我们数据缺失的 *原因*——是因为不适用还是仅仅未知。如果这个区分对您的数据库很重要，您需要使用额外的列来指示 ``NULL`` 的含义，或者使用其他非 ``NULL`` 的值。

        因为 ``NULL`` 确实是信息的缺失，表达式中使用的 ``NULL`` 值通常在评估时会导致结果为 ``NULL``。例如，``2 + NULL`` 的结果是什么？我们根本无法知道——``NULL`` 没有告诉我们任何信息，因此结果是未知的，即 ``NULL``。

        这种行为的一个非常重要的结果是，``NULL`` 值无法与任何东西进行有用的比较，即使是其他 ``NULL`` 值！也就是说，像 ``x = NULL`` 这样的表达式永远不会为 ``True``，即使 *x* 本身包含 ``NULL``。这可能看起来不符合直觉，但如果您把表达式 ``NULL = NULL`` 理解为在问“这个未知的东西和另一个未知的东西是否相同？”，您就会明白答案应该是“未知”，即 ``NULL``。 [#]_

        要检查一个值是否为 ``NULL`` 或非 ``NULL``，需要使用特殊运算符:**IS NULL** 和 **IS NOT NULL**。例如，如果我们想找出没有死亡日期的作者，我们可以执行以下查询:

        .. activecode:: expressions_example_null
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_authors WHERE death IS NULL;

        您可以通过在上述查询中将 **IS NULL** 替换为 **IS NOT NULL** 来查找我们确实有死亡日期的作者。

        如果我们改为写以下查询，会发生什么呢？

        .. code:: sql

            SELECT * FROM simple_authors WHERE death = NULL;

        在这种情况下，表达式 ``death = NULL`` 将在表中的每一行评估为 ``NULL``。**WHERE** 子句将过滤这些结果，因为它只接受评估为 ``True`` 的表达式，而 ``NULL`` 并不等同于 ``True``。

        ``NULL`` 值有时可能会使我们迷失方向。考虑寻找所有在 2000 年或之后仍然健在的作者的问题。可能会很想写一个查询，例如:

        .. code:: sql

            SELECT * FROM simple_authors
            WHERE birth <= '2000-12-31'
            AND death >= '2000-01-01';

        这是一个完全有效的查询——以这种标准格式表示的日期可以在我们的数据库中进行比较。然而，如果您运行这个查询，您会发现并不是所有在世的作者都包含在结果中。这再次发生，是因为那些行中的 **death** 列包含了 ``NULL`` 值:将这些与 ``'2000-01-01'`` 进行比较也会得到 ``NULL``，因此 **WHERE** 子句将它们过滤掉。

        在这种情况下，我们需要使用更多的逻辑，查询数据库如下:

        .. code:: sql

            SELECT * FROM simple_authors
            WHERE birth <= '2000-12-31' AND
                (death >= '2000-01-01' OR death IS NULL);

        这个查询是正确的，但您可能想知道为什么。我们说过在表达式中使用的 ``NULL`` 通常会导致结果为 ``NULL``，但这里我们有一个使用 **AND** 和 **OR** 运算符的复合布尔表达式。那么，为什么我们不会再次失去所有在世的作者呢？实际上，布尔运算符是一个例外。这是因为，当在布尔表达式中使用时，``NULL`` 意味着我们根本无法知道该值是 ``True`` 还是 ``False``；该值是未知的。然而，**OR** 表达式只要求一个操作数评估为 ``True``，就会返回 ``True``:在布尔逻辑中，``True OR True`` 为 ``True``，``True OR False`` 也是 ``True``。无论哪种方式，我们得到的都是 ``True``，因此不知道它可能是什么并不重要。因此，括号中的表达式在其中任何一个条件为真时都是 ``True``。

        另一方面，``False OR NULL`` 会返回 ``NULL``。在这种情况下，``NULL`` 代表 ``True`` 还是 ``False`` 实际上很重要，因为两者会导致不同的结果。由于我们不知道结果，因此返回 ``NULL``。

        因为布尔表达式可以结果为 ``True``、``False`` 或 ``NULL``，我们称 SQL 为 *三值逻辑*(而非真正的布尔逻辑)。附录 B - :ref:`appendix-b-boolean-operators` 提供了这种三值逻辑的真值表，但正如上面所示，您通常可以通过简单地将 ``NULL`` 理解为“未知”来推导出答案。

    .. md-tab-item:: 英文

        In many database applications, it is sometimes necessary to record the *absence of information* on some aspect of a piece of data.  For example, in querying our **authors** table, we can see that some entries in the **death** column are blank.  This probably means that the author for that row had not yet died at the time the data was entered, and thus the column was simply not applicable for that author; there is no death date.  Additionally, some **birth** dates are blank; in this case, the column certainly applies to the author - they were clearly born at some point!  However, that information was unknown to the person entering the data into the table, so nothing was entered.

        These notions of data entries that are *not applicable* or *unknown* are captured with a special value in SQL:  ``NULL``. [#]_ ``NULL`` values represent the absence of information.  When we query the **authors** table, the blanks in our result do not indicate that empty strings are in the database.  Instead, ``NULL`` values stand in for the missing information.  Unfortunately, ``NULL`` does not tell us the *reason* the data is missing - whether it is not applicable or simply unknown.  If this distinction is important for your database, you will need to use extra columns to indicate the meaning of the ``NULL``, or use some value other than ``NULL``.

        Because ``NULL`` is truly an absence of information, ``NULL`` values used in expressions usually result in ``NULL`` when the expression is evaluated.  For example, what is the result of ``2 + NULL``?  We simply cannot know - the ``NULL`` is not telling us anything, so the result is unknown, or ``NULL``.

        A very important consequence of this behavior is that ``NULL`` values cannot be usefully compared with anything, even other ``NULL`` values!  That is, an expression like ``x = NULL`` is never ``True`` even if *x* itself contains ``NULL``.  This might seem counterintuitive, but if you think of the expression ``NULL = NULL`` as asking the question, "Is this unknown thing the same as this other unknown thing?", you can see that the answer should be "unknown", or ``NULL``. [#]_

        To find out if a value is ``NULL`` or not ``NULL`` requires special operators: **IS NULL** and **IS NOT NULL**.  For example, if we want to discover authors for whom we have no death date, we would execute the query:

        .. activecode:: expressions_example_null
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_authors WHERE death IS NULL;

        You can discover authors for whom we do have death dates by replacing **IS NULL** with **IS NOT NULL** in the above query.

        What happens if we instead write the following query?

        .. code:: sql

            SELECT * FROM simple_authors WHERE death = NULL;

        In this case, the expression ``death = NULL`` will evaluate to ``NULL`` for every row in the table.  The **WHERE** clause will filter these out, because it only accepts expressions that evaluate to ``True``, and ``NULL`` is not the same as ``True``.

        ``NULL`` values can sometimes lead us astray.  Consider the question of finding all authors who were alive in the year 2000 or later.  It might be tempting to write a query such as

        .. code:: sql

            SELECT * FROM simple_authors
            WHERE birth <= '2000-12-31'
            AND death >= '2000-01-01';

        This is a perfectly valid query - dates in this standard format can be compared in this fashion in our database.  However, if you run the query, you will see that not all of our living authors are in the result.  This happened, again, because the **death** column in those rows contained ``NULL`` values: comparing these to ``'2000-01-01'`` also yielded ``NULL``, and the **WHERE** clause therefore filtered them out.

        In this case, we need to use more logic, and query the database thus:

        .. code:: sql

            SELECT * FROM simple_authors
            WHERE birth <= '2000-12-31' AND
                (death >= '2000-01-01' OR death IS NULL);

        This works correctly, but you might be wondering why.  We said that ``NULL`` used in expressions usually results in ``NULL``, but here we have a compound Boolean expression using the operators **AND** and **OR**.  So why are we not again losing all living authors?  Well, it turns out that Boolean operators are an exception.  This is because, when used in Boolean expressions, ``NULL`` means that we simply cannot know if the value is ``True`` or ``False``; the value is unknown.  However, the **OR** expression only requires one operand to evaluate to ``True`` in order to return ``True``: ``True OR True`` is ``True``, and so is ``True OR False`` in Boolean logic.  Either way, we get ``True``, so not knowing which it might be doesn't matter.  Therefore the expression in the parentheses is ``True`` if either one of the two conditions within it is true.

        On the other hand, ``False OR NULL`` will give us ``NULL``.  In this case, whether the ``NULL`` is standing in for ``True`` or ``False`` actually matters, because each gives a different outcome. Since we do not know the outcome, the result is ``NULL``.

        Because Boolean expressions can result in ``True``, ``False``, or ``NULL``, we say that SQL has *three-valued logic* (not truly Boolean logic).  Appendix B - :ref:`appendix-b-boolean-operators` provides truth tables for this three-valued logic, but as shown above, you can usually work out the answer by simply thinking of ``NULL`` as meaning "unknown".

排序和 NULL
------------------

**Ordering and NULLs**

.. md-tab-set::

    .. md-tab-item:: 中文

        鉴于您无法有意义地将 ``NULL`` 与其他值进行比较，当我们 **ORDER BY** 包含 ``NULL`` 值的列时会发生什么？不幸的是，这取决于您使用的数据库实现。您需要查阅数据库文档(或简单地进行实验)以查看其默认行为。标准确实提供了一种方式来指定 ``NULL`` 值应该排序到顶部还是底部。比较以下两个查询:

        .. code:: sql

            SELECT * FROM simple_authors ORDER BY death NULLS FIRST;

            SELECT * FROM simple_authors ORDER BY death NULLS LAST;

        (注意:**NULLS FIRST** 和 **NULLS LAST** 修饰符在 MySQL 或 SQL Server 中不受支持。)

    .. md-tab-item:: 英文

        Given that you cannot meaningfully compare ``NULL`` with other values, what happens when we **ORDER BY** a column containing ``NULL`` values?  Unfortunately, it depends on which database implementation you are working with.  You will need to consult your database documentation (or simply try an experiment) to see what its default behavior is.  The standard does provide a way to specify whether ``NULL`` values should sort to the top or bottom.  Compare these two queries:

        .. code:: sql

            SELECT * FROM simple_authors ORDER BY death NULLS FIRST;

            SELECT * FROM simple_authors ORDER BY death NULLS LAST;

        (Note: the **NULLS FIRST** and **NULLS LAST** modifiers are not supported in MySQL or SQL Server.)

.. index:: conditional expressions

条件表达式
:::::::::::::::::::::::

**Conditional expressions**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 提供了用于简单条件逻辑的表达式。基本的条件表达式是 **CASE** 表达式，它有两种形式。在最一般的形式中，**CASE** 允许您根据条件列表指定表达式应该评估的结果。其效果类似于某些编程语言中的 if/else 或 switch/case 语句。

        **CASE** 表达式的基本形式为

        .. code:: sql

            CASE WHEN condition1 THEN result1
                [WHEN condition2 THEN result2]
                ...
                [ELSE result]
            END

        **CASE** 关键字首先出现，后面跟着一个或多个 **WHEN** 子句，给出条件及其为真时所需的结果。第一个为真的条件决定了返回的结果。如果没有条件评估为 ``True``，则使用 **ELSE** 结果(如果提供)，或者如果没有 **ELSE** 子句则返回 ``NULL``。表达式以 **END** 关键字结束。

        例如，我们可以将书籍分成不同的类别，也许用于图书馆中的不同区域，使用 **CASE**:

        .. activecode:: expressions_example_case
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
                author, title,
                CASE WHEN genre = 'fantasy' THEN 'speculative fiction'
                    WHEN genre = 'science fiction' THEN 'speculative fiction'
                    WHEN genre = 'poetry' THEN 'poetry'
                    WHEN genre = 'history' THEN 'non-fiction'
                    ELSE 'general fiction'
                END
                AS category
            FROM simple_books;

        在这里，我们包含了一些在当前数据集中不存在的类别的测试。一个图书馆应用程序可能有许多类别，每个类别包含多个类型。使用 **CASE** 表达式是输出书籍及其类别的一种方式，尽管这取决于对数据库中所有可能类型的了解。一种更数据驱动的方法是通过使用 *join* 查找另一个数据库表中的类别，这一技术我们将在 :numref:`Chapter {number} <joins-chapter>` 中讨论。

        另一种 **CASE** 形式将表达式与可能的值匹配。上述查询可以使用这种形式重写为:

        .. code:: sql

            SELECT
                author, title,
                CASE genre
                    WHEN 'fantasy' THEN 'speculative fiction'
                    WHEN 'science fiction' THEN 'speculative fiction'
                    WHEN 'poetry' THEN 'poetry'
                    WHEN 'history' THEN 'non-fiction'
                    ELSE 'general fiction'
                END
                AS category
            FROM simple_books;

        此外，还有两个执行特定条件逻辑的函数。**COALESCE** 函数接受可变数量的参数。该函数的结果是参数列表中第一个非 ``NULL`` 的表达式，如果所有参数都是 ``NULL``，则返回 ``NULL``。这对于用更具描述性的值替换 ``NULL`` 值很有用:

        .. code:: sql

            SELECT name, COALESCE('died: ' || death, 'living')
            FROM simple_authors;

        最后，**NULLIF** 函数接受两个参数:如果参数相等，则该函数返回 ``NULL``，否则返回第一个参数。这可以用于用 ``NULL`` 替换特定值。例如，

        .. code:: sql

            SELECT title, author, NULLIF(genre, 'science fiction')
            FROM simple_books;

    .. md-tab-item:: 英文

        SQL provides expressions for doing simple conditional logic.  The basic conditional expression in SQL is the **CASE** expression, which comes in two forms.  In the most general form, **CASE** lets you specify what the expression should evaluate to depending on a list of conditions.  The effect is similar to using if/else or switch/case statements in some programming languages.

        The basic form of the **CASE** expression is

        .. code:: sql

            CASE WHEN condition1 THEN result1
                [WHEN condition2 THEN result2]
                ...
                [ELSE result]
            END

        The **CASE** keyword comes first, followed by one or more **WHEN** clauses giving a condition and the desired result if the condition is true.  The first true condition determines the result that will be returned.  If none of the conditions evaluate to ``True``, then the **ELSE** result is used, if provided, or ``NULL`` if there is no **ELSE** clause.  The expression is finished with the **END** keyword.

        For example, we could put our books into different categories, maybe for different sections in a library, using **CASE**:

        .. activecode:: expressions_example_case
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
                author, title,
                CASE WHEN genre = 'fantasy' THEN 'speculative fiction'
                    WHEN genre = 'science fiction' THEN 'speculative fiction'
                    WHEN genre = 'poetry' THEN 'poetry'
                    WHEN genre = 'history' THEN 'non-fiction'
                    ELSE 'general fiction'
                END
                AS category
            FROM simple_books;

        Here we have included tests for some genres not present in our current dataset.  A library application might have many categories, each encompassing multiple genres.  Using a **CASE** expression would be one way to output books with their categories, although it depends on knowledge of all the possible genres in our database.  A more data-driven way would be to look up categories in another database table using a *join*, a technique we will discuss in :numref:`Chapter {number} <joins-chapter>`.

        Another form of **CASE** matches an expression to possible values.  The above query can be rewritten using this form:

        .. code:: sql

            SELECT
                author, title,
                CASE genre
                    WHEN 'fantasy' THEN 'speculative fiction'
                    WHEN 'science fiction' THEN 'speculative fiction'
                    WHEN 'poetry' THEN 'poetry'
                    WHEN 'history' THEN 'non-fiction'
                    ELSE 'general fiction'
                END
                AS category
            FROM simple_books;

        Additionally, there are two functions that perform specialized conditional logic.  The **COALESCE** function takes a variable number of arguments.  The result of the function is the first non-``NULL`` expression in the argument list, or ``NULL`` if all arguments are ``NULL``.  This can be useful for replacing ``NULL`` values with more descriptive values:

        .. code:: sql

            SELECT name, COALESCE('died: ' || death, 'living')
            FROM simple_authors;

        Finally, the **NULLIF** function takes two arguments: if the arguments are equal, the function results in ``NULL``, otherwise it results in the first argument.  This can be used to replace specific values with ``NULL``.  For example,

        .. code:: sql

            SELECT title, author, NULLIF(genre, 'science fiction')
            FROM simple_books;



自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含一些使用上述文本中相同的书籍和作者数据库的练习。如果您遇到困难，请点击练习下方的“显示答案”按钮以查看正确答案。

        - 编写查询以查找从 1980 年到 2000 年出版的所有书籍，并按出版年份排序。

        .. admonition:: 显示答案
            :class: dropdown

            通常在 SQL 中实现同一目标有多种方法。以下是两种解决方案:

            .. code:: sql

                SELECT * FROM simple_books
                WHERE publication_year >= 1980 AND publication_year <= 2000
                ORDER BY publication_year;

                SELECT * FROM simple_books
                WHERE publication_year BETWEEN 1980 AND 2000
                ORDER BY publication_year;


        - 编写查询以查找名字以字母 "J" 开头的作者。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name FROM simple_authors WHERE name LIKE 'J%';


        - 编写查询以查找在 1950 年到 1999 年之间写的书籍，排除诗歌。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books
                WHERE publication_year >= 1950 AND publication_year <= 1999
                AND genre <> 'poetry';


        - 编写查询以查找在 1950 年之前或 1999 年之后写的书籍，排除科学小说。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books
                WHERE (publication_year < 1950 OR publication_year > 1999)
                AND genre <> 'science fiction';


        - 编写查询以查找标题以字母 "T" 或 "I" 开头的书籍，属于小说、幻想或诗歌类型。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books
                WHERE (title LIKE 'T%' OR title LIKE 'I%')
                AND (genre = 'fiction' OR genre = 'fantasy' OR genre = 'poetry');


        - 编写查询以查找没有出生日期的作者。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name FROM simple_authors WHERE birth IS NULL;


        - 编写查询以查找 1915 年后出生的已故作者。

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT name FROM simple_authors
                WHERE death IS NOT NULL
                AND birth > '1915-12-31';


        - 编写查询以获取书名和作者，以及它们所写的世纪，写成“Twentieth Century”这种形式(您只需考虑 20 世纪和 21 世纪)。

        .. admonition:: 显示答案  
            :class: dropdown

            .. code:: sql

                SELECT title, author,
                    CASE WHEN publication_year > 1900 AND publication_year <= 2000
                        THEN 'Twentieth Century'
                        WHEN publication_year > 2000 AND publication_year <= 2100
                        THEN 'Twenty-first Century'
                    END
                    AS century
                FROM simple_books;



    .. md-tab-item:: 英文

        This section contains some exercises using the same books and authors database used in the text above.  If you get stuck, click on the "Show answer" button below the exercise to see a correct answer.

        - Write a query to find all books published from the year 1980 through the year 2000, in order by publication year.

        .. admonition:: Show answer
            :class: dropdown

            There are usually many ways to achieve the same goal in SQL.  Here are two solutions:

            .. code:: sql

                SELECT * FROM simple_books
                WHERE publication_year >= 1980 AND publication_year <= 2000
                ORDER BY publication_year;

                SELECT * FROM simple_books
                WHERE publication_year BETWEEN 1980 AND 2000
                ORDER BY publication_year;


        - Write a query to find the authors whose name starts with the letter "J".

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name FROM simple_authors WHERE name LIKE 'J%';


        - Write a query to find books written between 1950 and 1999, excluding poetry.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books
                WHERE publication_year >= 1950 AND publication_year <= 1999
                AND genre <> 'poetry';


        - Write a query to find books written before 1950 or after 1999, excluding science fiction.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books
                WHERE (publication_year < 1950 OR publication_year > 1999)
                AND genre <> 'science fiction';


        - Write a query to find books with a title beginning with the letters "T" or "I", in the fiction, fantasy, or poetry genres.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM simple_books
                WHERE (title LIKE 'T%' OR title LIKE 'I%')
                AND (genre = 'fiction' OR genre = 'fantasy' OR genre = 'poetry');


        - Write a query to find authors for whom we have no birth date.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name FROM simple_authors WHERE birth IS NULL;


        - Write a query to find deceased authors born after 1915.

        .. admonition:: Show answer  
            :class: dropdown

            .. code:: sql

                SELECT name FROM simple_authors
                WHERE death IS NOT NULL
                AND birth > '1915-12-31';


        - Write a query giving book titles and authors together with the century in which they were written, spelled out like 'Twentieth Century' (you only need to worry about the 20th - 21st centuries).

        .. admonition:: Show answer  
            :class: dropdown

            .. code:: sql

                SELECT title, author,
                    CASE WHEN publication_year > 1900 AND publication_year <= 2000
                        THEN 'Twentieth Century'
                        WHEN publication_year > 2000 AND publication_year <= 2100
                        THEN 'Twenty-first Century'
                    END
                    AS century
                FROM simple_books;




----

**Notes**

.. [#] 数据库学者们经常拒绝将 ``NULL`` 称为 *值*。如果 ``NULL`` 真的是一个值，那么它应该能够与自己及其他值进行比较。一个替代的说法是将列视为处于 ``NULL`` *状态*，而不是说它包含一个 ``NULL`` 值。然而，这一区别在其他 SQL 环境中，如分组和聚合(在 :numref:`Chapter {number} <grouping-chapter>` 中讨论)会失效。由于这些和其他原因，``NULL`` 在 SQL 中的包含是有争议的。

.. [#] 这导致了 SQL 中一个不幸的逻辑不一致:当 *x* 为 ``NULL`` 时，表达式 ``x = x`` 的结果为 ``NULL``。从逻辑上讲，答案应该是 ``True``，无论 *x* 是什么。

.. [#] Database scholars frequently reject calling ``NULL`` a *value*.  If ``NULL`` were truly a value, then it should be comparable to itself and other values.  One alternative is to say that a column is in a ``NULL`` *state*, rather than that it contains a ``NULL`` value.  However, this distinction breaks down in other SQL settings, such as grouping and aggregation (discussed in :numref:`Chapter {number} <grouping-chapter>`).  Because of this and other concerns, the inclusion of ``NULL`` in SQL is controversial.

.. [#] This results in an unfortunate logical inconsistency in SQL: the expression ``x = x`` evaluates to ``NULL`` when *x* is ``NULL``.  Logically, the answer should be ``True``, regardless of what *x* is.


