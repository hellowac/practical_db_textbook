.. _subqueries-chapter:

==========
子查询
==========

**Subqueries**

.. index:: subquery, subquery expression, nested query

.. md-tab-set::

    .. md-tab-item:: 中文

        子查询只是一个用括号括起来并嵌套在另一个查询或语句中的 **SELECT** 查询。这个 *子查询表达式* 根据查询结果和子查询出现的上下文,可以评估为标量、行、列或表。在本章中,我们将讨论在另一个查询中使用查询结果的多种方式。

    .. md-tab-item:: 英文

        A subquery is simply a **SELECT** query enclosed with parentheses and nested within another query or statement.  This *subquery expression* evaluates to a scalar, a row, a column, or a table, depending on the query results and the context in which the subquery appears.  In this chapter we discuss the many ways in which we can use the result of a query within another query.


本章中使用的表
:::::::::::::::::::::::::::

**Tables used in this chapter**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中,我们将使用书籍数据集(表 **books**、**authors** 等),该数据集在 :ref:`附录 A <appendix-a>` 中进行了描述。

    .. md-tab-item:: 英文

        For this chapter we will be using the books dataset (tables **books**, **authors**, etc.), described in :ref:`Appendix A <appendix-a>`.

.. index:: scalar value, row value, row value constructor, table value

标量、行和表
:::::::::::::::::::::::::

**Scalars, rows, and tables**

.. md-tab-set::

    .. md-tab-item:: 中文

        在讨论子查询的用法之前,讨论一些在 SQL 中出现的额外数据类型是有用的。到目前为止,我们假设所有表达式都计算为 *标量* 值。标量值是单一类型的简单值,例如 ``42`` 或 ``'hello'`` 。我们还可以在 SQL 中处理 *行* 值。行只是一个有序的值列表。我们可以通过将用逗号分隔的表达式列表放在括号之间来写出一个文字行(SQL 称这些为“行值构造器”)：

        .. code:: sql

            (1, 'hello', 3.1415)

        在大多数数据库中(但不包括 SQLite),您可以将上述表达式作为文字进行 **SELECT**,结果将显示为单列。

        行可以用于比较表达式。以下两个查询是等效的(尽管第二个查询可能因为风格问题更受欢迎)：

        .. activecode:: subqueries_example_row_expressions
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT b.title
            FROM
              books AS b
              JOIN authors AS a ON a.author_id = b.author_id
            WHERE
              (a.name, b.publication_year) = ('V. S. Naipaul', 1961);

            SELECT b.title
            FROM
              books AS b
              JOIN authors AS a ON a.author_id = b.author_id
            WHERE a.name = 'V. S. Naipaul'
            AND b.publication_year = 1961;

        我们将在以下部分看到行表达式的更多有用应用。

        超出行的范围,我们还可以将 *表* 视为值。在这里,我们使用“表”来表示一组行,而不一定是数据库中存在的命名对象。从 **SELECT** 查询得到的结果在这个意义上是一个表。
        
    .. md-tab-item:: 英文

        Before we discuss the uses of subqueries, it is useful to talk about some additional types of data that come up in SQL.  So far we have assumed that all expressions evaluate to a *scalar* value.  Scalar values are simple values of a single type, such as ``42`` or ``'hello'``.  We can also work with *row* values in SQL.  A row is just an ordered list of values.  We can write down a literal row (SQL calls these "row value constructors") by putting a comma-separated list of expressions between parentheses:

        .. code:: sql

            (1, 'hello', 3.1415)

        In most databases (but not SQLite), you can **SELECT** the above expression as a literal, with the result showing as a single column.

        Rows can be used in comparison expressions. The two queries below are equivalent (although the second is probably preferred as a matter of style):

        .. activecode:: subqueries_example_row_expressions
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT b.title
            FROM
              books AS b
              JOIN authors AS a ON a.author_id = b.author_id
            WHERE
              (a.name, b.publication_year) = ('V. S. Naipaul', 1961);

            SELECT b.title
            FROM
              books AS b
              JOIN authors AS a ON a.author_id = b.author_id
            WHERE a.name = 'V. S. Naipaul'
            AND b.publication_year = 1961;


        We will see more useful applications of row expressions in the following sections.

        Beyond rows, we can also think in terms of *tables* as values.  Here we are using "tables" to mean a collection of rows, not necessarily the named object living in the database.  The result from a **SELECT** query is a table in this sense.

.. index:: subquery; used in Boolean expression

使用子查询的布尔表达式
::::::::::::::::::::::::::::::::::::

**Boolean expressions using subqueries**

.. md-tab-set::

    .. md-tab-item:: 中文

        首先,我们将使用子查询来检查布尔表达式。这些表达式适合在另一个查询或语句的 **WHERE** 子句中使用。

    .. md-tab-item:: 英文

        To start with, we will examine Boolean expressions using subqueries.  These are appropriate for use within the **WHERE** clause of another query or statement.

标量或行结果
--------------------

**Scalar or row result**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们可以用子查询代替标量表达式,只要我们知道子查询将返回单行单列。让我们回到 :numref:`Chapter {number} <joins-chapter>` 中的一个示例,使用我们的 **books** 表：我们如何找到与《三体》同年出版的所有书籍？我们将使用子查询(下面括号中的 **SELECT** 查询)首先获取《三体》的 **publication_year**,然后使用该结果获取我们的书籍列表：

        .. activecode:: subqueries_example_single_row
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM books WHERE publication_year =
              (SELECT publication_year
              FROM books
              WHERE title = 'The Three-Body Problem')
            ;

        要查看此查询的工作原理,首先单独执行子查询：

        .. code:: sql

            SELECT publication_year
            FROM books
            WHERE title = 'The Three-Body Problem';

        由于这个特定的查询返回正好一行一列,我们将结果(整数 ``2008``)视为标量值,并简单地将标量替换为子查询：

        .. code:: sql

            SELECT * FROM books WHERE publication_year = 2008;

        请注意,这只有在我们只有一本书名为《三体》的情况下才有效。一般来说,除非您在已知保存唯一值的列上使用 **WHERE** 子句条件,或者您正在对一组行计算聚合统计(我们将在 :numref:`Chapter {number} <grouping-chapter>` 中讨论聚合),否则假设查询将返回单行并不是一个好主意。如果子查询返回多行,查询将导致错误。然而,如果子查询返回零行,则结果被视为 ``NULL``,而不是错误。

        这种方法同样适用于行表达式,尽管语法可能有些不一致。如果子查询返回多列,那么您只需要在比较的左侧使用行表达式。也就是说,以下 SQL 是正确的：

        .. code:: sql

            SELECT * FROM books
            WHERE (author_id, publication_year) =
              (SELECT author_id, publication_year
              FROM books
              WHERE title = 'The Hundred Thousand Kingdoms')
            ;

        在子查询的 **SELECT** 子句中将列用括号括起来会导致错误。

        与标量结果的比较不必是等于;您可以使用任何比较运算符：

        .. code:: sql

            SELECT * FROM books
            WHERE publication_year >
              (SELECT publication_year FROM books
              WHERE title = 'Americanah')
            ;

    .. md-tab-item:: 英文

        We can use a subquery in place of a scalar expression as long as we know the subquery will return a single row and column.  Let us return to an example from :numref:`Chapter {number} <joins-chapter>` using our **books** table: how can we find all books published in the same year as *The Three-Body Problem*?  We will use a subquery (the **SELECT** query inside the parentheses below) to first obtain the **publication_year** of *The Three-Body Problem*, and then we will use that result to get our list of books:

        .. activecode:: subqueries_example_single_row
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM books WHERE publication_year =
              (SELECT publication_year
              FROM books
              WHERE title = 'The Three-Body Problem')
            ;

        To see what is happening in this query, first execute the subquery on its own:

        .. code:: sql

            SELECT publication_year
            FROM books
            WHERE title = 'The Three-Body Problem';

        Since this particular query returns exactly one row and one column, we treat the result (the integer ``2008``) as a scalar value, and simply substitute the scalar in place of the subquery:

        .. code:: sql

            SELECT * FROM books WHERE publication_year = 2008;

        Note that this only works because we only have one book with the title *The Three-Body Problem*.  In general, it is not a good idea to assume a query will return a single row unless you use a **WHERE** clause condition on a column known to hold unique values, or unless you are computing an aggregate statistic over a set of rows (we will discuss aggregates in :numref:`Chapter {number} <grouping-chapter>`).  If multiple rows are returned by the subquery, the query will result in an error.  However, if zero rows are returned from the subquery, the result is considered to be ``NULL``, rather than an error.

        This same approach works with row expressions, although the syntax is perhaps a bit inconsistent.  If a subquery would return multiple columns, then you need to use a row expression on the left-hand side of your comparison only.  That is, the below is correct SQL:

        .. code:: sql

            SELECT * FROM books
            WHERE (author_id, publication_year) =
              (SELECT author_id, publication_year
              FROM books
              WHERE title = 'The Hundred Thousand Kingdoms')
            ;

        Putting parentheses around the columns in the **SELECT** clause of the subquery will cause an error.

        Comparisons with scalar results do not have to be equality; you can use any comparison operator instead:

        .. code:: sql

            SELECT * FROM books
            WHERE publication_year >
              (SELECT publication_year FROM books
              WHERE title = 'Americanah')
            ;


表或列结果
----------------------

**Table or column result**

.. md-tab-set::

    .. md-tab-item:: 中文

        当查询可以返回多行(列或表)时,我们有一组不同的运算符可供使用。在本节中,我们讨论 **IN** 运算符以及与 **ALL**、**ANY** 和 **SOME** 一起使用的比较运算符。另一个布尔运算符 **EXISTS** 将在我们稍后讨论相关子查询时再进行讨论。所有可以处理多行的运算符也适用于返回零行或一行的子查询。

    .. md-tab-item:: 英文

        When a query can return multiple rows (a column or table), we have a different set of operators to work with.  In this section, we discuss the **IN** operator and the use of comparison operators with **ALL**, **ANY**, and **SOME**.  Another Boolean operator, **EXISTS**, will wait until we discuss correlated subqueries later in the chapter.  All of the operators that work with multiple rows also work on subqueries which return zero rows or one row.

.. index:: IN, NOT IN

IN
####

.. md-tab-set::

    .. md-tab-item:: 中文
      
        **IN** 运算符允许我们将某个表达式与子查询返回的每一行进行比较。如果该表达式等于子查询中的任何结果,则 **IN** 表达式的值为 ``True``。例如,我们可以向数据库请求获奖书籍的列表(书籍 ID 匹配 **books_awards** 表中的某个书籍 ID)：

        .. activecode:: subqueries_example_multiple_rows
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM books WHERE book_id IN
              (SELECT book_id FROM books_awards)
            ;

        SQL 还提供 **NOT IN** 运算符,它只是 **IN** 的布尔逆运算符。通过简单修改上述查询,我们可以获得未获得数据库中列出的任何奖项的书籍列表：

        .. code:: sql

            SELECT * FROM books WHERE book_id NOT IN
              (SELECT book_id FROM books_awards)
            ;

        **IN** 运算符同样适用于行表达式,当我们想要与多个列的子查询结果进行比较时。下面是一个查询,询问与作者去世年份相同的书籍。(我们使用 SQLite 实现的 **substring** 函数,仅提取每位作者去世日期的前四个字符。尽管子字符串是字符型,而书籍出版年份存储为整数,SQLite 能够进行适当的类型转换以进行比较。)

        .. code:: sql

            SELECT a.name AS author, b.title, b.publication_year
            FROM
              authors AS a
              JOIN books AS b ON a.author_id = b.author_id
            WHERE
              (a.author_id, b.publication_year) IN
                (SELECT author_id, substring(death, 1, 4) FROM authors)
            ;

        和往常一样,单独执行子查询以查看它返回的值,可以帮助我们更好地理解整个查询的作用。

        **IN** 还有一个不涉及子查询的有用应用。如果我们在 **IN** 后面跟一个用逗号分隔的表达式列表(用括号括起来),该运算符将对 **IN** 左侧的表达式与括号内列出的每个表达式进行测试。注意,虽然表达式列表看起来像行表达式,但它是非常不同的; **IN** 后列表中的每个表达式都应该与正在比较的表达式具有兼容的类型。

        例如,我们可能对几位不同作者的书籍感兴趣：

        .. code:: sql

            SELECT a.name AS author, b.title
            FROM
              books AS b
              JOIN authors AS a ON a.author_id = b.author_id
            WHERE author IN
              ('Virginia Woolf', 'Kazuo Ishiguro', 'Iris Murdoch');


        如果我们想比较多个值(即行表达式),必须为每个表达式使用括号。在这种情况下,表达式的一般形式是：

        .. code:: sql

            (expr1, expr2, ...) IN ((test11, test12, ...), (test21, test22, ...), ...)

    .. md-tab-item:: 英文

        The **IN** operator lets us compare some expression to every row returned from a subquery.  If the expression equals any result from the subquery, then the **IN** expression evaluates to ``True``.  For example, we can ask our database for a list of books which have won awards (books with book ids matching some book id in the **books_awards** table):

        .. activecode:: subqueries_example_multiple_rows
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM books WHERE book_id IN
              (SELECT book_id FROM books_awards)
            ;

        SQL also provides the **NOT IN** operator as simply the Boolean inverse of **IN**.  We can get a list of books that did not win any of the awards listed in our database by a simple modification of the above query:

        .. code:: sql

            SELECT * FROM books WHERE book_id NOT IN
              (SELECT book_id FROM books_awards)
            ;

        The **IN** operator also works with row expressions, when we want to compare against multiple column subquery results.  Here is a query that asks for books published in the same year as the author's death.  (We are using the **substring** function as implemented by SQLite to get just the first four characters of each author's death date.  Although the substring is a character string and book publication years are stored as integers, SQLite is able to do an appropriate type conversion to make the comparison.)

        .. code:: sql

            SELECT a.name AS author, b.title, b.publication_year
            FROM
              authors AS a
              JOIN books AS b ON a.author_id = b.author_id
            WHERE
              (a.author_id, b.publication_year) IN
                (SELECT author_id, substring(death, 1, 4) FROM authors)
            ;

        As always, it can be helpful to execute the subquery separately to see what values it returns in order to better understand what the entire query is doing.

        **IN** also has a useful application that does not involve a subquery.  If we follow **IN** with a comma-separated list of expressions inside parentheses, the operator will test the expression to the left of **IN** against every expression listed in the parentheses. Note that while the expression list looks like a row expression, it is very different; every expression in the list after **IN** should have a type compatible with the expression being compared.

        For example, we might be interested in books by a few different authors:

        .. code:: sql

            SELECT a.name AS author, b.title
            FROM
              books AS b
              JOIN authors AS a ON a.author_id = b.author_id
            WHERE author IN
              ('Virginia Woolf', 'Kazuo Ishiguro', 'Iris Murdoch');


        If we want to compare multiple values (i.e., row expressions), we must use parentheses for each expression.  In this case, the general form of the expression is

        .. code:: sql

            (expr1, expr2, ...) IN ((test11, test12, ...), (test21, test22, ...), ...)

.. index:: ALL, ANY, SOME

ALL、ANY 和 SOME
##################

**ALL, ANY, and SOME**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们也可以结合使用比较运算符与 **ALL**、**ANY** 或 **SOME** 关键字,将某个表达式与子查询的结果进行比较。例如,我们可以再次请求获奖书籍的列表,使用等于运算符与 **ANY** 关键字,如下所示(注意,**ALL**/**ANY**/**SOME** 关键字在 SQLite 中不受支持,因此你不能在教科书的互动工具中测试这一点)：

        .. code:: sql

            SELECT * FROM books WHERE book_id = ANY
              (SELECT book_id FROM books_awards);

        **SOME** 只是 **ANY** 的同义词。当 **IN** 运算符与子查询结合使用时,相当于 **= ANY**。然而,**ANY** 不能像 **IN** 那样与表达式列表一起使用。

        相反,**ALL** 要求子查询返回的每一行都通过比较测试。例如,要查找所有由作者威拉·凯瑟(Willa Cather)出版的书籍之前出版的书籍：

        .. code:: sql

            SELECT * FROM books WHERE publication_year < ALL
              (SELECT publication_year FROM books WHERE author_id =
                (SELECT author_id FROM authors WHERE name = 'Willa Cather')
              )
            ;

        注意,这里我们在另一个子查询内部使用了子查询！我们可以以这种方式嵌套子查询;我们还可以在复合布尔表达式中使用多个子查询。

        **NOT IN** 运算符相当于 **<> ALL**。

    .. md-tab-item:: 英文

        We can alternately use comparison operators in conjunction with the **ALL** or **ANY** or **SOME** keywords to compare an expression against the results of a subquery.  For example, we can ask again for books which have won awards by using the equality operator together with the **ANY** keyword as follows (note that the **ALL**/**ANY**/**SOME** keywords are not supported by SQLite, so you cannot test this within the textbook's interactive tools):

        .. code:: sql

            SELECT * FROM books WHERE book_id = ANY
              (SELECT book_id FROM books_awards);

        **SOME** is just a synonym for **ANY**.  The **IN** operator when used with subqueries is equivalent to **= ANY**.  However, **ANY** cannot be used with an expression list in the same way **IN** can.

        In contrast, **ALL** requires that every row returned the subquery passes the comparison test.  For example, to find books published before all books by the author Willa Cather:

        .. code:: sql

            SELECT * FROM books WHERE publication_year < ALL
              (SELECT publication_year FROM books WHERE author_id =
                (SELECT author_id FROM authors WHERE name = 'Willa Cather')
              )
            ;

        Note here we have used a subquery inside another subquery!  We can nest subqueries in this fashion; we can also use multiple subqueries within a compound Boolean expression.

        The **NOT IN** operator is equivalent to **<> ALL**.

.. index:: subquery; used in statement

在语句中使用
-----------------

**Use in statements**

.. md-tab-set::

    .. md-tab-item:: 中文

        子查询不仅可以用于其他 **SELECT** 查询中。将子查询用于 **DELETE** 或 **UPDATE** 语句的 **WHERE** 子句中可以非常强大,往往弥补了在这些类型的语句中无法进行连接的缺点。例如,我们可以使用子查询从数据库中删除没有书籍的作者：

        .. code:: sql

            DELETE FROM authors
            WHERE author_id NOT IN
              (SELECT author_id FROM books);

        数据库中没有符合此条件的行(除非你添加它们),因此上述查询不会删除任何行,但它成功执行。

    .. md-tab-item:: 英文

        Subqueries do not have to be used only within other **SELECT** queries.  The use of subqueries within the **WHERE** clause of **DELETE** or **UPDATE** statements can be very powerful, often making up for the fact that we cannot do joins within those types of statements.  For example, we could use a subquery to remove any authors from our database for whom we have no books:

        .. code:: sql

            DELETE FROM authors
            WHERE author_id NOT IN
              (SELECT author_id FROM books);

        There are no rows matching this condition in the database (unless you add them), so the above query does not remove any rows, although it runs successfully.

.. index:: correlated subquery, subquery; correlated

相关子查询
:::::::::::::::::::::

**Correlated subqueries**

.. md-tab-set::

    .. md-tab-item:: 中文

        到目前为止,在我们的所有示例中,我们使用的子查询都是可以独立执行的单独 **SELECT** 查询。子查询可以执行一次,其结果在外部查询中替代。然而,也可以构造依赖于外部查询的子查询。当子查询在表达式中引用外部查询的某个属性时,我们称该子查询与外部查询是 *相关的*。

        例如,考虑查找在作者去世后出版的书籍(遗作)的问题。我们之前看到了一种使用子查询获取与作者去世年份相同年份出版的书籍的方法：

        .. code:: sql

            SELECT a.name AS author, b.title, b.publication_year
            FROM
              authors AS a
              JOIN books AS b ON a.author_id = b.author_id
            WHERE
              (a.author_id, b.publication_year) IN
                (SELECT author_id, substring(death, 1, 4) FROM authors)
            ;

        目前尚不清楚我们如何修改该查询的 **WHERE** 子句以查找在作者去世 *之后* 出版的书籍。我们希望作者 ID 匹配(相等),但需要不同的运算符(大于)来将出版年份与作者的去世年份进行比较。我们想要做的是,对于外部查询中的每本书,将其出版年份与 *其作者的去世年份* 进行比较。为此,我们需要子查询仅返回与外部查询当前行相关的结果——在这种情况下,子查询应返回表示书籍作者去世年份的标量值。

        以下是解决方案：

        .. activecode:: subqueries_example_correlated
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
              a1.name AS author, a1.death, b.title, b.publication_year
            FROM
              authors AS a1
              JOIN books AS b ON a1.author_id = b.author_id
            WHERE b.publication_year >
              (SELECT substring(death, 1, 4)
              FROM authors AS a2
              WHERE a2.author_id = a1.author_id)
            ;

        注意,我们面临着需要使用别名解决歧义的情况——我们有两个 **authors** 表的实例,一个用于外部查询,一个用于子查询。如果我们简单地在子查询中引用 **author_id**,SQL 会假设我们指的是子查询的 **authors** 表。要引用外部查询的 **authors** 表,我们必须给它一个别名(**a1**)以区别。虽然不是必要的,但我们也选择为子查询的表(**a2**)起别名,以避免任何混淆的可能性。

        正如你所看到的,我们不再能够独立于外部查询运行子查询。实际上,我们正在对外部查询中遇到的每一行重复运行子查询。

        与此示例一样,当外部查询和子查询处理同一张表时,相关子查询往往最为有用。当外部查询和子查询处理不同的表时,通常可以将查询写成无相关的形式。

    .. md-tab-item:: 英文

        In all of our examples so far, we used subqueries which are executable on their own as separate **SELECT** queries.  The subquery can be executed once, with the result of the subquery substituted in its place in the outer query.  It is possible, however, to construct subqueries that are dependent on the outer query.  When a subquery references some attribute from the outer query in an expression, we say that the subquery is *correlated* with the outer query.

        For example, consider the problem of finding books published after the author's death (posthumous books).  We previously saw a way of using a subquery to get books published in the same year as the author's death:

        .. code:: sql

            SELECT a.name AS author, b.title, b.publication_year
            FROM
              authors AS a
              JOIN books AS b ON a.author_id = b.author_id
            WHERE
              (a.author_id, b.publication_year) IN
                (SELECT author_id, substring(death, 1, 4) FROM authors)
            ;

        It is not clear how we can modify this query's **WHERE** clause to find books published *after* the author's death.  We want the author ids to match (equality), but we need a different operator (greater than) to compare the publication year with the author's death year.  What we want to do is, for each book in the outer query, compare its publication year to the death year of *its author only*.  To do this, we need our subquery to only return results relevant for the current row in the outer query - in this case, the subquery should return the scalar value representing the book's author's death year.

        Here is the solution:

        .. activecode:: subqueries_example_correlated
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
              a1.name AS author, a1.death, b.title, b.publication_year
            FROM
              authors AS a1
              JOIN books AS b ON a1.author_id = b.author_id
            WHERE b.publication_year >
              (SELECT substring(death, 1, 4)
              FROM authors AS a2
              WHERE a2.author_id = a1.author_id)
            ;

        Note that we have a situation where ambiguity must be resolved using aliasing - we have two instances of the **authors** table, one used in the outer query and one in the subquery.  If we simply refer to **author_id** in the subquery, SQL assumes we mean the subquery's **authors** table.  To refer to the outer query's **authors** table, we must give it an alias (**a1**) to distinguish it.  While not necessary, we have chosen to alias the subquery's table (**a2**) as well, to avoid any chance of confusion.

        As you can see, we can no longer run the subquery independent of the outer query.  In effect, we are running the subquery over and over again, once for each row we encounter in the outer query.

        As in this example, correlated subqueries tend to be most useful when both the outer query and the subquery work with the same table.  When the outer query and subquery work with different tables, it is typically possible to write the query as uncorrelated.

.. index:: EXISTS, NOT EXISTS

EXISTS
------

**EXISTS**

.. md-tab-set::

    .. md-tab-item:: 中文

        **EXISTS** 运算符在子查询之前,子查询是唯一的操作数。只有当子查询返回一行或多行时,**EXISTS** 表达式才会评估为 ``True``。子查询中的实际数据被忽略,因此你可以在 **SELECT** 子句中放入任何你想要的内容。我们在示例中将使用常量 ``1``,只是为了强调我们返回的数据并不重要。

        许多无相关子查询可以重写为使用 **EXISTS** 的相关子查询。例如,要查找所有获得奖项的书籍,我们可以写：

        .. code:: sql

            SELECT * FROM books WHERE book_id IN
              (SELECT book_id FROM books_awards)
            ;

        就像我们之前做的那样,或者使用 **EXISTS**：

        .. code:: sql

            SELECT * FROM books AS b WHERE EXISTS
              (SELECT 1
              FROM books_awards AS ba
              WHERE ba.book_id = b.book_id)
            ;

        你还可以使用 **NOT EXISTS**,它的值为 **EXISTS** 的布尔反值。

    .. md-tab-item:: 英文

        The **EXISTS** operator precedes a subquery, which is the only operand.  An **EXISTS** expression evaluates to ``True`` only if the subquery returns one or more rows.  The actual data from the subquery is ignored, so you can put anything you want in the **SELECT** clause.  We will use a constant ``1`` in our examples, just to emphasize that the data we are returning is unimportant.

        Many uncorrelated subqueries can be rewritten as correlated subqueries using **EXISTS**.  For example, to find all books that have won awards, we can either write

        .. code:: sql

            SELECT * FROM books WHERE book_id IN
              (SELECT book_id FROM books_awards)
            ;

        as we did earlier, or, using **EXISTS**:

        .. code:: sql

            SELECT * FROM books AS b WHERE EXISTS
              (SELECT 1
              FROM books_awards AS ba
              WHERE ba.book_id = b.book_id)
            ;

        You can also use **NOT EXISTS**, which evaluates to the Boolean inverse of **EXISTS**.

其他子句中的子查询
:::::::::::::::::::::::::::

**Subqueries in other clauses**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们已经看到许多在 **WHERE** 子句中使用子查询的示例。然而,子查询表达式可以在其他上下文中使用。特别是,返回标量的子查询可以在 **SELECT** 子句和 **UPDATE** 语句的 **SET** 子句中非常有用。返回表的子查询也可以用作 **SELECT** 子句的 **FROM** 子句中的命名表。

    .. md-tab-item:: 英文

        We have seen numerous examples of subqueries used in **WHERE** clauses.  However, subquery expressions can be used in other contexts.  In particular, subqueries returning scalars can be useful in **SELECT** clauses and in the **SET** clauses of **UPDATE** statements.  Subqueries returning tables can also be used in place of named tables in the **FROM** clause of a **SELECT** clause.

.. index:: subquery; used in SELECT clause

SELECT
------

**SELECT**

.. md-tab-set::

    .. md-tab-item:: 中文

        在 **SELECT** 子句中,子查询可以用来检索不容易从外部查询使用的表中获得的值。以这种方式使用时,子查询必须返回一个标量。这些子查询几乎总是相关的,因为我们希望返回特定于每一行的值。

        例如,在一本书的列表中,我们可能希望包括作者撰写的书籍总数。为此,我们将使用聚合表达式 **COUNT(*)**,它简单地计算与 **SELECT** 查询中的 **WHERE** 子句匹配的行数 [#]_ . (聚合函数在 :numref:`Chapter {number} <grouping-chapter>` 中将详细讨论。)

        .. activecode:: subqueries_example_other_clauses
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
              a.name AS author,
              (SELECT COUNT(*) FROM books AS b2 WHERE b2.author_id = a.author_id)
                AS author_total,
              b1.title
            FROM
              authors AS a
              JOIN books AS b1 ON b1.author_id = a.author_id
            ;

    .. md-tab-item:: 英文

        Used in a **SELECT** clause, subqueries can be used to retrieve values that are not easily obtained from the tables used in the outer query.  Used in this way, the subquery must return a scalar.  These subqueries are almost always correlated, as we want to return a value that is specific to each row.

        For example, in a listing of books, we might want to include the total number of books written by the author.  For this we will use the aggregate expression **COUNT(\*)**, which simply counts the number of rows matching the **WHERE** clause in a **SELECT** query [#]_.  (Aggregates are discussed fully in :numref:`Chapter {number} <grouping-chapter>`.)

        .. activecode:: subqueries_example_other_clauses
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT
              a.name AS author,
              (SELECT COUNT(*) FROM books AS b2 WHERE b2.author_id = a.author_id)
                AS author_total,
              b1.title
            FROM
              authors AS a
              JOIN books AS b1 ON b1.author_id = a.author_id
            ;


.. index:: subquery; used in update

SET
---

**SET**

.. md-tab-set::

    .. md-tab-item:: 中文

        在 **UPDATE** 语句的 **SET** 子句中,子查询提供了一种解决我们无法在 **UPDATE** 中使用连接的问题的方法。如果我们想用第二个表中的数据更新某个表中的行,可以简单地使用子查询来获取适当的值。

        作为一个例子,在为本书的数据库做准备时,运行了一条语句来使用书籍版本信息填充 **books** 表中的 **publication_year** 列。(数据库中的 **editions** 表仅包含少数书籍的条目,以保持大小可控,但原始数据库有完整的数据。)该语句使用另一个聚合表达式来获取每本书在版本表中的最早出版年份：

        .. code:: sql

            UPDATE books
            SET publication_year =
              (SELECT MIN(publication_year)
              FROM editions
              WHERE books.book_id = editions.book_id)
            ;

        注意：如果您运行上述语句,大多数书籍的出版年份将被更新为 ``NULL`` - 当子查询返回零行时,结果被解释为 ``NULL``。(如果您执行了此语句,请不要担心 - 变更仅会对数据的副本进行。您可以通过刷新浏览器窗口获取未修改的数据库副本。)您可以修改该语句,仅更新我们有版本数据的行,使用另一个子查询：

        .. code:: sql

            UPDATE books
            SET publication_year =
              (SELECT MIN(publication_year)
              FROM editions
              WHERE books.book_id = editions.book_id)
            WHERE EXISTS
              (SELECT 1 FROM editions WHERE books.book_id = editions.book_id)
            ;

    .. md-tab-item:: 英文

        Used in the **SET** clause of an **UPDATE** statement, subqueries provide a way to work around the issue that we cannot use joins in an **UPDATE**.  If we want to update rows in some table with data from a second table, we can simply use a subquery to obtain the proper value.

        As an example, in preparation of this book's database, a statement was run to populate the **publication_year** column of **books** using book edition information.  (The **editions** table in the database only has entries for a few books, to keep the size manageable, but the original database had complete data.)  This statement uses another aggregate expression to obtain the earliest publication year from the editions table for each book:

        .. code:: sql

            UPDATE books
            SET publication_year =
              (SELECT MIN(publication_year)
              FROM editions
              WHERE books.book_id = editions.book_id)
            ;

        Note: if you run the statement above, you will update most books to have a ``NULL`` publication year - when the subquery returns zero rows, the result is interpreted as ``NULL``.  (Do not worry if you executed this statement - changes are only made to a copy of the data.  You can obtain an unmodified copy of the database by refreshing your browser window.)  You can modify the statement to only update rows for which we have editions data using another subquery:

        .. code:: sql

            UPDATE books
            SET publication_year =
              (SELECT MIN(publication_year)
              FROM editions
              WHERE books.book_id = editions.book_id)
            WHERE EXISTS
              (SELECT 1 FROM editions WHERE books.book_id = editions.book_id)
            ;

.. index:: subquery; used in FROM clause

FROM
----

**FROM**

.. md-tab-set::

    .. md-tab-item:: 中文

        子查询也可以用于 **SELECT** 查询的 **FROM** 子句,在这种情况下,子查询的结果就像一个表,包含子查询返回的确切数据。在这种用法中,子查询表达式 *必须* 使用别名命名。子查询不能是相关的！子查询表达式可以用于获取在数据库中任何表中不可用的计算数据。例如,上面我们使用了一个相关子查询逐行检索作者的书籍数量以配合每个书名。我们可以改为使用一个不相关的子查询计算所有作者的总数,然后将每个结果像表一样连接到主查询中。(这里的子查询使用了分组和聚合,详见 :numref:`Chapter {number} <grouping-chapter>`。)

        .. code:: sql

            SELECT
              a.name AS author,
              c.count AS author_total,
              b.title
            FROM
              authors AS a
              JOIN books AS b ON b.author_id = a.author_id
              JOIN
                (SELECT author_id, COUNT(*) AS count
                FROM books
                GROUP BY author_id) AS c
                ON c.author_id = a.author_id
            ;

    .. md-tab-item:: 英文

        Subqueries can also be used within the **FROM** clause of a **SELECT** query, in which case the subquery result acts like a table containing exactly the data returned by the subquery.  In this usage, the subquery expression *must* be given a name using aliasing.  The subquery cannot be correlated!  The subquery expression can be used to obtain computed data not available in any table in the database.  For example, above we used a correlated subquery to retrieve author's book counts on a row-by-row basis to go with each book title.  We could instead compute all author totals using an uncorrelated subquery, and then join each to the result as if it were a table.  (Here the subquery uses both grouping and aggregation, covered in :numref:`Chapter {number} <grouping-chapter>`.)

        .. code:: sql

            SELECT
              a.name AS author,
              c.count AS author_total,
              b.title
            FROM
              authors AS a
              JOIN books AS b ON b.author_id = a.author_id
              JOIN
                (SELECT author_id, COUNT(*) AS count
                FROM books
                GROUP BY author_id) AS c
                ON c.author_id = a.author_id
            ;

.. index:: subquery; compared to join, join; compared to subquery

与连接的比较
:::::::::::::::::::::

**Comparison with joins**

.. md-tab-set::

    .. md-tab-item:: 中文

        子查询在某种意义上可以与连接比较,因为它们都涉及多个表。在许多情况下,子查询可以替代连接,反之亦然。然而,它们之间存在一些微妙的差异。

        首先,当然,除了使用 **SELECT** 子句的子查询外,你只能返回外部查询表中实际出现的数据。如果需要结果包含多个表中的数据,通常最好是连接这些表,而不是使用 **SELECT** 子句的子查询。(上面使用的 **SELECT** 子句子查询的例子是一个例外,因为我们提取的数据实际上并没有存储在任何表中。)对于每个所需列使用单独的子查询是笨拙的,难以阅读,并且可能效率低下。

        另一方面,如果你仅从一个表中检索数据,使用子查询有时是有利的。考虑以下两个查询来检索获奖的书籍：

        .. activecode:: subqueries_example_comparison
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM books WHERE book_id IN
              (SELECT book_id FROM books_awards)
            ORDER BY title;

            SELECT b.*
            FROM
              books AS b
              JOIN books_awards AS ba ON ba.book_id = b.book_id
            ORDER BY b.title;

        这两个查询返回相同的数据,但第二个查询有重复行——每本书因为获得的奖项而出现多次。在第一个查询中,**IN** 操作符仅测试书籍在奖项表中的存在性,而不是它出现的次数,因此避免了重复。

        **NOT EXISTS** 和 **NOT IN** 操作符尤其有趣,因为它们可以为那些否则需要外连接的问题提供清晰的解决方案,例如列出未获奖的书籍。

        然而,在许多情况下,你在处理查询时有多种选择。你使用哪种方式取决于个人喜好和风格。以下是三种不同的查询,用于查找与作者去世年份相同的书籍——一种使用不相关的子查询(重复前面的内容),一种使用带有 **EXISTS** 的相关子查询,另一种使用连接：

        .. code:: sql

            SELECT a.name AS author, b.title, b.publication_year
            FROM
              authors AS a
              JOIN books AS b ON a.author_id = b.author_id
            WHERE
              (a.author_id, b.publication_year) IN
                (SELECT author_id, substring(death, 1, 4) FROM authors)
            ;

            SELECT a1.name AS author, b.title, b.publication_year
            FROM
              authors AS a1
              JOIN books AS b ON a1.author_id = b.author_id
            WHERE EXISTS
              (SELECT 1
              FROM authors AS a2
              WHERE a2.author_id = a1.author_id
              AND substring(a2.death, 1, 4) = b.publication_year)
            ;

            SELECT a1.name AS author, b.title, b.publication_year
            FROM
              authors AS a1
              JOIN books AS b ON a1.author_id = b.author_id
              JOIN authors AS a2 ON
                a2.author_id = a1.author_id
                AND substring(a2.death, 1, 4) = b.publication_year
            ;

    .. md-tab-item:: 英文

        Subqueries are comparable to joins in the sense that they both involve multiple tables.  There are many cases in which a subquery can substitute for a join or vice-versa.  However, there are some subtle differences.

        First, of course, is that short of using **SELECT** clause subqueries, you can only return data that actually appears in the outer query's tables.  If you need your result to contain data contained in multiple tables, it is generally best to join the tables rather than using **SELECT** clause subqueries.  (The example used above of a **SELECT** clause subquery is an exception, since the data we pulled in was not actually stored in any table.)  Using a separate subquery for each column needed is unwieldy, hard to read, and probably inefficient.

        On the other hand, if you are retrieving data from one table only, it is sometimes advantageous to use a subquery.  Consider these two queries to retrieve books that have won awards:

        .. activecode:: subqueries_example_comparison
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM books WHERE book_id IN
              (SELECT book_id FROM books_awards)
            ORDER BY title;

            SELECT b.*
            FROM
              books AS b
              JOIN books_awards AS ba ON ba.book_id = b.book_id
            ORDER BY b.title;

        Both queries return the same data, but the second query has duplicate rows - each book appears once for each award it has won.  In the first query, the **IN** operator merely tests for the presence of a book in the awards table, not how many times it appears, so duplicates are avoided.

        The **NOT EXISTS** and **NOT IN** operators are particularly interesting in that they can provide clean solutions to questions that otherwise require an outer join, such as listing the books which have *not* won awards.

        In many cases, though, you have choices in how you approach a query.  Which you use depends on your personal preference and style.  Here are three different queries for finding books published in the same year as the author's death - one using an uncorrelated subquery (repeated from above), one using a correlated subquery with **EXISTS**, and one using a join:

        .. code:: sql

            SELECT a.name AS author, b.title, b.publication_year
            FROM
              authors AS a
              JOIN books AS b ON a.author_id = b.author_id
            WHERE
              (a.author_id, b.publication_year) IN
                (SELECT author_id, substring(death, 1, 4) FROM authors)
            ;

            SELECT a1.name AS author, b.title, b.publication_year
            FROM
              authors AS a1
              JOIN books AS b ON a1.author_id = b.author_id
            WHERE EXISTS
              (SELECT 1
              FROM authors AS a2
              WHERE a2.author_id = a1.author_id
              AND substring(a2.death, 1, 4) = b.publication_year)
            ;

            SELECT a1.name AS author, b.title, b.publication_year
            FROM
              authors AS a1
              JOIN books AS b ON a1.author_id = b.author_id
              JOIN authors AS a2 ON
                a2.author_id = a1.author_id
                AND substring(a2.death, 1, 4) = b.publication_year
            ;


自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含一些使用书籍数据集的练习(提醒：你可以在 :ref:`Appendix A <appendix-a>` 中获取所有表的完整描述)。如果遇到困难,可以点击练习下方的“显示答案”按钮查看正确答案。回答这些问题的方法有很多;请尽量为每个问题使用至少一个子查询。

        - 编写查询列出作者 Viet Thanh Nguyen 的书籍(标题、出版年份)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT title FROM books WHERE author_id =
                  (SELECT author_id FROM authors WHERE name = 'Viet Thanh Nguyen')
                ;


        - 编写查询给出《How We Became Human》的作者。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE author_id =
                  (SELECT author_id FROM books WHERE title = 'How We Became Human')
                ;


        - 编写查询列出出生在作者阿尔贝·加缪去世之后的作者。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE birth >
                  (SELECT death FROM authors WHERE name = 'Albert Camus')
                ;


        - 编写查询列出我们有版本信息的书籍。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT * FROM books WHERE book_id IN
                  (SELECT book_id FROM editions)
                ;


        - 编写查询列出现存作者的书籍标题(假设 ``NULL`` 的死亡日期表示作者仍在世)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT title FROM books WHERE author_id IN
                  (SELECT author_id FROM authors WHERE death IS NULL)
                ;


        - 编写查询列出获得诺贝尔文学奖的作者(作者奖项)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE author_id IN
                  (SELECT author_id FROM authors_awards WHERE award_id =
                    (SELECT award_id FROM awards WHERE name = 'Nobel Prize in Literature'))
                ;


        - 编写查询列出其书籍获得任何种类普利策奖的作者(书籍奖项以字符串 'Pulitzer' 开头)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE author_id IN
                  (SELECT author_id FROM books WHERE book_id IN
                    (SELECT book_id FROM books_awards WHERE award_id IN
                      (SELECT award_id FROM awards WHERE name LIKE 'Pulitzer%')))
                ;


        - 编写查询列出获得书籍奖项但未获得作者奖项的作者。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name
                FROM authors
                WHERE author_id IN
                  (SELECT author_id FROM books WHERE book_id IN
                    (SELECT book_id FROM books_awards))
                AND author_id NOT IN
                  (SELECT author_id FROM authors_awards)
                ;


        - 编写查询查找只有一本书的作者的书籍(根据我们的数据库)。*提示*：一种方法是问,对于每本书,是否存在该作者的*其他*书籍。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT a.name, b1.title
                FROM
                  authors AS a
                  JOIN books AS b1 ON a.author_id = b1.author_id
                WHERE NOT EXISTS
                  (SELECT 1
                  FROM books AS b2
                  WHERE b2.author_id = b1.author_id
                  AND b2.book_id <> b1.book_id)
                ORDER BY a.name;  -- 以便更容易验证


        - 编写查询列出作者 J. M. Coetzee 获得的所有奖项(作者奖项或书籍奖项)。

        .. admonition:: 显示答案
            :class: dropdown

            .. code:: sql

                SELECT name
                FROM awards
                WHERE award_id IN
                  (SELECT award_id FROM authors_awards WHERE author_id =
                    (SELECT author_id FROM authors WHERE name = 'J. M. Coetzee'))
                OR award_id IN
                  (SELECT award_id FROM books_awards WHERE book_id IN
                    (SELECT book_id FROM books WHERE author_id =
                      (SELECT author_id FROM authors WHERE name = 'J. M. Coetzee')))
                ;

    .. md-tab-item:: 英文

        This section contains some exercises using the books data set (reminder: you can get full descriptions of all tables in :ref:`Appendix A <appendix-a>`).  If you get stuck, click on the "Show answer" button below the exercise to see a correct answer.  There are many ways to answer these questions; try to use at least one subquery for each.

        - Write a query to list books (title, publication_year) by the author Viet Thanh Nguyen.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT title FROM books WHERE author_id =
                  (SELECT author_id FROM authors WHERE name = 'Viet Thanh Nguyen')
                ;


        - Write a query giving the author of *How We Became Human*.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE author_id =
                  (SELECT author_id FROM books WHERE title = 'How We Became Human')
                ;


        - Write a query to list authors born after the death of author Albert Camus.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE birth >
                  (SELECT death FROM authors WHERE name = 'Albert Camus')
                ;


        - Write a query to list books for which we have editions information.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT * FROM books WHERE book_id IN
                  (SELECT book_id FROM editions)
                ;


        - Write a query to list the titles of books by living authors (assume a ``NULL`` death date means the author is living).

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT title FROM books WHERE author_id IN
                  (SELECT author_id FROM authors WHERE death IS NULL)
                ;


        - Write a query to list the authors who have won the Nobel Prize in Literature (an author award).

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE author_id IN
                  (SELECT author_id FROM authors_awards WHERE award_id =
                    (SELECT award_id FROM awards WHERE name = 'Nobel Prize in Literature'))
                ;


        - Write a query to list the authors whose books have won any kind of Pulitzer prize (a book award starting with the string 'Pulitzer').

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name FROM authors WHERE author_id IN
                  (SELECT author_id FROM books WHERE book_id IN
                    (SELECT book_id FROM books_awards WHERE award_id IN
                      (SELECT award_id FROM awards WHERE name LIKE 'Pulitzer%')))
                ;


        - Write a query to list authors who have won book awards but not author awards.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name
                FROM authors
                WHERE author_id IN
                  (SELECT author_id FROM books WHERE book_id IN
                    (SELECT book_id FROM books_awards))
                AND author_id NOT IN
                  (SELECT author_id FROM authors_awards)
                ;


        - Write a query to find books by authors with only one book (according to our database).  *Hint*: one way is to ask, for each book, whether there exist *other* books by the same author.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT a.name, b1.title
                FROM
                  authors AS a
                  JOIN books AS b1 ON a.author_id = b1.author_id
                WHERE NOT EXISTS
                  (SELECT 1
                  FROM books AS b2
                  WHERE b2.author_id = b1.author_id
                  AND b2.book_id <> b1.book_id)
                ORDER BY a.name;  -- to make it easier to verify


        - Write a query to list all awards (either author awards or book awards) won by author J. M. Coetzee.

        .. admonition:: Show answer
            :class: dropdown

            .. code:: sql

                SELECT name
                FROM awards
                WHERE award_id IN
                  (SELECT award_id FROM authors_awards WHERE author_id =
                    (SELECT author_id FROM authors WHERE name = 'J. M. Coetzee'))
                OR award_id IN
                  (SELECT award_id FROM books_awards WHERE book_id IN
                    (SELECT book_id FROM books WHERE author_id =
                      (SELECT author_id FROM authors WHERE name = 'J. M. Coetzee')))
                ;


----

**Notes**

.. [#] 对于这个特定问题,我们可以使用一种叫做 *窗口函数* 的方法,这将在 :numref:`Chapter {number} <advanced-sql-chapter>` 中简要讨论。

.. [#] For this particular problem, we could instead use something called a *window function*, which will be discussed briefly in :numref:`Chapter {number} <advanced-sql-chapter>`.




