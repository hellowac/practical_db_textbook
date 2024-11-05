.. _relational-model-chapter:

====================================
数据库的关系模型
====================================

**The relational model of the database**

.. index:: database; relational model of, relational model of databases

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中，我们介绍了关系数据库所基于的数学模型。数据库的 *关系模型(relational model)* 提供了一个描述和推理数据库的数学基础。尽管大多数关系数据库系统在实践中与数学模型存在一些小的差异（见 :numref:`Chapter {number} <sql-vs-theory-chapter>`），理解这个模型有助于深入理解这些系统。

        鉴于其数学基础，关系模型最方便的表达方式是使用至少一些数学符号和术语。然而，为了使本书能够尽可能广泛地接触到读者，我们将用最少的符号来介绍模型的基本概念，并在使用时解释相关术语。

    .. md-tab-item:: 英文

        In this chapter we introduce the mathematical model that relational databases are based on.  The *relational model* of the database provides a mathematical foundation for describing and reasoning about databases.  While most relational database systems in practice vary in small ways from the mathematical model (see :numref:`Chapter {number} <sql-vs-theory-chapter>`), understanding the model facilitates a deeper understanding of these systems.

        Given its mathematical foundations, the relational model is most conveniently expressed using at least some mathematical notation and terminology.  In the interests of keeping this book accessible to as wide an audience as possible, however, we will give the basics of the model using a minimum of notation and explain terms as we use them.


模型基础
::::::::::::

**Model basics**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们首先给出 *集合(set)* 的工作定义，这是一种数学对象，我们将在定义其他术语时使用。然后，我们定义 *关系(relations)*，这是关系模型的基本对象，以及与之相关的术语。

    .. md-tab-item:: 英文

        We start with a working definition of *set*, a mathematical object that we will use in defining other terms.  We then define *relations*, the fundamental objects of the relational model, and their associated terms.

集合
----

**Sets**

.. md-tab-set::

    .. md-tab-item:: 中文

        集合是一个数学对象，表示一组不同值的集合。集合可以通过值的共同属性来定义，或者仅仅通过列出集合中的所有值来定义。对于某个任意值和某个集合，我们可以问该值是否是集合的 *成员(member)*，即它是否是集合中的某个值。例如，2 是所有数字的集合（一个无限集合）的成员，同时也是集合 {1, 2, 3, 4}（一个包含四个值的有限集合）的成员。另一方面，2 不是奇数集合或描述颜色的词的集合的成员（即 {blue, yellow, ...}）。

        集合的 *子集(subset)* 是一个包含零个或多个来自该集合的元素的集合，并且仅包含该集合中的元素。对于集合 {1, 2, 3, 4}，子集包括 {2, 4}、{1, 2, 3, 4} 和 {} （ *空集合(empty set)* ）。注意，任何集合都是其自身的子集；一个不等于整个集合的子集称为该集合的 *真子集(proper subset)*。

        集合的 *超集(superset)* 是一个包含该集合中所有元素的集合，并且可能包含不在该集合中的元素。对于集合 {1, 2, 3, 4}，超集包括 {1, 2, 3, 4}、{1, 2, 3, 4, 5} 和 {0, 1, 2, 3, 4, 5, 7}。注意，任何集合都是其自身的超集；一个包含不在该集合中的元素的超集称为该集合的 *真超集(proper superset)*。

    .. md-tab-item:: 英文

        A set is a mathematical object that represents a collection of distinct values.  Sets can be defined by some property that values have in common, or simply by listing all of the values in the set.  For some arbitrary value and some set, we can ask whether the value is a *member* of the set, that is, whether it is one of the values in the set.  For example, 2 is a member of the set of all numbers (an infinite set) and also a member of the set {1, 2, 3, 4} (a finite set containing four values).  On the other hand, 2 is not a member of the set of odd integers or the set of words describing colors (i.e., {blue, yellow, ...}).

        A *subset* of a set is a set containing zero or more elements from the set and only from the set.  For the set {1, 2, 3, 4}, subsets include {2, 4}, {1, 2, 3, 4}, and {} (the *empty set*).  Note that any set is a subset of itself; a subset which is not equal to the whole set is termed a *proper subset* of the set.

        A *superset* of a set is a set containing all elements from the set, and may contain elements not from the set.  For the set {1, 2, 3, 4}, supersets include {1, 2, 3, 4}, {1, 2, 3, 4, 5}, and {0, 1, 2, 3, 4, 5, 7}.  Note that any set is a superset of itself; a superset which contains elements not in the set is termed a *proper superset* of the set.

.. index:: relation

关系
---------

**Relations**

.. md-tab-set::

    .. md-tab-item:: 中文

        在关系模型中，数据存在于关系中。关系通常被描绘为一种表格数据结构：

        .. image:: books.svg
            :alt: 名为 simple_books 的关系的表格示例，显示带有属性名称的标题和几行数据（或元组）。

        这个插图只是描绘关系 **simple_books** 的一种可能方式，而表格（或二维数组）只是用于存储关系的一种数据结构。从关系模型的角度来看，关系是数学对象，而不是数据结构。

        正式地说，关系是一组共享相同 *域* 的 *元组*。

    .. md-tab-item:: 英文

        In the relational model, data exist in relations.  A relation is often depicted as a tabular data structure:

        .. image:: books.svg
            :alt: A tabular illustration of a relation named simple_books, showing a header with attribute names and several rows of data, or tuples.

        This illustration is just one possible way of depicting the relation **simple_books**, and tables (or two-dimensional arrays) are just one data structure that can be used for storing relations.  From the perspective of the relational model, relations are mathematical objects, not data structures.

        Formally, a relation is a set of *tuples* that share the same *domain*.

.. index:: tuple, domain

元组
------

**Tuples**

.. md-tab-set::

    .. md-tab-item:: 中文

        在关系模型中，元组有两种不同的定义；具体使用哪种取决于在特定上下文中哪种更为方便。我们将从元组的常规数学定义开始，将其视为一个有序值列表。元组中的单个值也称为元组的 *元素* 。我们用括号中的逗号分隔列表来表示元组。元组对应于上表中的行。例如， **simple_books** 关系中的一个元组可以写成：

            (*The House of the Spirits*, Isabel Allende, 1982, magical realism)

        元组的每个元素都属于某个集合，我们称之为元素的 *域(domain)* 。在我们示例的元组中，第一个元素属于书名的域。

        元组本身也属于一个域，该域是根据元组中每个值的域来定义的。 **simple_books** 关系中的元组属于具有四个元素的元组的域，其中第一个元素属于书名的域，第二个元素来自作者的域，第三个元素属于日历年份的域，第四个元素在文学流派的域中。

    .. md-tab-item:: 英文

        A tuple in the relational model is defined in two different ways; which is used depends on which is more convenient in a particular context.  We will start with the normal mathematical definition of a tuple as an ordered list of values.  A single value in the tuple is also called an *element* of the tuple.  We denote tuples as a comma-separated list within parentheses.  Tuples correspond to rows in the table above.  For example, one tuple from the **simple_books** relation could be written as:

            (*The House of the Spirits*, Isabel Allende, 1982, magical realism)

        Each element of a tuple belongs to some set, which we call the *domain* of the element.  In our example tuple, the first element belongs to the domain of book titles.

        The tuple itself also belongs to a domain, which is defined in terms of the domains of each value in the tuple.  Tuples of the **simple_books** relation belong to the domain of tuples with four elements for which the first element belongs to the domain of book titles, the second element is from the domain of authors, the third element belongs to the domain of calendar years, and the fourth element is in the domain of literary genres.

.. index:: tuple; attribute

属性
----------

**Attributes**

.. md-tab-set::

    .. md-tab-item:: 中文

        在元组的另一种定义中，我们可以谈论元组的 *属性*。我们可以将属性视为由元组表示的值的命名属性。例如，如果 **simple_books** 关系中的一个元组代表一本书，那么该元组的一个属性就是书的 **标题**。在我们的示例元组中， **标题** 属性是 *The House of the Spirits* 。我们关系中的其他书籍属性包括 **作者**、 **年份** 和 **流派**。属性名称在上图表的表头行中显示。

        在这种元组的定义中，元组不一定是有序列表；元组中的每个值不是与位置关联，而是与属性关联。每个属性都与一个域相关联。例如， **simple_books** 中任何元组的 **标题** 属性必须是书名域的一个成员。将名称与元组中的值关联起来比在查询数据库时引用第 *n* 个元素要方便得多。

        这两种元组的定义并不排斥。在第一种元组定义中，顺序集合中的每个位置也对应于一个特定的属性——在我们的例子中，第一个元素是 **标题** 属性。虽然我们可以认为元组具有无特定顺序的命名属性，但在实际应用中，我们通常会给关系中的属性分配一个顺序——因此这两种元组的定义是同时使用的。

    .. md-tab-item:: 英文

        In an alternate definition of tuple, we can speak of the *attributes* of the tuple.  We can think of attributes as the named properties of the value represented by the tuple.  For example, if a tuple in the **simple_books** relation represents one book, then one attribute of the tuple is the book's **title**.  In our example tuple, the **title** attribute is *The House of the Spirits*.  The other attributes of books in our relation are **author**,  **year**, and **genre**.  Attribute names are shown in the header row of the table in the illustration above.

        In this definition of tuple, tuples are not necessarily ordered lists; each value in the tuple is associated not with a position but with an attribute.  Each attribute is associated with a domain. For example, the **title** attribute for any tuple in **simple_books** must be a member of the domain of book titles.  Having names associated with values in a tuple is much more convenient than having to refer to the *n*-th element when we want to query our database.

        The two definitions of tuple are not exclusive.  In the first definition of tuple, each position in the ordered collection also corresponds to a specific attribute - in our example, the first element is the **title** attribute.  While we can think of tuples as having named attributes in no particular order, in practice we typically assign an ordering to the attributes in a relation - so both definitions of tuple are used simultaneously.

.. index:: schema, relation schema

模式
-------

**Schemas**

.. md-tab-set::

    .. md-tab-item:: 中文

        关系的属性和域由其 *模式(schema)* 定义。如果一个关系（一个元组的集合）符合模式给出的定义，那么它被认为是该关系模式的 *实例(instance)* ；也就是说，如果关系中的所有元组都具有模式定义的命名属性，并且属性值属于正确的域。在某些定义中，关系模式还包括关系必须遵循的约束，例如下面讨论的 *键(key)* 约束。

        在典型的数据库中，每个关系模式都与恰好一个关系配对，该关系是该模式的当前关系。当对当前关系中的数据进行修改时，会产生一个新的当前关系。除了某些特定类型的数据库外，关系模式通常没有与过去关系相关的历史。因此，使用相同的名称来表示关系及其模式是常见的做法。

        *数据库(database)* 可以定义为一组关系模式及其相关的当前关系。关系模式的集合称为数据库模式。

    .. md-tab-item:: 英文

        A relation's attributes and domains are defined by its *schema*.  A relation (a set of tuples) is considered to be an *instance* of the relation schema if it conforms to the definition given by the schema; that is, if all of the tuples in the relation have the named attributes defined by the schema, and the attribute values are members of the correct domains.  In some definitions, relation schemas also include constraints which relations must conform to, such as *key* constraints, discussed below.

        In a typical database, each relation schema is paired with exactly one relation, which is the current relation for the schema.  When a modification is made to the data in the current relation, it produces a new current relation.  Except in some specialized types of databases, there is no history of past relations associated with a relation schema.  Thus, it is frequent practice to use the same name for the relation and its schema.

        A *database* may be defined as a collection of relation schemas and their associated current relations.  The collection of relation schemas is called the database schema.

唯一性和排列
:::::::::::::::::::::::::::

**Uniqueness and permutations**

.. md-tab-set::

    .. md-tab-item:: 中文

        关系作为元组的集合，分享了一些集合的重要属性。首先，集合中的项必须是不同的。在关系模型中，元组也必须是不同的，也就是说，没有两个元组可以在每个属性上具有相同的值。对于我们的 **simple_books** 关系，完全可以假设我们会添加一些与其他元组具有相同作者的书籍，或者在同一年出版的书籍。然而，我们禁止添加与现有元组重复的元组。

        集合的另一个属性（或许说是缺乏某种属性）是集合中的元素没有定义的顺序。集合中的元素没有在集合内的等级或位置。关系同样没有元组的内在排序。

        当我们提供 **simple_books** 关系的表格示例时，我们指出这只是关系的一种可能表示。例如，我们可以在不改变关系的情况下，改变表格的行顺序。如果我们应用上面提到的第二个元组定义，其中值同样没有顺序，而是与特定属性相关联，那么改变列的顺序也是有效的。因此，我们可以说，下面的 **simple_books** 的示例与之前的示例是等价的：

        .. image:: books_permuted.svg
            :alt: 简单书籍的表格图示，其中行和列排列顺序。

    .. md-tab-item:: 英文

        Relations, as sets of tuples, share certain important properties of sets.  First, items in a set must be distinct.  In the relational model, tuples must likewise be distinct, that is, no two tuples can have the same values for every attribute.  For our **simple_books** relation, it is entirely reasonable to suppose that we will add books that have the same author as some other tuple, or books published in the same year as another book.  However, we are forbidden to add a tuple that duplicates an existing tuple.

        Another property (or perhaps lack of property) of sets is that there is no defined order of elements in a set.  An element of a set has no rank or position within the set.  Relations likewise have no intrinsic ordering of tuples.

        When we provided a tabular illustration of the **simple_books** relation above, we noted that it was just one possible depiction of the relation.  We can, for example, permute the rows of the table, without changing the relation.  If we apply the second definition of tuple above, in which values are likewise not ordered but rather associated with specific attributes, it is valid to permute columns as well.  We would say, then, that the illustration of **simple_books** below is equivalent to our previous illustration:

        .. image:: books_permuted.svg
            :alt: A tabular illustration of simple_books, with rows and columns permuted.


约束
:::::::::::

**Constraints**

.. md-tab-set::

    .. md-tab-item:: 中文

        *约束(Constraints)* 是关于关系的陈述，要求在任何时候都必须为真。一些约束在上述定义中是隐含的；例如，元组中的属性值被限制为所属域的成员。关系模型还包含两种类型的显式约束：键和外键。

    .. md-tab-item:: 英文

        *Constraints* are statements about relations which are required to be true at all times.  Some constraints are implicit in the definitions above; for example, the attribute values in a tuple are constrained to be members of the associated domain.  The relational model also incorporates two types of explicit constraint: keys and foreign keys.

.. index:: key - relational model, key - relational model; primary, primary key - relational model, key - relational model; candidate, candidate key, key - relational model; unique, unique key

键和主键
---------------------

**Keys and primary keys**

.. md-tab-set::

    .. md-tab-item:: 中文

        在许多情况下，关系可能包含能够唯一标识元组的属性子集。例如，对于我们的 **simple_books** 关系，我们将断言属性对 **author** 和 **title** 能够唯一标识我们关系中的任何书籍，或者任何我们将来可能选择添加到关系中的书籍。另一方面，单独的 **author** 或 **title** 都不足以唯一标识一本书——可能有两个不同的作者创作同名的书籍，当然，许多书籍可能有相同的作者。我们声明集合 {**author**, **title**} 是 **simple_books** 关系的 *键(key)* 。

        键在关系理论中扮演重要角色，正如我们将看到的。我们将在后面的章节进一步探讨的一个含义是，我们的 **simple_books** 关系中的任何两个元组（现在或将来）都不能共享完全相同的 **author** 和 **title** 值。事实上，声明没有两个元组可以共享相同的 **author** 和 **title**，反过来又意味着 **author** 和 **title** 共同唯一标识任何一本书。这些断言是等价的。

        重要的是要强调，键属性是我们对现实世界所做的陈述，而不是关系中数据的短暂属性。例如，我们当前的 **simple_books** 示例中 **year** 没有重复值。然而，要使 **year** 成为键，需要 **year** 对于我们可能存储在 **simple_books** 关系中的任何书籍集合而言，永远不包含重复值。由于每年会出版许多书籍，我们应该预期，如果我们将书籍添加到关系中，会累积重复的 **year** 值。

        关系可能有多个键。一个常见的例子是公司的员工表。在许多国家，工人必须拥有政府签发的身份证号码。这些号码可以用于唯一标识一名员工。然而，这些号码通常被视为敏感的员工数据，仅应与公司内某些值得信赖的个人共享。在这些情况下，公司会生成一个内部员工 ID 号码，这与政府签发的 ID 完全独立。公司的数据库将包含这两种唯一标识符。

        关系的键也被称为 *候选键(candidate keys)* 。从中选择一个候选键作为关系的 *主键(primary key)* 。其余的键有时称为 *唯一键(unique keys)* 。

        在关系模型中，所有键都被限制为唯一。如果根据某个关系模式（例如，**simple_books** 模式中的相同 **author** 和 **title**）一个元组集合包含某个键的重复值，我们不认为这是该模式的有效关系。

    .. md-tab-item:: 英文

        In many cases, relations may contain subsets of attributes which uniquely identify tuples.  For example, for our **simple_books** relation, we will assert that the pair of attributes **author** and **title** uniquely identify any book in our relation, or any book we might choose to add to our relation in the future.  On the other hand, neither **author** nor **title** are sufficient on their own to uniquely identify a book - it is possible for two different authors to create books with the same name, and of course, many books may have the same author.  We state that the set {**author**, **title**} is a *key* for the **simple_books** relation.

        Keys play an important part in relational theory, as we will see.  One implication that we will explore further in a later chapter is that no two tuples in our **simple_books** relation (now or ever) can share the exact same **author** and **title** values.  In fact, the assertion that no two tuples can share the same **author** and **title** in return implies that **author** and **title** together uniquely identify any book.  The assertions are equivalent.

        It is important to emphasize that the key property is a fact we are stating about the world, not a transitory property of the data in a relation.  For example, our current **simple_books** illustration shows no duplicate values for **year**.  For **year** to be a key, though, requires that **year** never contain duplicates *for any collection of books* we might store in the **simple_books** relation.  Since many books are published every year, we should expect to accumulate duplicate **year** values if we add books to the relation.

        Relations may have more than one key.  A common example is that of a table of employees for a company.  In many countries, workers must have a government issued identification (ID) number.  These numbers can be used to uniquely identify an employee.  However, these numbers are often considered sensitive employee data, which should only be shared with certain trusted individuals in the company.  In these cases, companies will generate an internal employee ID number, which is completely independent of the government issued ID.  The company's database will contain both of these unique identifiers.

        The keys of a relation are also known as *candidate keys*.  One candidate key is chosen as the *primary key* for the relation.  The remaining keys are sometimes called *unique keys*.

        In the relational model, all keys are constrained to be unique.  If a set of tuples contains duplicate values for some key according to some relation schema (e.g., the same **author** and **title** per the **simple_books** schema), we do not consider that a valid relation of the schema.

.. index:: key - relational model; foreign, foreign key - relational model

外键
------------

**Foreign keys**

.. md-tab-set::

    .. md-tab-item:: 中文

        关系数据库不会显式存储相关记录之间的连接。相反，我们必须在一个关系中存储可以用来“查找”另一个关系中相关值的值。在设计良好的关系数据库中，我们几乎总是会存储相关关系的主键的值。存储来自其他关系的键的属性或属性组称为 *外键(foreign key)* 。

        考虑下面表示的关系 **simple_authors**：

        .. image:: authors.svg
            :alt: 关系 simple_authors 的表格说明，其具有姓名、出生日期和死亡日期等属性。

        这个关系的主键是 **name** 属性。名字通常不是一个很好的键选择，因为人们经常与其他人共享相同的名字，但这只是一个简单的示例，并不是良好数据库设计的范例。

        由于 **simple_books** 中的每个 **author** 值都与 **simple_authors** 中某个 **name** 值匹配，我们可以将每本书与其作者的信息联系起来。为了断言在 **simple_books** 中的任何元组都应始终与 **simple_authors** 中的一个元组匹配，我们声明 **simple_books** 的 **author** 属性为一个外键，*引用* **simple_authors** 的 **name** 属性。这个外键约束不仅适用于当前的关系，也适用于 **simple_books** 和 **simple_authors** 的任何未来状态。外键也称为 *引用完整性(referential integrity)* 约束。

        请注意，外键是对两个关系的约束；在任一关系中的某些更改可能导致约束违规。然而，这个约束不是对称的；我们可以在 **simple_authors** 中列出一些作者，而 **simple_books** 中没有列出任何书籍。

    .. md-tab-item:: 英文

        Relational databases do not explicitly store connections between related records.  Instead, we must store values in one relation which we can use to "look up" related values in another relation.  In a properly designed relational database, we will nearly always store values from the primary key of the related relation.  The attribute or group of attributes storing the key from the other relation is called a *foreign key*.

        Consider the relation **simple_authors** represented below:

        .. image:: authors.svg
            :alt: A tabular illustration of the relation simple_authors, which has attributes for name, birth date, and death date.

        Our primary key for this relation is the **name** attribute.  Names are generally not a very good choice for keys, as people often share a name with other people, but this is just a simple illustration and not intended to be an example of good database design.

        Because every **author** value in **simple_books** matches some **name** value in **simple_authors**, we can connect each book to information about its author.  To assert that it should always be true that any tuple in **simple_books** matches a tuple in **simple_authors**, we declare the **author** attribute of **simple_books** to be a foreign key *referencing* the **name** attribute of **simple_authors**.  This foreign key constraint applies not only to the current relations, but to any future states of **simple_books** and **simple_authors**.  Foreign keys are also known as *referential integrity* constraints.

        Note that the foreign key is a constraint on both relations; certain changes in either relation could result in a constraint violation.  The constraint is not symmetric, however; we can have authors listed in **simple_authors** for whom no books are listed in **simple_books**.

.. index:: database; consistency, consistency, inconsistent

一致性
-----------

**Consistency**

.. md-tab-set::

    .. md-tab-item:: 中文

        一个约束被违反的数据库被认为是 *不一致(inconsistent)* 的。关系数据库系统应当强制执行一致性，并防止任何会违反约束的数据修改操作。一致性有助于确保我们从查询中获得良好的答案，或者至少帮助我们避免某些常见问题。例如，保证员工关系中的唯一 ID 值可以防止混淆两个员工的潜在问题，例如向同一个人发放两张工资支票（而另一人则没有发放任何支票）。外键约束可以防止当一个关系中的数据引用另一个关系中不存在的数据时产生无意义的结果。

    .. md-tab-item:: 英文

        A database in which constraints are violated is considered *inconsistent*.  A relational database system is expected to enforce consistency and prevent any data modification operations which would violate constraints.  Consistency helps ensure that we get good answers from our queries, or at least helps us avoid certain common problems.  For example, guaranteeing unique ID values in an employee relation prevents potential issues from confusing two employees, such as issuing two paychecks to the same person (and none to another person).  Foreign key constraints can prevent meaningless results when data in one relation refers to non-existent data in another relation.

修改操作
:::::::::::::::::::::::

**Modification operations**

.. md-tab-set::

    .. md-tab-item:: 中文

        关系模型假设关系可以通过三种操作进行修改：元组可以被添加（插入）到关系中，元组内的值可以在不添加或删除元组的情况下被修改（更新），或者元组可以从关系中被删除（删除）。在修改后，数据库的状态必须与所有约束保持一致，否则操作必须被数据库系统拒绝。在某些情况下（例如存在循环外键关系），可能需要将多个修改组合在一起使用 *事务(transaction)* ；在事务的上下文中，约束可能会暂时被违反，但在所有操作完成后必须解决，否则任何操作都不能生效。

        ..
            （我们将在 :numref:`Chapter {number} <transactions-chapter>` 中讨论事务的常见实现。）

        插入操作可能会违反关系上的主键和唯一键约束，如果被插入的元组包含的值与关系中已存在的另一个元组重复。此外，如果为外键属性提供了一个在引用表中不存在的值，则插入操作也可能违反关系上的外键约束。例如，以下每个元组如果添加到 **simple_books** 关系中（假设以上讨论的主键和外键），都会违反约束：

            (*The House of the Spirits*, Isabel Allende, 1999, history)

            (*A Wizard of Earthsea*, Ursula K. Le Guin, 1968, fantasy)

        在第一个案例中，该作者和书名已经存在于 **simple_books** 关系中。在第二个案例中，作者在 **simple_authors** 关系中不存在。

        另一方面，删除操作永远不会违反主键或唯一键约束。然而，删除一个关系中的元组可能会违反外键约束，如果另一个关系中的外键值引用了被删除的主键。例如，我们不能从 **simple_authors** 中删除以下元组：

            (Ralph Ellison, 1914-03-01, 1994-04-16)

        该作者在 **simple_books** 表中有一本书。

        更新可以引发上述任何约束违反。例如，改变主键值的更新不能更改为与另一个元组的主键重复的值。同样，如果另一个关系中的外键值依赖于被更新的主键值，则该更新不能进行。最后，更新也不能将外键值更改为引用表中不存在的值。

    .. md-tab-item:: 英文

        The relational model assumes that a relation may be modified with one of three operations: tuples may be added (inserted) into the relation, values within tuples may be modified (updated) without adding or removing the tuple, or tuples may be removed (deleted) from the relation.  The state of the database must be consistent with all constraints after modification, or the operation must be rejected by the database system.  In certain cases (such as the existence of a circular foreign key relationship), it may be necessary to group multiple modifications together with a *transaction*; constraints may be temporarily violated within the context of the transaction, but must be resolved when all operations have been completed, or none of the operations may take effect.

        ..
            (We discuss transactions as commonly implemented in :numref:`Chapter {number} <transactions-chapter>`.)

        Insertion operations can violate primary and unique key constraints on a relation if the tuple being inserted contains values that duplicate another tuple already in the relation.  Insertion operations can also violate foreign key constraints on a relation if a value is provided for a foreign key attribute that does not exist in the referenced table.  For example, each of the tuples below would violate constraints if added to the **simple_books** relation (assuming the primary and foreign keys discussed in the text above):

            (*The House of the Spirits*, Isabel Allende, 1999, history)

            (*A Wizard of Earthsea*, Ursula K. Le Guin, 1968, fantasy)

        In the first case, this author and title already exists in the **simple_books** relation.  In the second case, the author is not present in the **simple_authors** relation.

        Deletions, on the other hand, can never violate primary or unique key constraints.  A deletion in one relation can violate a foreign key constraint, however, if a foreign key value in another relation references the deleted key being deleted.  For example, we may not delete from **simple_authors** the tuple:

            (Ralph Ellison, 1914-03-01, 1994-04-16)

        This author has a book in the **simple_books** table.

        Updates can create any of the constraint violations described above.  For example, an update which changes the value of a primary key must not change the value such that it would duplicate another tuple's primary key.  Similarly, if a foreign key value in another relation depends on the primary key value being updated, then the update cannot proceed.  Finally, an update may not change a foreign key value to something which is not in the referenced table.

.. index:: NULL - relational model

NULL
::::

**NULL**

.. md-tab-set::

    .. md-tab-item:: 中文

        在之前显示的 **simple_authors** 关系中，有两个条目没有 **death** 属性的值，因为这两位作者仍然在世。如果我们认为 **death** 属性的域是日历日期的域，那么实际上没有任何值能够准确表示这种情况。相反，我们使用一个特殊的占位符来表示 *信息的缺失*。在关系模型中，这个占位符称为 *NULL* 。

        NULL 的本质，实际上，它在关系模型中的存在，是有争议的。一些数据库学者将 NULL 视为包含在每个域中的特殊值。因此，我们可以说我们在表中为每位在世作者的死亡属性放置了一个 NULL 值。然而，NULL 具有一些特殊属性，使其作为值时存在问题，例如它无法与其他值进行比较，包括其他 NULL 值——稍后将详细讨论。出于这个原因，其他学者更倾向于将 NULL 视为属性的一种特殊 *状态*；我们可以说当作者仍在世时， **death** 属性处于空状态。最后，一些学者完全拒绝 NULL，认为其与关系理论根本不兼容。

        NULL 被创造出来解决的问题是缺失信息的问题。信息可能由于多种原因而未知：可能是没有人知道真实值，或者在将数据输入数据库时被忽略，或者其他多种原因。数据可能是不相关或不适用的，例如在在世作者的 **death** 日期的例子中。研究人员已经确定了许多可以赋予 NULL 的不同含义，这导致一些学者提议使用多个占位符，而不仅仅是一个（尽管其中一些提议是为了强调 NULL 的问题，而不是改善模型）。问题在于，元组的定义要求每个在关系模式中定义的属性都必须关联 *某个东西(something)* ；即使没有任何来自域的适当值，元组也不能简单地是不完整的。

        虽然有替代 NULL 的选项，但这些替代方案本身也存在问题。大多数基于关系模型的数据库系统都支持 NULL。因此，NULL 是我们讨论关系模型时的重要组成部分。

    .. md-tab-item:: 英文

        In the **simple_authors** relation shown earlier, two of the entries show no value for the attribute **death**, which is because those two authors are still living.  If we consider the domain of the **death** attribute to be the domain of calendar dates, then there is truly no value we can choose that accurately represents the situation.  Instead, we are using a special placeholder to represent the *absence of information*.  In the relational model, that placeholder is called *NULL*.

        The nature of NULL, and in fact, its very presence in the relational model, is controversial.  Some database scholars treat NULL as a special value that is included with every domain.  So we can say that we have put a NULL value in our table for the death attribute for each living author.  However, NULL exhibits special properties that make it problematic as a value, such as the fact that it cannot be compared with other values, including other NULLs - more on this in a bit.  For this reason, other scholars prefer to treat NULL as a special *state* of the attribute; we can say that the **death** attribute for an author is in a null state when the author is living.  Finally, some scholars reject NULL entirely as fundamentally incompatible with relational theory.

        The problem NULL was created to solve is the problem of missing information.  Information may be unknown for many reasons: it may be that nobody knows the true value, or it may have been simply overlooked when entering data into the database, or any number of other causes.  Data may be irrelevant or inapplicable, as in the example of the **death** date for living authors.  Researchers have identified many different meanings that can be ascribed to NULL, which has led some scholars to propose additional placeholders instead of just one (although some of those proposals were intended to highlight the problems with NULL, rather than improve the model).  The problem is, the definition of a tuple requires there to be *something* associated with every attribute defined in the relation schema; even if nothing from the domain is appropriate, the tuple cannot simply be incomplete.

        While there are alternatives to the use of NULL, the alternatives are problematic in their own ways.  Most database systems based on the relational model include support for NULL.  For these reasons, NULL is an important part of our discussion of the relational model.

.. index:: three-value logic - relational model

三值逻辑
------------------

**Three-valued logic**

.. md-tab-set::

    .. md-tab-item:: 中文

        对关系的许多操作都利用布尔逻辑和逻辑表达式的常规运算。在布尔逻辑中只有两个值： *真(true)* 和 *假(false)* 。基本的布尔运算符易于理解和应用。NOT 操作简单地反转布尔值: “NOT true” 等于 false ，而 “NOT false” 等于 true [#]_ . 给定两个布尔值 *a* 和 *b*，表达式 “a AND b” 仅当 *a* 和 *b* 都为真时才为真。另一方面，表达式 “a OR b” 仅当 *a* 或 *b* 为真时为真，只有当 *a* 和 *b* 都为假时才为假。

        然而，当 NULL 在大多数表达式中使用时，答案是否为真或假是未知的。例如，表达式 “2 = x”，其中 *x* 被赋值为 NULL（或者说处于空状态，如果你愿意）无法确定为真或假。问题在于，NULL 不是一个独特的值，而是代表信息的完全缺失。因此，我们 *不知道* *x* 是否等于 2 或其他什么。即使是表达式 “x = y”，其中 *x* 和 *y* 都是 NULL，也无法确定为真或假！

        解决方案是通过引入第三个值 *未知* 来增强布尔逻辑，从而形成 *三值逻辑*。由于组合众多，最简单的方法是通过以下表格总结 AND、OR 和 NOT 操作的结果：

        ======== ======== =========== ==========
        *a*      *b*      *a* AND *b* *a* OR *b*
        ======== ======== =========== ==========
        true     true     true        true
        true     false    false       true
        true     unknown  unknown     true
        false    true     false       true
        false    false    false       false
        false    unknown  false       unknown
        unknown  true     unknown     true
        unknown  false    false       unknown
        unknown  unknown  unknown     unknown
        ======== ======== =========== ==========

        ======== =======
        *a*      NOT *a*
        ======== =======
        true     false
        false    true
        unknown  unknown
        ======== =======

        如果应用一些常识，就没有必要记住这些表格。考虑表达式 “a OR b”，让 *b* 为未知。要确定 “a OR b” 的结果，我们只需考虑在不知道 *b* 的值的情况下是否有足够的信息。事实上，如果 *a* 为真，那么 *b* 是真还是假并不重要——结果 “a OR b” 为真。因此 “true OR unknown” 等于 true。另一方面，如果 *a* 为假，那么 *b* 的真假就确实很重要；由于我们不知道，结果 “a OR b” 是未知的。对其他运算可以应用类似的思考过程。

    .. md-tab-item:: 英文

        Many operations on relations make use of Boolean logic and the usual operations on logical expressions.  There are only two values in Boolean logic: *true* and *false* .  The basic Boolean operators are easy to understand and apply.  The NOT operation simply inverts the Boolean value: "NOT true" equals false, and "NOT false" equals true [#]_.  Given two Boolean values, *a* and *b*, the expression "a AND b" yields true if and only if *a* is true and *b* is true.  On the other hand, the expression "a OR b" is true if *a* is true or *b* is true, and is false only if both *a* and *b* are false.

        However, when NULL is used in most expressions, it is unknown whether the answer is true or false.  For example, the expression "2 = x", where *x* is assigned NULL (or is in the null state, if you prefer) cannot be determined to be true or false.  The problem is that NULL is not a distinct value of its own, but represents the absence of information altogether.  Thus, we *do not know* if *x* equals 2 or something else.  Even the expression "x = y", where both *x* and *y* are NULL cannot be determined to be true or false!

        The solution is to enhance Boolean logic with a third value, *unknown*, giving a *three-valued logic*.  With so many combinations, it is easiest to summarize the results of AND, OR, and NOT operations with the following tables:

        ======== ======== =========== ==========
        *a*      *b*      *a* AND *b* *a* OR *b*
        ======== ======== =========== ==========
        true     true     true        true
        true     false    false       true
        true     unknown  unknown     true
        false    true     false       true
        false    false    false       false
        false    unknown  false       unknown
        unknown  true     unknown     true
        unknown  false    false       unknown
        unknown  unknown  unknown     unknown
        ======== ======== =========== ==========

        ======== =======
        *a*      NOT *a*
        ======== =======
        true     false
        false    true
        unknown  unknown
        ======== =======

        It is not necessary to memorize these tables, if some common sense is applied.  Consider the expression "a OR b", and let *b* be unknown.  To determine the result of "a OR b", we simply need to consider whether or not we have enough information without knowing the value of *b*.  In fact, if *a* is true, it does not matter if *b* is true or false - the result "a OR b" is true.  Thus "true OR unknown" equals true.  On the other hand, if *a* is false, then it really does matter whether *b* is true or false; since we don't know, the result "a OR b" is unknown.  A similar thought process can be applied to the other operations.

约束和 NULL
--------------------

**Constraints and NULL**

.. md-tab-set::

    .. md-tab-item:: 中文

        在我们的模型中引入 NULL 后，我们必须对关于约束的规则进行一些小调整。首先，我们必须进一步限制所有主键属性，确保其永远不为 NULL。请记住，主键应该是关系中元组的标识符，每个元组都必须有一个唯一的主键值。然而，如果某个元组的任何主键属性中存在 NULL，就无法搜索和找到该元组——任何尝试将主键与查找值进行比较的操作都会返回未知结果。我们同样无法正确执行唯一性约束，因为无法将包含主键为 NULL 的元组与其他元组进行比较，以确定它们是否不同。

        其次，我们修改外键的规则。新规则是外键可以为 NULL，其他情况下必须匹配引用表中的某个值。允许外键为 NULL 可能看起来令人惊讶，但考虑到我们的示例关系，我们如何处理作者未知（匿名）的书籍呢？如果不允许作者为 NULL，那么在 **simple_authors** 表中没有相应记录的情况下，我们无法将书籍添加到 **simple_books** 中。然而，对于未知作者， **simple_authors** 表中的记录又意味着什么呢？（请注意，由于主键的原因，我们不能在 **simple_authors** 中为作者的名称设置 NULL。）虽然有多种方法可以解决这个问题，但允许作者为 NULL 是一种可能的解决方案。

    .. md-tab-item:: 英文

        With NULL in our model, we must make some small adjustments to our rules regarding constraints.  First, we must further constrain all primary key attributes to never be NULL.  Remember that a primary key should be an identifier for tuples in a relation, and every tuple must have a unique primary key value.  However, if NULL is present in any primary key attribute for some tuple, it is impossible to search for and find the tuple - any attempt to compare the primary key with a lookup value gives an unknown result.  We likewise cannot properly enforce uniqueness, because we cannot compare a tuple with NULL in the primary key with other tuples to determine if they are distinct from one another.

        Second, we modify the rule for a foreign key.  The new rule is that a foreign key may be NULL, otherwise it must match a value in the referenced table.  Allowing NULL in a foreign key may seem surprising, but considering our example relations, how might we handle a book for whom the author is unknown (anonymous)?  If NULL is not allowed for the author, then we cannot add the book to **simple_books** without some matching record in the **simple_authors** table.  However, what is the meaning of a record in the **simple_authors** table for an unknown author?  (Note also we cannot have a NULL name for the author in **simple_authors** due to the primary key.)  While there are multiple ways to approach this problem, allowing NULL for the author is one possible solution.


自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文

        本节包含一些问题，您可以用来检查对关系数据库模型的理解。

        - 将术语拖动到其匹配的定义。

          - 集合
          - 关系
          - 属性
          - 域
          - 关系模式

          ----

          - 元组的命名属性
          - 一组不同的值
          - 属性值所属的值的集合
          - 关系的属性和域的定义
          - 来自同一域的一组元组

        .. admonition:: 显示答案
            :class: dropdown

            - 集合 <-> 一组不同的值
            - 关系 <-> 来自同一域的一组元组
            - 属性 <-> 元组的命名属性
            - 域 <-> 属性值所属的值的集合
            - 关系模式 <-> 关系的属性和域的定义

        - 在关系模型中，*元组*的定义是什么？

          - 一组有序的值；元组中的每个位置都与一个域相关联。
          - 与命名属性相关联的一组值；每个属性都与一个域相关联。
          - 上述定义中的任一个或两者都可以使用，具体取决于上下文。

        .. admonition:: 显示答案
            :class: dropdown

            - 一组有序的值；元组中的每个位置都与一个域相关联。

                - 这是一个定义。

            - 与命名属性相关联的一组值；每个属性都与一个域相关联。

                - 这是一个定义。

            - 上述定义中的任一个或两者都可以使用，具体取决于上下文。

                + 正确。

        - 哪一个最能描述关系？

          - 按主键值排序的一组元组。每个元组必须唯一，并具有相同数量和类型的属性。
          - 没有特定顺序的一组元组。每个元组必须唯一，并具有相同数量和类型的属性。
          - 没有特定顺序的一组元组，可能有重复。每个元组必须具有相同数量和类型的属性。
          - 没有特定顺序的一组元组。每个元组必须唯一。每个元组都有自己的属性，可能在元组之间有所不同。

        .. admonition:: 显示答案
            :class: dropdown

            - 按主键值排序的一组元组。每个元组必须唯一，并具有相同数量和类型的属性。

                - 关系没有内在排序。

            - 没有特定顺序的一组元组。每个元组必须唯一，并具有相同数量和类型的属性。

                + 正确。

            - 没有特定顺序的一组元组，可能有重复。每个元组必须具有相同数量和类型的属性。

                - 关系中的元组必须是不同的，即不能有重复的元组。

            - 没有特定顺序的一组元组。每个元组必须唯一。每个元组都有自己的属性，可能在元组之间有所不同。

                - 关系中的元组必须来自同一元组域；即每个元组在属性和相关域的定义上是相同的。

        接下来的四个问题与下面的两个关系有关，这些关系将 ISO（国际标准化组织）国家代码映射到国家名称和 ISO 货币代码，以及货币代码映射到货币名称。**countries** 的主键是 **country_code**，**currencies** 的主键是 **currency_code**。**countries** 中的 **principal_currency_code** 列是一个外键，引用 **currencies** 中的 **currency_code**。显然，由于空间原因，这代表了可用数据的一个子集。

        .. image:: countries.svg
            :alt: 显示国家关系的元组的表格。列出的国家有澳大利亚（AU）、索马里（SO）、泰国（TH）、墨西哥（MX）、基里巴斯（KI）和丹麦（DK）。

        .. image:: currencies.svg
            :alt: 显示货币关系的元组的表格。列出的货币有墨西哥比索（MXN）、澳大利亚元（AUD，澳大利亚和基里巴斯使用）、丹麦克朗（DKK）、泰铢（THB）和索马里先令（SOS）。

        - 如果我们将元组 (DK, Danmark, DKK) 插入 **countries** 关系，将会违反什么约束？

          - **countries** 关系上的主键。
          - **countries** 关系上的主键和 **principal_currency_code** 的外键约束。
          - **principal_currency_code** 的外键约束。
          - 不会违反任何约束。

        .. admonition:: 显示答案
            :class: dropdown

            - **countries** 关系上的主键。

                + 正确。

            - **countries** 关系上的主键和 **principal_currency_code** 的外键约束。

                - DKK 是 **currencies** 关系中的货币代码。

            - **principal_currency_code** 的外键约束。

                - DKK 是 **currencies** 关系中的货币代码。

            - 不会违反任何约束。

                - 错误。

        - 如果我们从 **countries** 关系中删除元组 (AU, Australia, AUD)，将违反什么约束？

          - **countries** 关系上的主键。
          - **countries** 关系上的主键和 **principal_currency_code** 的外键约束。
          - **principal_currency_code** 的外键约束。
          - 不会违反任何约束。

        .. admonition:: 显示答案
            :class: dropdown

            - **countries** 关系上的主键。

                - 不，**country_code** 列仍将包含唯一的、非空的条目。

            - **countries** 关系上的主键和 **principal_currency_code** 的外键约束。

                - 不，**country_code** 列仍将包含唯一的、非空的条目，并且所有 **principal_currency_code** 值仍与 **currencies** 关系中的值匹配。

            - **principal_currency_code** 的外键约束。

                - 不，所有 **principal_currency_code** 值仍与 **currencies** 关系中的值匹配。

            - 不会违反任何约束。

                + 正确。

        - 如果我们从 **currencies** 关系中删除元组 (THB, Baht)，将违反什么约束？

          - **currencies** 关系上的主键。
          - **currencies** 关系上的主键和 **principal_currency_code** 的外键约束。
          - **principal_currency_code** 的外键约束。
          - 不会违反任何约束。

        .. admonition:: 显示答案
            :class: dropdown

            - **currencies** 关系上的主键。

                - 不，**currency_code** 列仍将包含唯一的、非空的条目。

            - **currencies** 关系上的主键和 **principal_currency_code** 的外键约束。

                - 不，**currency_code** 列仍将包含唯一的、非空的条目。

            - **principal_currency_code** 的外键约束。

                + 正确。**countries** 中泰国的条目将有一个 **principal_currency_code**，该值在 **currencies** 关系中没有匹配项。

            - 不会违反任何约束。

                - 错误。

        - 如果我们将元组 (ARS, Argentine Peso) 插入 **currencies** 关系，将违反什么约束？

          - **currencies** 关系上的主键。
          - **currencies** 关系上的主键和 **principal_currency_code** 的外键约束。
          - **principal_currency_code** 的外键约束。
          - 不会违反任何约束。

        .. admonition:: 显示答案
            :class: dropdown

            - **currencies** 关系上的主键。

                - 不，ARS 与之前表中的货币代码不同。

            - **currencies** 关系上的主键和 **principal_currency_code** 的外键约束。

                - 不，ARS 与之前表中的货币代码不同，并且外键约束 **principal_currency_code** 的值必须在 **currencies** 的 **currency_code** 列中，但反之则不然。

            - **principal_currency_code** 的外键约束。

                - 不，外键约束 **principal_currency_code** 的值必须在 **currencies** 的 **currency_code** 列中，但反之则不然。

            - 不会违反任何约束。

                + 正确。

        - 如果我们将元组 (AQ, Antarctica, NULL) 插入 **countries** 关系，将违反什么约束？（是的，南极洲在技术上并不是一个国家，但他们确实有 ISO 国家代码。）

          - **countries** 关系上的主键。
          - **countries** 关系上的主键和 **principal_currency_code** 的外键约束。
          - **principal_currency_code** 的外键约束。
          - 不会违反任何约束。

        .. admonition:: 显示答案
            :class: dropdown

            - **countries** 关系上的主键。

                - 不，AQ 与之前表中的国家代码不同。

            - **countries** 关系上的主键和 **principal_currency_code** 的外键约束。

                - 不，AQ 与之前表中的国家代码不同。**principal_currency_code** 的值为 NULL，这是外键定义下允许的。

            - **principal_currency_code** 的外键约束。

                - 不，**principal_currency_code** 的值为 NULL，这是外键定义下允许的。

            - 不会违反任何约束。

                + 正确。

        - 如果我们将 **currencies** 中的元组 (AUD, Australian Dollar) 修改为 (DKK, Australian Dollar)，将违反什么约束？

          - **currencies** 关系上的主键。
          - **currencies** 关系上的主键和 **principal_currency_code** 的外键约束。
          - **principal_currency_code** 的外键约束。
          - 不会违反任何约束。

        .. admonition:: 显示答案
            :class: dropdown

            - **currencies** 关系上的主键。

                - 正确，但是否可能违反其他约束？

            - **currencies** 关系上的主键和 **principal_currency_code** 的外键约束。

                + 正确。DKK 重复了 **currencies** 中的现有货币代码，并且该更改还会将 AUD 从货币列表中移除，而 AUD 被 **countries** 中的两个行引用。

            - **principal_currency_code** 的外键约束。

                - 正确，但是否可能违反其他约束？

            - 不会违反任何约束。

                - 错误。

        - 将表达式拖到其求值结果。

          - true AND unknown
          - true OR unknown
          - false AND true
        
          ----

          - unknown
          - true
          - false

        .. admonition:: 显示答案
            :class: dropdown

            - true AND unknown <-> unknown
            - true OR unknown <-> true
            - false AND true <-> false

        - 将表达式拖到其求值结果。

          - NOT false
          - unknown AND false
          - false OR unknown

          ----

          - true
          - false
          - unknown

        .. admonition:: 显示答案
            :class: dropdown

            - NOT false <-> true
            - unknown AND false <-> false
            - false OR unknown <-> unknown

    .. md-tab-item:: 英文

        This section has some questions you can use to check your understanding of the relational model of the database.

        - Drag the term to its matching definition.

          - set
          - relation
          - attribute
          - domain
          - relation schema

          ----

          - A named property of a tuple
          - A collection of distinct values
          - A set of values which attribute values belong to
          - A definition of the attributes and domains of a relation
          - A set of tuples from the same domain

        .. admonition:: Show answer
            :class: dropdown

            - set <-> A collection of distinct values
            - relation <-> A set of tuples from the same domain
            - attribute <-> A named property of a tuple
            - domain <-> A set of values which attribute values belong to
            - relation schema <-> A definition of the attributes and domains of a relation

        - What is the definition of *tuple* as used in the relational model?

          - An ordered collection of values; each position in the tuple is associated with a domain.
          - A set of values associated with a named attribute; each attribute is associated with a domain.
          - Either or both of the above definitions may be used, depending on the context.

        .. admonition:: Show answer
            :class: dropdown

            -   An ordered collection of values; each position in the tuple is associated with a domain.

                - This is one definition.

            -   A set of values associated with a named attribute; each attribute is associated with a domain.

                - This is one definition.

            -   Either or both of the above definitions may be used, depending on the context.

                + Correct.

        - Which of these best describes a relation?

          - A collection of tuples in order by primary key value.  Each tuple must be unique and have the same number and types of attributes.
          - A collection of tuples in no particular order.  Each tuple must be unique and have the same number and types of attributes.
          - A collection of tuples in no particular order, possibly with duplicates.  Each tuple must have the same number and types of attributes.
          - A collection of tuples in no particular order.  Each tuple must be unique.  Each tuple has its own attributes, which may differ from tuple to tuple.

        .. admonition:: Show answer
            :class: dropdown

            -   A collection of tuples in order by primary key value.  Each tuple must be unique and have the same number and types of attributes.

                - Relations have no intrinsic ordering.

            -   A collection of tuples in no particular order.  Each tuple must be unique and have the same number and types of attributes.

                + Correct.

            -   A collection of tuples in no particular order, possibly with duplicates.  Each tuple must have the same number and types of attributes.

                - Tuples in a relation must be distinct, that is, there cannot be duplicate tuples.

            -   A collection of tuples in no particular order.  Each tuple must be unique.  Each tuple has its own attributes, which may differ from tuple to tuple.

                - Tuples in a relation must come from the same domain of tuples; that is, each tuple shares the same definition in terms of attributes and associated domains.

        The next four questions concern the two relations pictured below, which map ISO (International Organization for Standardization) country codes to country names and ISO currency codes, and currency codes to the name of the currency.  The primary key for **countries** is **country_code**, and the primary key for **currencies** is **currency_code**.  The **principal_currency_code** column in **countries** is a foreign key referencing **currency_code** in **currencies**.  Obviously this represents a subset of available data, for space reasons.

        .. image:: countries.svg
            :alt: A table showing tuples for the countries relation.  The countries listed are Australia (AU), Somalia (SO), Thailand (TH), Mexico (MX), Kiribati (KI), and Denmark (DK).

        .. image:: currencies.svg
            :alt: A table showing tuples for the currencies relation.  The currencies listed are the Mexican Peso (MXN), Australian Dollar (AUD, used by Australia and Kiribati), the Danish Krone (DKK), the Thai Baht (THB), and the Somali Shilling (SOS).


        - What constraint or constraints would be violated if we insert the tuple (DK, Danmark, DKK) into the **countries** relation?

          - Primary key on the **countries** relation.
          - Primary key on the **countries** relation and the foreign key constraint on **principal_currency_code**.
          - Foreign key constraint on **principal_currency_code**.
          - No constraints would be violated.

        .. admonition:: Show answer
            :class: dropdown

            -   Primary key on the **countries** relation.

                + Correct.

            -   Primary key on the **countries** relation and the foreign key constraint on **principal_currency_code**.

                - DKK is a currency code in the **currencies** relation.

            -   Foreign key constraint on **principal_currency_code**.

                - DKK is a currency code in the **currencies** relation.

            -   No constraints would be violated.

                - Incorrect.

        - What constraint or constraints would be violated if we delete the tuple (AU, Australia, AUD) from the **countries** relation?

          - Primary key on the **countries** relation.
          - Primary key on the **countries** relation and the foreign key constraint on **principal_currency_code**.
          - Foreign key constraint on **principal_currency_code**.
          - No constraints would be violated.

        .. admonition:: Show answer
            :class: dropdown

            -   Primary key on the **countries** relation.

                - No, the **country_code** column will still contain unique, non-null entries.

            -   Primary key on the **countries** relation and the foreign key constraint on **principal_currency_code**.

                - No, the **country_code** column will still contain unique, non-null entries, and all **principal_currency_code** values still match values in the **currencies** relation.

            -   Foreign key constraint on **principal_currency_code**.

                - No, all **principal_currency_code** values still match values in the **currencies** relation.

            -   No constraints would be violated.

                + Correct.

        - What constraint or constraints would be violated if we delete the tuple (THB, Baht) from the **currencies** relation?

          - Primary key on the **currencies** relation.
          - Primary key on the **currencies** relation and the foreign key constraint on **principal_currency_code**.
          - Foreign key constraint on **principal_currency_code**.
          - No constraints would be violated.

        .. admonition:: Show answer
            :class: dropdown

            -   Primary key on the **currencies** relation.

                - No, the **currency_code** column will still contain unique, non-null entries.

            -   Primary key on the **currencies** relation and the foreign key constraint on **principal_currency_code**.

                - No, the **currency_code** column will still contain unique, non-null entries.

            -   Foreign key constraint on **principal_currency_code**.

                + Correct.  The entry for Thailand in **countries** will have a **principal_currency_code** that is not matched by anything in the **currencies** relation.

            -   No constraints would be violated.

                - Incorrect.

        - What constraint or constraints would be violated if we insert the tuple (ARS, Argentine Peso) into the **currencies** relation?

          - Primary key on the **currencies** relation.
          - Primary key on the **currencies** relation and the foreign key constraint on **principal_currency_code**.
          - Foreign key constraint on **principal_currency_code**.
          - No constraints would be violated.

        .. admonition:: Show answer
            :class: dropdown

            -   Primary key on the **currencies** relation.

                - No, ARS is distinct from the currency codes previously in the table.

            -   Primary key on the **currencies** relation and the foreign key constraint on **principal_currency_code**.

                - No, ARS is distinct from the currency codes previously in the table, and the foreign key constrains **principal_currency_code** values to be in the **currency_code** column of **currencies**, but not vice-versa.

            -   Foreign key constraint on **principal_currency_code**.

                - No, the foreign key constrains **principal_currency_code** values to be in the **currency_code** column of **currencies**, but not vice-versa.

            -   No constraints would be violated.

                + Correct.


        - What constraint or constraints would be violated if we insert the tuple (AQ, Antarctica, NULL) into the **countries** relation?  (Yes, Antarctica is technically not a country, but they do have an ISO country code.)

          - Primary key on the **countries** relation.
          - Primary key on the **countries** relation and the foreign key constraint on **principal_currency_code**.
          - Foreign key constraint on **principal_currency_code**.
          - No constraints would be violated.

        .. admonition:: Show answer
            :class: dropdown

            -   Primary key on the **countries** relation.

                - No, AQ is distinct from the country codes previously in the table.

            -   Primary key on the **countries** relation and the foreign key constraint on **principal_currency_code**.

                - No, AQ is distinct from the country codes previously in the table.  The **principal_currency_code** value is NULL, which is allowed under the definition of a foreign key.

            -   Foreign key constraint on **principal_currency_code**.

                - No, the **principal_currency_code** value is NULL, which is allowed under the definition of a foreign key.

            -   No constraints would be violated.

                + Correct.

        - What constraint or constraints would be violated if we modify the tuple (AUD, Australian Dollar) in **currencies** to be (DKK, Australian Dollar)?

          - Primary key on the **currencies** relation.
          - Primary key on the **currencies** relation and the foreign key constraint on **principal_currency_code**.
          - Foreign key constraint on **principal_currency_code**.
          - No constraints would be violated.

        .. admonition:: Show answer
            :class: dropdown

            -   Primary key on the **currencies** relation.

                - True, but might another constraint be violated?

            -   Primary key on the **currencies** relation and the foreign key constraint on **principal_currency_code**.

                + Correct.  DKK duplicates an existing currency code in **currencies**, and the change would also remove AUD from the list of currencies, which is referenced by two rows in **countries**.

            -   Foreign key constraint on **principal_currency_code**.

                - True, but might another constraint be violated?

            -   No constraints would be violated.

                - Incorrect.

        - Drag the expression to the outcome of its evaluation.

          - true AND unknown
          - true OR unknown
          - false AND true
        
          ----

          - unknown
          - true
          - false

        .. admonition:: Show answer
            :class: dropdown

            - true AND unknown <-> unknown
            - true OR unknown <-> true
            - false AND true <-> false

        - Drag the expression to the outcome of its evaluation.

          - NOT false
          - unknown AND false
          - false OR unknown

          ----

          - true
          - false
          - unknown

        .. admonition:: Show answer
            :class: dropdown

            - NOT false <-> true
            - unknown AND false <-> false
            - false OR unknown <-> unknown

----

**Notes**

.. [#] There are many notations for Boolean logic operators.  For simplicity, we will simply use NOT, AND, and OR instead of more compact notation.


