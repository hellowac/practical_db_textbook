.. _relational-algebra-chapter:

==================
关系代数
==================

**Relational algebra**

.. index:: relational algebra; relational calculus

.. md-tab-set::

    .. md-tab-item:: 中文

        在上一章中，我们介绍了数据库的关系模型，并定义了模型中的基本数学对象—— *关系(relation)*。在本章中，我们讨论 *关系代数(relational algebra)* ，它是可以对关系执行的一组代数运算。关系代数可以看作是表达存储在关系中的数据查询的一种机制，理解关系代数对于理解关系数据库如何表示和优化查询非常重要。我们将仅覆盖基本的关系代数，排除后来的扩展，如分组和聚合操作以及外连接。

        一个相关的话题是 *关系演算(relational calculus)* ，但我们在本书中不予覆盖。关系演算提供了对关系查询的另一种数学表达，其表达能力与关系代数相等。

    .. md-tab-item:: 英文

        In the last chapter, we introduced the relational model of the database, and defined the fundamental mathematical object in the model, the *relation*.  In this chapter, we discuss *relational algebra*, which is the set of algebraic operations that can be performed on relations.  Relational algebra can be viewed as one mechanism for expressing queries on data stored in relations, and an understanding of relational algebra is important in understanding how relational databases represent and optimize queries.  We will cover only basic relational algebra, excluding later extensions such as those for group and aggregate operations and those for outer joins.

        A related topic, which we do not cover in this book, is *relational calculus*.  Relational calculus provides another mathematical expression of queries on relations, and is equivalent in expressiveness to relational algebra.

一元运算
::::::::::::::::

**Unary operations**

.. index:: selection, projection, renaming, relational algebra operations; selection, relational algebra operations; projection, relational algebra operations; renaming

.. md-tab-set::

    .. md-tab-item:: 中文

        关系代数中的一元运算作用于一个关系并产生另一个关系。一元运算包括 *选择* 、 *投影* 和 *重命名* ，其相关操作符通常用与运算名称首字母相匹配的希腊字母表示：

        - :math:`\sigma` (sigma): 选择(selection)
        - :math:`\pi` (pi): 投影(projection)
        - :math:`\rho` (rho): 重命名(renaming)

        我们将探讨这些一元运算符在下面的 **books** 关系中的应用：

        .. table:: **books**
            :class: lined-table

            ======= ========= ============================ ====
            book_id author_id title                        year
            ======= ========= ============================ ====
            1       3         *The House of the Spirits*   1982
            2       1         *Invisible Man*              1952
            3       6         *The Hobbit*                 1937
            4       2         *Unaccustomed Earth*         2008
            5       6         *The Fellowship of the Ring* 1954
            6       4         *House Made of Dawn*         1968
            7       5         *A Wizard of Earthsea*       1968
            ======= ========= ============================ ====

        **books** 关系的主键是 **book_id**，而 **author_id** 是指向我们将在本章后面使用的另一个表的外键。

    .. md-tab-item:: 英文

        The unary operations in relational algebra act on one relation and result in another relation.  The unary operations are *selection*, *projection*, and *renaming*, and their associated operators are typically written as the Greek letters which match the starting letters of the operation:

        - :math:`\sigma` (sigma): selection
        - :math:`\pi` (pi): projection
        - :math:`\rho` (rho): renaming

        We will explore each of these unary operators in application to the relation **books** shown below:

        .. table:: **books**
            :class: lined-table

            ======= ========= ============================ ====
            book_id author_id title                        year
            ======= ========= ============================ ====
            1       3         *The House of the Spirits*   1982
            2       1         *Invisible Man*              1952
            3       6         *The Hobbit*                 1937
            4       2         *Unaccustomed Earth*         2008
            5       6         *The Fellowship of the Ring* 1954
            6       4         *House Made of Dawn*         1968
            7       5         *A Wizard of Earthsea*       1968
            ======= ========= ============================ ====

        The **books** relation has primary key **book_id**, while **author_id** is a foreign key to another table we will use later in this chapter.

选择
---------

**Selection**

.. md-tab-set::

    .. md-tab-item:: 中文

        选择运算对关系中的元组应用布尔条件。选择操作的结果是一个关系，包含正好那些使选择条件为真的元组。例如，如果我们对1960年以后出版的书籍感兴趣，可以写出选择操作以检索这些书籍：

        .. math::

            \sigma_{\text{year} > 1960}(\text{books})

        操作符以布尔条件作为下标，然后在括号中给出操作数（输入关系）。请注意，布尔条件指的是 **books** 关系中的一个属性，并将其与一个常量值进行比较。此操作的结果是一个与 **books** 具有相同模式的关系，但没有名称：

        .. table::
            :class: lined-table

            ======= ========= ============================ ====
            book_id author_id title                        year
            ======= ========= ============================ ====
            1       3         *The House of the Spirits*   1982
            4       2         *Unaccustomed Earth*         2008
            6       4         *House Made of Dawn*         1968
            7       5         *A Wizard of Earthsea*       1968
            ======= ========= ============================ ====

        关系代数中的简单布尔表达式通常涉及一个属性与常量的比较，使用任何比较运算符。更复杂的布尔表达式可以通过使用 **AND**、 **OR** 和 **NOT** 从简单表达式构造。例如，如果我们对1960年后出版的书籍以及 **author_id** 等于6的书籍感兴趣，我们可以写：

        .. math::

            \sigma_{\text{year} > 1960 \text{ OR } \text{author_id} = 6}(\text{books})

        选择操作的结果可以是一个包含原始关系中所有元组的关系（与原始关系等效），也可以是一些原始元组，或者完全没有元组（一个空集）。在空关系的情况下，我们仍然认为该关系具有与原始关系相同的模式。

        由于选择的结果是一个关系，我们可以对结果应用另一个选择。例如，我们可以找到1950年后出版的书籍，然后从该结果中选择 **author_id** 等于6的书籍：

        .. math::

            \sigma_{\text{author_id} = 6}(\sigma_{\text{year} > 1950}(\text{books}))

        这将给我们一个结果，其中包含一个元组：

        .. table::
            :class: lined-table

            ======= ========= ============================ ====
            book_id author_id title                        year
            ======= ========= ============================ ====
            5       6         *The Fellowship of the Ring* 1954
            ======= ========= ============================ ====

        这种选择操作的组合等同于使用选择条件的 *合取(conjunction)* （AND）进行单一选择操作：

        .. math::

            \sigma_{\text{author_id} = 6 \text{ AND } \text{year} > 1950}(\text{books})

    .. md-tab-item:: 英文

        Selection applies a Boolean condition to the tuples in a relation.  The result of a selection operation is a relation containing exactly those tuples for which the selection condition is true.  For example, if we are interested in books published after 1960, we can write the selection operation to retrieve just those books as:

        .. math::

            \sigma_{\text{year} > 1960}(\text{books})

        The operator is written with the Boolean condition as a subscript, and then the operand (the input relation) is given in parentheses.  Note that the Boolean condition refers to an attribute of the **books** relation, comparing it to a constant value.  The result of this operation is a relation with the same schema as **books**, but with no name:

        .. table::
            :class: lined-table

            ======= ========= ============================ ====
            book_id author_id title                        year
            ======= ========= ============================ ====
            1       3         *The House of the Spirits*   1982
            4       2         *Unaccustomed Earth*         2008
            6       4         *House Made of Dawn*         1968
            7       5         *A Wizard of Earthsea*       1968
            ======= ========= ============================ ====

        Simple Boolean expressions in the relational algebra usually involve comparisons of an attribute with a constant, using any comparison operator.  More complex Boolean expressions can be constructed from simple expressions using **AND**, **OR**, and **NOT**.  For instance, if we are interested in books published after 1960 as well as books by the author with **author_id** equal to 6, we could write:

        .. math::

            \sigma_{\text{year} > 1960 \text{ OR } \text{author_id} = 6}(\text{books})

        Selection can result in a relation that has all of the tuples from the original (a relation equivalent to the original), some of the tuples from the original, or no tuples at all (an empty set).  In the case of an empty relation, we still consider the relation to have the same schema as the original relation.

        Since the result of a selection is a relation, we can apply another selection to the result.  For example, we could find the books published after 1950, and then select from that result the books with **author_id** equal to 6:

        .. math::

            \sigma_{\text{author_id} = 6}(\sigma_{\text{year} > 1950}(\text{books}))

        This would give us a result with one tuple:

        .. table::
            :class: lined-table

            ======= ========= ============================ ====
            book_id author_id title                        year
            ======= ========= ============================ ====
            5       6         *The Fellowship of the Ring* 1954
            ======= ========= ============================ ====

        This composition of selection operations is equivalent to a single selection operation using a *conjunction* (AND) of the selection conditions:

        .. math::

            \sigma_{\text{author_id} = 6 \text{ AND } \text{year} > 1950}(\text{books})

投影
----------

**Projection**

.. md-tab-set::

    .. md-tab-item:: 中文

        投影操作创建一个新关系，该关系具有输入关系的属性子集。例如，我们可以使用投影来获取一个元组集合，仅表示书籍的标题和出版年份。我们将投影操作符写成属性名称列表作为下标，后面跟着括号中的操作数：

        .. math::

            \pi_{\text{title, year}}(\text{books})

        这个结果包含 **books** 中每个元组的一个元组，但结果中的元组仅具有投影操作指定的属性，因此结果关系与原始关系具有不同的模式：

        .. table::
            :class: lined-table

            ============================ ====
            title                        year
            ============================ ====
            *The House of the Spirits*   1982
            *Invisible Man*              1952
            *The Hobbit*                 1937
            *Unaccustomed Earth*         2008
            *The Fellowship of the Ring* 1954
            *House Made of Dawn*         1968
            *A Wizard of Earthsea*       1968
            ============================ ====

        乍一看，投影的结果似乎总是与输入关系具有相同数量的元组，但实际上并非如此。考虑如果我们将 **books** 投影到单个属性 **year** 时会发生什么。**books** 中有两个元组具有相同的 **year** 值 1968。由于关系不能包含重复项，我们的投影操作的结果只能包含一个 **year** 等于 1968 的元组。因此，结果的元组数量比输入关系 *少*：

        .. table:: :math:`\pi_{\text{year}}(\text{books})`
            :class: lined-table

            +------+
            | year |
            +======+
            | 1982 |
            +------+
            | 1952 |
            +------+
            | 1937 |
            +------+
            | 2008 |
            +------+
            | 1954 |
            +------+
            | 1968 |
            +------+

        由于投影的结果是一个关系，我们可以对结果应用选择：

        .. math::

            \sigma_{\text{year}=1968}(\pi_{\text{title, year}}(\text{books}))

        注意这里的操作顺序：首先，我们将 **books** 作为输入提供给投影操作；其次，投影的结果作为选择操作的输入。

        同样，由于选择的结果是一个关系，我们可以在选择后应用投影。上面的表达式等同于：

        .. math::

            \pi_{\text{title, year}}(\sigma_{\text{year}=1968}(\text{books}))

        在这两种情况下的结果都是：

        .. table::
            :class: lined-table

            ======================== ====
            title                    year
            ======================== ====
            *House Made of Dawn*     1968
            *A Wizard of Earthsea*   1968
            ======================== ====

        然而，需要注意的是，并不总是可以改变投影和选择的顺序以获得等效的结果。考虑以下表达式：

        .. math::

            \pi_{\text{title}}(\sigma_{\text{year}=1968}(\text{books}))

        .. math::

            \sigma_{\text{year}=1968}(\pi_{\text{title}}(\text{books}))

        在第一个表达式中，我们选择1968年出版的书籍，然后将结果元组投影到 **title** 属性上。这个结果是：

        .. table::
            :class: lined-table

            +-------------------------+
            | title                   |
            +=========================+
            | *House Made of Dawn*    |
            +-------------------------+
            | *A Wizard of Earthsea*  |
            +-------------------------+

        然而，第二个表达式是不正确的表达式。投影首先发生，生成一个只有一个名为 **title** 的属性的关系。随后的选择则不正确，因为它引用了一个在输入关系中不存在的属性 **year** 。

        投影也可以应用于另一个投影的结果；然而，结果等同于仅执行第二个投影。比较：

        .. math::

            \pi_{\text{title}}(\pi_{\text{title, year}}(\text{books}))

        .. math::

            \pi_{\text{title}}(\text{books})

        请注意，我们不能改变第一个表达式中两个投影操作的顺序，因为表达式将变得不正确。

    .. md-tab-item:: 英文

        The projection operation creates a new relation which has a subset of the attributes of the input relation.  We could use projection, for example, to get a set of tuples expressing just the title and publication year of our books.  We write the projection operator with the list of attribute names in the subscript, followed by the operand in parentheses:

        .. math::

            \pi_{\text{title, year}}(\text{books})

        This result contains a tuple for each tuple in **books**, but the tuples in the result only have the attributes specified by the projection operation, thus the result relation has a different schema from the original:

        .. table::
            :class: lined-table

            ============================ ====
            title                        year
            ============================ ====
            *The House of the Spirits*   1982
            *Invisible Man*              1952
            *The Hobbit*                 1937
            *Unaccustomed Earth*         2008
            *The Fellowship of the Ring* 1954
            *House Made of Dawn*         1968
            *A Wizard of Earthsea*       1968
            ============================ ====

        At first glance, it might seem the result of a projection will always have the same number of tuples as the input relation, but this is not the case.  Consider what happens if we project **books** onto the single attribute **year**.  There are two tuples in **books** with the same **year** value of 1968.  Since relations cannot contain duplicates, the result of our projection operation can contain only one tuple with **year** equal to 1968.  Thus, the result has *fewer* tuples than the input relation:

        .. table:: :math:`\pi_{\text{year}}(\text{books})`
            :class: lined-table

            +------+
            | year |
            +======+
            | 1982 |
            +------+
            | 1952 |
            +------+
            | 1937 |
            +------+
            | 2008 |
            +------+
            | 1954 |
            +------+
            | 1968 |
            +------+

        Since the result of projection is a relation, we can apply selection to the result:

        .. math::

            \sigma_{\text{year}=1968}(\pi_{\text{title, year}}(\text{books}))

        Note the order of operations here: first, we supply **books** as an input to the projection operation; second, the result of the projection is given as the input to the selection operation.

        Similarly, since the result of a selection is a relation, we can apply projection after selection.  The above expression is equivalent to:

        .. math::

            \pi_{\text{title, year}}(\sigma_{\text{year}=1968}(\text{books}))

        The result in both cases is:

        .. table::
            :class: lined-table

            ======================== ====
            title                    year
            ======================== ====
            *House Made of Dawn*     1968
            *A Wizard of Earthsea*   1968
            ======================== ====

        It is important to note, however, that you cannot always change the order of projection and selection for an equivalent result.  Consider the following expressions:

        .. math::

            \pi_{\text{title}}(\sigma_{\text{year}=1968}(\text{books}))

        .. math::

            \sigma_{\text{year}=1968}(\pi_{\text{title}}(\text{books}))

        In the first expression, we select the books which were published in 1968, and then project the resulting tuples onto the **title** attribute.  This result is:

        .. table::
            :class: lined-table

            +-------------------------+
            | title                   |
            +=========================+
            | *House Made of Dawn*    |
            +-------------------------+
            | *A Wizard of Earthsea*  |
            +-------------------------+

        However, the second expression is not a correct expression.  The projection occurs first, yielding a relation with just one attribute named **title**.  The following selection is then incorrect, because it makes reference to an attribute, **year**, which does not exist in the input relation.

        Projection can also be applied to the result of another projection; however, the result is equivalent to just performing the second projection.  Compare:

        .. math::

            \pi_{\text{title}}(\pi_{\text{title, year}}(\text{books}))

        .. math::

            \pi_{\text{title}}(\text{books})

        Note that we cannot change the order of the two projection operations in the first expression above, as the expression would then be incorrect.

重命名
--------

**Renaming**

.. md-tab-set::

    .. md-tab-item:: 中文

        最后一种一元操作允许对关系及其属性进行重命名。正如我们将看到的，这个操作主要用于消除某些二元操作中的名称冲突，即涉及两个关系的表达式，其中某个属性的名称在两个关系中相同。重命名操作符的一般形式允许我们为关系及其所有属性提供新名称：

        .. math::

            \rho_{\text{mybooks(b_id, a_id, title, year)}}(\text{books})

        这将产生一个名为 **mybooks** 的关系，具有属性 **b_id**、 **a_id**、 **title** 和 **year**。新关系的元组具有与旧关系元组相同的值，但这些值与新属性名称相关联。

        如同这个例子所示，并不需要更改每个属性的名称（我们将属性名称 **title** 和 **year** 保持不变），但每个属性都必须提供一个名称。一种非标准的替代符号允许我们仅重命名我们想要更改的属性：

        .. math::

            \rho_{\text{mybooks(book_id} \rightarrow \text{b_id, author_id} \rightarrow \text{a_id)}}(\text{books})

        我们可以选择性地省略关系名称或属性列表。例如，以下表达式是正确的，结果是一个名为 **books** 的关系，具有属性 **book_id**、 **author_id**、 **title** 和 **publication_year**：

        .. math::

            \rho_{\text{(year} \rightarrow \text{publication_year)}}(\text{books})

    .. md-tab-item:: 英文

        The final unary operation allows for relations and their attributes to be renamed.  As we will see, this operation is primarily useful in eliminating name conflicts in certain binary operations - that is, in expressions involving two relations in which the name of some attribute is the same in both relations.  The general form of the renaming operator lets us provide new names for the relation and all of its attributes:

        .. math::

            \rho_{\text{mybooks(b_id, a_id, title, year)}}(\text{books})

        This results in a relation with the name **mybooks** with attributes **b_id**, **a_id**, **title**, and **year**.  The tuples of the new relation have the same values as the tuples of the old relation, but the values are associated with the new attribute names.

        As in this example, it is not necessary to alter the name of every attribute (we left unchanged the attribute names **title** and **year**), but some name must be provided for every attribute.  A non-standard alternative notation allows us to rename only the attributes we want to change:

        .. math::

            \rho_{\text{mybooks(book_id} \rightarrow \text{b_id, author_id} \rightarrow \text{a_id)}}(\text{books})

        We can optionally leave out either the relation name or the list of attributes.  For example, the following expression is correct and results in a relation named **books** with attributes **book_id**, **author_id**, **title**, and **publication_year**:

        .. math::

            \rho_{\text{(year} \rightarrow \text{publication_year)}}(\text{books})




交叉积和连接
::::::::::::::::::::::::

**Cross products and joins**

.. md-tab-set::

    .. md-tab-item:: 中文

        我们现在将注意力转向将一个关系中的元组与另一个关系中的元组扩展的操作。在本节中，我们将使用 **books** 和第二个关系 **authors**：

        .. table:: **authors**
            :class: lined-table

            ========== ================== =========== ============
            author_id  name               birth       death
            ========== ================== =========== ============
            1          Ralph Ellison      1914-03-01  1994-04-16
            2          Jhumpa Lahiri      1967-07-11
            3          Isabel Allende     1942-08-02
            4          N\. Scott Momaday  1934-02-27
            5          Ursula K. Le Guin  1929-10-21  2018-01-22
            6          J.R.R. Tolkien     1892-01-03  1973-09-02
            7          Kazuo Ishiguro     1954-11-08
            ========== ================== =========== ============

        **authors** 关系的主键是 **author_id** 。 **books** 关系通过 **author_id** 上的外键与 **authors** 相关联。

    .. md-tab-item:: 英文

        We now turn our attention to operations which extend tuples in one relation with tuples from another relation.  For this section, we will be using **books** and a second relation, **authors**:

        .. table:: **authors**
            :class: lined-table

            ========== ================== =========== ============
            author_id  name               birth       death
            ========== ================== =========== ============
            1          Ralph Ellison      1914-03-01  1994-04-16
            2          Jhumpa Lahiri      1967-07-11
            3          Isabel Allende     1942-08-02
            4          N\. Scott Momaday  1934-02-27
            5          Ursula K. Le Guin  1929-10-21  2018-01-22
            6          J.R.R. Tolkien     1892-01-03  1973-09-02
            7          Kazuo Ishiguro     1954-11-08
            ========== ================== =========== ============

        The **authors** relation has a primary key of **author_id**.  The **books** relation is related to **authors** via a foreign key on **author_id**.

.. index:: cross product - relational algebra, relational algebra operations; cross product

交叉积
-------------

**Cross product**

.. md-tab-set::

    .. md-tab-item:: 中文

        两个关系 **A** 和 **B** 的交叉积（或 *笛卡尔积(Cartesian product)* ）是一个新关系，包含可以通过将 **B** 中的某个元组与 **A** 中的某个元组连接而创建的所有元组 [#]_. 这里我们使用元组的定义为有序值列表。新关系的属性通常是 **A** 和 **B** 的属性的连接。然而，如果存在名称冲突，例如，如果 **A** 和 **B** 都有某个属性 **x**，我们将通过在新关系的属性前加上关系名来消除歧义，也就是说，交叉积将具有属性 **A.x** 和 **B.x**；如果我们首先对一个关系进行重命名，则可以避免这样做。

        交叉积运算符用 :math:`\times` 表示，并写在两个操作数之间。首先，考虑两个相对抽象的关系 **S** 和 **T**：

        .. table:: **S**
            :class: lined-table

            == ===
            u  v
            == ===
            1  one
            2  two
            == ===

        .. table:: **T**
            :class: lined-table

            ======= ======== ======
            x       y        z
            ======= ======== ======
            green   3.1415   apple
            blue    2.71828  pear
            yellow  1.618    mango
            ======= ======== ======

        我们将 **S** 和 **T** 的交叉积写为：

        .. math::

            \text{S} \times \text{T}

        这将给我们一个包含每个元组从 **S** 与每个元组从 **T** 配对的关系：

        .. table::
            :class: lined-table

            == === ======= ======== =======
            u  v   x       y        z
            == === ======= ======== =======
            1  one green   3.1415   apple
            1  one blue    2.71828  pear
            1  one yellow  1.618    mango
            2  two green   3.1415   apple
            2  two blue    2.71828  pear
            2  two yellow  1.618    mango
            == === ======= ======== =======

        根据定义，很容易确定交叉积的大小是操作数大小的乘积。

    .. md-tab-item:: 英文

        The cross product (or *Cartesian product*) of two relations **A** and **B** is a new relation containing all tuples that can be created by concatenating some tuple from **B** onto some tuple from **A** [#]_.  Here we are using the definition of tuple as an ordered list of values.  The attributes of the new relation are normally the attributes of **A** and **B** concatenated.  However, if there is a name collision, e.g., if both **A** and **B** have some attribute **x**, we will disambiguate the attributes in the new relation by prepending the relation names, that is, the cross product will have attributes **A.x** and **B.x**; we can avoid having to do this if we first apply renaming to one relation or the other.

        The cross product operator is denoted :math:`\times`, and is written between its two operands. To start, consider two rather abstract relations **S** and **T**:

        .. table:: **S**
            :class: lined-table

            == ===
            u  v
            == ===
            1  one
            2  two
            == ===

        .. table:: **T**
            :class: lined-table

            ======= ======== ======
            x       y        z
            ======= ======== ======
            green   3.1415   apple
            blue    2.71828  pear
            yellow  1.618    mango
            ======= ======== ======

        We write the cross product of **S** and **T** as:

        .. math::

            \text{S} \times \text{T}

        which gives us the relation containing every pairing of a tuple from **S** with every tuple from **T**:

        .. table::
            :class: lined-table

            == === ======= ======== =======
            u  v   x       y        z
            == === ======= ======== =======
            1  one green   3.1415   apple
            1  one blue    2.71828  pear
            1  one yellow  1.618    mango
            2  two green   3.1415   apple
            2  two blue    2.71828  pear
            2  two yellow  1.618    mango
            == === ======= ======== =======

        From the definition, it is trivial to determine that the size of the cross product is the product of the sizes of the operands.

.. index:: join - relational algebra, relational algebra operations; join

连接
----

**Join**

.. md-tab-set::

    .. md-tab-item:: 中文

        交叉积是关系代数中的一个基本操作，但在考虑实际数据时并不普遍有用。考虑 **books** 和 **authors** 的交叉积：

        .. math::

            \text{books} \times \text{authors}

        这个关系中的元组全集非常大（书籍数量乘以作者数量），因此我们只在下面展示一个子集：

        .. table::
            :class: lined-table

            ======= =============== ============================ ===== ================== ================== ============ ============
            book_id books.author_id title                        year  authors.author_id  name               birth       death
            ======= =============== ============================ ===== ================== ================== ============ ============
            1       3               *The House of the Spirits*   1982  1                  Ralph Ellison      1914-03-01  1994-04-16
            1       3               *The House of the Spirits*   1982  2                  Jhumpa Lahiri      1967-07-11
            1       3               *The House of the Spirits*   1982  3                  Isabel Allende     1942-08-02
            2       1               *Invisible Man*              1952  1                  Ralph Ellison      1914-03-01  1994-04-16
            2       1               *Invisible Man*              1952  2                  Jhumpa Lahiri      1967-07-11
            2       1               *Invisible Man*              1952  3                  Isabel Allende     1942-08-02
            ======= =============== ============================ ===== ================== ================== ============ ============

        *The House of the Spirits* 的作者是 Isabel Allende。那么，将 *The House of the Spirits* 与作者 Ralph Ellison（*Invisible Man* 的作者）配对的元组有什么意义呢？

        我们通常只对将关系的某些元组与另一关系的某些元组配对感兴趣。在上面的例子中，我们感兴趣的是 **books** 中的 **author_id** 属性与 **authors** 中的 **author_id** 属性相符的元组。这种关系不仅通过我们为属性使用的名称来指示，还通过 **books** 和 **authors** 之间的外键约束来指示。为了保留仅具有匹配 **author_id** 值的元组，我们可以对交叉积的结果应用选择操作：

        .. math::

            \sigma_{\text{books.author_id}=\text{authors.author_id}}(\text{books} \times \text{authors})

        这将产生一个有用的结果：

        .. table::
            :class: lined-table

            ======= =============== ============================ ===== ================== ================== ============ ============
            book_id books.author_id title                        year  authors.author_id  name               birth       death
            ======= =============== ============================ ===== ================== ================== ============ ============
            1       3               *The House of the Spirits*   1982  3                  Isabel Allende     1942-08-02
            2       1               *Invisible Man*              1952  1                  Ralph Ellison      1914-03-01  1994-04-16
            3       6               *The Hobbit*                 1937  6                  J.R.R. Tolkien     1892-01-03  1973-09-02
            4       2               *Unaccustomed Earth*         2008  2                  Jhumpa Lahiri      1967-07-11
            5       6               *The Fellowship of the Ring* 1954  6                  J.R.R. Tolkien     1892-01-03  1973-09-02
            6       4               *House Made of Dawn*         1968  4                  N\. Scott Momaday  1934-02-27
            7       5               *A Wizard of Earthsea*       1968  5                  Ursula K. Le Guin  1929-10-21  2018-01-22
            ======= =============== ============================ ===== ================== ================== ============ ============

        由于在交叉积之后应用选择的模式如此常见，我们有一个将两者结合为称为 *连接* 的操作的运算符 [#]_. 使用连接运算符，上面的表达式变为：

        .. math::

            \text{books} \Join_{\text{books.author_id}=\text{authors.author_id}} \text{authors}

        或者，您也可以将表达式格式化为：

        .. math::

            \text{books} \underset{\text{books.author_id}=\text{authors.author_id}}\Join \text{authors}

        注意，**authors** 中的一个元组没有对连接产生贡献。这个元组的 **author_id** 与 **books** 中的任何元组都不匹配，因此使用它的组合元组不会出现在连接结果中。我们称这个元组为 *悬挂元组*。悬挂元组可能表明数据中存在问题；在这个例子中，这可能表明我们缺少有关某位作者的书籍的信息。

    .. md-tab-item:: 英文

        The cross product is a fundamental operation in relational algebra, but not a generally useful one when we consider actual data.  Consider the cross product of **books** and **authors**:

        .. math::

            \text{books} \times \text{authors}

        The full set of tuples in this relation is large (the number of books multiplied by the number of authors), so we only show a subset below:

        .. table::
            :class: lined-table

            ======= =============== ============================ ===== ================== ================== =========== ============
            book_id books.author_id title                        year  authors.author_id  name               birth       death
            ======= =============== ============================ ===== ================== ================== =========== ============
            1       3               *The House of the Spirits*   1982  1                  Ralph Ellison      1914-03-01  1994-04-16
            1       3               *The House of the Spirits*   1982  2                  Jhumpa Lahiri      1967-07-11
            1       3               *The House of the Spirits*   1982  3                  Isabel Allende     1942-08-02
            2       1               *Invisible Man*              1952  1                  Ralph Ellison      1914-03-01  1994-04-16
            2       1               *Invisible Man*              1952  2                  Jhumpa Lahiri      1967-07-11
            2       1               *Invisible Man*              1952  3                  Isabel Allende     1942-08-02
            ======= =============== ============================ ===== ================== ================== =========== ============

        The author of *The House of the Spirits* is Isabel Allende.  What meaning, then, can we make of a tuple that pairs *The House of the Spirits* with the author Ralph Ellison (the author of *Invisible Man*)?

        We are typically interested in pairing only certain tuples of a relation with certain tuples of another.  In the above example, we are interested in tuples where the **author_id** attribute from **books** agrees with the **author_id** attribute from **authors**.  This relationship is indicated not only by the names we have used for attributes, but also by the foreign key constraint on **books** and **authors**.  To retain only the tuples with matching **author_id** values, we can apply a selection operation to the result of our cross product:

        .. math::

            \sigma_{\text{books.author_id}=\text{authors.author_id}}(\text{books} \times \text{authors})

        This yields a useful result:

        .. table::
            :class: lined-table

            ======= =============== ============================ ===== ================== ================== =========== ============
            book_id books.author_id title                        year  authors.author_id  name               birth       death
            ======= =============== ============================ ===== ================== ================== =========== ============
            1       3               *The House of the Spirits*   1982  3                  Isabel Allende     1942-08-02
            2       1               *Invisible Man*              1952  1                  Ralph Ellison      1914-03-01  1994-04-16
            3       6               *The Hobbit*                 1937  6                  J.R.R. Tolkien     1892-01-03  1973-09-02
            4       2               *Unaccustomed Earth*         2008  2                  Jhumpa Lahiri      1967-07-11
            5       6               *The Fellowship of the Ring* 1954  6                  J.R.R. Tolkien     1892-01-03  1973-09-02
            6       4               *House Made of Dawn*         1968  4                  N\. Scott Momaday  1934-02-27
            7       5               *A Wizard of Earthsea*       1968  5                  Ursula K. Le Guin  1929-10-21  2018-01-22
            ======= =============== ============================ ===== ================== ================== =========== ============

        Since this pattern of applying a selection after a cross product is so common, we have an operator that combines the two into an operation known as a *join* [#]_.  Using the join operator, the above expression becomes:

        .. math::

            \text{books} \Join_{\text{books.author_id}=\text{authors.author_id}} \text{authors}

        or, you can instead format the expression as:

        .. math::

            \text{books} \underset{\text{books.author_id}=\text{authors.author_id}}\Join \text{authors}

        Note that one tuple from **authors** does not contribute to the join.  This tuple's **author_id** matches none of the tuples in **books**, and thus no combined tuple using it can appear in the join result.  We call this tuple a *dangling tuple*.  Dangling tuples may be an indication of a problem in the data; in this example, it may suggest that we are missing information about books by one author.

.. index:: equijoin, theta join

Theta 连接和等值连接
-----------------------

**Theta-join and equijoin**

.. md-tab-set::

    .. md-tab-item:: 中文

        虽然在连接中通常使用等式条件，但更一般地，可以使用以下形式的任何条件：

        .. math::

            \text{A.x } \Theta \text{ B.y}

        其中 **A.x** 是一个关系中的属性， **B.y** 是另一个关系中的属性，而 :math:`\Theta` 是一个比较运算符（例如 =、< 等）。这种形式的条件称为 *theta 条件*，使用这种条件或其结合（AND）的连接称为 *theta-join*。

        仅使用等式比较的 theta-join（如我们上面的例子所示）进一步称为 *equijoin*。

        这个术语在理解代数时并不是特别重要，但如果您打算深入研究关系代数，您可能会遇到它。

    .. md-tab-item:: 英文

        While an equality condition is typically used in joins, more generally any condition of the following form can be used:

        .. math::

            \text{A.x } \Theta \text{ B.y}

        where **A.x** is an attribute from one relation, **B.y** is an attribute from the other relation, and :math:`\Theta` is a comparison operator (such as =, <, etc.).  A condition of this form is known as a *theta condition*, and a join using such a condition or a conjunction (AND) of such conditions is known as a *theta-join*.

        A theta-join using only equality comparisons (as in our example above) is further known as an *equijoin*.

        This terminology is not especially important in understanding the algebra, but is something you may encounter if you intend a deeper study of  relational algebra.

.. index:: relational algebra operations; natural join, natural join

自然连接
------------

**Natural join**

.. md-tab-set::

    .. md-tab-item:: 中文

        当我们将 **books** 与 **authors** 连接时，会遇到两个关系都包含名为 **author_id** 的属性的问题。由于一个关系不能有多个同名属性，因此连接（或对这两个关系进行笛卡尔积）要求我们以某种方式重命名属性。这可以通过在连接之前进行显式的重命名操作来完成，或者通过在原始关系名前添加前缀（如我们在示例中所做的）。由于我们的连接条件是在 **author_id** 属性上的相等，因此结果关系中的 **books.author_id** 和 **authors.author_id** 始终相等。可以通过投影和重命名来消除这种不必要的冗余。

        在这种特殊情况下，我们希望通过在两个关系中相等的同名属性来进行连接，并随后去除“重复”属性，我们可以进行 *自然连接*。我们可以使用不带条件的连接运算符表示自然连接 [#]_ ：

        .. math::

            \text{books} \Join \text{authors}

        这将产生简化后的关系：

        .. table::
            :class: lined-table

            ======= ========= ============================ ===== ================== =========== ============
            book_id author_id title                        year  name               birth       death
            ======= ========= ============================ ===== ================== =========== ============
            1       3         *The House of the Spirits*   1982  Isabel Allende     1942-08-02
            2       1         *Invisible Man*              1952  Ralph Ellison      1914-03-01  1994-04-16
            3       6         *The Hobbit*                 1937  J.R.R. Tolkien     1892-01-03  1973-09-02
            4       2         *Unaccustomed Earth*         2008  Jhumpa Lahiri      1967-07-11
            5       6         *The Fellowship of the Ring* 1954  J.R.R. Tolkien     1892-01-03  1973-09-02
            6       4         *House Made of Dawn*         1968  N\. Scott Momaday  1934-02-27
            7       5         *A Wizard of Earthsea*       1968  Ursula K. Le Guin  1929-10-21  2018-01-22
            ======= ========= ============================ ===== ================== =========== ============

    .. md-tab-item:: 英文

        When we join **books** with **authors** we run into the issue that both relations contain an attribute named **author_id**.  Since a relation cannot have more than one attribute with the same name, joining (or taking a cross product of) these two relations requires us to rename the attributes in some fashion. This can be done either by an explicit renaming operation prior to joining or by prepending the original relation name (as we did in our example).  Because our join condition was equality on the **author_id** attributes, both the **books.author_id** and **authors.author_id** in the resulting relation always agree.  This unnecessary redundancy can be removed using projection and renaming.

        In this special situation in which we wish to join specifically by equating the attributes with the same names in both relations - subsequently removing the "duplicate" attributes - we can instead do a *natural join*.  We can indicate a natural join using the join operator with no conditions [#]_:

        .. math::

            \text{books} \Join \text{authors}

        which yields the simplified relation:

        .. table::
            :class: lined-table

            ======= ========= ============================ ===== ================== =========== ============
            book_id author_id title                        year  name               birth       death
            ======= ========= ============================ ===== ================== =========== ============
            1       3         *The House of the Spirits*   1982  Isabel Allende     1942-08-02
            2       1         *Invisible Man*              1952  Ralph Ellison      1914-03-01  1994-04-16
            3       6         *The Hobbit*                 1937  J.R.R. Tolkien     1892-01-03  1973-09-02
            4       2         *Unaccustomed Earth*         2008  Jhumpa Lahiri      1967-07-11
            5       6         *The Fellowship of the Ring* 1954  J.R.R. Tolkien     1892-01-03  1973-09-02
            6       4         *House Made of Dawn*         1968  N\. Scott Momaday  1934-02-27
            7       5         *A Wizard of Earthsea*       1968  Ursula K. Le Guin  1929-10-21  2018-01-22
            ======= ========= ============================ ===== ================== =========== ============

.. index:: set operation - relational algebra, set operation - relational algebra; union, set operation - relational algebra; intersection, set operation - relational algebra; difference, relational algebra operations; union, relational algebra operations; intersection, relational algebra operations; set difference

集合运算
::::::::::::::

**Set operations**

.. md-tab-set::

    .. md-tab-item:: 中文

        不出所料，由于关系是集合，关系代数包含了通常的集合操作——*并集*、*交集*和*集合差*，但有一些限制。这些二元操作用以下符号表示：

        - :math:`\cup`: 并集
        - :math:`\cap`: 交集
        - :math:`-`: 集合差

        给定两个关系 **A** 和 **B**，并集 :math:`\text{A} \cup \text{B}` 是存在于 **A** 中、存在于 **B** 中或同时存在于两者中的所有元组的集合。交集 :math:`\text{A} \cap \text{B}` 是同时存在于 **A** 和 **B** 中的所有元组的集合。最后，集合差 :math:`\text{A} - \text{B}` 是存在于 **A** 中但不在 **B** 中的所有元组的集合。

        例如，让 **A** 和 **B** 为以下关系：

        .. table:: **A**
            :class: lined-table

            ======= ===
            x       y
            ======= ===
            apple   42
            orange  19
            cherry  77
            ======= ===

        .. table:: **B**
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            banana   8
            apple    42
            coconut  17
            ======== ===

        那么我们有：

        .. table:: :math:`\text{A} \cup \text{B}`
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            apple    42
            orange   19
            cherry   77
            banana   8
            coconut  17
            ======== ===

        .. table:: :math:`\text{A} \cap \text{B}`
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            apple    42
            ======== ===

        .. table:: :math:`\text{A} - \text{B}`
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            orange   19
            cherry   77
            ======== ===

        .. table:: :math:`\text{B} - \text{A}`
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            banana   8
            coconut  17
            ======== ===

        请注意，并集和交集是可交换的，但集合差则不是。

        关系代数中对集合操作的重要限制是关系的模式必须兼容。“兼容”的含义有所不同，但对于我们的目的，假设我们将关系中的元组视为有序值列表，其中列表中的每个位置与特定属性和类型域相关联。那么，如果我们有两个关系，我们要求对于任一关系中元组的给定位置，属性和类型域必须相同。对于上述的 **A** 和 **B**，我们可以断言第一个位置对应属性 **x** 并包含字符字符串，而第二个位置 (**y**) 包含整数。

        一个更宽松的要求允许属性名称（但不允许类型域）在关系之间不同。这个要求与上一章中给出的元组的第二个定义不太一致，但它消除了在应用集合操作之前偶尔需要重命名操作的需求。如果两个关系中的属性名称不匹配，我们将采用左操作数的属性名称作为结果关系的属性名称。

        虽然交集是一个有用的操作，但在代数中并不严格必要，因为可以通过集合差得到相同的结果：

        .. math::

            \text{A} \cap \text{B} \equiv \text{A} - (\text{A} - \text{B})

    .. md-tab-item:: 英文

        Unsurprisingly, given that relations are sets, relational algebra includes the usual set operations - *union*, *intersection*, and *set difference* - with some restrictions.  These binary operations are denoted by:

        - :math:`\cup`: union
        - :math:`\cap`: intersection
        - :math:`-`: set difference

        Given two relations **A** and **B**, the union :math:`\text{A} \cup \text{B}` is the set of all tuples that exist in **A**, or exist in **B**, or both.  The intersection :math:`\text{A} \cap \text{B}` is the set of all tuples that exist in both **A** and **B**.  Finally, the set difference :math:`\text{A} - \text{B}` is the set of all tuples that exist in **A** but do not exist in **B**.

        For example, let **A** and **B** be the relations below:

        .. table:: **A**
            :class: lined-table

            ======= ===
            x       y
            ======= ===
            apple   42
            orange  19
            cherry  77
            ======= ===

        .. table:: **B**
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            banana   8
            apple    42
            coconut  17
            ======== ===

        Then we have:

        .. table:: :math:`\text{A} \cup \text{B}`
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            apple    42
            orange   19
            cherry   77
            banana   8
            coconut  17
            ======== ===

        .. table:: :math:`\text{A} \cap \text{B}`
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            apple    42
            ======== ===

        .. table:: :math:`\text{A} - \text{B}`
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            orange   19
            cherry   77
            ======== ===

        .. table:: :math:`\text{B} - \text{A}`
            :class: lined-table

            ======== ===
            x        y
            ======== ===
            banana   8
            coconut  17
            ======== ===

        Note that union and intersection are commutative, but set difference is not.

        The important restriction on set operations in relational algebra is that the relations must be compatible in terms of their schemas.  The meaning of "compatible" varies, but for our purposes, assume we view the tuples in a relation as ordered lists, where each position in the list is associated with a particular attribute and type domain.  Then, if we have two relations, we require that, for a given position in the tuples in either relation, the attribute and type domain are the same.  For **A** and **B** shown above, we might assert that the first position corresponds to attribute **x** and contains character strings, while the second position (**y**) contains integers.

        A looser requirement allows attribute names (but not type domains) to differ between relations.  This requirement aligns less closely with the second definition of tuple given in the previous chapter, but it eliminates the occasional need for renaming operations prior to applying set operations. If the attribute names do not match in the two relations, we adopt the attribute names from the left-hand operand for the result relation.

        While intersection is a useful operation, it is not strictly needed for the algebra, as the same result can be obtained using set difference:

        .. math::

            \text{A} \cap \text{B} \equiv \text{A} - (\text{A} - \text{B})

.. index:: division, relational algebra operations; division

除法
::::::::

**Division**

.. md-tab-set::

    .. md-tab-item:: 中文

        上述操作对于大多数查询需求是足够的。然而，另一个二元操作——*除法*，通常被包含在基本关系代数中。要将关系 **P** 除以另一个关系 **R**，我们写作：

        .. math::

            \text{P} \div \text{R}

        除法是最难描述的操作；在一个非常宽松的意义上，它充当了交叉乘积的一种逆。也就是说，如果 **P**、 **Q** 和 **R** 是关系，并且

        .. math::

            \text{P} = \text{Q} \times \text{R}

        那么有

        .. math::

            \text{P} \div \text{R} = \text{Q}

        然而，反过来并不一定成立。设 **P** 为某个关系，具有属性 **x** 和 **y** [#]_. 我们要求 **R** 具有属性 **y**。那么 :math:`\text{P} \div \text{R}` 将包含与 **R** 中列出的 *每个* **y** 值配对的 **P** 中的 **x** 值。

        我们将从一个抽象示例开始。设 **P** 为下图所示的关系：

        .. table::  **P**
            :class: lined-table

            === =========
            x   y
            === =========
            1   blue
            1   green
            1   yellow
            2   blue
            2   yellow
            3   blue
            3   green
            3   yellow
            3   red
            === =========

        设 **R** 为

        .. table:: **R**
            :class: lined-table

            +---------+
            | y       |
            +=========+
            | blue    |
            +---------+
            | green   |
            +---------+
            | yellow  |
            +---------+

        那么 :math:`\text{Q} = \text{P} \div \text{R}` 是

        .. table:: **Q**
            :class: lined-table

            +----+
            | x  |
            +====+
            | 1  |
            +----+
            | 3  |
            +----+

        因为只有值 1 和 3 与 **P** 中的蓝色、绿色和黄色配对。值 2 与绿色不配对，因此它不会出现在商中。值 3 也与红色配对，但红色不在 **R** 中，因此不会影响结果。

        对于一个更具体的例子，考虑以下关系，命名为 **authors_awards**：

        .. table:: **authors_awards**
            :class: lined-table

            ================== ===========================
            author             award
            ================== ===========================
            Ralph Ellison      National Book Award
            Jhumpa Lahiri	     Pulitzer Prize for Fiction
            N\. Scott Momaday	 Pulitzer Prize for Fiction
            Ursula K. Le Guin	 Hugo Award
            Ursula K. Le Guin	 Nebula Award
            C\. J\. Cherryh	   Hugo Award
            Kazuo Ishiguro	   Booker Prize
            Kazuo Ishiguro	   Nobel Prize in Literature
            Michael Chabon	   Hugo Award
            Michael Chabon	   Nebula Award
            Michael Chabon	   Pulitzer Prize for Fiction
            ================== ===========================

        以及关系 **science_fiction_awards**：

        .. table:: **science_fiction_awards**
            :class: lined-table

            +--------------+
            | award        |
            +==============+
            | Hugo Award   |
            +--------------+
            | Nebula Award |
            +--------------+

        我们可能会问，“哪些作者获得了所有的科幻书籍奖？” 答案由

        .. table:: :math:`\text{authors_awards} \div \text{science_fiction_awards}`
            :class: lined-table

            +-------------------+
            | author            |
            +===================+
            | Ursula K. Le Guin |
            +-------------------+
            | Michael Chabon    |
            +-------------------+

        像连接和集合交集操作一样，除法可以通过其他关系代数操作实现；然而，这种构造相当复杂。如果我们有关系 **P** 具有属性 **x** 和 **y**，以及关系 **R** 具有属性 **y**，那么

        .. math::

            \text{P} \div \text{R} \equiv \pi_{\text{x}}(\text{P}) - \pi_{\text{x}}((\pi_{\text{x}}(\text{P}) \times \text{R}) - \text{P})

        通过仔细应用上述右侧表达式到我们的示例之一，您可以验证获得所需结果，但基本的直觉是我们必须首先找到在 **P** 中与 **R** 中列出的一个或多个 **y** 值 *不* 配对的 **x** 值，然后将该 **x** 值列表从 **P** 中所有 **x** 值的列表中减去：

        1. 创建一个关系，包含 **P** 中的每个 **x** 值与 **R** 中的每个 **y** 值的配对：

        .. math::

            \pi_{\text{x}}(\text{P}) \times \text{R}

        2. 从上述交叉乘积结果中减去（使用集合差） **P**。这些是 **P** 中与 **R** 中 **y** 的可能配对，但在 **P** 中 *不存在*：

        .. math::

            (\pi_{\text{x}}(\text{P}) \times \text{R}) - \text{P}

        3. 将最后结果投影到属性 **x**。这些是没有与 **R** 中某个值配对的 **x** 值：

        .. math::

            \pi_{\text{x}}((\pi_{\text{x}}(\text{P}) \times \text{R}) - \text{P})

        4. 将最后结果从 **P** 中所有 **x** 值的集合中减去，以得到最终解决方案：

        .. math::

            \pi_{\text{x}}(\text{P}) - \pi_{\text{x}}((\pi_{\text{x}}(\text{P}) \times \text{R}) - \text{P})

    .. md-tab-item:: 英文

        The operations described above are sufficient for most query needs.  However, one other binary operation, *division*, is typically included in the basic relational algebra.  To divide a relation **P** by another relation **R**, we write:

        .. math::

            \text{P} \div \text{R}

        Division is the most difficult operation to describe; in a very loose sense it acts as a kind of inverse to a cross product.  That is, if **P**, **Q**, and **R** are relations and

        .. math::

            \text{P} = \text{Q} \times \text{R}

        then it is true that

        .. math::

            \text{P} \div \text{R} = \text{Q}

        However, the reverse is not necessarily true.  Rather, let **P** be some relation, with attributes **x** and **y** [#]_.  We require that **R** has attribute **y**.  Then :math:`\text{P} \div \text{R}` will contain the values of **x** which are paired (in **P**) with *every* value of **y** listed in **R**.

        We will start with an abstract example.  Let **P** be the relation pictured below:

        .. table::  **P**
            :class: lined-table

            === =========
            x   y
            === =========
            1   blue
            1   green
            1   yellow
            2   blue
            2   yellow
            3   blue
            3   green
            3   yellow
            3   red
            === =========

        Let **R** be

        .. table:: **R**
            :class: lined-table

            +---------+
            | y       |
            +=========+
            | blue    |
            +---------+
            | green   |
            +---------+
            | yellow  |
            +---------+

        Then :math:`\text{Q} = \text{P} \div \text{R}` is

        .. table:: **Q**
            :class: lined-table

            +----+
            | x  |
            +====+
            | 1  |
            +----+
            | 3  |
            +----+

        because only the values 1 and 3 are paired with blue, green, and yellow in **P**.  The value 2 is not paired with green, so it does not appear in the quotient.  The value 3 is also paired with red, but red is not in **R** and thus does not affect the result.

        For a more tangible example, consider the following relation, named **authors_awards**:

        .. table:: **authors_awards**
            :class: lined-table

            ================== ===========================
            author             award
            ================== ===========================
            Ralph Ellison      National Book Award
            Jhumpa Lahiri	     Pulitzer Prize for Fiction
            N\. Scott Momaday	 Pulitzer Prize for Fiction
            Ursula K. Le Guin	 Hugo Award
            Ursula K. Le Guin	 Nebula Award
            C\. J\. Cherryh	   Hugo Award
            Kazuo Ishiguro	   Booker Prize
            Kazuo Ishiguro	   Nobel Prize in Literature
            Michael Chabon	   Hugo Award
            Michael Chabon	   Nebula Award
            Michael Chabon	   Pulitzer Prize for Fiction
            ================== ===========================

        and the relation **science_fiction_awards**:

        .. table:: **science_fiction_awards**
            :class: lined-table

            +--------------+
            | award        |
            +==============+
            | Hugo Award   |
            +--------------+
            | Nebula Award |
            +--------------+

        We might ask the question, "Which authors have received all of the science fiction book awards?"  The answer is given by

        .. table:: :math:`\text{authors_awards} \div \text{science_fiction_awards}`
            :class: lined-table

            +-------------------+
            | author            |
            +===================+
            | Ursula K. Le Guin |
            +-------------------+
            | Michael Chabon    |
            +-------------------+

        Like the join and set intersection operations, division can be accomplished using other relational algebra operations; however, the construction is fairly complex.  If we have relation **P** with attributes **x** and **y**, and relation **R** with attribute **y**, then

        .. math::

            \text{P} \div \text{R} \equiv \pi_{\text{x}}(\text{P}) - \pi_{\text{x}}((\pi_{\text{x}}(\text{P}) \times \text{R}) - \text{P})

        By carefully applying the right-hand side expression above to one of our examples, you can verify that the desired result is obtained, but the basic intuition is that we must first find the values of **x** in **P** which are *not* paired (in **P**) with one or more **y** values listed in **R**, and then subtract that list of **x** values from the list of all **x** values in **P**:

        1. Create a relation containing every **x** value in **P** paired with every **y** value in **R**:

        .. math::

            \pi_{\text{x}}(\text{P}) \times \text{R}

        2. Subtract (using set difference) **P** from the cross product result above.  These are the possible pairings of **x** (in **P**) and **y** (in **R**) that do *not* exist in **P**:

        .. math::

            (\pi_{\text{x}}(\text{P}) \times \text{R}) - \text{P}

        3. Project the last result onto attribute **x**. These are the **x** values that are not paired with some value from **R**:

        .. math::

            \pi_{\text{x}}((\pi_{\text{x}}(\text{P}) \times \text{R}) - \text{P})

        4. Subtract the last result from the set of all **x** values in **P** for the final solution:

        .. math::

            \pi_{\text{x}}(\text{P}) - \pi_{\text{x}}((\pi_{\text{x}}(\text{P}) \times \text{R}) - \text{P})


查询
:::::::

**Queries**

.. md-tab-set::

    .. md-tab-item:: 中文

        正如我们所见，关系代数的操作作用于关系并生成关系，因此我们可以按顺序应用关系操作以获得最终所需的结果。通过我们讨论的操作，我们可以表达出各种各样的 *查询*（需要通过数据回答的问题）。在本章中，我们看到了一些简单查询的例子，主要涉及一个或两个基本操作。

        然而，即使是简单的问题，也可能需要多次操作的应用。考虑这个问题：“J.R.R.托尔金有哪些书在1950年后出版？” 这与我们之前问过的一个问题相似，只是使用作者的ID值而不是作者的名字。只有作者的名字时，我们需要做更多的工作。

        有许多方法可以达到我们想要的结果。一个可能的方法可能从提出的条件开始：作者是J.R.R.托尔金，出版年份大于1950年。作者名字在 **authors** 关系中，而出版年份在 **books** 关系中。因此，我们可以猜测需要在每个关系上进行两个选择操作：

        .. math::

            \sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors})

        和

        .. math::

            \sigma_{\text{year} > 1950}(\text{books})

        这给我们提供了两个关系，它们通过在两者中都存在的 **author_id** 属性相关联。因此，自然连接可能是我们的下一步：

        .. math::

            \sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \Join \sigma_{\text{year} > 1950}(\text{books})

        最后，我们只对书名（或可能的书名和出版年份）感兴趣，因此我们以投影操作结束：

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \Join \sigma_{\text{year} > 1950}(\text{books}))

        这只是许多可能表达式中的一种，产生相同的结果。以下是一些等效表达式：

        ..
            在第XXX章中，我们将研究一些可以应用的代数恒等式，以将一个表达式转换为不同但等效的表达式，并探索这些恒等式如何被数据库软件使用以加速查询的执行。现在，我们提供以下等效表达式，不作讨论：

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien AND year} > 1950}(\text{authors} \Join \text{books}))

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\sigma_{\text{year} > 1950}(\text{books}) \Join \text{authors}))

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors} \Join \text{books}) \cap \sigma_{\text{year} > 1950}(\text{authors} \Join \text{books}))

    .. md-tab-item:: 英文

        As we have seen, the operations of the relational algebra act on relations and result in relations, and thus we can apply relational operations sequentially to obtain a final desired result.  With the operations we have discussed, we can express a very wide array of *queries* (questions to be answered by the data).  We have seen examples of simple queries throughout this chapter, mostly involving one or two basic operations.

        Even simple questions, however, can require the application of multiple operations.  Consider the question, "What books by J.R.R. Tolkien were published after 1950?".  This is similar to a question we asked earlier, using the author ID value rather than the author's name.  With only the author's name, we have to do a bit more work.

        There are many ways to get to our desired result.  One possible approach might begin with the conditions presented: the author is J.R.R. Tolkien, and the publication year is greater than 1950.  Author names are in the **authors** relation, while publication years are in the **books** relation.  So we might guess we need two selection operations, one on each relation:

        .. math::

            \sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors})

        and

        .. math::

            \sigma_{\text{year} > 1950}(\text{books})

        This gives us two relations which are related by the **author_id** attribute present in both.  So a natural join might be our next step:

        .. math::

            \sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \Join \sigma_{\text{year} > 1950}(\text{books})

        Finally, we are only interested in the book titles (or possibly titles and publication years), so we finish with a projection operation:

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \Join \sigma_{\text{year} > 1950}(\text{books}))

        This is only one of many possible expressions that yield identical results.  Here are some equivalent expressions:

        ..
            In chapter XXX, we will look at some of the algebraic identities that can be applied to transform an expression into a different but equivalent expression, and explore how these identities can be used by database software to speed up the execution of queries.  For now, we provide the following equivalent expressions without discussion:

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien AND year} > 1950}(\text{authors} \Join \text{books}))

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\sigma_{\text{year} > 1950}(\text{books}) \Join \text{authors}))

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors} \Join \text{books}) \cap \sigma_{\text{year} > 1950}(\text{authors} \Join \text{books}))


操作序列
-------------------

**Operation sequences**

.. md-tab-set::

    .. md-tab-item:: 中文

        随着查询变得更加复杂，像上述表达式那样的表达式可能变得相当冗长且难以理解。一种替代方法是使用中间变量来分解和标记表达式的部分。这样可以更顺序地查看操作。

        我们将通过上一节中的一个查询来演示这种方法：

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \Join \sigma_{\text{year} > 1950}(\text{books}))

        使用变量，我们可以将其写成一系列操作：

        .. math::

            \begin{eqnarray*}
            \text{A} &=& \sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \\
            \text{B} &=& \sigma_{\text{year} > 1950}(\text{books}) \\
            \text{C} &=& \text{A} \Join \text{B} \\
            \text{R} &=& \pi_{\text{title}}(\text{C}) \\
            \end{eqnarray*}

        其中 **R** 保存我们的最终结果。

    .. md-tab-item:: 英文

        As queries become more complex, expressions like the ones shown above can become quite long and difficult to understand.  An alternative approach is to use intermediate variables to decompose and label the parts of our expression.  The result is a more sequential view of the operations.

        We will demonstrate this approach with one of the queries from the last section:

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \Join \sigma_{\text{year} > 1950}(\text{books}))

        Using variables, we can write this as a sequence of operations:

        .. math::

            \begin{eqnarray*}
            \text{A} &=& \sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \\
            \text{B} &=& \sigma_{\text{year} > 1950}(\text{books}) \\
            \text{C} &=& \text{A} \Join \text{B} \\
            \text{R} &=& \pi_{\text{title}}(C) \\
            \end{eqnarray*}

        with **R** holding our final result.

.. index:: query trees

表达式树
----------------

**Expression trees**

.. md-tab-set::

    .. md-tab-item:: 中文

        关系代数表达式的另一种表示形式是树的形式。表达式树是查询的有用视觉表示。

        ..

            我们将在第 XXX 章中再次使用它们，该章关注数据库软件如何考虑执行查询的不同行动计划。

        我们将再次使用以下查询进行演示：

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \Join \sigma_{\text{year} > 1950}(\text{books}))

        该查询的树形表示如下：

        .. image:: tree1.svg

        操作从树的底部开始，涉及关系 **authors** 和 **books**，并向上进行。我们可以先应用任一选择操作，然后再应用另一操作；在执行连接之前，必须先应用这两个操作，最后进行投影。

        这里是另一个示例，对应于以下表达式：

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\sigma_{\text{year} > 1950}(\text{books}) \Join \text{authors}))

        树形表示为：

        .. image:: tree2.svg

    .. md-tab-item:: 英文

        Another representation of relational algebra expressions is in the form of a tree.  Expression trees are a useful visual representation of a query.

        ..

            We will make use of them again in Chapter XXX, which is concerned with how database software considers different action plans for executing a query.

        We will again demonstrate using the query:

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\text{authors}) \Join \sigma_{\text{year} > 1950}(\text{books}))

        The tree representation of this query looks like:

        .. image:: tree1.svg

        Operations start at the bottom of the tree, with the relations **authors** and **books**, and proceed upwards.  We can apply either selection operation first, then the other; both must be applied before we can perform the join, and we finish with the projection.

        Here is another example, corresponding to the expression:

        .. math::

            \pi_{\text{title}}(\sigma_{\text{name} = \text{J.R.R. Tolkien}}(\sigma_{\text{year} > 1950}(\text{books}) \Join \text{authors}))

        The tree is:

        .. image:: tree2.svg




----

**Notes**

.. [#] 这与一般数学中元组集合的笛卡尔积定义是一致的。

.. [#] This is consistent with the definition of the Cartesian product of sets of tuples in general mathematics.

.. [#] 实际上，最初介绍关系模型的论文讨论的是连接而不是交叉乘积。然而，交叉乘积现在被认为是关系代数中的一种更基本操作。

.. [#] In fact, the original paper introducing the relational model discusses joins and not cross products.  However, the cross product is now recognized as a more fundamental operation in relational algebra.

.. [#] 一些作者使用 * 来表示自然连接。

.. [#] Some authors use * instead to indicate a natural join.

.. [#] 更一般地说，**x** 和 **y** 可以代表一组属性；也就是说，**x** 可能是某些属性 **x1**, **x2**, ... 的列表，**y** 也是如此。我们只要求 **x** 和 **y** 一起代表 **P** 的所有属性，并且 **x** 和 **y** 之间不重叠。

.. [#] More generally, **x** and **y** can stand in for a list of attributes; that is, **x** might be some list of attributes **x1**, **x2**, ... and similarly for **y**.  We only require that **x** and **y** together represent all attributes of **P**, and that **x** and **y** do not overlap.


