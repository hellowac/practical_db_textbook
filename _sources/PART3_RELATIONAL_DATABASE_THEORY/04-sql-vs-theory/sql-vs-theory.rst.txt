.. _sql-vs-theory-chapter:

================================================
SQL 与关系模型之间的差异
================================================

**Differences between SQL and the relational model**

.. md-tab-set::

    .. md-tab-item:: 中文

        关系数据库模型启发并影响关系数据库系统。然而，该模型与大多数此类系统的实际实现存在差异。结构化查询语言（SQL，详见 :numref:`Part {number} <sql-part>`）在很大程度上决定了关系数据库系统的行为，因此我们将本章框架设置为 SQL 与关系模型之间的比较。本章旨在为已经学习关系模型的学生提供关于这些差异的实用指南，同时也为学习关系模型的 SQL 用户提供帮助。

    .. md-tab-item:: 英文

        The relational model of the database inspires and informs relational database systems.  However, the model differs from the actual implementation of most such systems.  The structured query language (SQL, covered in :numref:`Part {number} <sql-part>`) largely dictates the behavior of relational database systems, and therefore we frame this chapter as a comparison between SQL and the relational model.  This chapter is intended as a practical guide to these differences for students who have learned the relational model and must now learn SQL, or users of SQL learning the relational model.

关系作为集合
:::::::::::::::::

**Relations as sets**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 和关系模型之间的一个关键区别在于对关系中重复元组的处理。由于关系是集合，在模型中不存在“重复”元组的概念。一个元组要么在关系中，要么不在关系中，没有重复性。相比之下，SQL 允许重复。一个 SQL 关系（或 *表*）可以包含多个相同的元组（或 *行*），如果没有主键约束——我们称 SQL 关系为 *多重集* 而不是集合。SQL 查询也可能返回重复的行，例如，当查询请求从一个关系或关系的连接中获取某些属性的子集（一个投影）时。

        如果不加小心，重复元组可能会导致严重错误。例如，考虑一个假设的数据库，其中包含以下关系：第一个关系列出了公司的员工，属性包括员工薪水，第二个关系列出了公司中的项目，而第三个关系将前两个关系连接在一个多对多关系中。假设员工表的主键是 **employee_id**，项目表的主键是 **project_id**，那么第三个关系只包含名为 **project_id** 和 **employee_id** 的属性，这些都是前两个表中同名属性的外键。该关系中存在的一个元组表示某特定员工在某特定项目上工作。

        现在，考虑一个查询，询问公司在一系列项目上的总员工薪资成本。使用关系代数或 SQL 解决此问题的一种方法是简单地将三张表连接在一起，然后对员工 ID 和薪水属性进行投影。最终答案通过对员工薪水求和获得。使用关系代数，这将产生正确的结果，因为每个参与感兴趣项目的员工只列出一次。然而，使用 SQL，如果任何员工参与了多个感兴趣的项目，则求和将不正确，因为这些员工将在连接结果中列出多次。

        当然，针对上述假设问题有多种解决方案。如果 SQL 查询被重构为使用子查询（使用 **IN**）而不是连接，或者如果交叉引用关系被重新设计为包含例如某个员工在特定项目上的工作百分比，那么可能会得到更准确的结果。然而，这需要 SQL 数据库的设计者和程序员付出一些努力，以防止出现使用关系代数时不会发生的结果。反论点是，使用关系代数时也必须小心；假设连接结果仅对员工薪水属性进行投影，毕竟，这是我们需要求和的唯一值。在这种情况下，如果两名员工的薪水相同，我们将获得错误结果！

        选择在查询结果中允许重复元组或许基于实际的性能考虑。为了确保查询结果的唯一性（例如，使用 SQL 的 **DISTINCT** 操作符时），数据库系统通常会对结果进行排序或索引，这会增加操作的成本。如果查询的结果非常大（在现代“数据大”时代并不少见），成本可能变得不可承受。虽然在某些情况下，数据库引擎可以利用查询中涉及的原始表上已经存在的索引来高效地产生唯一结果，但这并不适用于所有查询（可以假设，如果早期的数据库设计者选择强制唯一性，技术和实际应用将会演变得大大消除这些顾虑；然而，性能对于早期的关系数据库在与更成熟的非关系系统竞争时是一个严重的关注点）。

    .. md-tab-item:: 英文

        A key difference between SQL and the relational model regards the treatment of duplicate tuples in a relation.  Since relations are sets, in the model there can be no notion of "duplicate" tuples.  A tuple either is or is not in the relation, without multiplicity.  By contrast, SQL permits duplicates.  A SQL relation (or *table*) may contain multiple identical tuples (or *rows*) if it is not constrained with a primary key - we say that SQL relations are *multisets* rather than sets.  SQL queries may also return duplicate rows, for example, if a query asks for some subset of attributes (a projection) from a relation or a join of relations.

        Duplicate tuples can be the source of serious errors if care is not taken.  As an example, consider a hypothetical database with the following relations: the first relation lists employees of a company with attributes including employee salary, the second lists projects in the company, while the third relation connects the first two relations in a many-to-many relationship.  Assuming that the primary key for the employee table is **employee_id** and the primary key for the project table is **project_id**, then the third relation contains only the attributes named **project_id** and **employee_id**, which are foreign keys on the attributes of the same name in the first two tables.  The existence of a tuple in this relation indicates that a particular employee works on a particular project.

        Now, consider a query asking for the total employee salary costs to the company for a list of projects.  One approach to this problem using relational algebra or SQL involves a simple join of the three tables followed by projection onto the employee id and salary attributes.  The final answer is obtained by summing the salaries of the employees.  Using relational algebra, this produces the correct result, because each employee engaged in any of the projects of interest is listed only once.  Using SQL, however, the sum is incorrect if any employees work on more than one of the projects of interest, because those employees will be listed more than once in the join result.

        There are, of course, multiple solutions to the hypothetical problem described above.  If the SQL query is restructured to use subqueries (using **IN**) instead of a join, or if the cross-reference relation is redesigned to include, say, a percentage of effort for an employee attributable to a particular project, then a more accurate result can occur.  However, this requires some effort on the designers and programmers of the SQL database to prevent a result that cannot happen using relational algebra.  The counter argument is that care must also be taken when applying relational algebra; suppose the join result is projected solely onto the employee salary attribute, which is, after all, the only value we need to sum.  In this case, we will obtain an incorrect result if two employees have the same salary!

        The choice to permit duplicate tuples in query results is perhaps based on practical performance considerations.  To ensure uniqueness in a query result (e.g., when using the SQL **DISTINCT** operator), database systems typically sort or index the result, which adds cost to the operation.  If a query has a very large result (not uncommon in the modern era of "big data") the cost may become prohibitive.  While there are situations which permit the database engine to utilize indexes already available on the original tables involved in a query in order to produce a unique result efficiently, this is not possible for all queries in the general case. (One can posit that, had early database designers chosen to enforce uniqueness, technology and practical use would have evolved to largely erase these concerns; however, performance was a serious concern for the early relational databases in competition with more mature non-relational systems.)

元组和属性
:::::::::::::::::::::

**Tuples and attributes**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQL 也在元组（或行）的某些方面与关系模型有所不同。在关系模型中，元组由值组成，每个值都与一个特定命名的属性相关联，并且这些值属于该属性的值域。模型中的元组有时可以被视为有序值的列表，但仅在隐含理解每个值与某个关系模式中定义的属性相关联的情况下。最后，元组中的属性名称必须是唯一的。

        在 SQL 中，行的处理方式更为灵活。存储在关系（或表）中的行通常符合上述对元组的要求。然而，从查询中返回的行可能没有与每个值关联的明确属性。当查询从某个表中返回列值时，这些值可以被视为与原始表的定义相关联的明确属性。SQL 还允许查询返回基于值的操作或函数结果的值；在大多数 SQL 数据库系统中，这些值至少会有一个关联类型，如“整数”或“字符字符串”。然而，除非查询明确为每个值提供名称，否则数据库系统可能选择提供一个通用名称或根本不提供名称。这些匿名值只能通过它们在行中的位置来识别。在某些 SQL 系统中，也可能有多个值与相同名称相关联。

        这些差异在通常实践中可能不会带来严重困难。然而，可以说这些值缺乏给予它们意义所需的上下文，因此有可能构造出出现问题的场景。例如，考虑一家根据某些复杂的数学公式在每年年底向员工颁发奖金和加薪的公司。可以使用 SQL 查询来计算这两个值。如果每个数字仅通过其在返回行中的列位置来识别，那么一名开发公司会计软件的开发者在短暂分心的情况下就可能会反转每个数字的预期应用。

    .. md-tab-item:: 英文

        SQL also differs from the relational model regarding some aspects of tuples (or rows).  In the relational model, tuples are composed of values which are each associated with a specific named attribute and which are members of the domain of values for the attribute.  Tuples in the model may sometimes be treated as ordered lists of values, but only with the implicit understanding that each value is associated with an attribute as defined in some relation schema.  Finally, attribute names within a tuple must be unique.

        In SQL, rows are treated somewhat more flexibly.  Rows stored in a relation (or table) generally conform to the above requirements on tuples.  However, rows returned from a query may not have well defined attributes associated with each value.  Where the query returns column values from some table, the values can be considered to be associated with a well defined attribute, following the definition of the original table.  SQL also permits queries to return values that are the results of operations or functions invoked on values; in most SQL database systems, those values will at least have an associated type, such as "integer" or "character string".  However, unless the query specifically provides a name for each such value, the database system may choose to provide a generic name or no name at all.  These anonymous values can be identified solely by their position in the row.  In some SQL systems, it is also possible to have multiple values associated with the same name.

        These differences may not present serious difficulties in usual practice.  However, there is a sense in which such values lack the context necessary to give them meaning, and it is therefore possible to contrive scenarios in which problems arise.  For example, consider a company which awards bonuses as well as pay raises to its employees at the end of each year based on some complex mathematical formulas.  A SQL query may be used to calculate both values.  It would take only a momentary distraction for a developer programming the company's accounting software to reverse the intended application of each number if each number is identified solely by its columnar position within the returned rows.

逻辑混淆
::::::::::::::::::

**Logical confusions**

.. md-tab-set::

    .. md-tab-item:: 中文

        虽然这不是关系模型与 SQL 之间的具体冲突，但 SQL 通过使用 NULL 实现三值逻辑可能会导致一些令人困惑的情况。其中一个被广泛引用的问题与 *重言式(tautological)* 表达式相关——即在逻辑上总是为真的表达式。例如，假设某个整数变量 *x* ，在没有 NULL 的情况下，“*x* 小于 17 或 *x* 大于等于 17”的陈述必须为真。

        然而，如果允许 NULL 并且 *x* 是 NULL，那么使用三值逻辑将 *x* 与 17 进行比较的结果为 *未知(unknown)*。在 SQL 中，两个未知值的 **OR** 运算会产生另一个未知值，而不是预期的真值。这个结果部分是由于实际限制；要求 SQL 解释器推理任意逻辑表达式以揭示重言式会影响查询的响应速度。如果我们的逻辑预期是该表达式在关系模型中必须为真，那么这就代表了 SQL 与关系模型之间的差异。

        然而，可以辩称这实际上是我们如何赋予 NULL 含义的问题。NULL 可能意味着 *x* 是某个整数，但我们不知道具体是哪个整数。然而，NULL 也用于其他含义，例如 *x* 是 *不适用(not applicable)* 。考虑一个存储某国居民数据的关系，其中包括一个人的护照号码属性。如果一个人从未出国旅行，他们可能没有护照，因此护照号码属性对该人没有意义。在这种情况下，很难争辩说像“该人护照号码的第一位数字小于 5 或第一位数字大于等于 5”这样的表达式应该评估为真。

        作为一个更简单的重言式问题示例，考虑下面的 SQL 查询，它返回没有将 NULL 指派给列 *x* 的行：

        .. code:: sql

            SELECT * FROM some_table WHERE x = x;

        在关系模型中包含 NULL 至少部分是因为这种类型的混淆而引发争议。

    .. md-tab-item:: 英文

        While not specifically a conflict between the relational model and SQL, SQL's implementation of three-valued logic using NULL can lead to some puzzling situations.  One of the more cited issues relates to *tautological* expressions - expressions which are logically always true.  For example, assuming some integer variable *x*, in the absence of NULL, the statement that "*x* is less than 17 or *x* is greater than or equal to 17" must be true.

        However, if NULL is permitted and *x* is NULL, then comparing *x* to 17 using three-valued logic gives us the result *unknown*.  In SQL, the **OR** of two unknown values yields another unknown, rather than the expected true.  This outcome is partially a result of practical limitations; asking the SQL interpreter to reason about arbitrary logical expressions in order to reveal tautologies would impact the speed with which queries can be answered.  If our logical expectation is that the expression must be true in the relational model, then this represents a difference between SQL and the relational model.

        It can be argued, though, that this is really a problem in how we assign meaning to NULL.  NULL may mean that *x* is some integer, but we do not know which integer it is.  However, NULL is also used for other meanings, such as that *x* is *not applicable*.  Consider a relation storing data on the inhabitants of some country where the relation includes an attribute for the person's passport number.  If a person never travels outside the country, they may not have a passport, and the passport number attribute has no meaning for the person.  In this case it is difficult to argue that an expression such as "the first digit of the person's passport number is less than 5 OR the first digit is greater than or equal to 5" should evaluate to true.

        As an even simpler example of a problem with tautology, consider the SQL query below, which returns no rows in which NULL is assigned to the column *x*:

        .. code:: sql

            SELECT * FROM some_table WHERE x = x;

        The inclusion of NULL in the relational model is controversial at least in part due to confusions of this type.





