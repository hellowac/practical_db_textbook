=======
前言
=======

**Preface**

.. md-tab-set::

   .. md-tab-item:: 中文

            *我们信仰上帝，其他人带数据来。*

            ——据说由W. Edwards Deming提出

        本书《数据库实用入门》旨在满足对于适合数据库入门课程的低成本、最新教材的需求：

        - 本书对学生和教师免费开放（虽然我们鼓励您支持Runestone Academy平台，以帮助确保其未来的可持续性和发展）。
        - 本书是开放的。 [#]_ 其内容受《知识共享署名-相同方式共享4.0国际许可协议》保护，这意味着任何人都可以为任何目的自由共享、修改和重新分发这些内容，只要适当标注并保持许可协议条款。 本书的源代码可在github上获取，您可以分叉、扩展并以任何形式重新发布本书（欢迎提交pull request！）。本书旨在作为一个动态文档，随着技术的变化，由任何感兴趣的作者定期更新和扩展。
        - 本书面向首次接触数据库的学生，重点关注未来软件工程师所需的关键技能。

        .. _`知识共享署名-相同方式共享 4.0 国际许可协议`: https://creativecommons.org/licenses/by-sa/4.0/

        在本书的首次发行中，涵盖了三个核心主题：SQL、数据建模和关系数据库理论。 [#]_ 在确定包含或排除哪些材料时，我们优先选择那些具有高影响力和实际应用价值的内容，而非追求内容的全面覆盖。因此，教师可以将本书作为基础教材，根据课程需要补充额外的材料。数据库高级课程的教师也可能发现本书对首次接触该主题的学生有补充价值。尽可能地，本书的内容是以允许不同的主题顺序呈现的方式编写的，尽管某些依赖关系是不可避免的。

        为了保持本书的应用导向，SQL在本书的 :numref:`第 {number} 部分 <sql-part>` 中作为起点提供。在学术界和工业界几乎每天都在数据库技术上取得新进展的时代，SQL所介导的关系数据库模型仍然是从业者的核心。SQL是评估求职者数据库技能的常见参考点。本在线书籍使用嵌入的SQLite数据库引擎提供交互示例并促进探索（如果需要， :ref:`附录A <appendix-a>` 中提供的脚本可用于在其他几个主要数据库系统上创建教科书中的数据库）。

        :numref:`第 {number} 部分 <data-modeling-part>` 讨论了数据建模。这里的重点是使用实体关系图（ERD）和相关工具进行数据库设计。内容包括一个详细的示例，演示了ERD构建以及将ERD转换为关系数据库架构的逐步说明。

        最后，文本的 :numref:`第 {number} 部分 <relational-theory-part>` 涵盖了关系数据库理论，包括关系代数和范式化（到第四范式）。

   .. md-tab-item:: 英文

            In God we trust, all others bring data.

            —attributed to W. Edwards Deming

        This book, *A Practical Introduction to Databases*, was created to fill the need for a low-cost, up-to-date textbook suitable for an introductory course on databases:

        - The book is free to students and instructors (although we encourage you to support the Runestone Academy platform to help ensure its future sustainability and growth).
        - The book is open. [#]_  Its contents are licensed under the `Creative Commons Attribution-ShareAlike 4.0 International License`_, meaning that anyone is free to share, adapt, and redistribute them for any purpose whatsoever, as long as appropriate credit is given and the license terms persist.  The  source for this book is available on github; you may fork, extend, and re-release this book in any form you wish (pull requests welcome!).  This book is intended as a living document, to be updated and expanded regularly as technology changes, by any interested author.
        - The book is oriented to students encountering databases for the first time, with a focus on key skills needed by future software engineers.

        .. _`Creative Commons Attribution-ShareAlike 4.0 International License`: https://creativecommons.org/licenses/by-sa/4.0/

        In this first release, the book covers three core topics: SQL, data modeling, and relational database theory. [#]_  In determining which material to include or exclude, choices were made to prefer material with high impact and practical application over exhaustive coverage.  Instructors may therefore wish to use this book as a foundation, supplemented with additional material as required for their course.  Instructors of more advanced courses in databases may also find value in providing this book as a supplement for students encountering the subject for the first time.  To the extent possible, the content is presented in a way that allows different orderings of topics, although some dependencies are unavoidable.

        In keeping with the applied focus of the book, SQL is offered as the starting point in :numref:`Part {number} <sql-part>` of the text.  At a time when academia and industry alike are developing new advances in database technology seemingly on a daily basis, the relational database model as mediated by SQL remains the gravitational center for practitioners.  SQL is the common point of reference used to evaluate job applicants on their database skills.  The online book uses an embedded SQLite database engine to provide interactive examples and facilitate exploration (scripts are provided in :ref:`Appendix A <appendix-a>` to create the textbook's database on several other major database systems, if preferred).

        :numref:`Part {number} <data-modeling-part>` discusses data modeling.  Here, the emphasis is on database design using entity-relationship diagrams (ERDs) and related tools.  The coverage includes a detailed example demonstrating ERD construction along with step-by-step instructions for converting ERDs to a relational database schema.

        Finally, :numref:`Part {number} <relational-theory-part>` of the text provides coverage of relational database theory, including relational algebra and normalization (through fourth normal form).



----

**注释**

**Notes**

.. md-tab-set::

   .. md-tab-item:: 中文

        .. [#] 本书是开放教育资源（OER），与 `《联合国教科文组织开放教育资源建议》`_ 等目标一致。

        .. [#] 计划未来发布版本，涵盖与数据库相关的软件编程、NoSQL和其他实用主题。

        .. _`《联合国教科文组织开放教育资源建议》`: https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer

   .. md-tab-item:: 英文


        .. [#] This book is an Open Education Resource (OER), and is aligned with the goals laid out in the `UNESCO Recommendation on Open Educational Resources`_, among others.

        .. [#] Future releases are planned, covering software programming with databases, NoSQL, and other topics of practical interest.

        .. _`UNESCO Recommendation on Open Educational Resources`: https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer