.. _data-modeling-intro-chapter:

=============================
数据建模简介
=============================

**Introduction to data modeling**

.. index:: data; modeling, data model, analysis, database; design

.. md-tab-set::

    .. md-tab-item:: 中文
        
        当开始一个需要数据库的项目时，花一些时间考虑适当的数据库结构是非常有用的。除非你的数据库非常小（只涉及一两个表），否则如果你只是坐下来开始创建表，可能会很快遇到麻烦。创建一个尽管存储了必要数据但难以理解、更新和查询的数据库是非常容易的。

        就像软件创建一样，数据库创建也受益于*分析*和*设计*的活动。分析可以包括与对要存储的数据有透彻理解的人进行讨论，与数据库的预期用户进行讨论，以及对代表性数据的检查。设计则利用从分析中获得的洞察来生成一个能够正确存储必要数据并满足用户需求的数据库结构。分析和设计是互补的活动；分析为设计提供信息，而设计又揭示出进一步分析的新问题。分析与设计之间的反复互动有助于消除由于部分理解和错误假设而导致的问题。

        分析和设计可以通过多种图形和非图形文档来促进。*数据模型*是创建数据库时最有用的一种文档。至少，数据模型必须捕捉各种数据类型及其相互关系。有些数据模型更为详细，捕捉特定的编程元素，甚至数据库将部署的物理计算机系统或网络的某些方面。

        我们可以使用数据模型对数据进行推理，而不考虑SQL或编程语言的细节。虽然数据模型的类型和符号似乎很多，但实际上只有少数几个重要的基本概念需要学习。使用数据模型有许多好处: 更好地实现用户需求、易于查询和一致更新的数据库结构、以及为新用户记录系统信息等。如果现有的数据库缺乏数据模型形式的文档，你可能会发现创建一个数据模型对更好地理解系统有价值。

        本部分书籍考察不同抽象层次的图形数据模型。在 :numref:`第 {number} 章 <erd-chapter>` 中，我们讨论*实体-关系图*（ERD），这是一种高级数据模型。ERD在分析与设计的交集中特别有用，促进了与用户和领域专家的讨论。:numref:`第 {number} 章 <erd-to-relational-chapter>` 解释了如何从ERD过渡到关系数据库。此过渡可能通过与关系数据库更密切对应的较少抽象模型进行调解，这些模型在 :numref:`第 {number} 章 <other-notations-chapter>` 中进行了讨论。:numref:`第 {number} 章 <other-notations-chapter>` 还讨论了一些常用符号的多种变体。

    .. md-tab-item:: 英文

        When beginning a project that requires a database, it is useful to expend some effort thinking about an appropriate database structure.  Unless your database will be very small (involving only one or two tables), if you simply sit down and start creating tables, you will likely run into trouble fairly quickly.  It is quite easy to create a database that - even though it stores the necessary data - is difficult to understand, update, and query.

        Much like software creation, database creation benefits from the activities of *analysis* and *design*.  Analysis can include discussions with people who have a thorough understanding of the data to be stored, discussions with the intended users of the database, and an examination of representative data.  Design uses the insights gained from analysis to produce a database structure that can correctly store the necessary data and meet user requirements.  Analysis and design are complementary activities; analysis informs design, which in turn uncovers new questions for further analysis.  The back-and-forth interaction between analysis and design works to eliminate the kinds of problems that otherwise result from partial understanding and incorrect assumptions.

        Analysis and design may be facilitated using a variety of graphical and non-graphical documents.  *Data models* are one type of document that are most useful when creating a database.  At minimum, a data model must capture the various types of data and how these types relate to each other.  Some data models go further in detail, capturing specific programming elements or even aspects of the physical computer systems or networks on which the database will be deployed.

        We can use data models to reason about data, abstracted from the details of SQL or a programming language.  While it may seem that there are very many types and notations for data models, in practice there are only a few important underlying concepts to learn.  There are many benefits to working with a data model: better realization of users' needs, a database structure that allows easy querying and consistent updates, and documentation of the system for new users, to list a few.  If an existing database lacks documentation in the form of a data model, you may find value in creating one to better understand the system.

        This part of the book examines graphical data models at varying levels of abstraction.  In :numref:`Chapter {number} <erd-chapter>`, we discuss the *entity-relationship diagram* (ERD), a high-level model of data.  ERDs are particularly useful at the intersection of analysis and design, facilitating discussion with users and domain experts.  :numref:`Chapter {number} <erd-to-relational-chapter>` explains how to transition from an ERD into a relational database.  This transition may be mediated by less abstract models which have closer correspondence with the relational database, discussed in :numref:`Chapter {number} <other-notations-chapter>`.  :numref:`Chapter {number} <other-notations-chapter>` also discusses some of the many variations in notation in common usage.







