.. _normalization-chapter:

=============
常规化
=============

.. index:: normalization

.. md-tab-set::

    .. md-tab-item:: 中文

        在本章中，我们将讨论数据库结构的一些方面——我们应该使用什么关系模式来存储数据？虽然本章的内容深深植根于关系数据库理论，但基本概念无需理论基础即可理解，并且对所有数据库从业者都很重要。如果您在阅读本章时没有阅读过有关数据库关系模型的前面章节，请注意我们在讨论数据库中的对象时使用了术语关系、属性和元组；这些术语与关系数据库系统中的术语表、列和行非常相似。

    .. md-tab-item:: 英文

        In this chapter we discuss some aspects of how a database is structured - what relation schemas should we use to store our data?  While the material in this chapter is deeply rooted in relational database theory, the basic concepts can be understood without the theoretical foundation, and are important for all database practitioners.  If you are reading this chapter without having read earlier chapters on the relational model of the database, note we use the terms relation, attribute, and tuple in discussing the objects in our database; these terms closely correspond to the terms table, column, and row in relational database systems.

简介
::::::::::::

*Introduction*

.. index:: redundancy

.. md-tab-set::

    .. md-tab-item:: 中文

        规范化是修改数据库结构以满足某些要求的过程。这些要求由一系列 *范式* 定义，我们将很快对其进行定义。

        规范化的主要目标是使维护正确的数据集合变得更容易。正确的数据是完整且自洽的。数据库不应包含与我们所理解的事实相矛盾的数据。

        有一些线索可以表明数据库容易受到常见数据损坏的影响。一个非常重要的线索是数据库表现出冗余，即相同的事实被记录多次。另一个线索是数据库在许多地方包含 NULL。当关系中存在这些问题时，通常也是关系做了太多事情的情况。当关系包含与单个事物或概念相关的数据时，效果最好。但有时很难检测到关系做了太多事情，这就是为什么冗余和过多的 NULL 是如此有用的线索。

    .. md-tab-item:: 英文

        Normalization is the process of modifying a database structure to meet certain requirements. These requirements are defined by a series of *normal forms*, which we will define shortly.

        A primary goal of normalization is to make it easier to maintain a correct collection of data.  Correct data is complete and self-consistent.  The database should not contain data contradicting what we understand to be true.

        There are a few clues that can indicate a database is susceptible to common kinds of data corruption.  A very big clue is when a database exhibits redundancy, that is, when the same facts are recorded multiple times.  Another clue is when the database contains NULL in many places.  When these issues are present in a relation, it is usually also the case that the relation is doing too many things.  Relations work best when they contain data regarding a single thing or concept.  It can sometimes be difficult to detect that a relation is doing too much, though, which is why redundancy and excessive NULLs are such useful clues. 

.. index:: modification anomaly

修改异常
----------------------

*Modification anomalies*

.. md-tab-set::

    .. md-tab-item:: 中文

        有三种常见的错误类型，我们可以考虑这些错误以更好地理解规范化的必要性。每一种 *修改异常* 都源于我们可用的数据修改操作：插入、更新和删除。我们可以用下面所示的关系来说明每一种，这个关系列出了一个虚构学校中一些课程和教师的信息。该关系提供了课程名称、开始时间、教室号码、讲师姓名、讲师办公室号码和讲师部门。我们应该立即关注的是，该关系中包含有关 *课程* 和 *讲师* 的信息。

        .. table:: **课程**
            :class: lined-table

            ==================== ===== ========= =========== ====== ==========
            课程名称             时间  教室      讲师        办公室 部门
            ==================== ===== ========= =========== ====== ==========
            代数 I               8:00  C01       Mr. Reyes   B24    数学
            几何                 10:00 C01       Mr. Reyes   B24    数学
            世界历史             9:00  C15       Ms. Tan     A11    人文学科
            英语文学             10:00 C09       Ms. Larsen  A05    人文学科
            物理                 11:00 C06       Ms. Musa    B22    科学
            化学                 13:00 C17       Ms. Musa    B22    科学
            音乐                 9:00  C25       Mr. Pal     A03    人文学科
            ==================== ===== ========= =========== ====== ==========

        该关系还表现出冗余。例如，我们多次得知Reyes先生在数学系且他的办公室在124号房间。请注意，Reyes先生多次出现本身并不是冗余，因为每次出现都是一个新事实: Reyes先生教授代数 I，Reyes先生教授几何。这个例子中没有NULL，但我们将很快看到在添加或删除数据时它们可能出现。

        ==================== ===== ========= =========== ====== ==========
        课程名称               时间   教室       讲师        办公室  部门
        ==================== ===== ========= =========== ====== ==========
        代数 I                8:00   C01       Reyes 先生   B24    数学
        几何                  10:00  C01       Reyes 先生   B24    数学
        世界历史               9:00   C15       Tan 女士     A11    人文学科
        英语文学               10:00  C09       Larsen 女士  A05    人文学科
        物理                  11:00  C06       Musa 女士    B22    科学
        化学                  13:00  C17       Musa 女士    B22    科学
        音乐                  9:00   C25       Pal 先生     A03    人文学科
        ==================== =====  ========= =========== ====== ==========

    .. md-tab-item:: 英文

        There are three common types of errors that we can consider to better understand the need for normalization.  Each of these *modification anomalies* arise from one of the data modification operations available to us: insert, update, and delete.  We can illustrate each of these with the relation pictured below, which lists information about some classes and teachers at a fictional school.  The relation gives the class name, starting time, room number, instructor name, instructor office number, and instructor department.  Right away, we should be concerned that there is information in the relation about both *classes* and *instructors*.

        .. table:: **classes**
            :class: lined-table

            ==================== ===== ========= =========== ====== ==========
            class_name           time  classroom instructor  office department
            ==================== ===== ========= =========== ====== ==========
            Algebra I            8:00  C01       Mr. Reyes   B24    Math
            Geometry             10:00 C01       Mr. Reyes   B24    Math
            World History        9:00  C15       Ms. Tan     A11    Humanities
            English Literature   10:00 C09       Ms. Larsen  A05    Humanities
            Physics              11:00 C06       Ms. Musa    B22    Science
            Chemistry            13:00 C17       Ms. Musa    B22    Science
            Music                9:00  C25       Mr. Pal     A03    Humanities
            ==================== ===== ========= =========== ====== ==========

        This relation also exhibits redundancy.  We are given the facts that Mr. Reyes is in the Math department and his office is in room 124 multiple times, for example.  Note that Mr. Reyes appearing multiple times is not itself redundancy, as each appearance is a new fact: Mr. Reyes teaches Algebra I, and Mr. Reyes teaches Geometry.  We do not have any NULLs in this example, but we will see shortly how they might appear when we add or remove data.

.. index:: insert anomaly

插入异常
##############

*Insert anomaly*

.. md-tab-set::

    .. md-tab-item:: 中文

        考虑一下当一位新讲师加入学校教职员工时会发生什么。Hassan先生是数学系的新教职员工，但他尚未被分配任何课程进行教学。我们应该如何将Hassan先生添加到数据库中？有几个选项，但没有一个是好的——无论我们怎么做，我们必须在新元组中为 **课程名称** 、 **教室** 和 **时间** 提供值。我们可能会认为对于这些属性NULL是最佳选择，因为否则我们必须创建虚假的课程信息。不管怎样，我们都在为自己将来的工作制造麻烦——我们的数据库现在包含一个必须以特殊方式处理的元组，这与关系中的其他元组不同。

    .. md-tab-item:: 英文

        Consider what happens when a new instructor joins the faculty at the school.  Mr. Hassan is a new faculty member in the department of Math, but he has not yet been assigned any classes to teach.  How should we add Mr. Hassan to the database?  There are a few options, but none of them are good - whatever we do, we must provide values for **class_name**, **classroom**, and **time** in our new tuple.  We might think that NULL is the best choice for each of these attributes, as otherwise we must create fake class information.  Either way, we are making trouble for ourselves later on - our database now contains a tuple that must be handled in a special fashion, different from the other tuples in the relation.

.. index:: delete anomaly

删除异常
##############

*Delete anomaly*

.. md-tab-set::

    .. md-tab-item:: 中文

        现在，考虑一下当Tan女士在另一所学校找到工作时会发生什么。如果我们不谨慎，就会删除Tan女士的元组——从我们的课程列表中完全移除世界历史。同样，我们不能在不删除所有关于Larsen女士信息的情况下，从课程列表中移除英语文学。避免当前数据库设计中这些问题的唯一方法是用NULL替换现有值。与插入异常示例一样，这使我们面临需要特殊处理的元组。

    .. md-tab-item:: 英文

        Now, consider what happens when Ms. Tan takes a job at another school.  If we are incautious, we will delete the tuple for Ms. Tan - removing World History from our list of classes altogether.  Similarly, we cannot remove English Literature from the list of classes without removing all information about Ms. Larsen.  The only way to avoid these issues with our current database design is to replace the existing values with NULLs.  As with the insert anomaly example, this leaves us with tuples that require special handling.

.. index:: update anomaly

更新异常
##############

*Update anomaly*

.. md-tab-set::

    .. md-tab-item:: 中文

        更新异常是我们数据库冗余的直接结果。考虑一下当Reyes先生更换办公室时会发生什么。如果我们不谨慎，就会更新列出Reyes先生教授代数 I 的元组，但忘记更新几何的元组，从而导致我们的数据内部不一致。Reyes先生将被列为拥有两个不同的办公室，而没有任何指示哪个是正确的。为了避免麻烦，我们必须始终记得更新 *所有* Reyes先生作为讲师的课程。

    .. md-tab-item:: 英文

        Update anomalies are a direct consequence of the redundancy in our database.  Consider what happens when Mr. Reyes changes offices.  If we are incautious, we will update the tuple listing Mr. Reyes as the teacher of Algebra I, but forget to update the tuple for Geometry, leaving our data internally consistent.  Mr. Reyes will be listed as having two different offices, without any indication which is correct.  To avoid trouble, we must remember to always update *all* classes for which Mr. Reyes is the instructor.

示例解决方案
----------------

*Example solution*

.. md-tab-set::

    .. md-tab-item:: 中文

        对 **课程** 关系进行规范化将防止上述每种情况的发生。实际上，规范化要求我们构造关系，使数据以非常简单和一致的形式表达。我们通常通过将关系 *分解* 为多个较小的关系来实现规范化。

        非正式地说，在一个规范化的关系中，某个事物或概念通过由一个或多个属性组成的主键唯一标识，而每个其他属性仅代表该事物或概念的 *单值* 事实。对于我们的例子， **课程** 关系描述了课程；它以 **课程名称** 作为主键， **教室** 、 **时间** 和 **讲师** 作为单值属性。（一个不是单值属性的例子是课程中的学生名单。我们称这样的属性为 *多值* 属性。）然而， **办公室** 和 **部门** 实际上并不是关于课程的事实；相反，它们是关于讲师的事实。这些扩展的事实需要通过对 **课程** 关系的 *分解* 移除到另一个关系中：

        .. table:: **课程**
            :class: lined-table

            ==================== ===== ========= ===========
            课程名称             时间  教室      讲师
            ==================== ===== ========= ===========
            代数 I               8:00  C01       Mr. Reyes
            几何                 10:00 C01       Mr. Reyes
            世界历史             9:00  C15       Ms. Tan
            英语文学             10:00 C09       Ms. Larsen
            物理                 11:00 C06       Ms. Musa
            化学                 13:00 C17       Ms. Musa
            音乐                 9:00  C25       Mr. Pal
            ==================== ===== ========= ===========

        .. table:: **讲师**
            :class: lined-table

            =========== ====== ==========
            姓名        办公室 部门
            =========== ====== ==========
            Reyes 先生   B24    数学
            Tan 女士     A11    人文学科
            Larsen 女士  A05    人文学科
            Musa 女士    B22    科学
            Pal 先生     A03    人文学科
            =========== ====== ==========

        请注意，我们通过这种分解消除了冗余。如果我们需要更新某个讲师的办公室信息，只需更新一个元组。我们也不再需要担心修改异常。添加或删除讲师与添加或删除课程完全独立；这也消除了在 **课程** 关系中需要过多NULL的必要性 [#]_ .

        ==================== ===== ========= ===========
        课程名称               时间  教室      讲师
        ==================== ===== ========= ===========
        代数 I                 8:00  C01       Reyes 先生
        几何                10:00 C01       Reyes 先生
        世界历史            9:00  C15       Tan 女士
        英语文学            10:00 C09       Larsen 女士
        物理                11:00 C06       Musa 女士
        化学                13:00 C17       Musa 女士
        音乐                9:00  C25       Pal 先生
        ==================== ===== ========= ===========

    .. md-tab-item:: 英文

        Normalizing the **classes** relation will prevent each of the situations above.  In effect, normalization requires us to structure relations such that the data is expressed in a very simple and consistent form.  We typically achieve normalization by *decomposing* a relation into multiple smaller relations.

        Informally, in a normalized relation, some thing or concept is uniquely identified by a primary key composed of one or more attributes and every other attribute represents a *single-valued* fact about the thing or concept only. For our example, the **classes** relation describes classes; it has **class_name** as a primary key, and **classroom**, **time**, and **instructor** as single-valued attributes.  (An example of an attribute that is not single-valued would be a list of students in the class.  We call such an attribute *multi-valued*.)  However, **office** and **department** are not really facts about a class; instead, they are facts about instructors.  These extended facts need to be removed to another relation through *decomposition* of the **classes** relation:

        .. table:: **classes**
            :class: lined-table

            ==================== ===== ========= ===========
            class_name           time  classroom instructor
            ==================== ===== ========= ===========
            Algebra I            8:00  C01       Mr. Reyes
            Geometry             10:00 C01       Mr. Reyes
            World History        9:00  C15       Ms. Tan
            English Literature   10:00 C09       Ms. Larsen
            Physics              11:00 C06       Ms. Musa
            Chemistry            13:00 C17       Ms. Musa
            Music                9:00  C25       Mr. Pal
            ==================== ===== ========= ===========

        .. table:: **instructors**
            :class: lined-table

            =========== ====== ==========
            name        office department
            =========== ====== ==========
            Mr. Reyes   B24    Math
            Ms. Tan     A11    Humanities
            Ms. Larsen  A05    Humanities
            Ms. Musa    B22    Science
            Mr. Pal     A03    Humanities
            =========== ====== ==========

        Note how we have eliminated redundancy through this decomposition.  If we need to update office information for an instructor, there is exactly one tuple to update.  We also no longer need to worry about modification anomalies.  Adding or removing an instructor is completely independent of adding or removing classes; this also removes any need for excessive NULLs in the **classes** relation [#]_.

.. index:: normal form

范式
::::::::::::

*Normal forms*

.. md-tab-set::

    .. md-tab-item:: 中文

        规范化的概念源于关系模型本身。随着时间的推移，增加了一些额外的细化，形成了一系列的范式，这些范式大多基于早期的范式。我们不会研究所有已提出的范式，而是专注于那些在大多数应用中最有用且最有价值的形式。我们考虑的第一种形式适当地被称为 *第一范式* ，简称为1NF。接下来我们将讨论第二、第三和第四范式（2NF、3NF、4NF），以及介于3NF和4NF之间的Boyce-Codd范式（BCNF）。

        当一个数据库满足某个范式的要求时，我们称该数据库 *处于* 该范式中。按照通常的定义，大多数范式都包括一个要求，即必须满足早期的范式。因此，任何处于4NF的数据库必然也处于1NF、2NF、3NF和BCNF；处于BCNF的数据库也必然在3NF及以下；依此类推。然而，高级范式也确实解决了不太常见的情况，因此，例如，经过重构以满足3NF的数据库很可能也满足BCNF甚至4NF。3NF通常被认为是数据库被视为“规范化”的最低要求。

        为了说明大多数范式，我们首先需要提供一些额外的基础知识，这将在接下来的几个部分中涵盖。然而，我们可以立即解释1NF。1NF要求关系的某个属性的域仅包含 *原子* 值。这里的原子简单地意味着我们无法有效地将值分解为更小的部分。非原子元素包括复合值、值数组和关系。例如，包含作者姓名的字符字符串可能是原子的 [#]_ ; 但用作者和书名识别一本书的字符串可能是复合的；而作者列表则是一个数组；包含一本书出版历史（包括每次出版的出版社、年份、ISBN等）的值表则是一个关系。为了满足1NF的要求，复合值应该拆分为单独的属性，而数组和关系则应该拆分为它们自己的关系（并用外键引用原始关系）。

        1NF通常被描述为关系数据库定义的一部分，早期的关系数据库系统确实没有提供允许违反1NF的功能。一些现代数据库系统现在提供对复合值的支持，以用户定义类型和数组值的形式。虽然从技术上讲，1NF仍然是所有高级范式的要求，但在某些应用中，这些1NF的违反可能非常有用。一些作者也主张允许关系值属性。

    .. md-tab-item:: 英文

        The concept of normalization originates with the relational model itself.  Additional refinements have been added over time, leading to a series of normal forms, which mostly build on earlier normal forms.  We will not study every normal form that has been proposed, but focus on the forms which are most useful and most likely to be of value in most applications.  The first form we consider is appropriately named the *first normal form*, abbreviated 1NF.  We proceed with the second, third, and fourth normal forms (2NF, 3NF, 4NF) as well as Boyce-Codd normal form (BCNF), which fits in between 3NF and 4NF.

        When a database meets the requirement for a normal form, we say that the database is *in* the form.  As commonly defined, most normal forms include a requirement that earlier normal forms are also met.  Therefore, any database that is in 4NF is necessarily also in 1NF, 2NF, 3NF, and BCNF; a database in BCNF is also in 3NF and below; and so forth.  However, it is also true that higher forms address less frequently occurring situations, so, for example, a database that has been restructured to be in 3NF is very likely to also be in BCNF or even 4NF.  3NF is generally considered the minimum requirement a database must meet to be considered "normalized".

        To explain most of the normal forms, we first need to provide some additional foundation, covered in the next few sections.  However, we can explain 1NF immediately.  1NF requires that the domain of an attribute of a relation contains *atomic* values only.  Atomic here simply means that we cannot usefully break the value down into smaller parts.  Non-atomic elements include compound values, arrays of values, and relations.  For example, a character string containing an author's name may be atomic [#]_, but a string identifying a book by author and title is probably compound; a list of authors would be an array; and a table of values giving a book's publication history (including publisher, year, ISBN, etc. for each publication) would be a relation.  To meet the 1NF requirements, compound values should be broken into separate attributes, while arrays and relations should be broken out into their own relations (with a foreign key referencing the original relation).

        1NF is often described as simply part of the definition of a relational database, and early relational database systems indeed provided no capabilities that would permit violations of 1NF.  Some modern database systems now provide support for compound values, in the form of user-defined types, and array values.  While 1NF technically remains a requirement for all higher normal forms, for certain applications these violations of 1NF may be highly useful.  Some authors have argued for permitting relation-valued attributes as well.

.. index:: key - normalization; superkey

键和超键
::::::::::::::::::

*Keys and superkeys*

.. md-tab-set::

    .. md-tab-item:: 中文

        本节重申了 :numref:`Chapter {number} <relational-model-chapter>` 中的某些内容，我们在其中定义了 *键(key)* 一词，但进行了更详细的阐述。我们首先定义一个更一般的术语， *超键(superkey)* 。

        一个关系的超键是该关系属性的某个子集，它唯一标识关系中的任何元组。考虑下面的 **图书馆** 关系（我们将广泛使用此示例）：

        .. table:: **图书馆**
            :class: lined-table

            ================= ========================== ==== ================ ============ ============ ===================
            作者              书名                       年份 类型             作者出生     作者去世     部门
            ================= ========================== ==== ================ ============ ============ ===================
            Ralph Ellison     Invisible Man              1952 小说             1914-03-01   1994-04-16   文学
            Jhumpa Lahiri     Unaccustomed Earth         2008 小说             1967-07-11                文学
            J.R.R. Tolkien    The Hobbit                 1937 奇幻             1892-01-03   1973-09-02   推测小说
            Isabel Allende    The House of the Spirits   1982 魔幻现实主义     1942-08-02                文学
            J.R.R. Tolkien    The Fellowship of the Ring 1954 奇幻             1892-01-03   1973-09-02   推测小说
            Ursula K. Le Guin The Dispossessed           1974 科幻             1929-10-21   2018-01-22   推测小说
            ================= ========================== ==== ================ ============ ============ ===================

        （此表中 **作者去世** 的空项表示NULL。在撰写本文时，这些作者仍在世。）

        我们断言属性集{**作者**、 **书名** 和 **年份** }是 **图书馆** 关系的超键。

        超键的定义不仅适用于当前关系中的数据，还适用于 *我们可能在关系中存储的任何数据* 。也就是说，超键不是数据的临时属性，而是我们对数据施加的约束。例如，尽管上面 **年份** 列中列出的每个出版年份在其书籍中是唯一的，但这不能保证未来我们可能添加到关系中的书籍。因此，集合{**年份**}不是 **图书馆** 的超键。

        超键的第二个等价定义是关系属性的子集，保证对关系中的任何元组包含唯一的值设置。对于我们的例子，这意味着 **图书馆** 关系中永远不可能有两本书具有相同的作者、书名和年份。根据这个第二个定义和关系的定义，我们注意到 *每个* 关系至少有一个超键：关系中所有属性的集合。集合{**作者** 、 **书名** 、 **年份**、 **类型** 、 **作者出生** 、 **作者去世** 、 **部门**}是 **图书馆** 关系的超键，因为关系中的每个元组必须是唯一的。

        我们还可以进一步指出，关系的任何属性子集，如果是某个超键的超集，也同样是该关系的超键。对于我们的例子，{**作者** 、 **书名** 、 **年份** 、 **作者出生**}必须是超键，因为它是已知超键的超集。

        一个关系的 *键* 是一个超键，从中我们无法去掉任何属性而仍得到超键。对于 **图书馆** 关系，我们断言{**作者** 、 **书名**}是该关系的超键；此外， **作者** 和 **书名** 都是必要的。也就是说，既不是{ **作者** }也不是{ **书名** }是 **图书馆** 的超键。因此，{**作者** 、 **书名**}是 **图书馆** 的键；集合{**作者** 、 **书名** 、 **年份**}是超键，但不是键，因为我们可以去掉 **年份** ，仍然有一个超键 [#]_ 。

        识别关系的键是分析一个关系是否已在2NF或更高范式下规范化的关键步骤。

    .. md-tab-item:: 英文

        This section reiterates some material from :numref:`Chapter {number} <relational-model-chapter>` in which we defined the term *key*, but in a bit more detail.  We start by defining a more general term, *superkey*.

        A superkey of a relation is some subset of attributes of the relation which uniquely identifies any tuple in the relation.  Consider the **library** relation below (we will be using this example extensively):

        .. table:: **library**
            :class: lined-table

            ================= ========================== ==== ================ ============ ============ ===================
            author            title                      year genre            author_birth author_death section
            ================= ========================== ==== ================ ============ ============ ===================
            Ralph Ellison     Invisible Man              1952 fiction          1914-03-01   1994-04-16   literature
            Jhumpa Lahiri     Unaccustomed Earth         2008 fiction          1967-07-11                literature
            J.R.R. Tolkien    The Hobbit                 1937 fantasy          1892-01-03   1973-09-02   speculative fiction
            Isabel Allende    The House of the Spirits   1982 magical realism  1942-08-02                literature
            J.R.R. Tolkien    The Fellowship of the Ring 1954 fantasy          1892-01-03   1973-09-02   speculative fiction
            Ursula K. Le Guin The Dispossessed           1974 science fiction  1929-10-21   2018-01-22   speculative fiction
            ================= ========================== ==== ================ ============ ============ ===================

        (The blank entries for **author_death** in this table represent NULLs.  The authors are still living at the time of this writing.)

        We assert that the set of attributes {**author**, **title**, and **year**} is a superkey for the **library** relation.

        The definition of superkey applies not just to the current data in the relation, but to *any data we might possibly store in the relation*.  That is, a superkey is not a transitory property of the data, but a constraint we impose on the data.  For example, although each publication year listed in the **year** column above is unique to its book, that cannot be guaranteed for future books we might add to the relation.  Therefore the set {**year**} is not a superkey for **library**.

        A second, and equivalent definition of superkey is as a subset of attributes of the relation that are guaranteed to contain a unique setting of values for any tuple in the relation.  For our example, this means there can never be two books in the **library** relation which share the same author, title, and year.  From this second definition and the definition of a relation, we note that *every* relation has at least one superkey: the set of all attributes of the relation.  The set {**author**, **title**, **year**, **genre**, **author_birth**, **author_death**, **section**} is a superkey for the **library** relation simply because every tuple in the relation must be unique.

        We can further state that any subset of attributes of the relation which is a superset of some superkey of the relation is also a superkey of the relation.  For our example, {**author**, **title**, **year**, **author_birth**} must be a superkey because it is a superset of a known superkey.

        A *key* of a relation is a superkey of the relation from which we cannot subtract any attributes and get a superkey.  For the **library** relation, we assert that {**author**, **title**} is a superkey of the relation; furthermore, both **author** and **title** are needed.  That is, neither {**author**} nor {**title**} is a superkey of **library**.  Therefore, {**author**, **title**} is a key of **library**; the set {**author**, **title**, **year**} is a superkey but not a key because we can remove **year** and still have a superkey [#]_.

        Identifying the keys of a relation is a key step in analyzing whether or not a relation is already normalized with respect to 2NF or higher.

.. index:: functional dependency

函数依赖关系
:::::::::::::::::::::::

*Functional dependencies*

.. md-tab-set::

    .. md-tab-item:: 中文

        现在我们转向函数依赖的主题，这与超键密切相关。

        *函数依赖* （functional dependency FD）是关于关系的两个属性集的陈述。考虑两个属性集，我们将其标记为 *X* 和 *Y* 。我们说 *X* *函数性决定* *Y* ，或 *Y* 对 *X* 是 *函数依赖的*，如果在关系中，任何两个元组在 *X* 中的值相同，那么它们在 *Y* 中的值也必须相同。其表示法为：

        .. math::
            X \rightarrow Y

        与键类似，FD是我们对数据施加的约束。另一个理解函数依赖的方式是，如果你有一个关系，该关系仅包含在 *X* 或 *Y* 中的属性，那么 *X* 将是该关系的超键。也就是说， *X* 唯一决定 *X* 和 *Y* 的并集中的所有内容。（我们现在可以提供另一个超键的定义，即一个关系的属性子集，它函数性决定该关系的所有属性集。）

        另一种理解FD的方式是，如果 *X* 函数性决定 *Y* ，那么如果我们知道 *X* 中的值，我们就知道或可以确定 *Y* 中的值，因为 *Y* 仅包含关于 *X* 的单值事实。在我们的 **图书馆** 关系中，集合{**作者** 、 **书名**}函数性决定集合{ **年份** }，因为如果我们知道书的作者和书名，那么我们应该能够找出出版年份；而我们查找年份的任何来源都应该给出相同的答案。这个依赖在这个意义上是“函数性的”；在（作者、书名）对的域与出版年份的域之间存在某种 *函数* ，对于每个有效输入都能得出正确答案。这个函数在这里仅仅是域之间的映射，而不是我们可以分析推导的东西。

        以下是 **图书馆** 关系的一些更多FD：

        .. math::

            \begin{eqnarray*}
            \text{\{作者, 书名\}} & \rightarrow & \text{\{类型\}} \\
            \text{\{作者\}} & \rightarrow & \text{\{作者出生, 作者去世\}} \\
            \text{\{类型\}} & \rightarrow & \text{\{部门\}} \\
            \text{\{作者, 书名\}} & \rightarrow & \text{\{书名, 年份\}} \\
            \text{\{书名, 类型\}} & \rightarrow & \text{\{书名\}} \\
            \end{eqnarray*}

        第一个FD告诉我们，每本书在我们的数据库中被归类为恰好一个类型。第二个FD告诉我们，作者的出生和去世日期在作者每次出现在数据库中时应该是相同的。第三个FD告诉我们，书籍在图书馆中的位置取决于书籍的类型。最后两个FD与之前的不同；在这些情况下，左侧的集合与右侧的集合之间存在重叠。我们稍后将对此给出特殊名称。目前，第四个FD告诉我们，如果我们知道一本书的作者和书名，那么我们就知道书名和出版年份。最后一个FD简单地告诉我们，任何两个具有相同书名和类型的元组，其书名都是相同的！

    .. md-tab-item:: 英文

        Now we turn to the topic of functional dependencies, which are closely related to superkeys.

        A *functional dependency* (FD) is a statement about two sets of attributes of a relation.  Consider two sets of attributes, which we will label *X* and *Y*.  We say that *X* *functionally determines* *Y*, or *Y* is *functionally dependent on* *X*, if, whenever two tuples in the relation agree on the values in *X*, they must also agree on the values in *Y*.  The notation for this is:

        .. math::
            X \rightarrow Y

        As with keys, FDs are constraints that we impose on the data.  Another way of thinking about a functional dependency is, if you had a relation such that the relation contains only the attributes that are in *X* or *Y*, then *X* would be a superkey for that relation.  That is, *X* uniquely determines everything in the union of *X* and *Y*.  (We can now provide another defintiion of superkey as a subset of attributes of a relation that functionally determines the set of all attributes of the relation.)

        Another way of thinking about FDs is, if *X* functionally determines *Y*, then if we know the values in *X*, we know or can determine the values in *Y*, because *Y* just contains single-valued facts about *X*.  In our **library** relation, the set {**author**, **title**} functionally determines the set {**year**}, because if we know the author and title of the book, then we should be able to find out what the publication year is; and whatever sources we consult to find the year should all give us the same answer.  The dependency is "functional" in this sense; there exists some *function* between the domain of (author, title) pairs and the domain of publication years that yields the correct answer for every valid input.  The function in this case is simply a mapping between domains, not something we can analytically derive.

        Here are some more FDs for the **library** relation:

        .. math::

            \begin{eqnarray*}
            \text{\{author, title\}} & \rightarrow & \text{\{genre\}} \\
            \text{\{author\}} & \rightarrow & \text{\{author_birth, author_death\}} \\
            \text{\{genre\}} & \rightarrow & \text{\{section\}} \\
            \text{\{author, title\}} & \rightarrow & \text{\{title, year\}} \\
            \text{\{title, genre\}} & \rightarrow & \text{\{title\}} \\
            \end{eqnarray*}

        The first FD tells us that each book is categorized into exactly one genre in our database.  The second tells us that an author's dates of birth and death should be the same every time the author appears in the database.  The third tells us that the location in the library in which a book is shelved depends on the genre of the book.  The last two FDs are different from the previous ones; in these, there is an overlap between the set on the left-hand side and the set on the right-hand side.  We will give special names to these in a moment.  For now, the fourth FD tells us that, if we know the author and title of a book, then we know the title and the publication year.  The final FD simply tells us that any two tuples having the same title and genre, have the same title!

函数依赖关系的类型
------------------------------

*Types of functional dependency*

.. md-tab-set::

    .. md-tab-item:: 中文

        FD被分为三种类型: *平凡* 、 *非平凡* 和 *完全非平凡* 。

        平凡FD是指FD的右侧是左侧的一个子集。在我们上述示例中的最后一个FD就是一个平凡FD。平凡FD并不传达有用的信息——它告诉我们“我们知道我们知道什么”——但在我们的规范化过程中，它们仍然有一定的用处。对于一个关系，只要FD的左侧是该关系属性的一个子集，我们所写的每一个平凡FD都是正确的。

        非平凡FD是指FD的右侧的某部分不在左侧。左侧和右侧的交集不为空，但右侧不是左侧的子集。上述的第四个FD就是一个非平凡FD。这些FD传达了一些新信息。在我们的关系中识别非平凡FD是规范化的关键步骤。

        正如你可能现在猜到的，完全非平凡FD是指左侧和右侧之间没有重叠——两个集合的交集是空集。上述的前三个FD就是完全非平凡的。

    .. md-tab-item:: 英文

        FDs are categorized into three types: *trivial*, *non-trivial*, and *completely non-trivial*.

        A trivial FD is one in which the right-hand side of the FD is a subset of the left-hand side.  The last FD in our example above is a trivial FD.  A trivial FD conveys no useful information - it tells us "we know what we know" - but they still have some use to us in our normalization procedures.  Every trivial FD we can write down for a relation is true, as long as the left-hand side of the FD is a subset of the attributes of the relation.

        A non-trivial FD is one in which some part of the right-hand side of the FD is not in the left-hand side.  The intersection of the left-hand side and the right-hand side is not empty, but the right-hand side is not a subset of the left-hand side.  The fourth FD above is a non-trival FD.  These FDs convey some new information.  Identifying non-trivial FDs in our relations is a crucial step in normalization.

        As you might guess by now, a completely non-trivial FD is one for which there is no overlap between the left-hand side and the right-hand side - the intersection of the two sets is the empty set.  The first three FDs above are completely non-trivial.

.. index:: functional dependency; inference rules

推理规则
---------------

*Inference rules*

.. md-tab-set::

    .. md-tab-item:: 中文

        许多FD可以从其他FD推导或推断出来。我们特别关注那些在右侧具有最大集合的非平凡FD，即，无法再添加其他内容而使FD不成立的集合。存在一个直接的算法可以从一组FD推导出这样的FD，我们将在下一节中讨论。我们需要以下五个推理规则来进行算法。前三个推理规则被称为 *阿姆斯特朗公理* ，可用于证明其余规则。

        我们将这些规则呈现但不提供证明，其直觉应该是明确的。设 *X* 、 *Y* 和 *Z* 是同一关系属性的子集。将 *Y* 和 *Z* 的并集记为 *YZ* 。则我们有：

        **反身规则**
            如果Y是X的子集，则

            .. math::
                X \rightarrow Y

            这只是一个声明，表明所有平凡FD都是真实的。

        **扩展规则**
            如果

            .. math::
                X \rightarrow Y

            则

            .. math::
                XZ \rightarrow YZ

            也成立。

            该规则表示我们可以向FD的左侧和右侧同时添加相同的属性。显然，如果我们将 *Z* 添加到已知的（左侧），那么我们应该能够在之前能够确定的基础上确定 *Z* （右侧）。

            在我们的 **图书馆** 示例中，我们有

            .. math::
                \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

            因此，也可以说

            .. math::
                \text{\{author, genre\}} \rightarrow \text{\{author_birth, author_death, genre\}}

            这个规则的一个特殊情况是，我们可以将左侧添加到两侧；这不会改变左侧，因为任何集合与自身的并集仍然是该集合：

            .. math::
                X \rightarrow Y

            意味着

            .. math::
                X \rightarrow XY

        **传递规则**
            如果我们有

            .. math::
                X \rightarrow Y \\
                Y \rightarrow Z

            那么

            .. math::
                X \rightarrow Z

            也成立。也就是说，如果知道 *X* 可以告诉我们 *Y* ，而从 *Y* 我们可以知道 *Z* ，那么知道 *X* 也可以告诉我们 *Z* 。

            在我们的 **图书馆** 关系中，我们有

            .. math::
                \text{\{author, title\}} \rightarrow \text{\{genre\}} \\
                \text{\{genre\}} \rightarrow \text{\{section\}} \\

            因此

            .. math::
                \text{\{author, title\}} \rightarrow \text{\{section\}}

        **分割规则（或分解、或投影规则）**
            如果

            .. math::
                X \rightarrow YZ

            成立，则

            .. math::
                X \rightarrow Y \\
                X \rightarrow Z

            也成立。简单地说，如果知道 *X* 的值可以告诉我们 *Y* **和** *Z* 的值，那么知道 *X* 的值也可以告诉我们 *Y* 的值，对 *Z* 也是一样。在我们的 **图书馆** 示例中，我们有

            .. math::
                \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

            因此，也可以说

            .. math::
                \text{\{author\}} \rightarrow \text{\{author_birth\}} \\
                \text{\{author\}} \rightarrow \text{\{author_death\}}

            请注意，我们只能“拆分”右侧。例如，给定：:math:`\text{\{author, title\}} \rightarrow \text{\{year\}}`, 则并 **不** 成立 :math:`\text{\{author\}} \rightarrow \text{\{year\}}`.

        **结合规则（或并集、或加法规则）**
            这是分割规则的反向。如果我们有

            .. math::
                X \rightarrow Y \\
                X \rightarrow Z

            那么

            .. math::
                X \rightarrow YZ

            也成立。在我们的 **图书馆** 示例中，我们有

            .. math::
                \text{\{author, title\}} \rightarrow \text{\{year\}} \\
                \text{\{author, title\}} \rightarrow \text{\{genre\}}

            因此

            .. math::
                \text{\{author, title\}} \rightarrow \text{\{year, genre\}}

        虽然可以通过上述规则从给定关系的FD集合中推导出所有可以推导的FD，但不幸的是，没有办法判断某个FD集合是否 *完整(complete)* ——即该FD集合是否让我们能够推导出关系上每一个可能真实的FD。FD源自数据库设计者和参与分析与设计的其他人的思维，这一过程需要一些“反复试验”，即迭代改进。

    .. md-tab-item:: 英文

        Many FDs can be inferred or derived from other FDs.  We are particularly interested in non-trivial FDs which have a maximal set on the right-hand side, that is, a set which cannot be added to without making the FD false.  There is a straightforward algorithm to infer such FDs from a set of FDs, which we discuss in the next section.  We need the five inference rules below for the algorithm.  The first three inference rules are known as *Armstrong's axioms*, and can be used to prove the remaining rules.

        We present these without proof, but the intuition behind these should be clear.  Let *X*, *Y*, and *Z* be subsets of the attributes of the same relation.  Let the union of *Y* and *Z* be denoted *YZ*.  Then we have:

        *Reflexive rule*
            If Y is a subset of X, then

            .. math::

                X \rightarrow Y

            This is simply a statement that all trivial FDs are true.

        *Augmentation rule*
            If

            .. math::

                X \rightarrow Y

            then

            .. math::

                XZ \rightarrow YZ

            also holds.

            This rule says we can add the same attributes to both the left-hand and right-hand sides of an FD.  Trivially, if we add *Z* to what we know (left-hand side), then we should be able to determine *Z* in addition to what we could determine previously (right-hand side).

            In our **library** example, we are given

            .. math::

                \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

            therefore, it is also true that

            .. math::

                \text{\{author, genre\}} \rightarrow \text{\{author_birth, author_death, genre\}}

            A special case of this is that we can add the left-hand side to both sides; this leaves the left-hand side unchanged, since the union of any set with itself is just the set:

            .. math::

                X \rightarrow Y

            implies

            .. math::

                X \rightarrow XY


        *Transitive rule*
            If we have both of

            .. math::

                X \rightarrow Y \\
                Y \rightarrow Z

            then

            .. math::

                X \rightarrow Z

            also holds.  That is, if knowing *X* tells us *Y*, and from *Y* we can know *Z*, then knowing *X* also tells us *Z*.

            In our **library** relation we have

            .. math::

                \text{\{author, title\}} \rightarrow \text{\{genre\}}
                \text{\{genre\}} \rightarrow \text{\{section\}} \\

            thus

            .. math::

                \text{\{author, title\}} \rightarrow \text{\{section\}}

        *Splitting rule (or decomposition, or projective, rule)*
            If

            .. math::

                X \rightarrow YZ

            holds, then so do

            .. math::

                X \rightarrow Y \\
                X \rightarrow Z

            Plainly stated, if knowing the values for *X* tells us the values for *Y* **and** *Z*, then knowing the values for *X* tells us the values for *Y*, and likewise for *Z*.  In our **library** example, we have

            .. math::

                \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

            therefore, it is also true that

            .. math::

                \text{\{author\}} \rightarrow \text{\{author_birth\}} \\
                \text{\{author\}} \rightarrow \text{\{author_death\}}

            Note that we can "split" the right-hand side only.  For example, given :math:`\text{\{author, title\}} \rightarrow \text{\{year\}}`, it is **not** true that :math:`\text{\{author\}} \rightarrow \text{\{year\}}`.

        *Combining rule (or union, or additive, rule)*
            This is the splitting rule in reverse.  If we have both of

            .. math::

                X \rightarrow Y \\
                X \rightarrow Z

            then

            .. math::

                X \rightarrow YZ

            also holds. In our **library** example, we have

            .. math::

                \text{\{author, title\}} \rightarrow \text{\{year\}} \\
                \text{\{author, title\}} \rightarrow \text{\{genre\}}

            thus

            .. math::

                \text{\{author, title\}} \rightarrow \text{\{year, genre\}}

        While any FDs that can be inferred from a given collection of FDs on a relation can be inferred using the above rules, there is unfortunately no way of deciding that some collection of FDs is, in fact, *complete* - that is, that the collection of FDs lets us infer every possible true FD on the relation.  FDs come from the minds of the database designer and others involved in analysis and design, a process which requires some "trial and error", i.e., iterative improvement.

.. index:: closure

闭包
-------

*Closure*

.. md-tab-set::

    .. md-tab-item:: 中文

        如前所述，我们特别关注那些在右侧具有最大集合的非平凡FD。给定某些FD集合，关系 *R* 的子集 *X* 的 *闭包* 是所有集合{ *a* }的并集，其中 *a* 是 *R* 的属性，并且我们可以推导出：:math:`X \rightarrow {a}`。非正式地说， *X* 的闭包是由 *X* 函数确定的属性集合。 *X* 的闭包记作 *X*:sup:`+`。

        我们对闭包感兴趣有几个原因。首先，从这个定义可以注意到，关系的超键的闭包是关系的所有属性的集合。我们可以利用这个事实来测试某个属性集合是否是超键；进一步地，理论上我们可以通过检查每个属性子集的闭包来找到关系的所有超键（实际上，随着属性数量的增加，这可能会变得非常繁琐）。其次，闭包将在我们规范化算法的分解步骤中发挥重要作用。

        可以使用以下算法来确定属性集合的闭包。

        **闭包算法**
            给定FD集合 *F* 和属性集合 *X* ：

            1. 设 *C* = *X* 。显然，:math:`X \rightarrow C`。
            2. 当存在某个函数依赖关系 :math:`Y \rightarrow Z` 在 *F* 中，使得 *Y* 是 *C* 的子集并且 *Z* 包含一些不在 *C* 中的属性时，将 *Z* 中的属性添加到 *C* 以创建 *C'* 。然后，

            .. math::

                \begin{eqnarray*}
                & & C \rightarrow Y    ~~\text{(反身规则)} \\
                & & C \rightarrow Z    ~~\text{(传递规则)} \\
                & & X \rightarrow Z    ~~\text{(传递规则)} \\
                & & X \rightarrow C'   ~~\text{(结合规则)} \\
                \end{eqnarray*}

            设 *C* = *C'* 。

            3. 当没有更多的FD满足上述条件时， *C* = *X*:sup:`+`。

        我们之前断言，集合{author, title}是我们示例 **图书馆** 关系的超键，因此闭包 {author, title}\ :sup:`+` 应该是 **图书馆** 的所有属性集合。我们现在展示这一点是如何从我们的推理规则和之前给出的FD中得出的：

        .. math::

            \begin{eqnarray*}
            \text{\{author, title\}} & \rightarrow & \text{\{year\}} \\
            \text{\{author, title\}} & \rightarrow & \text{\{genre\}} \\
            \text{\{author\}} & \rightarrow & \text{\{author_birth, author_death\}} \\
            \text{\{genre\}} & \rightarrow & \text{\{section\}} \\
            \text{\{author, title\}} & \rightarrow & \text{\{title, year\}} \\
            \text{\{title, genre\}} & \rightarrow & \text{\{title\}} \\
            \end{eqnarray*}

        1. 设 *C* = {author, title}。
        2. 我们有 :math:`\text{\{author, title\}} \rightarrow \text{\{year\}}` ，且{author, title}是 *C* 的子集，因此将 **year** 添加到 *C* 中： *C* = {author, title, year} 。
        3. 类似地， :math:`\text{\{author, title\}} \rightarrow \text{\{genre\}}` ，所以设 *C* = {author, title, year, genre} 。
        4. 我们有 :math:`\text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}` ，且 {author} 是 *C* 的子集。设 *C* = {author, title, year, genre, author_birth, author_death} 。
        5. 我们有 :math:`\text{\{genre\}} \rightarrow \text{\{section\}}` ，且 {genre} 是 *C* 的子集。设 *C* = {author, title, year, genre, author_birth, author_death, section} 。
        6. 此时算法完成，因为所有未使用的FD的右侧都已经是 *C* 的子集；无论如何， *C* 已经包含 **图书馆** 的所有属性。

        因此， {author, title}\ :sup:`+` = {author, title, year, genre, author_birth, author_death, section} 。

    .. md-tab-item:: 英文

        As mentioned, we are going to be particularly interested in non-trivial FDs which have a maximal set on the right-hand side.  The *closure* of a subset *X* of relation *R* given some collection of FDs is the union of all sets {*a*} such that *a* is an attribute of *R* and we can infer :math:`X \rightarrow {a}`.  Informally, the closure of *X* is the set of attributes which are functionally determined by *X*.  The closure of *X* is denoted *X*:sup:`+`.

        We are interested in closure for a couple of reasons.  First, note from this definition that the closure of a superkey of a relation is the set of all attributes of the relation.  We can use this fact to test whether or not some set of attributes is a superkey; further, we could in theory find all superkeys of a relation by examining the closure of every subset of attributes (in practice this can become too much work fairly quickly as the number of attributes increases).  Second, closure will be useful in the decomposition step of our normalization algorithms.

        The closure of a set of attributes can be determined using the following algorithm.

        *Closure algorithm*
            Given a collection *F* of FDs and a set of attributes *X*:

            1. Let *C* = *X*.  Trivially, :math:`X \rightarrow C`.
            2. While there exists some functional dependency :math:`Y \rightarrow Z` in *F* such that *Y* is a subset of *C* and *Z* contains some attributes not in *C*, add the attributes in *Z* to *C* to create *C\'*.  Then,

            .. math::

                \begin{eqnarray*}
                & & C \rightarrow Y    ~~\text{(reflexive rule)} \\
                & & C \rightarrow Z    ~~\text{(transitive rule)} \\
                & & X \rightarrow Z    ~~\text{(transitive rule)} \\
                & & X \rightarrow C'   ~~\text{(combining rule)} \\
                \end{eqnarray*}

            Let *C* = *C\'*.

            3. When no more FDs meet the criteria above, *C* = *X*:sup:`+`.

        We previously asserted that the set {author, title} is a superkey for our example **library** relation, so the closure {author, title}\ :sup:`+` should be the set of all attributes of **library**.  We now show that this follows from our inference rules, and from the FDs given previously:

        .. math::

            \begin{eqnarray*}
            \text{\{author, title\}} & \rightarrow & \text{\{year\}} \\
            \text{\{author, title\}} & \rightarrow & \text{\{genre\}} \\
            \text{\{author\}} & \rightarrow & \text{\{author_birth, author_death\}} \\
            \text{\{genre\}} & \rightarrow & \text{\{section\}} \\
            \text{\{author, title\}} & \rightarrow & \text{\{title, year\}} \\
            \text{\{title, genre\}} & \rightarrow & \text{\{title\}} \\
            \end{eqnarray*}

        1. Let *C* = {author, title}.
        2. We have :math:`\text{\{author, title\}} \rightarrow \text{\{year\}}`, and {author, title} is a subset of *C*, so add **year** to *C*: *C* = {author, title, year}.
        3. Similarly, :math:`\text{\{author, title\}} \rightarrow \text{\{genre\}}`, so let *C* = {author, title, year, genre}.
        4. We have :math:`\text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}`, and {author} is a subset of *C*.  Let *C* = {author, title, year, genre, author_birth, author_death}.
        5. We have :math:`\text{\{genre\}} \rightarrow \text{\{section\}}`, and {genre} is a subset if *C*.  Let *C* = {author, title, year, genre, author_birth, author_death, section}.
        6. The algorithm completes at this point because the right-hand sides of all of the unused FDs are already subsets of *C*; and in any case, *C* already has all attributes of **library**.

        Thus, {author, title}\ :sup:`+` = {author, title, year, genre, author_birth, author_death, section}.

.. index:: second normal form, 2NF, third normal form, 3NF, Boyce-Codd normal form, BCNF

第二范式、第三范式和 Boyce-Codd 范式
::::::::::::::::::::::::::::::::::::::::::

*Second, third, and Boyce-Codd normal forms*

.. md-tab-set::

    .. md-tab-item:: 中文

        现在我们准备讨论 Boyce-Codd 范式 (BCNF) 之前的范式。在本节中，我们将提供范式的定义以及示例。

    .. md-tab-item:: 英文

        We are now ready to discuss the normal forms up to Boyce-Codd normal form (BCNF).  In this section we will provide definitions of the normal forms, with examples.

第二范式
------------------

*Second normal form*

.. md-tab-set::

    .. md-tab-item:: 中文

        一个关系处于第二范式（2NF）当且仅当它处于第一范式（1NF）并且没有 *非键属性* 在键的真子集上是函数依赖的。非键属性是指不属于任何键的属性。

        从这个定义中，我们可以看出 **图书馆** 不 满足2NF。 **图书馆** 的键是 {author, title} 。然而，我们有以下函数依赖：

        .. math::

            \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

        在这个依赖中，左侧仅包含 **author** 。我们称上述函数依赖 *违反* 第二范式。

        请注意，任何键只有一个属性的关系（处于1NF）自动满足2NF。

    .. md-tab-item:: 英文

        A relation is in second normal form (2NF) if it is in 1NF and there are no *non-key attributes* which are functionally dependent on a proper subset of the key.  A non-key attribute is an attribute which is not part of any key.

        From this definition, we can see that **library** is not in 2NF.  The key of **library** is {author, title}.  However, we have the FD

        .. math::

            \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

        in which the left-hand side only contains **author**.  We say that the above FD *violates* second normal form.

        Note that any relations (in 1NF) for which the key has a single attribute is automatically in 2NF.

第三范式
-----------------

*Third normal form*

.. md-tab-set::

    .. md-tab-item:: 中文

        一个关系处于第三范式（3NF）当且仅当它处于第二范式（2NF）并且没有非键属性在其他非键属性上是函数依赖的。

        再次考虑 **图书馆** 关系，依赖关系

        .. math::

            \text{\{genre\}} \rightarrow \text{\{section\}}

        违反了3NF，因为 **genre** 和 **section** 都不属于任何键。

    .. md-tab-item:: 英文

        A relation is in third normal form (3NF) if it is in 2NF and there are no non-key attributes which are functionally dependent on other non-key attributes.

        Considering the **library** relation again, the dependency

        .. math::

            \text{\{genre\}} \rightarrow \text{\{section\}}

        violates 3NF because neither **genre** nor **section** are part of any key.

Boyce-Codd 范式
----------------------

*Boyce-Codd normal form*

.. md-tab-set::

    .. md-tab-item:: 中文

        博伊斯-科德 [#]_ 范式是第三范式的一个稍微更强的版本；任何处于BCNF的关系也必定处于3NF。然而，大多数处于3NF的关系也处于BCNF。BCNF有一个简单而通用的定义，涵盖了2NF和3NF的定义:

        **BCNF的定义**
            一个关系处于BCNF当且仅当它处于1NF，并且对于关系中的每一个非平凡函数依赖形式为 :math:`X \rightarrow Y`， *X* 是该关系的超键。

        从这个定义中可能并不明显关系在BCNF中也是在2NF和3NF。我们将证明对于2NF这是成立的；类似的论证也适用于3NF。回想一下，2NF要求我们没有非键属性在键的适当子集上是函数依赖的。根据键的定义，键的适当子集不能是键或超键；因此，2NF所禁止的FD的左侧必须不是超键。另一方面，非键属性根本不能是键的一部分。2NF所禁止的FD的右侧与左侧没有交集，因此该FD是完全非平凡的。因此，任何违反2NF的FD也满足违反BCNF的标准。

        3NF和BCNF之间的区别在于，3NF允许右侧是键的子集的FD。这种情况相对不常见，这就是为什么大多数处于3NF的关系也处于BCNF的原因。我们将在后面的部分进一步探讨这个区别。

    .. md-tab-item:: 英文

        Boyce-Codd [#]_ normal form is a slightly stronger version of third normal form; any relation in BCNF is also in 3NF.  However, most relations in 3NF are also in BCNF.  BCNF has a simple and general definition which encompasses the definitions of 2NF and 3NF:

        *Definition of BCNF*
            A relation is in BCNF if it is in 1NF and if, for every non-trivial functional dependency of the form :math:`X \rightarrow Y` on the relation, *X* is a superkey of the relation.

        It may not be obvious from this definition that relations in BCNF are also in 2NF and 3NF.  We will demonstrate that this is true for 2NF; a similar argument holds for 3NF.  Recall that 2NF requires we have no non-key attributes functionally dependent on a proper subset of the key.  By the definition of key, a proper subset of the key cannot be a key or superkey; therefore, an FD forbidden by 2NF must have a left-hand side that is not a superkey.  On the other hand, non-key attributes cannot be part of the key at all.  The right-hand side of an FD forbidden by 2NF can have no intersection with the left-hand side, so the FD is completely non-trivial.  Thus any FDs that would violate 2NF also meet the criteria for violating BCNF.

        The difference between 3NF and BCNF is simply that 3NF permits FDs for which the right-hand side is a subset of a key.  This situation is fairly uncommon, which is why most relations in 3NF are also in BCNF.  We will explore this difference further in a later section.

.. index:: decomposition, normalization; decomposition

分解
:::::::::::::

*Decomposition*

.. md-tab-set::

    .. md-tab-item:: 中文

        我们说一个数据库在某个范式下是规范化的，如果数据库中的所有关系都处于该范式中。为了规范化一个数据库，我们必须 *分解* 那些有违反FD的关系。关系的分解涉及创建两个新关系，每个关系都有原始关系的一个属性子集。然后可以丢弃原始关系。

        在本节中，我们讨论BCNF分解算法，并提供一个规范化的示例演示。最后，我们探讨为什么某些有问题的关系可能更适合保留在3NF中。

    .. md-tab-item:: 英文

        We say that a database is normalized with respect to some normal form if all relations in the database are in the normal form.  To normalize a database, we must *decompose* relations which have some violating FD.  Decomposition of a relation involves creating two new relations, each of which has a subset of the attributes of the original relation.  The original relation can then be discarded.

        In this section we discuss the BCNF decomposition algorithm and provide an example walkthrough of normalization.  We close the section by exploring why some problematic relations may be better left in 3NF.

分解算法
-----------------------

*Decomposition algorithm*

.. md-tab-set::

    .. md-tab-item:: 中文

        有一种简单的分解方法，可以消除范式的违反，并且在所有情况下允许精确恢复原始关系。下面的算法是以BCNF为基础表达的，但对于2NF和3NF同样适用：

        *分解算法*
            给定某个关系 *R* 和一个违反BCNF的函数依赖 :math:`X \rightarrow Y` ：

            1. （可选，但强烈推荐）将由 *X* 函数决定的任何属性添加到 *Y* 中，且这些属性不在 *Y* 中；即，让 *Y* = *X*:sup:`+` 。（很容易证明：给定原始违反， :math:`X \rightarrow X^{+}` 违反了BCNF，所以我们只是用一个违反的FD替换另一个。）
            2. 让 *Z* 为 *R* 中不在 *X* 或 *Y* 中的属性集合。（这个集合必须非空，因为根据定义，*X* 不是一个超键。）
            3. 创建关系 *R1* 和 *R2*，使得 *R1* 拥有 *X* 和 *Y* 的并集中的属性，而 *R2* 拥有 *X* 和 *Z* 的并集中的属性。在关系代数中，我们使用投影来创建新关系：

            .. math::

                R1 = \pi_{XY}(R) \\
                R2 = \pi_{XZ}(R)

            4. 丢弃 *R* 。

    .. md-tab-item:: 英文

        There is a simple approach to decomposition that both eliminates a violation of a normal form, and that allows for exact recovery of the original relation in all cases.  The algorithm below is expressed in terms of BCNF, but works equally well for 2NF and 3NF:

        *Decomposition algorithm*
            Given some relation *R*, and a functional dependency :math:`X \rightarrow Y` on *R* that violates BCNF:

            1. (Optional, but strongly recommended) Add to *Y* any attributes that are functionally determined by *X* and that are not already in *Y*; i.e., let *Y* = *X*:sup:`+`.  (It is easy to show that :math:`X \rightarrow X^{+}` violates BCNF given the original violation, so we are merely substituting one violating FD for another.)
            2. Let *Z* be the set of attributes of *R* that are not in *X* or *Y*.  (This set must be non-empty because, by definition, *X* is not a superkey.)
            3. Create relations *R1* and *R2* such that *R1* has the attributes in the union of *X* and *Y*, and *R2* has the attributes in the union of *X* and *Z*.  In relational algebra terms, we use projection to create the new relations:

            .. math::

                R1 = \pi_{XY}(R) \\
                R2 = \pi_{XZ}(R)

            4. Discard *R*.

示例
--------------

*Worked example*

.. md-tab-set::

    .. md-tab-item:: 中文

        现在我们将这个算法应用于最初仅由 **library** 关系组成的数据库。首先，我们之前提到的函数依赖

        .. math::

            \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

        违反了2NF，因此也违反了BCNF。为了对这个违反应用分解算法：

        1. 让 *Y* 为 {author} 的闭包，即 {author, author_birth, author_death}。
        2. 让 *Z* 为 {title, year, genre, section}。
        3. *X* 和 *Y* 的并集就是 *Y* ，因为我们在步骤1中进行了可选的闭包。*X* 和 *Z* 的并集是 {author, title, year, genre, section}。对这些属性集进行投影得到以下关系，我们将其重命名为 **authors** 和 **library2**：

        .. table:: **authors**
            :class: lined-table

            ================= ============ ============
            author            author_birth author_death
            ================= ============ ============
            Ralph Ellison     1914-03-01   1994-04-16
            Jhumpa Lahiri     1967-07-11
            J.R.R. Tolkien    1892-01-03   1973-09-02
            Isabel Allende    1942-08-02
            Ursula K. Le Guin 1929-10-21   2018-01-22
            ================= ============ ============

        .. table:: **library2**
            :class: lined-table

            ================= ========================== ==== ================ ====================
            author            title                      year genre            section
            ================= ========================== ==== ================ ====================
            Ralph Ellison     Invisible Man              1952 fiction          literature
            Jhumpa Lahiri     Unaccustomed Earth         2008 fiction          literature
            J.R.R. Tolkien    The Hobbit                 1937 fantasy          speculative fiction
            Isabel Allende    The House of the Spirits   1982 magical realism  literature
            J.R.R. Tolkien    The Fellowship of the Ring 1954 fantasy          speculative fiction
            Ursula K. Le Guin The Dispossessed           1974 science fiction  speculative fiction
            ================= ========================== ==== ================ ====================

        4. 丢弃 **library**。

        注意，我们可以通过对 **authors** 和 **library2** 应用自然连接操作来恢复原始关系。

        现在我们必须查看我们的新关系，并确定它们是否已规范化。第一步是确定新关系的键和函数依赖。根据旧关系上的函数依赖，有一种正式过程可以计算新关系的超键和函数依赖 [#]_ . 然而，在实践中，数据库设计者通常可以根据他们对数据的了解来识别新关系的函数依赖和键，而不必进行上述所有计算。

        对于我们的例子，在 **authors** 中，我们可以快速确定唯一有用的非平凡函数依赖是

        .. math::

            \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

        由此我们还可以看到 {author} 的闭包包括 **authors** 中的所有属性，因此 {author} 是一个键。在这个关系中没有剩余的违反函数依赖，所以它在BCNF下是规范化的。

        现在考虑关系 **library2**。注意，上述函数依赖不适用，因为 **author_birth** 和 **author_death** 不是 **library2** 中的属性。根据我们对 **library** 关系中函数依赖的了解，我们可以确定以下函数依赖在 **library2** 中成立：

        .. math::

            \begin{eqnarray*}
            \text{\{author, title\}} & \rightarrow & \text{\{year, genre, section\}} \\
            \text{\{genre\}} & \rightarrow & \text{\{section\}} \\
            \end{eqnarray*}

        并且键是 {author, title}。

        上述第二个函数依赖违反了BCNF（和3NF）。对这个函数依赖进行分解，我们有 *X* = {genre}，*Y* = {section}，*Z* = {title, author, year, genre}。分解结果为以下关系，我们将其重命名为 **books** 和 **genres**：

        .. table:: **books**
            :class: lined-table

            ================= ========================== ==== ================
            author            title                      year genre
            ================= ========================== ==== ================
            Ralph Ellison     Invisible Man              1952 fiction
            Jhumpa Lahiri     Unaccustomed Earth         2008 fiction
            J.R.R. Tolkien    The Hobbit                 1937 fantasy
            Isabel Allende    The House of the Spirits   1982 magical realism
            J.R.R. Tolkien    The Fellowship of the Ring 1954 fantasy
            Ursula K. Le Guin The Dispossessed           1974 science fiction
            ================= ========================== ==== ================

        .. table:: **genres**
            :class: lined-table

            =============== ===================
            genre           section
            =============== ===================
            fiction         literature
            fantasy         speculative fiction
            magical realism literature
            science fiction speculative fiction
            =============== ===================

        我们丢弃 **library2**，最终只剩下三个关系：**authors**、**books** 和 **genres**。这三个关系现在都在BCNF中，因此不再可能进行进一步的规范化（相对于BCNF或更低）。我们可以通过对 **books** 和 **genres** 进行自然连接来恢复 **library2** 关系；或者我们可以通过对所有三个关系进行自然连接来恢复原始的 **library** 关系。

        注意，规范化后的数据库在不同关系中有明确的关注点分离；一个关系仅涉及作者，另一个关系涉及书籍，还有一个关系提供关于图书馆布局的专门信息。冗余得到了减少，修改异常的可能性也大大降低。

    .. md-tab-item:: 英文

        We now apply this algorithm to a database initially composed of just the **library** relation.  To start, we previously noted that the FD

        .. math::

            \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

        violates 2NF and thus BCNF.  To apply the decomposition algorithm to this violation:

        1. Let *Y* be the closure of {author}, which is {author, author_birth, author_death}.
        2. Let *Z* then be {title, year, genre, section}.
        3. The union of *X* and *Y* is just *Y* because we did the optional closure in step 1.  The union of *X* and *Z* is {author, title, year, genre, section}.  Projecting on to these attribute sets yields the following relations, which we rename to **authors** and **library2**:

        .. table:: **authors**
            :class: lined-table

            ================= ============ ============
            author            author_birth author_death
            ================= ============ ============
            Ralph Ellison     1914-03-01   1994-04-16
            Jhumpa Lahiri     1967-07-11
            J.R.R. Tolkien    1892-01-03   1973-09-02
            Isabel Allende    1942-08-02
            Ursula K. Le Guin 1929-10-21   2018-01-22
            ================= ============ ============

        .. table:: **library2**
            :class: lined-table

            ================= ========================== ==== ================ ====================
            author            title                      year genre            section
            ================= ========================== ==== ================ ====================
            Ralph Ellison     Invisible Man              1952 fiction          literature
            Jhumpa Lahiri     Unaccustomed Earth         2008 fiction          literature
            J.R.R. Tolkien    The Hobbit                 1937 fantasy          speculative fiction
            Isabel Allende    The House of the Spirits   1982 magical realism  literature
            J.R.R. Tolkien    The Fellowship of the Ring 1954 fantasy          speculative fiction
            Ursula K. Le Guin The Dispossessed           1974 science fiction  speculative fiction
            ================= ========================== ==== ================ ====================

        4. Discard **library**.

        Note that we can recover the original relation by applying a natural join operation to **authors** and **library2**.

        We must now look at our new relations, and determine if they are now normalized.  A first step is determining keys and FDs for the new relations.  There is a formal process to compute the superkeys and FDs of the new relation from the FDs on the old relation [#]_.  However, in practice it is usually possible for a database designer to identify the FDs and keys of the new relations given their knowledge of the data, without all of the computations implied above.

        For our example, in **authors** we can quickly determine that the only useful non-trivial FD is

        .. math::

            \text{\{author\}} \rightarrow \text{\{author_birth, author_death\}}

        From this we can also see that the closure of {author} includes all attributes in authors, and thus {author} is a key.  There are no violating FDs remaining in this relation, so it is normalized with respect to BCNF.

        Now consider the relation **library2**.  Note that the FD above does not apply, because **author_birth** and **author_death** are not attributes in **library2**.  From our knowledge of the FDs in the **library** relation, we can determine that these FDs hold in **library2**:

        .. math::

            \begin{eqnarray*}
            \text{\{author, title\}} & \rightarrow & \text{\{year, genre, section\}} \\
            \text{\{genre\}} & \rightarrow & \text{\{section\}} \\
            \end{eqnarray*}

        and that the key is {author, title}.

        The second FD above violates BCNF (and 3NF).  Decomposing on this FD, we have *X* = {genre}, *Y* = {section}, and *Z* = {title, author, year, genre}.  Decomposition results in the following relations, which we rename to **books** and **genres**:

        .. table:: **books**
            :class: lined-table

            ================= ========================== ==== ================
            author            title                      year genre
            ================= ========================== ==== ================
            Ralph Ellison     Invisible Man              1952 fiction
            Jhumpa Lahiri     Unaccustomed Earth         2008 fiction
            J.R.R. Tolkien    The Hobbit                 1937 fantasy
            Isabel Allende    The House of the Spirits   1982 magical realism
            J.R.R. Tolkien    The Fellowship of the Ring 1954 fantasy
            Ursula K. Le Guin The Dispossessed           1974 science fiction
            ================= ========================== ==== ================

        .. table:: **genres**
            :class: lined-table

            =============== ===================
            genre           section
            =============== ===================
            fiction         literature
            fantasy         speculative fiction
            magical realism literature
            science fiction speculative fiction
            =============== ===================

        We discard **library2**, leaving us with just three relations: **authors**, **books**, and **genres**. All three relations are now in BCNF, so no further normalization (with respect to BCNF or lower) is possible.  We can recover the **library2** relation by a natural join of **books** and **genres**; or we can recover the original **library** relation by a natural join of all three relations.

        Note that the normalized database has a clear separation of concerns in the different relations; one relation is just about authors, another about books, and a third with specialized information about the layout of a library.  Redundancy has been reduced, and modification anomalies are much less likely.

分解属性
------------------------

*Decomposition properties*

.. md-tab-set::

    .. md-tab-item:: 中文

        规范化分解有两个理想的特性，我们将在本节中讨论。

    .. md-tab-item:: 英文

        There are two desirable properties for a normalization decomposition, which we discuss in this section.

精确恢复
##############

*Exact recovery*

.. md-tab-set::

    .. md-tab-item:: 中文

        我们提到的第一个性质是，原始关系必须能够通过连接分解结果来恢复。这意味着连接后的关系必须包含原始关系的所有元组，而没有额外的元组。这个性质是不可妥协的；关系的连接必须给出真实的答案。事实上，所呈现的BCNF分解算法满足这一条件；而任意分解则不一定满足。

        我们省略了分解算法正确性的完整证明。直观理解可以从考虑函数依赖的意义开始。某个函数依赖 :math:`X \rightarrow Y` 的存在告诉我们 *Y* 属性必须与 *X* 属性保持一致。 *X* 的任何不同值都可以与正好一个 *Y* 值的设置相关联；因此 *X* 唯一标识 *Y*。因此，如果我们有一个关系可以让我们查找每个不同 *X* 值对应的 *Y* 值，我们可以仅使用原始关系中的 *X* 属性作为 *X* 和 *Y* 的代表。分解算法正是创建了这种情况；对参与函数依赖的属性进行投影创建了“查找”关系（在我们第一个分解示例中为 **authors** ）； *X* 属性（**author**）作为外键保留，而 *Y* 属性（ **author_birth** 、 **author_death** ）可以被移除。基于共享外键的关系连接恢复了 *Y* 值到正确的元组中。

    .. md-tab-item:: 英文

        This first property we have mentioned, which is that the original relation must be recoverable by joining the decomposition products.  This means that the joined relation must have all of the tuples of the original, and no extra tuples.  This property is non-negotiable; a join of the relations must give true answers.  In fact, the BCNF decomposition algorithm as presented fulfills this condition; an arbitrary decomposition would not necessarily do so.

        We omit a full proof of the correctness of the decomposition algorithm.  An intuitive understanding begins with a consideration of the meaning of functional dependency.  The existence of some functional dependency :math:`X \rightarrow Y` tells us that the *Y* attributes must remain in lockstep with the *X* attributes.  Any distinct value of *X* can be associated with exactly one setting of *Y* values; so *X* uniquely identifies *Y*.  Therefore, if we have a relation that lets us look up the values for *Y* for each distinct value of *X*, we can use *just the* X *attributes* in the original relation as representative of both *X* and *Y*.  The decomposition algorithm creates exactly this situation; projection onto the attributes involved in the functional dependency creates the "lookup" relation (**authors** in our first decomposition example); the *X* attributes (**author**) remain as a foreign key and the *Y* attributes (**author_birth**, **author_death**) can be removed.  A join of the relations on the shared foreign key restores the *Y* values to the correct tuples.

依赖关系保存
#######################

*Dependency preservation*

.. md-tab-set::

    .. md-tab-item:: 中文

        第二个期望的分解属性 *并不* 总是通过BCNF分解来满足。这个第二个属性要求所有由原始函数依赖暗示的约束在分解后保留在数据库中。事实证明，我们可以通过将其规范化到3NF来保证这一属性，但不一定是BCNF。这一点通过一个例子来说明。

        考虑下面的关系，涉及到科幻类文学作品的雨果奖和星云奖。这两个奖项每年在多个类别中颁发，例如“最佳小说”、“最佳短篇小说”等。通常在某一年中，某一特定格式的作品只能赢得一个奖项（我们假设这个规则始终被执行，以便于示例）。因此，如果我们知道奖项、年份和格式，就可以明确地确定获奖作品。下面的关系给出了一些代表性的数据：

        .. table:: **scifi_awards**
            :class: lined-table

            ====== ==== =========== ================= ====================
            award  year format      author            title
            ====== ==== =========== ================= ====================
            Hugo   1975 novel       Ursula K. Le Guin The Dispossessed
            Hugo   1975 short story Larry Niven       The Hole Man
            Hugo   1974 novel       Arthur C. Clarke  Rendezvous With Rama
            Nebula 1975 novel       Joe Haldeman      The Forever War
            Nebula 1974 novel       Ursula K. Le Guin The Dispossessed
            ====== ==== =========== ================= ====================

        有两个重要的函数依赖。第一个反映了每种格式中每年只能有一部作品获奖的规则：

        .. math::

            \text{\{award, year, format\}} \rightarrow \text{\{author, title\}}

        第一个约束不违反3NF或BCNF，因为左侧是关系的一个键。

        第二个FD承认每部作品属于特定格式；作品可以是小说或短篇小说，但不能同时是两者：

        .. math::

            \text{\{author, title\}} \rightarrow \text{\{format\}}

        这个关系属于在3NF但不在BCNF的狭窄类别。正如本例所示，这种情况发生在关系包含属性集 *A*、*B* 和 *C*，并且有 :math:`AB \rightarrow C` 和 :math:`C \rightarrow B`。第二个FD违反BCNF，因为 {author, title} 不是该关系的一个键（如上面的示例数据所示）。然而，这个FD并不违反3NF，因为右侧（{format}）是关系键的一部分。

        如果我们按BCNF的违反进行常规分解，直接的分解结果必须连接在一起以返回原始关系，从而拥有正确的数据，因此这并不是问题。然而，经过分解后，我们有了属性为 {author, title, format} 和 {award, year, author, title} 的关系。上述第一个FD，即限制每年每种格式只能有一部作品获奖的约束，现在不再适用于任何一个关系。这些新关系无法防止我们存储如下数据：

        .. table:: **scifi_awards_1**
            :class: lined-table

            ================= ==================== ======
            author            title                format
            ================= ==================== ======
            Ursula K. Le Guin The Dispossessed     novel
            Roger Zelazny     Doorways in the Sand novel
            ================= ==================== ======

        .. table:: **scifi_awards_2**
            :class: lined-table

            ===== ==== ================= ====================
            award year author            title
            ===== ==== ================= ====================
            Hugo  1975 Ursula K. Le Guin The Dispossessed
            Hugo  1975 Roger Zelazny     Doorways in the Sand
            ===== ==== ================= ====================

        由于雨果奖在某一年颁给多部作品（只是因为作品的不同类别），第二个关系中的数据 *可能* 是有效的——但前提是这两部作品确实属于不同的类别。然而，正如第一个关系所示，它们实际上属于同一类别（实际上，第二个关系包含了错误数据）。只有在连接这两个关系后，我们才能看到约束被违反。

        在这个特定的案例中，保留原始关系在3NF，并用由 {award, year, format} 组成的主键来保持约束，将是更可取的。考虑到作品在关系中最多只能出现两次（因为我们只有两个奖项），涉及的冗余是小的。然而，如果你遇到这种情况，你必须确定适合你特定案例的最佳解决方案。如果你将关系保留在3NF，那么你必须管理BCNF违反所暗示的修改异常（在应用软件中或通过其他机制）。如果你将关系移到BCNF，那么你必须以其他方式强制执行丢失的约束。

    .. md-tab-item:: 英文

        A second desirable property for a decomposition is *not* always met with BCNF decomposition.  This second property requires that all constraints implied by the original functional dependencies are preserved in the database after decomposition.  It turns out that we can guarantee this property by normalizing to 3NF, but not BCNF.  This is best illustrated with an example.

        Consider the relation below, regarding the Hugo and Nebula awards for literary and other works in the science fiction genre.  These two awards are given each year in multiple categories, such as "Best Novel", "Best Short Story" and so forth.  Typically only one work in a given format in a given year wins a given award (we will assume that rule is always enforced for example purposes).  Therefore, if we are given the award, year, and format, we can unambiguously determine the award winning work.  The relation below gives some representative data:

        .. table:: **scifi_awards**
            :class: lined-table

            ====== ==== =========== ================= ====================
            award  year format      author            title
            ====== ==== =========== ================= ====================
            Hugo   1975 novel       Ursula K. Le Guin The Dispossessed
            Hugo   1975 short story Larry Niven       The Hole Man
            Hugo   1974 novel       Arthur C. Clarke  Rendezvous With Rama
            Nebula 1975 novel       Joe Haldeman      The Forever War
            Nebula 1974 novel       Ursula K. Le Guin The Dispossessed
            ====== ==== =========== ================= ====================

        There are two important functional dependencies.  The first, reflecting the rule that only one work in each format can win a particular award in a given year, is

        .. math::

            \text{\{award, year, format\}} \rightarrow \text{\{author, title\}}

        The first constraint does not violate 3NF or BCNF, because the left-hand side is a key for the relation.

        The second FD acknowledges that each work is in a particular format; a work may be a novel or a short story, but not both:

        .. math::

            \text{\{author, title\}} \rightarrow \text{\{format\}}

        This relation falls into the narrow category of relations that are in 3NF but not in BCNF.  As in this example, this occurs when the relation contains sets of attributes *A*, *B*, and *C*, with :math:`AB \rightarrow C` and :math:`C \rightarrow B`.  The second FD violates BCNF, because {author, title} is not a key for this relation (as demonstrated in the example data above).  However, the FD does not violate 3NF, because the right-hand side ({format}) is part of a key for the relation.

        If we decompose as usual on the BCNF violation, the immediate decomposition products must join together to return the original relation, which has correct data, so that is not a problem.  However, after decomposition, we have relations with attributes {author, title, format} and {award, year, author, title}.  The first FD above, which enforced the constraint of an award going to only one work in each format each year, no longer applies to either relation.  The new relations cannot prevent us storing data such as the following:

        .. table:: **scifi_awards_1**
            :class: lined-table

            ================= ==================== ======
            author            title                format
            ================= ==================== ======
            Ursula K. Le Guin The Dispossessed     novel
            Roger Zelazny     Doorways in the Sand novel
            ================= ==================== ======

        .. table:: **scifi_awards_2**
            :class: lined-table

            ===== ==== ================= ====================
            award year author            title
            ===== ==== ================= ====================
            Hugo  1975 Ursula K. Le Guin The Dispossessed
            Hugo  1975 Roger Zelazny     Doorways in the Sand
            ===== ==== ================= ====================

        Since the Hugo award is given to multiple works in a given year (just for different categories of work), the data in the second relation *could be* valid - but only if the two works listed happen to be in different categories.  However, as the first relation shows, they are in the same category (the second relation, as it happens, contains false data).  Only if we join these two relations can we see that we have violated our constraint.

        In this particular case, it would be preferable to leave the original relation in 3NF and preserve the constraint with a primary key composed of {award, year, format}.  The redundancy involved is small, given that works can appear at most twice in the relation (since we only have the two awards).  If you encounter such a situation, however, you must determine the best way forward for your particular case.  If you leave the relation in 3NF, then you must manage the modification anomalies implied implied by the BCNF violation (in the application software, or some other mechanism).  If you move the relation to BCNF, then you must enforce the lost constraint in some other fashion.

.. index:: multivalued dependency, fourth normal form, 4NF

多值依赖关系和第四范式
:::::::::::::::::::::::::::::::::::::::::::::::

*Multivalued dependencies and fourth normal form*

.. md-tab-set::

    .. md-tab-item:: 中文

        违反BCNF的关系在正常的数据收集活动中经常出现。例如，一个记录活动日志的网络服务器可能会记录用户信息以及用户在网站上访问的页面的信息。在多个日志条目中出现相同的用户信息时，冗余就显而易见。

        相比之下，第四范式（4NF）违反不太可能在数据收集过程中发生。4NF解决的问题是当试图将包含多个独立一对多关系的数据存储在单个关系中时所出现的问题。在这种情况下的冗余更加微妙，且更难以识别。

        作为一个例子，我们将考虑一些授予文学成就的许多奖项。有些奖项授予作者（如诺贝尔文学奖、纽斯塔特国际文学奖），而不涉及特定作品。另一些奖项（如普利策奖、星云奖）则是对特定作品的认可。一个作者可以获得任一类型的多个奖项。如果我们在设计时不谨慎，可能会得出如下的关系：

        .. table:: **authors_and_awards**
            :class: lined-table

            =============== =========================== ===================================
            author          author_award                book_award
            =============== =========================== ===================================
            Louise Glück    Nobel Prize                 Pulitzer Prize
            Louise Glück    Nobel Prize                 National Book Award
            John Steinbeck  Nobel Prize                 Pulitzer Prize
            Alice Munro     Nobel Prize                 Giller Prize
            Alice Munro     International Booker Prize  Giller Prize
            Alice Munro     Nobel Prize                 National Book Critics Circle Award
            Alice Munro     International Booker Prize  National Book Critics Circle Award
            =============== =========================== ===================================

        这只是一个示例；我们可能希望在关系中包含其他属性，例如每个奖项获奖的年份，或者某个书籍奖项获奖的书名，但这些额外的属性会转移我们试图解决的中心问题。

        乍一看，这个关系中似乎存在许多冗余。例如，我们有两个元组显示Louise Glück获得诺贝尔奖，Alice Munro也是如此。我们在两个不同的元组中显示Alice Munro获得Giller奖 [#]_ 。然而，对于这个关系，没有任何非平凡的函数依赖。该关系的唯一键是集合 {author, author_award, book_award}，因此每个元组都是唯一的。因此，该关系处于BCNF中。

        这里的模式指示了一种称为 *多值依赖* （MVD）的情况。MVD的正式定义相当晦涩，我们在此不进行阐述。非正式地说，我们有属性子集 *A*、*B* 和 *C*，对于给定的 *A*，每个 *B* 的不同值必须与与 *A* 相关联的每个 *C* 的不同值配对。当这成立时，我们称 *A* *多决定* *B*，并写作：

        .. math::

            A \twoheadrightarrow B

        这个情况也是对称的；当 *A* 多决定 *B* 时，它也多决定 *C*。因此我们可以写作：

        .. math::

            A \twoheadrightarrow B|C

        在我们的例子中，考虑Alice Munro和她的诺贝尔奖，她获得了哪些书籍奖项？答案必须包括Giller奖和全国图书评论圈奖。考虑她的国际布克奖时，答案也是如此。我们可以考虑Alice Munro和她的Giller奖，问她获得了哪些作者奖项；这次答案包括她的诺贝尔奖和国际布克奖。因此，对于该关系，MVD

        .. math::

            \text{\{author\}} \twoheadrightarrow \text{\{author_award\}} | \text{\{book_award\}}

        成立。

        第四范式的定义看起来与BCNF的定义非常相似，只是将MVD替代为FD：

        **第四范式的定义**
            如果对于关系中的每个非平凡多值依赖形式 :math:`X \twoheadrightarrow Y`，*X* 是该关系的超键，则该关系处于4NF。

        显然在我们的示例关系中，集合 {author} 不是超键，因此该关系不在4NF。4NF违反的解决方案恰好与BCNF违反的解决方案相同。给定一个违反4NF的MVD :math:`X \twoheadrightarrow Y`，我们将其分解为两个关系，一个包含属性 *XY*，另一个包含属性 *XZ*，其中 *Z* 是不在 *X* 或 *Y* 中的所有内容（*Z* 也如上所述由 *X* 多决定）。分解消除了独立概念的配对。在我们的例子中，分解产生：

        .. table:: **author_awards**
            :class: lined-table

            =============== ===========================
            author          author_award
            =============== ===========================
            Louise Glück    Nobel Prize
            John Steinbeck  Nobel Prize
            Alice Munro     Nobel Prize
            Alice Munro     International Booker Prize
            =============== ===========================

        .. table:: **author_book_awards**
            :class: lined-table

            =============== ===================================
            author          book_award
            =============== ===================================
            Louise Glück    Pulitzer Prize
            Louise Glück    National Book Award
            John Steinbeck  Pulitzer Prize
            Alice Munro     Giller Prize
            Alice Munro     National Book Critics Circle Award
            =============== ===================================

        MVD的正式定义是足够一般的，以至于每个FD都符合MVD的条件。因此，处于4NF的关系也在BCNF中。

    .. md-tab-item:: 英文

        Relations that violate BCNF frequently occur in normal data collection activities.  For example, a web server keeping activity logs might record user information along with information about the pages the user visits on the website.  Redundancy is apparent in the user information appearing identically in multiple log entries.

        In contrast, fourth normal form (4NF) violations are unlikely to occur in data gathering.  Instead, 4NF addresses problems that occur when an attempt is made to store data that includes multiple independent one-to-many relationships in a single relation.  Redundancy in this setting is more subtle and harder to identify.

        For an example, we will consider some of the many awards given for literary merit.  Some awards are given to authors (Nobel Prize in Literature, Neustadt International Prize for Literature) without reference to a specific work.  Others (Pulitzer Prize, Nebula Award) are given in recognition of specific works.  An author can win multiple awards of either type.  If we are incautious in our design, we might come up with a relation like the following:

        .. table:: **authors_and_awards**
            :class: lined-table

            =============== =========================== ===================================
            author          author_award                book_award
            =============== =========================== ===================================
            Louise Glück    Nobel Prize                 Pulitzer Prize
            Louise Glück    Nobel Prize                 National Book Award
            John Steinbeck  Nobel Prize                 Pulitzer Prize
            Alice Munro     Nobel Prize                 Giller Prize
            Alice Munro     International Booker Prize  Giller Prize
            Alice Munro     Nobel Prize                 National Book Critics Circle Award
            Alice Munro     International Booker Prize  National Book Critics Circle Award
            =============== =========================== ===================================

        This is just an illustration; we would probably want to include other attributes to our relation such as the year each award was won, or the book for which a book award was won, but these extra attributes distract from the central concern we are trying to address.

        At a casual glance it appears that there are many redundancies in this relation.  For example, we have two tuples showing that Louise Glück won a Nobel Prize, and the same for Alice Munro.  We show Alice Munro winning the Giller Prize in two different tuples [#]_.  For this relation, however, there are no non-trivial functional dependencies whatsoever.  The only key for the relation is the set {author, author_award, book_award}, so each tuple is unique.  Therefore the relation is in BCNF.

        The pattern here is indicative of something called a *multivalued dependency* (MVD).  The formal definition of an MVD is rather opaque, and we will not state it here.  Informally, we have subsets of attributes *A*, *B*, and *C*, such that, for a given *A*, every distinct value of *B* must be paired with every distinct value of *C* associated with the value of *A*.  When this is true we state that *A* *multidetermines* *B*, and write

        .. math::

            A \twoheadrightarrow B

        The situation is also symmetric; when *A* multidetermines *B* it also multidetermines *C*.  Thus we may write

        .. math::

            A \twoheadrightarrow B|C

        In our example, considering Alice Munro and her Nobel Prize, what book awards did she win?  The answer must include both the Giller Prize and the National Book Critics Circle Award.  The same answer applies when we consider her International Booker Prize.  We might instead consider Alice Munro and her Giller prize and ask what author awards she won; this time the answer would include her Nobel Prize and her International Booker Prize.  Thus, for this relation the MVD

        .. math::

            \text{\{author\}} \twoheadrightarrow \text{\author_award\}} | \text{\{book_award\}}

        holds.

        The definition of fourth normal form looks much like the definition of BCNF, substitution MVD for FD:

        **Definition of 4NF**
            A relation is in 4NF if, for every non-trivial multivalued dependency of the form :math:`X \twoheadrightarrow Y` on the relation, *X* is a superkey of the relation.

        Clearly in our example relation, the set {author} is not a superkey, so the relation is not in 4NF.  The solution to a 4NF violation happens to be identical to the solution for a BCNF violation.  Given an MVD :math:`X \twoheadrightarrow Y` that violates 4NF, we decompose into two relations, one with the attributes in *XY*, and the other with the attributes in *XZ*, where *Z* is everything not in *X* or *Y* (*Z* is also multidetermined by *X* as discussed above).  The decomposition eliminates the pairing of independent concepts.  For our example, the decomposition yields:

        .. table:: **author_awards**
            :class: lined-table

            =============== ===========================
            author          author_award
            =============== ===========================
            Louise Glück    Nobel Prize
            John Steinbeck  Nobel Prize
            Alice Munro     Nobel Prize
            Alice Munro     International Booker Prize
            =============== ===========================

        .. table:: **author_book_awards**
            :class: lined-table

            =============== ===================================
            author          book_award
            =============== ===================================
            Louise Glück    Pulitzer Prize
            Louise Glück    National Book Award
            John Steinbeck  Pulitzer Prize
            Alice Munro     Giller Prize
            Alice Munro     National Book Critics Circle Award
            =============== ===================================

        The formal definition of MVD is sufficiently general that every FD qualifies as an MVD.  Therefore, a relation in 4NF is also in BCNF.

权衡
::::::::::

*Trade-offs*

.. md-tab-set::

    .. md-tab-item:: 中文

        正如我们所见，规范化的过程会导致关系的数量增加（通常较小）。尽管关系数量激增，规范化实际上简化了应用软件，因为它消除了修改异常和相关问题。较小的关系也可能带来适度的空间节省，并且对关系进行单独查询的速度更快。然而，当一个查询需要从许多不同的关系中收集数据时，性能可能会受到影响。尤其是在涉及大量数据时，连接操作对于关系数据库系统来说变得非常昂贵。

        因此，有时创建一个 *反规范化* 数据库是可取的，其中数据被存储在一个或多个大型关系中，表示将多个关系合并的结果。这样的决定不应轻率做出，而应考虑到修改异常的影响。一种流行的方法是创建两个包含相同数据的数据库，而不是一个。在这种方法中，一个数据库是完全规范化的，用于处理数据更新。另一个反规范化数据库仅用于只读查询，可能仅定期更新（可能是每日或每小时）。反规范化数据库的用户会获得稍微过时的答案，但速度更快。

    .. md-tab-item:: 英文

        As we have seen, the process of normalization leads to increased numbers of (generally smaller) relations.  Despite this proliferation of relations, normalization actually simplifies application software due to eliminating modification anomalies and related issues.  Smaller relations may also provide modest space savings, and performing queries on the relations in isolation will be faster.  However, when a query requires data collected into many different relations, performance can suffer.  Particularly when large volumes of data are involved, join operations become expensive for relational database systems.

        As a result, there are occasions when it is desirable to create a *de-normalized* database, in which data is held in one or more large relations representing the result of joining together numerous relations.  Such a decision should not be made lightly and without consideration for the impact of modification anomalies.  One popular approach creates not one, but two databases containing the same data.  In this approach, one database is fully normalized and is used to process data updates.  The other, de-normalized database is used solely for read-only queries, and may be updated (or re-created) only periodically (perhaps daily or hourly).  Users of the de-normalized database receive slightly out-of-date answers, but faster.

数据库设计中的规范化
::::::::::::::::::::::::::::::::

*Normalization in database design*

.. md-tab-set::

    .. md-tab-item:: 中文

        数据库可以通过多种方法创建。所采取的方法在很大程度上取决于导致需要数据库的具体情况。

        在某些情况下，数据可能之前已经以某种方式收集并存储，但并没有组织成我们认为的数据库。许多科学、工业和商业流程会产生大量数据，例如传感器读数、应用日志、报告和表单响应。这些数据可能存在于电子形式或纸质形式。数据可能几乎没有结构；它可能以 *扁平(flat)* 形式存在，其中只有一种类型的记录存储与某个事件相关的所有信息。创建一个数据库以更有效地处理这些数据，最好采用自上而下的方法，通过系统性地分解关系来实现。数据建模（:numref:`Part {number} <data-modeling-part>`）可以作为这个过程的一部分，用于记录、沟通和推理不断发展的数据库。

        相反，在创建新的软件应用程序时，可能更倾向于自下而上的方法。应用程序开发人员和其他相关方努力识别需要收集和存储的数据属性。多个关系自然出现，分别对应应用程序的不同部分。数据建模通常应该在这个过程的早期进行。

        数据建模在生成准确表示独立概念及其之间关系的关系方面非常有效。然而，有些关系可能仍然需要规范化。规范化提供了对数据库设计的不同视角。与数据建模一样，我们对现实世界和数据的理解会影响我们的选择。然而，数据建模专注于将现实世界中的概念映射到关系，而规范化则旨在产生对数据错误更具抵抗力的数据库结构。数据建模确保我们的数据库准确捕获所需的数据，而规范化则确保我们的数据库可以有效使用。因此，这两项活动是互补的。无论是否正式应用规范化，理解规范化及其权衡对任何数据库设计师来说都是重要的。

    .. md-tab-item:: 英文

        Databases can be created using a number of approaches.  The approach taken depends greatly on the circumstances which have led to the need for a database.

        In some cases, data have been previously collected and stored in some fashion, but not organized into something we would consider a database.  Many scientific, industrial, and business processes produce large amounts of data in the form of sensor readings, application logs, reports, and form responses.  This data may exist in electronic form or on paper.  There may be little structure to the data; it may exist in a *flat* form in which there is only one type of record which stores every piece of information relevant to some event.  Creating a database to more efficiently work with such data may be best accomplished using a top-down approach, in which relations are systematically decomposed.  Data modeling (:numref:`Part {number} <data-modeling-part>`) may be used as part of this process, to document, communicate, and reason about the evolving database.

        In contrast, when creating a new software application, a bottom-up approach may be preferred.  The application developers and other interested parties work to identify the data attributes that need to be collected and stored.  Multiple relations emerge naturally, corresponding to different parts of the application.  Data modeling should almost always occur early in this process.

        Data modeling is very effective at producing relations that accurately represent independent concepts and the relationships between them.  However, some relations may still require normalization.  Normalization provides a different perspective on database design.  As with data modeling, our understanding of the real world and our data informs our choices.  However, while data modeling focuses on mapping concepts in the real world to relations, normalization works to produce a database structure that is more resistant to data errors.  Data modeling ensures our database accurately captures the data we need, while normalization ensures our database can be used effectively.  The two activities are thus complementary.  Whether or not normalization is applied formally, an understanding of normalization and its trade-offs is important for any database designer.




----

**Notes**

.. [#] 当信息确实未知或缺失时，我们可能需要使用 NULL；例如，对于当前没有分配讲师的课程，我们会将 **instructor** 属性设置为 NULL。类似地，对于尚未拥有办公室的新讲师，我们可能会将 **office** 属性设置为 NULL。这两种情况都不需要在我们的软件中进行特殊处理，因此我们认为这些 NULL 是可以接受的。虽然有可能设计一个甚至避免这些 NULL 的数据库，但这样会使数据库复杂化（增加更多关系），而收益很小。

.. [#] We may need to use NULLs when information is truly unknown or absent; for example, we would set the **instructor** attribute NULL for classes which have no instructor assigned at the current time.  Similarly, we might set the **office** attribute NULL for new instructors who do not yet have an office.  Neither of these cases requires special handling in our software, so we consider these NULLs acceptable.  While it is possible to design a database that avoids even these NULLs, it would complicate the database (with more relations) for little gain.

.. [#] 在一些以英语为主要语言的国家，将姓名分为名（或给定名）、中间名和姓（或姓氏）是常见做法。然而，这种命名方案并不是普遍适用的，即使对英语使用者而言也是如此。除非有强烈的需求将姓名拆分为组件，否则我们建议使用单一的姓名属性。有关此主题的更多信息，请参见 https://www.w3.org/International/questions/qa-personal-names。

.. [#] It is common practice in some countries where English is the primary language to break a name into first (or given), middle, and last name (or surname).  However, this naming scheme is by no means universal, even for English speakers.  Unless there is a compelling need to break a name into components for your application, we recommend a single name attribute.  For more on this topic, see https://www.w3.org/International/questions/qa-personal-names.

.. [#] 我们重申，超键是我们对数据施加的约束。在设计数据库时，我们当然希望创建一个能够容纳现实世界真实事实的结构，但 a) 由于对世界信息的不足，我们有时会失败，b) 我们有时会妥协，选择一个能够容纳 *大多数* 事实的更简单设计。对于我们的 **simple_books** 关系，我们不知道是否有同一作者在同一年出版的同名书籍，因此我们可以自信地断言 {**author**, **title**, **year**} 是一个有效的超键（但我们可能是错的）。另一方面，这种设计故意未能捕捉现实世界中书籍的许多复杂性。举个例子，作者偶尔会在原始出版多年后，以相同的书名重新出版稍作修改的书籍。这是同一本“书”（在这种情况下，**year** 实际上代表“首次出版年份”），还是不同的书（在这种情况下，{**author**, **title**} 不是超键）？另一个例子是，我们完全忽略了一些书籍有多个作者，或一些书籍没有已知作者的事实。关于书籍的数据库可以非常复杂！

.. [#] We reiterate that a superkey is a constraint *we impose* on the data.  When designing a database, we of course hope to create a structure that accommodates true facts from the world, but a) we sometimes fail due to incomplete information about the world, and b) we sometimes compromise on a simpler design that accommodates *most* facts from the world.  For our **simple_books** relation, we are unaware of any books by the same author with the same title in the same year, so we are comfortable asserting that {**author**, **title**, **year**} is a valid superkey (but we could be wrong).  On the other hand, this design intentionally fails to capture any number of the complexities of books in the real world.  For one example, authors occasionally re-publish a book with small changes, under the same title, years after the original publication.  Is this the same "book" (in which case **year** really stands for "year of first publication"), or a different book (in which case {**author**, **title**} is *not* a superkey)?  For another example, we are completely ignoring the fact that some books have multiple authors, and some have no known authors.  Databases about books can be very complex!

.. [#] 以 Raymond F. Boyce 和 Edgar F. Codd 的名字命名，他们在 1974 年发布了一篇 :ref:`论文 <relational-theory-references>` 定义了这一范式。然而，Ian Heath 在 1971 年的一篇论文中早先给出了描述。

.. [#] Named after Raymond F. Boyce and Edgar F. Codd, who published a :ref:`paper <relational-theory-references>` in 1974 defining this normal form.  However, a 1971 paper by Ian Heath gave a prior description.

.. [#] 给定 *R* 和 *R1* 以及在 *R1* 上的一组 FD，对于 *R1* 属性的每个子集 *X*，计算在 *R* 中的闭包 *X*:sup:`+`。对于 *R1* 的每个属性 *a*，如果它在 *X* 的闭包中，根据拆分规则，:math:`X \rightarrow \{a\}` 是 *R1* 的一个 FD。如果 *X*:sup:`+` 包含 *R1* 的每个属性，则 *X* 是 *R1* 的一个超键。

.. [#] Given *R* and *R1* and a collection of FDs on R1, for every subset *X* of the attributes of *R1*, compute the closure, *X*:sup:`+` in *R*. For every attribute *a* of *R1* that is in the closure of *X*, by the splitting rule, :math:`X \rightarrow \{a\}` is an FD for *R1*. If *X*:sup:`+` contains every attribute of *R1*, then *X* is a superkey of *R1*.

.. [#] 实际上，Alice Munro 在不同年份赢得了两次 Giller Prize；如果我们包含一个年份属性，我们就必须将 Alice Munro 的条目数量翻倍！

.. [#] As it happens, Alice Munro won two Giller Prizes, in different years; if we included an attribute for year, we would have to double the number of entries for Alice Munro!


