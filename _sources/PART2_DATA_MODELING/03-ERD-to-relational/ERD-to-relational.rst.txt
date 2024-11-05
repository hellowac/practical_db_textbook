.. _erd-to-relational-chapter:

====================================
将 ERD 转换为关系模型
====================================

**Converting ERD to a relational model**

.. |right-arrow| unicode:: U+2192

.. index:: ERD; conversion to SQL

.. md-tab-set::

    .. md-tab-item:: 中文
        
        在本章中，我们将解释从实体关系模型创建关系数据库的过程。虽然许多步骤主要是机械的，但在这个过程中需要做出一些决策。我们将探讨每个决策的权衡。我们将使用第 :numref:`{number} <erd-chapter>` 章中的计算机制造商数据模型作为例子。

        本章假设你熟悉关系数据库模型的基本知识，包括表和主键及外键约束。必要的基础知识在第一部分（第 :numref:`{number} <basics-chapter>` 章和第 :numref:`{number} <constraints-chapter>` 章）或第三部分（第 :numref:`Chapter {number} <relational-model-chapter>` 章）中涵盖。

        表示关系数据库的方法有很多种：逻辑或物理数据模型（第 :numref:`Chapter {number} <other-notations-chapter>` 章）、文本或表格描述，或者 SQL 代码。你使用哪种方法将取决于你的开发过程和需求。在本章中，我们将提供以表格格式呈现的简单文本描述。

        我们从基本转换规则开始，逐步转换示例数据模型的各个部分。我们转换后得到的完整表格集将在本章末尾给出。

    .. md-tab-item:: 英文

        In this chapter we explain the process of creating a relational database from an entity-relationship model.  While many steps are largely mechanical, a number of decisions need to be made along the way.  We will explore the trade-offs for each decision.  We will use the computer manufacturer data model from :numref:`Chapter {number} <erd-chapter>` as our example.

        This chapter assumes you are familiar with the basics of the relational model of the database, including tables and primary and foreign key constraints.  The necessary foundations are covered in either Part I (Chapters :numref:`{number} <basics-chapter>` and :numref:`{number} <constraints-chapter>`) or Part III (:numref:`Chapter {number} <relational-model-chapter>`).

        There are many ways to represent the relational database: logical or physical data models (:numref:`Chapter {number} <other-notations-chapter>`), text or tabular descriptions, or SQL code.  Which you use will depend on your development process and needs.  In this chapter, we will provide simple text descriptions in tabular format.

        We start with the basic conversion rules, converting pieces of our example data model as we go.  The full set of tables resulting from our conversion is given at the end of the chapter.

实体
::::::::

**Entities**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        从 ERD 创建关系数据库的第一步是为数据模型中的每个实体创建一个表。弱实体需要与常规实体稍有不同的处理，因此我们将单独处理它们，从常规实体开始。

    .. md-tab-item:: 英文

        The first step in building a relational database from an ERD is creating a table from each entity in the data model.  Weak entities need slightly different handling than regular entities, so we will address them separately, starting with regular entities.

常规实体
-----------------

**Regular entities**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        首先，为表格决定一个名称——这并不一定要与实体名称相同！表格的命名方案有很多。如果你为有命名标准的公司或组织建立数据库，当然要遵循这些标准。否则，选择一种基本的方法并保持一致。例如，一些数据库为表格使用复数名词，而其他数据库则使用单数名词。在我们来自 :numref:`Chapter {number} <erd-chapter>` 的数据模型中，实体 **employee** 可以变成一个名为 **employee** 或 **employees** 的表格。另一个命名问题是表格名称包含多个单词；一些数据库选择将这些单词连在一起，而其他数据库则使用下划线字符。例如，实体 **assembly line** 可以变成一个名为 **assemblyline** 或 **assembly_line** 的表格。在下面的示例中，我们将使用单数名词和下划线。

        实体的大多数属性应转换为新表中的列。不要为派生属性创建列，因为这些值不打算存储。也不要为多值属性创建列；我们稍后会处理这些问题。对于复合属性，仅为组件属性创建列，而不是复合属性本身。与实体一样，你需要为每个新列决定一个名称，这个名称不必与属性名称相同。你还需要为列指定类型和任何约束。确定某些列的适当类型可能需要咨询你的数据领域专家。根据需要添加约束。下面的描述中，我们将使用简单的类型和约束描述，而不是 SQL 语法。

        选择一个关键属性（每个常规实体至少应有一个），并使用由它创建的列作为新表的主键。如果实体有多个关键属性，你需要决定哪个最适合作为主键。通常，较简单的主键比复杂的主键更受欢迎。如果需要，你可以将其他关键属性生成的列约束为非空且唯一，类似于主键列。例如，员工表可以使用公司生成的 ID 号码作为主键，同时包括一个政府颁发的 ID 号码列，并希望约束以防止重复。

        以下是我们对 **employee** 实体的 ERD 描述：

        .. image:: employee.svg
            :alt: 员工实体及其属性

        以下是将 **employee** 实体初步转换为名为 **employee** 的关系表：

        .. table:: 表 **employee** （初步）
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | 列名          | 类型     | 约束         | 备注                        |
            +===============+==========+==============+=============================+
            | id            | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | position      | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_rate      | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_type      | character| 's' 或 'h'   | s = 固定薪资, h = 时薪      |
            +---------------+----------+--------------+-----------------------------+
            | **键**                                                                |
            |                                                                       |
            | 主键: id                                                              |
            +---------------+----------+--------------+-----------------------------+

        这还不是最终的 **employee** 表！当我们处理 **employee** 实体参与的关系时，我们将向表中添加额外的列。

    .. md-tab-item:: 英文

        First, decide on a name for the table - this does not have to be the same as the entity name!  There are many naming schemes for tables.  If you are building a database for a company or organization that has naming standards, you will of course want to follow those.  Otherwise, choose a basic approach and be consistent.  For example, some databases use plural nouns for tables, while others use singular nouns.  In our data model from :numref:`Chapter {number} <erd-chapter>`, the entity **employee** might become a table named **employee** or **employees**.  Another naming issue arises with table names containing multiple words; some databases choose to run these together, while others employ underscore characters.  For example, the entity **assembly line** could become a table named **assemblyline** or **assembly_line**.  In our examples below, we will use singular nouns and underscores.

        Most attributes for the entity should be converted to columns in the new table.  Do not create columns for derived attributes, as these values are not intended to be stored.  Do not create columns for multivalued attributes; we will address these later.  For composite attributes, create columns only for the component attributes, not the composite itself.  As with entities, you will need to decide on a name for each new column, which does not have to be the same as the attribute name.  You will also need to specify a type and any constraints for the column.  Determining appropriate types for some columns may require consultation with your data domain experts.  Constraints may be added as appropriate.  In the descriptions below, we will use simple type and constraint descriptions, rather than SQL syntax.

        Choose a key attribute (every regular entity should have at least one) and use the column created from it as the primary key for the new table.  If the entity has multiple key attributes, you will need to decide which one makes most sense as a primary key.  Simpler primary keys are usually preferred over more complex ones.  If desired, you can constrain the columns resulting from other keys to be not null and unique similar to primary key columns.  For example, an employee table might use a company generated ID number as its primary key, and also include a column for a government issued ID number which we would want to constrain to prevent duplicates.

        Here is our ERD depiction of the **employee** entity:

        .. image:: employee.svg
            :alt: The employee entity and its attributes

        Here is a preliminary conversion of the **employee** entity into a relational table named **employee**:

        .. table:: Table **employee** (preliminary)
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | id            | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | position      | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_rate      | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_type      | character| 's' or 'h'   | s = salaried, h = hourly    |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: id                                                       |
            +---------------+----------+--------------+-----------------------------+

        This is not yet the final **employee** table!  We will add additional columns to the table when we address the relationships that the **employee** entity participates in.

弱实体
-------------

**Weak entities**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        弱实体几乎以与常规实体相同的方式转换为表格。然而，请记住，弱实体没有标识键属性。相反，它具有一个部分键，必须与父实体的键结合。在我们的示例中，**assembly line** 实体是弱实体。它的部分键是特定工厂内的组装线编号，必须与工厂标识结合以实现完整的标识。

        因此，从弱实体创建的表必须将父实体的键作为额外列纳入。新表的主键将由从父键和部分键创建的列组成。此外，从父键创建的列应被约束为始终匹配父表中的某个键，使用外键约束。

        以下是 **assembly line** 及其父实体 **factory** 的 ERD：

        .. image:: assembly_line.svg
            :alt: 组装线和工厂实体，它们的属性，以及连接它们的包含关系

        根据上述指南，我们应该创建 **factory** 和 **assembly_line** 表，并在 **assembly_line** 中包含一个用于 **factory** 的 **city** 列值的列。这些“借用”列的名称一个好的选择是将原表和列名称连接在一起；在我们的例子中，这给我们提供了列 **factory_city**。（我们将使用“借用”这个术语来指代在一个表中插入一列以存储相关表的主键列值的过程。）以下是 **factory** 的初步转换和 **assembly line** 的最终转换：

        .. table:: 表 **factory** （初步）
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | 列名          | 类型     | 约束         | 备注                        |
            +===============+==========+==============+=============================+
            | city          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | **键**                                                                |
            |                                                                       |
            | 主键: city                                                            |
            +---------------+----------+--------------+-----------------------------+

        .. table:: 表 **assembly_line**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | 列名          | 类型     | 约束         | 备注                        |
            +===============+==========+==============+=============================+
            | city          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | number        | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | throughput    | real     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **键**                                                                |
            |                                                                       |
            | 主键: factory_city, number                                            |
            |                                                                       |
            | 外键: factory_city |right-arrow| factory (city)                       |
            +---------------+----------+--------------+-----------------------------+

    .. md-tab-item:: 英文

        Weak entities are converted into tables in nearly the same way as regular entities.  However, recall that a weak entity has no identifying key attribute.  Instead, it has a partial key, which must be combined with the key of the parent entity.  In our example, the **assembly line** entity is weak.  Its partial key, the number of the assembly line within a particular factory, must be combined with the factory identity for full identification.

        The table created from a weak entity must therefore incorporate the key from the parent entity as an additional column.  The primary key for the new table will be composed of the columns created from the parent key and from the partial key.  Additionally, the column created from the parent key should be constrained to always match some key in the parent table, using a foreign key constraint.

        Here is the ERD of **assembly line** and its parent entity, **factory**:

        .. image:: assembly_line.svg
            :alt:  The assembly line and factory entities, their attributes, and the contains relationship connecting them

        Using the above guidelines, we should create tables **factory** and **assembly_line**, and include a column in **assembly_line** for values from the **city** column of **factory**.  A good choice of name for these "borrowed" columns is to concatenate the original table and column names together; in our case, this gives us the column **factory_city**.  (We will use the term "borrow" in reference to this process of inserting a column in one table to hold values from the primary key column of a related table.)  Here is the preliminary conversion of **factory** and the final conversion of **assembly line**:

        .. table:: Table **factory** (preliminary)
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | city          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: city                                                     |
            +---------------+----------+--------------+-----------------------------+

        .. table:: Table **assembly_line**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | factory_city  | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | number        | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | throughput    | real     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: factory_city, number                                     |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            +---------------+----------+--------------+-----------------------------+


关系
:::::::::::::

**Relationships**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        关系可以通过几种不同的方法处理，具体取决于关系的基数比。一般来说，我们可以创建一个表来表示该关系。这种表称为 *交叉引用(cross-reference)* 表，并作为与参与关系的两个（或更多）表之间的三方连接的中介。正如我们将看到的，一些基数比允许更简单的解决方案。

    .. md-tab-item:: 英文

        Relationships can be handled using a few different approaches, depending on the cardinality ratio of the relationship.  Most generally, we can create a table to represent the relationship.  This kind of table is known as a *cross-reference* table, and acts as an intermediary in a three-way join with the two (or more) tables whose entities participate in the relationship.  As we will see, some cardinality ratios permit simpler solutions.

多对多
------------

**Many-to-many**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        多对多关系是最一般类型的关系；适应多对多关系的数据库结构也可以适应一对多或一对一关系，因为“一”只是“多”的一个特殊情况。多对多关系的挑战在于如何表示一张表中的记录与另一张表中的多条记录之间的连接。虽然现代 SQL 允许在表中使用数组值列，但并不是所有数据库都支持它们。传统的解决方案是创建一个交叉引用表。

        给定表 **A** 和表 **B**，我们创建一个交叉引用表，其中列对应于 **A** 和 **B** 的主键。交叉引用表中的每一行存储来自 **A** 的一个主键值与来自 **B** 的一个主键值的唯一配对。因此，每一行表示 **A** 中的一行与 **B** 中的一行之间的单个连接。如果 **A** 中的一行与 **B** 中的多行相关联，则会有多条记录具有相同的 **A** 主键值，并与每个相关的 **B** 主键值配对。

        例如，我们的 ERD 指示 **vendor** 和 **part** 实体之间存在多对多关系。一个计算机部件（如 8TB 硬盘）可以来自多个供应商，而供应商可以销售多种不同的计算机部件：

        .. image:: supplies.svg
            :alt: 供应商和部件实体，它们的属性，以及连接它们的供应关系

        我们按照上述指导原则创建表 **vendor** 和 **part**，然后创建交叉引用表 **vendor_part**。（通常将交叉引用表命名为与两个相关表的名称组合在一起，尽管当然可以使用其他方案。）请注意，**supplies** 关系还有一个关系属性 **price**，我们可以将其合并到交叉引用表中。结果，结合一些虚构数据，见下图：

        .. image:: vendor_part_xref.svg
            :alt: 表 vendor、part 和 vendor_part 以及示例数据

        交叉引用表中的数据在多个方面受到约束。首先，我们只想存储行之间的关系一次，因此我们将相关表的主键组合作为交叉引用表的主键。在我们的例子中，主键是 **vendor_name** 和 **part_number** 的组合。其次，每个借用的主键列应受到约束，只能保存在原始表中存在的值，使用外键约束。

        以下是 **vendor**、**part** 和 **vendor_part** 交叉引用表的描述：

        .. table:: 表 **vendor**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | email         | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | phone         | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: name                                                     |
            +---------------+----------+--------------+-----------------------------+

        .. table:: 表 **part**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | part_number   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | description   | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: part_number                                              |
            +---------------+----------+--------------+-----------------------------+

        .. table:: 表 **vendor_part**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | vendor_name   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | part_number   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | price         | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: vendor_name, part_number                                 |
            |                                                                       |
            | Foreign key: vendor_name |right-arrow| vendor (name)                  |
            |                                                                       |
            | Foreign key: part_number |right-arrow| part (part_number)             |
            +---------------+----------+--------------+-----------------------------+

    .. md-tab-item:: 英文

        Many-to-many relationships are the most general type of relationship; a database structure accommodating a many-to-many relationship can also accommodate one-to-many or one-to-one relationships, as "one" is just a special case of "many".  The challenge for many-to-many relationships is how to represent a connection from a record in one table to multiple records in the other table.  While modern SQL allows array valued columns in tables, not all databases support them.  The traditional solution is to create a cross-reference table.

        Given a table **A** and a table **B**, we create a cross-reference table with columns corresponding to the primary keys of **A** and **B**.  Each row in the cross-reference table stores one unique pairing of a primary key value from **A** with a primary key value from **B**.  Each row thus represents a single connection between one row in **A** with one row in **B**.  If a row in **A** is related to multiple rows in **B**, then there will be multiple entries with the same **A** primary key value, paired with each related **B** primary key value.

        For example, our ERD indicates a many-to-many relationship between the entities **vendor** and **part**.  A computer part (such as an 8TB hard drive) can come from multiple sellers, while sellers can sell multiple different computer parts:

        .. image:: supplies.svg
            :alt: The vendor and part entities, their attributes, and the supplies relationship connecting them

        We create tables **vendor** and **part** following the guidelines above, and then create the cross-reference table **vendor_part**.  (It is common to name a cross-reference table using the names of the two tables being related, although other schemes can of course be used.)  Note that the **supplies** relationship also has a relationship attribute, **price**, which we can incorporate into the cross-reference table.  The result, with some fictional data, is pictured below:

        .. image:: vendor_part_xref.svg
            :alt: The tables vendor, part, and vendor_part with sample data

        Data in the cross-reference table is constrained in several ways.  First, we only want to store the relationship between rows once, so we make the combination of primary keys from the related tables into a primary key for the cross-reference table.  In our example, the primary key is the combination of **vendor_name** and **part_number**.  Second, each of the borrowed primary key columns should be constrained to only hold values that are present in the original tables, using foreign key constraints.

        Table descriptions for **vendor**, **part**, and the **vendor_part** cross-reference table are given below:

        .. table:: Table **vendor**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | email         | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | phone         | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: name                                                     |
            +---------------+----------+--------------+-----------------------------+

        .. table:: Table **part**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | part_number   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | description   | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: part_number                                              |
            +---------------+----------+--------------+-----------------------------+

        .. table:: Table **vendor_part**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | vendor_name   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | part_number   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | price         | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: vendor_name, part_number                                 |
            |                                                                       |
            | Foreign key: vendor_name |right-arrow| vendor (name)                  |
            |                                                                       |
            | Foreign key: part_number |right-arrow| part (part_number)             |
            +---------------+----------+--------------+-----------------------------+


一对多
-----------

**One-to-many**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        作为多对多关系的特例，一对多关系可以使用交叉引用表在数据库中实现，如上所述。然而，我们还有另一个选择。注意到关系的“多”侧的行最多可以与“一个”侧的行相关联，我们可以选择通过在“多”侧表中存储“一个”侧表的主键来捕捉这种关系。

        在我们的 ERD 中，**employee** 实体与 **factory** 及其自身之间参与了一对多关系：

        .. image:: one_to_many.svg
            :alt: 员工和工厂实体及其属性，以及监督、管理和工作于关系

        **employee** 和 **factory** 之间也存在一对一关系，我们将在下一节中处理。

        首先考虑 **works at** 关系，我们看到每个员工最多只在一个工厂工作。因此，我们可以在 **employee** 表中包含一个工厂城市的列。为了与之前的选择保持一致，我们将该列命名为 **factory_city**。此列应受到外键约束，引用 **factory** 表。

        我们还需要处理 **supervises** 关系。与上述方法类似，我们应在 **employee** 表中包含一个列，存储来自 **employee** 表的主键。然而，我们应仔细考虑为这个新增列命名；**employee_id** 将是一个非常误导的选择！更好的选择是考虑将要存储的员工的角色，并将列命名为 **supervisor_id**。

        经过这些更改，**employee** 表现在如下所示：

        .. table:: 表 **employee**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | id            | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | position      | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_rate      | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_type      | character|   's' or 'h' | s = salaried, h = hourly    |
            +---------------+----------+--------------+-----------------------------+
            | factory_city  | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | supervisor_id | integer  |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: id                                                       |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            |                                                                       |
            | Foreign key: supervisor_id |right-arrow| employee (id)                |
            +---------------+----------+--------------+-----------------------------+

        使用交叉引用表代替上述方案是一个完全有效的选择，如果有任何可能性数据模型可能会更改，使得一对多关系变为多对多关系，这可能更可取。在我们的示例 ERD 中，特定计算机型号只在一个工厂生产（而工厂可以生产多种不同的型号）；然而，如果在某个时候我们想允许在多个地点生产模型，这也并不奇怪。我们可能选择为 **factory** 和 **model** 之间的关系使用交叉引用表，以预见这一可能性。

    .. md-tab-item:: 英文

        As a special case of many-to-many relationships, one-to-many relationships can be implemented in the database using a cross-reference table as above.  We have another choice, however.  Observing that rows on the "many" side of the relationship can be associated with at most one row from the "one" side, we can choose to capture the relationship by storing the primary key of the "one" side table in the "many" side table.

        In our ERD, the **employee** entity participates in one-to-many relationships with both **factory** and itself:

        .. image:: one_to_many.svg
            :alt: The employee and factory entities and their attributes, and the supervises, manages, and works at relationships

        There is also a one-to-one relationship between **employee** and **factory**, which we will deal with in the next section.

        Considering first the **works at** relationship, we see that each employee works at no more than one factory.  Therefore, we can include a column for the factory's city in the **employee** table.  For consistency with previous choices, we will call this column **factory_city**.  This column should be constrained by a foreign key referencing the **factory** table.

        We also have the **supervises** relationship to deal with.  In the same fashion as above, we should include a column in the **employee** table containing primary keys from the **employee** table.  However, we should give careful consideration to the name we give this added column; **employee_id** would be a very misleading choice!  A better choice is to consider the role of the employee whose id will be stored, and call the column **supervisor_id**.

        With these changes, the **employee** table now looks like:

        .. table:: Table **employee**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | id            | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | position      | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_rate      | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_type      | character|   's' or 'h' | s = salaried, h = hourly    |
            +---------------+----------+--------------+-----------------------------+
            | factory_city  | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | supervisor_id | integer  |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: id                                                       |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            |                                                                       |
            | Foreign key: supervisor_id |right-arrow| employee (id)                |
            +---------------+----------+--------------+-----------------------------+

        Using a cross-reference table instead of the above scheme is a perfectly valid choice, and may be preferable if there is any chance the data model might change such that the one-to-many relationship becomes many-to-many.  In our example ERD, a given computer model is built at only one factory (while factories can build multiple different models); however, it would not be surprising if, at some point, we want to allow for models to be built at multiple locations.  We might choose to use a cross-reference table for the relationship between **factory** and **model** in anticipation of this possibility.

一对一
----------

**One-to-one**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        一对一关系可以被视为一对多关系的特例，因此您可以使用适合一对多关系的任何方法。在大多数情况下，最好是从一个表中借用主键作为另一个表中的外键。使用这种方法，您可以从任一侧借用；然而，通常一种选择比另一种选择更可取。

        在我们的示例中，**employee** 和 **factory** 之间存在一对一关系 **manages**。因此，我们可以在 **employee** 表中添加另一列，这次是员工管理的工厂的城市。然而，大多数员工并不管理工厂，因此该列最终将包含许多 ``NULL`` 值。

        另一方面，每个工厂都应该有一位经理（由 **factory** 在关系中的完全参与隐含）。因此，在 **factory** 表中添加一列用于表示管理该工厂的员工是完全合理的。这是另一个情况下，给该列命名为员工在此关系中的角色是有意义的，因此我们将新列命名为 **manager_id**。

        这是完成的 **factory** 表：

        .. table:: 表 **factory**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | city          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | manager_id    | integer  |see note [#]_ |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: city                                                     |
            |                                                                       |
            | Foreign key: manager_id |right-arrow| employee (id)                   |
            +---------------+----------+--------------+-----------------------------+

        在一些少见的情况下，处理一对一关系可能通过简单地将参与的表合并为一个表来进行。这种情况应该留给两者在关系中都有完全参与的情况。

    .. md-tab-item:: 英文

        One-to-one relationships can be considered a special case of one-to-many relationships, so you can utilize either approach suitable for one-to-many relationships.  In most cases, it will be preferable to borrow the primary key from one table as a foreign key in the other table.  Using this approach, you could borrow from either side; however, one choice is often preferable to another.

        In our example, we have a one-to-one relationship, **manages**, between **employee** and **factory**.  We could therefore add another column to the **employee** table, this time for the city of the factory that the employee manages.  However, most employees do not manage factories, so the column will end up containing many ``NULL`` values.

        On the other hand, every factory should have a manager (implied by the total participation of **factory** in the relationship). It makes perfect sense, then, to add a column to the **factory** table for the employee managing the factory.  This is another situation in which it makes sense to name the column for the role of the employee in this relationship, so we will call the new column **manager_id**.

        Here is the completed **factory** table:

        .. table:: Table **factory**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | city          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | manager_id    | integer  |see note [#]_ |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: city                                                     |
            |                                                                       |
            | Foreign key: manager_id |right-arrow| employee (id)                   |
            +---------------+----------+--------------+-----------------------------+

        In some rare cases, it may make sense to handle a one-to-one relationship by simply merging the participating tables into one table.  This should probably be reserved for situations in which both entities have total participation in the relationship.

高元数关系
--------------------------

**Higher arity relationships**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        对于有三个或更多参与者的关系，包含每个参与表的主键的交叉引用表是最佳选择。

    .. md-tab-item:: 英文

        For relationships with three or more participants, a cross-reference table incorporating primary keys from each of the participating tables is the best choice.

识别关系
-------------------------

**Identifying relationships**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        识别弱实体的关系必然是一对多或一对一。但是，弱实体的转换已经包含来自父表的主键值列。这足以捕获关系。

    .. md-tab-item:: 英文

        Identifying relationships for weak entities are necessarily one-to-many or one-to-one.  However, the conversion of the weak entity already incorporates a column containing primary key values from the parent table.  This suffices to capture the relationship.

多值属性
::::::::::::::::::::::

**Multivalued attributes**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        多值属性可以用于建模几种不同的场景。因此，在关系数据库中存储多值数据有多种选择。

        在最简单的情况下，当需要存储任意值的列表时，但没有特别期望这些值在数据库搜索中被检查，这时可以使用多值属性。在这种情况下，对于支持此类列的数据库，数组值列可能是合适的选择。

        当需要查询与多值属性相关的值时，或者对于不支持数组值列的数据库，最好的选择可能是创建一个简单的表，包含两个列，一个用于拥有表的主键，一个用于值本身。表中的每个条目将一个值与实体的实例关联。

        在我们的示例中，计算机模型可以面向不同应用程序的客户，例如游戏、视频编辑或商业用途。这在我们的数据模型中用多值 **application** 属性表示：

        .. image:: multivalued.svg
            :alt: 模型实体及其属性

        因此，我们可以使用以下两个表实现模型实体及其属性：

        .. table:: 表 **model** (初步)
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | number        | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | type          | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: name, number                                             |
            +---------------+----------+--------------+-----------------------------+

        .. table:: 表 **model_application** (初步)
            :class: lined-table

            +---------------+----------+--------------+----------------------------------+
            | Column name   | Type     | Constraints  | Notes                            |
            +===============+==========+==============+==================================+
            | model_name    | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | model_number  | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | application   | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | **Keys**                                                                   |
            |                                                                            |
            | Primary key: model_name, model_number, application                         |
            |                                                                            |
            | Foreign key: (model_name, model_number) |right-arrow| model (name, number) |
            +---------------+----------+--------------+----------------------------------+

        许多应用程序还要求与多值属性相关联的值限制在某个值列表中。在这种情况下，使用一个额外的表。额外的表仅用于包含允许的值，从而允许我们将数据限制为这些值。对于更复杂的值，可以添加一个人工标识符作为主键，并在多值属性表中使用主键而不是值本身，此时多值属性表变成交叉引用表。对于简单值的小列表（如我们的示例），这会增加不必要的复杂性。

        在我们的示例中，我们将使用引用此简单表的外键约束来约束 **application** 列：

        .. table:: 表 **application**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | application   | text     | not null     | gaming, business, etc.      |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: application                                              |
            +---------------+----------+--------------+-----------------------------+

    .. md-tab-item:: 英文

        Multivalued attributes can be used to model a few different scenarios.  As a result, there are multiple choices for how to store multivalued data in a relational database.

        In the simplest case, a multivalued attribute is used when a list of arbitrary values needs to be stored, but there is no particular expectation that the values will be examined in a search of the database.  In this case, an array-valued column may be an appropriate choice for databases that support such columns.

        When there is a need to query the values associated with a multivalued attribute, or for databases that do not support array-valued columns, the best choice may be to make a simple table with two columns, one for the primary key of the owning table, and one for the values themselves.  Each entry in the table associates one value with the instance of the entity.

        In our example, computer models can be marketed to customers for different applications, such as gaming, video editing, or business use.  This is represented in our data model with the multivalued **application** attribute:

        .. image:: multivalued.svg
            :alt: The model entity and its attributes

        We might, then, implement the model entity and its attributes using the following two tables:

        .. table:: Table **model** (preliminary)
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | number        | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | type          | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: name, number                                             |
            +---------------+----------+--------------+-----------------------------+

        .. table:: Table **model_application** (preliminary)
            :class: lined-table; in this case

            +---------------+----------+--------------+----------------------------------+
            | Column name   | Type     | Constraints  | Notes                            |
            +===============+==========+==============+==================================+
            | model_name    | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | model_number  | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | application   | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | **Keys**                                                                   |
            |                                                                            |
            | Primary key: model_name, model_number, application                         |
            |                                                                            |
            | Foreign key: (model_name, model_number) |right-arrow| model (name, number) |
            +---------------+----------+--------------+----------------------------------+

        Many applications also require the values associated with a multivalued attribute to be restricted to a certain list of values.  In this case, an additional table is used.  The additional table exists just to contain the allowed values, allowing us to constrain the data to just those values.  For more complex values, an artificial identifier may be added as a primary key, and the primary key used in the multivalued attribute table instead of the values themselves, in which case the multivalued attribute table becomes a cross-reference table. For small lists of simple values (as in our example), this adds unnecessary complication.

        For our example, we will constrain the **application** column using a foreign key constraint referencing this simple table:

        .. table:: Table **application**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | application   | text     | not null     | gaming, business, etc.      |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: application                                              |
            +---------------+----------+--------------+-----------------------------+


完整的模型转换
:::::::::::::::::::::

**Full model conversion**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        在本节中，我们将收集所有从示例数据模型中产生的表，使用上述概述的方法。对于每个表，我们将包含一个简短的说明，阐述该表与数据模型的关系。

        .. table:: 表 **employee**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | id            | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | position      | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_rate      | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_type      | character| 's' or 'h'   | s = salaried, h = hourly    |
            +---------------+----------+--------------+-----------------------------+
            | factory       | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | supervisor_id | integer  |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: id                                                       |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            |                                                                       |
            | Foreign key: supervisor_id |right-arrow| employee (id)                |
            +---------------+----------+--------------+-----------------------------+

        **employee** 表包含 **employee** 实体的属性列以及实现 **works at** 和 **supervises** 关系的外键。

        .. table:: 表 **factory**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | city          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | manager_id    | integer  |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: city                                                     |
            |                                                                       |
            | Foreign key: manager_id |right-arrow| employee (id)                   |
            +---------------+----------+--------------+-----------------------------+

        **factory** 表包含 **factory** 实体的属性列以及实现 **manages** 关系的外键。**throughput** 属性在表中没有反映，因为它是一个派生属性。一个工厂的产出可以通过对该工厂的所有装配线的产出求和来计算。

        .. table:: 表 **assembly_line**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | factory_city  | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | number        | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | throughput    | real     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: factory_city, number                                     |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            +---------------+----------+--------------+-----------------------------+

        **assembly_line** 表实现了 **assembly line** 弱实体。它包含一个引用 **factory** 父实体的外键。其主键由父实体键 (**factory_city**) 和部分键 (**number**) 组成。

        .. table:: 表 **model**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | number        | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | type          | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | factory_city  | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: name, number                                             |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            +---------------+----------+--------------+-----------------------------+

        **model** 表包含 **model** 实体的属性列。仅包含复合属性 **designation** 的组件属性；由于 **designation** 也是 **model** 的关键属性，**model** 表具有复合主键。该表还包含一个实现 **builds** 关系的外键。如上文所述，**builds** 关系也可以使用连接 **factory** 和 **builds** 的交叉引用表来实现，但我们在这里选择了更简单的解决方案。我们假设计算机模型的标识包括计算机系列的名称（例如 "Orion"）和某个特定版本的计算机系列，我们称之为模型的 "number"。这些版本可能包含字母和数字（例如 "xz450"），这就是为什么命名为 "number" 的列实现为文本类型。

        .. table:: 表 **model_application**
            :class: lined-table

            +---------------+----------+--------------+----------------------------------+
            | Column name   | Type     | Constraints  | Notes                            |
            +===============+==========+==============+==================================+
            | model_name    | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | model_number  | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | application   | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | **Keys**                                                                   |
            |                                                                            |
            | Primary key: model_name, model_number, application                         |
            |                                                                            |
            | Foreign key: (model_name, model_number) |right-arrow| model (name, number) |
            |                                                                            |
            | Foreign key: application |right-arrow| application (application)           |
            +---------------+----------+--------------+----------------------------------+

        在这种情况下 **model_application** 表实现了 **model** 实体的多值属性 **application**。表的每一行包含描述特定计算机模型的单个 **application** 值。注意，由于 **model** 实体具有复合主键，**model_application** 表具有引用其父级的复合外键（*而不是*为父键的每个组件提供两个独立的外键）。此外，我们限制 **application** 中的值来自于 **application** 表（如下）中包含的一组可能值。

        .. table:: 表 **application**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | application   | text     | not null     | gaming, business, etc.      |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: application                                              |
            +---------------+----------+--------------+-----------------------------+

        **application** 表包含一个简单的唯一值列表，可插入到 **model_application** 表中。

        .. table:: 表 **part**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | part_number   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | description   | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: part_number                                              |
            +---------------+----------+--------------+-----------------------------+

        **part** 表包含 **part** 实体的属性列。此处的列 **part_number** 类似于上面的模型 "number"，可以包含字符和数字，因此我们再次使用文本类型的列。

        .. table:: 表 **model_part**
            :class: lined-table

            +---------------+----------+--------------+----------------------------------+
            | Column name   | Type     | Constraints  | Notes                            |
            +===============+==========+==============+==================================+
            | model_name    | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | model_number  | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | part_number   | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | **Keys**                                                                   |
            |                                                                            |
            | Primary key: model_name, model_number, part_number                         |
            |                                                                            |
            | Foreign key: (model_name, model_number) |right-arrow| model (name, number) |
            |                                                                            |
            | Foreign key: part_number |right-arrow| part (part_number)                  |
            +---------------+----------+--------------+----------------------------------+

        **model_part** 表是一个交叉引用表，实现了 **can use** 关系。

        .. table:: 表 **vendor**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | email         | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | phone         | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: name                                                     |
            +---------------+----------+--------------+-----------------------------+

        **vendor** 表包含 **vendor** 实体的属性列。仅反映 **contact info** 属性的组件属性。

        .. table:: 表 **vendor_part**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | vendor_name   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | part_number   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | price         | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: vendor_name, part_number                                 |
            |                                                                       |
            | Foreign key: vendor_name |right-arrow| vendor (name)                  |
            |                                                                       |
            | Foreign key: part_number |right-arrow| part (part_number)             |
            +---------------+----------+--------------+-----------------------------+

        **vendor_part** 表是一个交叉引用表，实现了 **supplies** 关系。除了与其相关的表的外键外，它还包含关系的 **price** 属性列。  

    .. md-tab-item:: 英文

        In this section, we collect together all of the tables produced from our example data model, using the approach outlined above.  For each table we include a short explanation of how the table relates to the data model.

        .. table:: Table **employee**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | id            | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | position      | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_rate      | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | pay_type      | character| 's' or 'h'   | s = salaried, h = hourly    |
            +---------------+----------+--------------+-----------------------------+
            | factory       | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | supervisor_id | integer  |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: id                                                       |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            |                                                                       |
            | Foreign key: supervisor_id |right-arrow| employee (id)                |
            +---------------+----------+--------------+-----------------------------+

        The **employee** table contains columns for the attributes of the **employee** entity and foreign keys implementing the relationships **works at** and **supervises**.

        .. table:: Table **factory**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | city          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | manager_id    | integer  |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: city                                                     |
            |                                                                       |
            | Foreign key: manager_id |right-arrow| employee (id)                   |
            +---------------+----------+--------------+-----------------------------+

        The **factory** table contains columns for the attributes of the **factory** entity and a foreign key implementing the relationship **manages**.  The **throughput** attribute is not reflected in the table, as it is a derived attribute.  The throughput of a factory can be computed by summing the throughputs of the assembly lines in the factory.

        .. table:: Table **assembly_line**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | factory_city  | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | number        | integer  | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | throughput    | real     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: factory_city, number                                     |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            +---------------+----------+--------------+-----------------------------+

        The **assembly_line** table implements the **assembly line** weak entity.  It incorporates a foreign key referencing the **factory** parent entity.  Its primary key is composed of the parent entity key (**factory_city**) and the partial key (**number**).

        .. table:: Table **model**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | number        | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | type          | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | factory_city  | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: name, number                                             |
            |                                                                       |
            | Foreign key: factory_city |right-arrow| factory (city)                |
            +---------------+----------+--------------+-----------------------------+

        The **model** table contains columns for the attributes of the **model** entity.  Only the component attributes of the composite attribute **designation** are included; as **designation** was also the key attribute for **model**, the **model** table has a composite primary key.  The table also includes a foreign key implementing the **builds** relationship.  As mentioned in the text above, the **builds** relationship could alternatively be implemented using a cross-reference table connecting **factory** and **builds**, but we have opted for the simpler solution here.  We assume that the designation of computer models includes the name of the computer line (e.g. "Orion") and some particular version of the computer line, which we call the "number" of the model.  These versions may contain letters as well as numbers (e.g., "xz450"), which is why a column named "number" is implemented as text.

        .. table:: Table **model_application**
            :class: lined-table; in this case

            +---------------+----------+--------------+----------------------------------+
            | Column name   | Type     | Constraints  | Notes                            |
            +===============+==========+==============+==================================+
            | model_name    | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | model_number  | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | application   | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | **Keys**                                                                   |
            |                                                                            |
            | Primary key: model_name, model_number, application                         |
            |                                                                            |
            | Foreign key: (model_name, model_number) |right-arrow| model (name, number) |
            |                                                                            |
            | Foreign key: application |right-arrow| application (application)           |
            +---------------+----------+--------------+----------------------------------+

        The **model_application** table implements the multivalued attribute **application** of the **model** entity.  Each row of the table contains a single **application** value describing a particular computer model.  Note that, as the **model** entity has a composite primary key, the **model_application** table has a composite foreign key referencing its parent (*not* two separate foreign keys for each component of the parent key).  Additionally, we constrain the values in **application** to come from a set list of possible values, contained in the **application** table (below).

        .. table:: Table **application**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | application   | text     | not null     | gaming, business, etc.      |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: application                                              |
            +---------------+----------+--------------+-----------------------------+

        The **application** table contains a simple list of unique values which are available to insert into the **model_application** table.

        .. table:: Table **part**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | part_number   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | description   | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: part_number                                              |
            +---------------+----------+--------------+-----------------------------+

        The **part** table contains columns for the attributes of the **part** entity.  The column **part_number** here, similar to the model "number" above, can contain characters as well as numbers, so again we use a text type column.

        .. table:: Table **model_part**
            :class: lined-table

            +---------------+----------+--------------+----------------------------------+
            | Column name   | Type     | Constraints  | Notes                            |
            +===============+==========+==============+==================================+
            | model_name    | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | model_number  | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | part_number   | text     | not null     |                                  |
            +---------------+----------+--------------+----------------------------------+
            | **Keys**                                                                   |
            |                                                                            |
            | Primary key: model_name, model_number, part_number                         |
            |                                                                            |
            | Foreign key: (model_name, model_number) |right-arrow| model (name, number) |
            |                                                                            |
            | Foreign key: part_number |right-arrow| part (part_number)                  |
            +---------------+----------+--------------+----------------------------------+

        The **model_part** table is a cross-reference table implementing the **can use** relationship.

        .. table:: Table **vendor**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | name          | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | email         | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | phone         | text     |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: name                                                     |
            +---------------+----------+--------------+-----------------------------+

        The **vendor** table contains columns for the attributes of the **vendor** entity.  Only the component attributes of the **contact info** attribute are reflected.

        .. table:: Table **vendor_part**
            :class: lined-table

            +---------------+----------+--------------+-----------------------------+
            | Column name   | Type     | Constraints  | Notes                       |
            +===============+==========+==============+=============================+
            | vendor_name   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | part_number   | text     | not null     |                             |
            +---------------+----------+--------------+-----------------------------+
            | price         | currency |              |                             |
            +---------------+----------+--------------+-----------------------------+
            | **Keys**                                                              |
            |                                                                       |
            | Primary key: vendor_name, part_number                                 |
            |                                                                       |
            | Foreign key: vendor_name |right-arrow| vendor (name)                  |
            |                                                                       |
            | Foreign key: part_number |right-arrow| part (part_number)             |
            +---------------+----------+--------------+-----------------------------+

        The **vendor_part** table is a cross-reference table implementing the **supplies** relationship.  In addition to the foreign keys for the tables it relates to, it contains a column for the **price** attribute of the relationship.


自检练习
::::::::::::::::::::

**Self-check exercises**

.. md-tab-set::

    .. md-tab-item:: 中文
        
        本节包含一些问题，您可以用来检查自己如何将ERD转换为关系数据库的理解。

        - 我们的ERD中的实体变成了关系数据库中的表。关系变成了什么？

          - A: 表
          - B: 外键
          - C: 表的合并
          - D: 以上所有

        .. admonition:: 显示答案
            :class: dropdown

            - A: 任何关系都可以转换为交叉引用表。这是唯一的可能性吗？
            - B: 一对一和一对多关系可以转换为我们数据库中的外键。这些是唯一的基数比率吗？
            - C: 一对一关系可以导致表的合并，尽管这很少见。
            + D: 上述每种方法都可以应用，具体取决于关系的基数比率和其他因素。

        - 考虑下面的ERD。我们创建表 **a** 和 **b**，每个表都有一个名为 "id" 的主键列。（假设有其他未显示的属性列。）转换 **A** 和 **B** 之间的关系的最简单方法是什么？

          .. image:: self_test_many_to_one.svg
              :alt: 实体A和B各自具有关键属性ID。A和B之间的关系是多对一（A侧为多）。

          - A: 创建一个名为 "a_id" 的列在表 **b** 中，并将其设为引用表 **a** 的外键。
          - B: 在表 **a** 中创建一个名为 "b_id" 的列，并将其设为引用表 **b** 的外键。
          - C: 创建一个交叉引用表 **a_b**，包含作为外键引用 **a** 和 **b** 的列 **a_id** 和 **b_id**。
          - D: 将表 **a** 和 **b** 合并为一个新表。

        .. admonition:: 显示答案
            :class: dropdown

            - A: 由于表 **b** 中的一行可能与表 **a** 中的多行相关，我们需要在列 **a_id** 中存储多个ID值。 一些数据库会允许这样做，但这会使查询和更新变得复杂。
            + B: 这是最简单的解决方案，假设我们不期望将来关系变为多对多。
            - C: 这是一个允许的转换。它是最简单的吗？
            - D: 这不是一个好的选择；虽然这样的结构可以使其正常工作，但不被认为是好的数据库设计，容易出错。
            我们会说这个表没有得到适当的*规范化*。我们将在 :numref:`Part {number} <relational-theory-part>` 中探讨规范化。

        - 考虑下面的ERD。我们创建表 **r**，主键列为 **id**。表 **w** 应该是什么样的？

          .. image:: self_test_weak.svg
              :alt: 实体R具有关键ID，而弱实体W具有部分关键partial。R和W之间的识别关系是一对多。

           - A: 表应具有列 **partial** 作为主键。此外，创建一个交叉引用表 **r_w**。
           - B: 表应具有列 **partial** 和 **r_id**。主键是 **partial**。 在 **r_id** 上添加外键约束，引用 **r**。
           - C: 表应具有列 **partial** 和 **r_id**。主键是 **r_id** 和 **partial** 的组合。 在 **r_id** 上添加外键约束，引用 **r**。
           - D: 表应具有列 **partial** 和 **r_id**。主键是 **r_id**。在 **r_id** 上添加外键约束，引用 **r**。

        .. admonition:: 显示答案
            :class: dropdown

            - A: 部分关键不能成为主键。它们并不代表弱实体实例的唯一标识符。
            - B: 部分关键不能成为主键。它们并不代表弱实体实例的唯一标识符。
            + C: 正确。
            - D: 父键不足以成为弱实体的主键；在 **w** 中会有多行具有相同的 **r_id** 值。 因此，它不能成为主键。

        - 考虑下面的ERD。我们创建表 **c** 和 **d**，每个表都有一个名为 "id" 的主键列。我们应该如何处理 **C** 和 **D** 之间的关系？

          .. image:: self_test_relationship_attribute.svg
              :alt: 实体C和D各自具有关键属性ID。C和D之间的关系是多对多，并具有名为 "x" 的属性。

        - A: 从一个表借用主键作为另一个表中的外键（任一方向都可以）。在具有外键列的表中添加名为 "x" 的列。
        - B: 创建一个交叉引用表 **c_d**，其列为 **c_id**、**d_id** 和 **x**。使用 **c_id** 和 **d_id** 作为复合主键。对 **c_id** 和 **d_id** 添加外键约束，分别引用 **c** 和 **d**。
        - C: 创建一个交叉引用表 **c_d**，其列为 **c_id** 和 **d_id**。使用 **c_id** 和 **d_id** 作为复合主键。 对 **c_id** 和 **d_id** 添加外键约束，分别引用 **c** 和 **d**。创建另一个表 **c_d_x**，其列为 **c_id**、**d_id** 和 **x**。表 **c_d_x** 具有主键 **x**，并在 **c_id** 和 **d_id** 上具有外键约束，引用表 **c_d**。
        - D: 创建一个交叉引用表 **c_d**，其列为 **c_id** 和 **d_id**。使用 **c_id** 和 **d_id** 作为复合主键。对 **c_id** 和 **d_id** 添加外键约束，分别引用 **c** 和 **d**。在 **c** 或 **d** 中添加列 **x**。

        .. admonition:: 显示答案
            :class: dropdown

            - A: 这不是一个好的选择；虽然这样的结构可以使其正常工作，但不被认为是好的数据库设计，容易出错。
                我们会说这个表没有得到适当的*规范化*。我们将在 :numref:`Part {number} <relational-theory-part>` 中探讨规范化。
            + B: 正确。
            - C: 这几乎可以工作（您需要为 **c_d_x** 使用不同的主键），但不必要地复杂。
            - D: **x** 的值会因不同的 **c** 和 **d** 组合而异。例如，如果我们把列放在 **c** 中，就没有好的方法捕捉 **x** 对 **d** 的依赖关系。

        - 以下哪项陈述是 *错误* 的？

            - A: 复合属性会为每个组件生成列以及复合列。
            - B: 多值属性通常需要在数据库中添加一个额外的表。
            - C: 不会为派生属性创建列。
            - D: 如果实体具有复合键属性，则结果表将具有复合主键。

        .. admonition:: 显示答案
            :class: dropdown

            + A: 我们不为复合属性创建列，仅创建组件。
            - B: 这是真的。在某些情况下，可能可以使用数组值列来处理多值属性，但否则我们需要一个或多个额外的表。
            - C: 这是真的。派生属性不打算存储，因为它们可以从数据库中的其他值计算得出。
            - D: 这是真的。

    .. md-tab-item:: 英文

        This section has some questions you can use to check your understanding of how to convert ERDs to a relational database.

        - Entities in our ERD become tables in our relational database.  What do relationships become?

          - A: Tables
          - B: Foreign keys
          - C: Merging of tables
          - D: All of the above

        .. admonition:: Show answer
            :class: dropdown

            - A: Any relationship can be converted into a cross-reference table.  Is that the only possibility?
            - B: One-to-one and one-to-many relationships can be converted into foreign keys in our database.  Are those the only cardinality ratios?
            - C: One-to-one relationships can result in merging tables, although this is rare.
            + D: Each of the methods above can be applied, depending on the cardinality ratio of the relationship and other factors.

        - Consider the ERD below.  We create tables **a** and **b**, each of which have a primary key column named "id".  (Assume there are additional columns from attributes not shown.)  What is the simplest way to convert the relationship between **A** and **B**?

          .. image:: self_test_many_to_one.svg
              :alt: Entities A and B each with key attribute ID.  The relationship between A and B is many-to-one (many on the A side).


          A:  Create a column named "a_id" in table **b**, and make it a foreign key referencing table **a**.

          B:   Create a column named "b_id" in table **a**, and make it a foreign key referencing table **b**.

          C:   Create a cross-reference table, **a_b**, containing columns **a_id** and **b_id** as foreign keys referencing **a** and **b** respectively.

          D:   Merge tables **a** and **b** into a new table.

        .. admonition:: Show answer
            :class: dropdown

            A: Since a row in **b** could be related to multiple rows in **a**, we would need to store multiple ID values in column **a_id**.
            Some databases would permit this, but it would complicate queries and updates on the database.

            B: This is the simplest solution, assuming we do not expect the relationship to change to many-to-many in the future.

            C: This is an allowable conversion.  Is it the simplest?

            D: This is not a good choice; while such a structure can be made to work, it is not considered good database design and is prone to errors.
            We would say that this table is not properly *normalized*.  We explore normalization in :numref:`Part {number} <relational-theory-part>`.

        - Consider the ERD below.  We create table **r** with primary key column **id**.  What should table **w** look like?

          .. image:: self_test_weak.svg
              :alt: Entity R with key ID, and weak entity W with partial key partial.  The identifying relationship between R and W is one-to-many.

          - A:  The table should have a column **partial** as primary key.  Additionally, create a cross-reference table **r_w**.

          - B:  The table should have columns **partial** and **r_id**.  The primary key is **partial**.
            Add a foreign key constraint on **r_id** referencing **r**.

          - C:  The table should have columns **partial** and **r_id**.  The primary key is a composite of **r_id** and **partial**.
            Add a foreign key constraint on **r_id** referencing **r**.

          - D:  The table should have columns **partial** and **r_id**.  The primary key is **r_id**.  Add a foreign key constraint on **r_id** referencing **r**.

        .. admonition:: Show answer
            :class: dropdown

            - A: Partial keys cannot become primary keys.  They do not represent unique identifiers for the instances of the weak entity.

            - B: Partial keys cannot become primary keys.  They do not represent unique identifiers for the instances of the weak entity.

            + C: Correct.

            - D: The parent key is not a sufficient key for the weak entity; there will be multiple rows in **w** with the same values for **r_id**.
                Therefore it cannot be a primary key.

        - Consider the ERD below.  We create tables **c** and **d**, each of which have a primary key column named "id".  How should we handle the relationship between **C** and **D**?

          .. image:: self_test_relationship_attribute.svg
              :alt: Entities C and D each with key attribute ID.  The relationship between C and D is many-to-many and has an attribute named "x".

          - A:  Borrow the primary key from one table as a foreign key into the other table (either direction is fine).  Add a column named "x" into the table with the foreign key column.

          - B:  Create a cross reference table **c_d** with columns **c_id**, **d_id**, and **x**.  Make a composite primary key using **c_id** and **d_id**. Add foreign key constraints on **c_id** and **d_id** referencing **c** and **d**, respectively.

          - C:  Create a cross reference table **c_d** with columns **c_id** and **d_id**.  Make a composite primary key using **c_id** and **d_id**.
            Add foreign key constraints on **c_id** and **d_id** referencing **c** and **d**, respectively.  Create another table, **c_d_x**, with columns **c_id**, **d_id**, and **x**.  Table **c_d_x** has primary key **x**, and a foreign key constraint on **c_id** and **d_id** referencing table **c_d**.

          - D:  Create a cross reference table **c_d** with columns **c_id** and **d_id**.  Make a composite primary key using **c_id** and **d_id**. Add foreign key constraints on **c_id** and **d_id** referencing **c** and **d**, respectively.  Add column **x** to either **c** or **d**.

        .. admonition:: Show answer
            :class: dropdown

            - A: This is not a good choice; while such a structure can be made to work, it is not considered good database design and is prone to errors.
                We would say that this table is not properly *normalized*.  We explore normalization in :numref:`Part {number} <relational-theory-part>`.

            + B: Correct.

            - C: This could almost work (you would need a different primary key for **c_d_x**), but it is unnecessarily complicated.

            - D: The values for **x** will differ for different combinations of **c** and **d**. There is no good way to capture the dependence of **x** on **d**, for example, if we put the column in **c**.

        - Which of the following statements is *false*?

            -   Composite attributes result in columns for each component as well as the composite.

            -   Multivalued attributes usually require an additional table in the database.

            -   No column is created for derived attributes.

            -   If an entity has a composite key attribute, the resulting table will have a composite primary key.

        .. admonition:: Show answer
            :class: dropdown

            + We do not create a column for the composite, just the components.

            - This is true.  In some cases it may be possible to use array-valued columns to handle a multivalued attribute, but otherwise we need an additional table or tables.

            - This is true.  Derived attributes are not intended to be stored, as they can be computed from other values in the database.

            - This is true.





----

**Notes**

.. [#] 由于 **factory** 在 **manages** 关系中的完全参与，似乎我们应该限制 **manager_id** 列永远不包含 ``NULL``。添加这样的约束时需要谨慎。虽然工厂“必须”有一个经理，但有时工厂可能没有经理，例如，当一名经理离开公司而尚未确定新经理时。如果 **manager_id** 列被限制为永远不包含 ``NULL``，那么在数据库中正确反映真实情况将变得困难。一般来说，在选择约束列之前，请谨慎并检查所有边缘情况。

.. [#] Due to the total participation of **factory** in the **manages** relationship, it might seem we should constrain the **manager_id** column to never contain ``NULL``.  Some care should be taken in adding such constraints.  While a factory "must" have a manager, there may be times when a factory has no manager, e.g., when a manager leaves the company and a new manager has not yet been identified.  If the **manager_id** column is constrained to never hold ``NULL``, it will be difficult to correctly reflect the true situation in the database.  In general, use caution and examine all of your edge cases before choosing to constrain a column.


