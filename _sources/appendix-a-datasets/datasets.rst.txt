.. _appendix-a:

==============================================
附录 A: 本书中使用的示例数据集
==============================================

**Appendix A: Example datasets used in this book**

.. md-tab-set::

    .. md-tab-item:: 中文

        本附录包含教科书数据库中表的描述，以及可以用于在其他数据库系统中重建该书数据库的 SQL 脚本和数据文件。

    .. md-tab-item:: 英文

        This appendix contains descriptions of the tables in the textbook database as well as SQL scripts and data files that can be used to recreate the book's database in other database systems.

.. contents:: Quick links
   :local:
   :depth: 2
   :backlinks: none

数据集说明
::::::::::::::::::::

**Dataset descriptions**

.. md-tab-set::

    .. md-tab-item:: 中文

        在本节中，我们提供每个数据集或相关表组的描述。这些表以表格格式详细描述。对于某些数据集，还提供了使用乌鸦脚标记法的实体关系图（ERD）和逻辑模型（如 :numref:`Part {number} <data-modeling-part>` 中所述）。最后，每个数据集部分都包含一个交互式查询工具，旨在从数据集中所有表中检索数据（请注意，交互式查询工具将结果限制为 100 行，并且某些表的行数超过该数量）。

    .. md-tab-item:: 英文

        In this section we provide descriptions of each dataset or group of related tables.  The tables are described in detail in tabular format. Entity-relationship diagrams (ERDs) and logical models using crow's foot notation (as described in :numref:`Part {number} <data-modeling-part>`) are also provided for some datasets.  Finally, each dataset section contains an interactive query tool set up to retrieve the data from all of the tables in the dataset (note that the interactive query tool limits results to 100 rows, and some tables have more than that number of rows).

简单图书数据集
------------------------

**The simple books dataset**

.. md-tab-set::

    .. md-tab-item:: 中文

        简单书籍数据集由 **simple_books** 和 **simple_authors** 表组成。**simple_books** 表包含 12 本书的数据，每本书由不同的作者创作，而 **simple_authors** 表包含出现在 **simple_books** 中的 12 位作者的数据。

        该数据集用于文本 :numref:`Part {number} <sql-part>` 的早期章节中引入 SQL，并不作为良好数据库设计的示例。**simple_books** 中的行隐式通过唯一书名进行识别，而 **simple_authors** 中的行则隐式通过作者姓名进行识别，但这两个表都没有主键。同样，**simple_books** 中的行与 **simple_authors** 中的行是一对一对应的，但表之间没有通过外键约束建立显式关系。

        .. container:: data-dictionary

            **simple_books** 表记录由单一作者创作的虚构、非虚构、诗歌等作品。

            ================ ================= ===================================
            column           type              description
            ================ ================= ===================================
            author           character string  书的作者
            title            character string  书的标题
            publication_year integer           书首次出版的年份
            genre            character string  描述书籍的类型
            ================ ================= ===================================

        .. container:: data-dictionary

            **simple_authors** 表记录了曾撰写书籍的人。

            ========== ================= ===================================
            column     type              description
            ========== ================= ===================================
            name       character string  作者的全名
            birth      date              作者的出生日期（如果已知）
            death      date              作者的死亡日期（如果已知）
            ========== ================= ===================================

        使用下面的查询工具查看数据。

        .. activecode:: appendix_a_simple_books_dataset
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books;
            SELECT * FROM simple_authors;

        要查看某个表的 **CREATE TABLE** 代码，可以使用上面的查询工具查询 **sqlite_master** 表，例如：

        .. code:: sql

                SELECT sql FROM sqlite_master WHERE name = 'simple_books';

    .. md-tab-item:: 英文

        The simple books dataset consists of the tables **simple_books** and **simple_authors**.  The **simple_books** table contains data about 12 books, each by a different author, while the **simple_authors** table contains data on each of the 12 authors appearing in **simple_books**.

        This dataset is used in the early chapters of :numref:`Part {number} <sql-part>` of the text to introduce SQL, and is not intended as an example of good database design.  The rows in **simple_books** are implicitly identified by unique book titles, and the rows in **simple_authors** are implicitly identified by author names, but neither table has a primary key.  Similarly, the rows in **simple_books** are in one-to-one correspondence with the rows in **simple_authors**, however, there is no explicit relationship between the tables via a foreign key constraint.

        .. container:: data-dictionary

            The **simple_books** table records works of fiction, non-fiction, poetry, etc. by a single author.

            ================ ================= ===================================
            column           type              description
            ================ ================= ===================================
            author           character string  the book's author
            title            character string  the book's title
            publication_year integer           year the book was first published
            genre            character string  a genre describing the book
            ================ ================= ===================================

        .. container:: data-dictionary

            The **simple_authors** table records persons who have authored books.

            ========== ================= ===================================
            column     type              description
            ========== ================= ===================================
            name       character string  full name of the author
            birth      date              birth date of the author, if known
            death      date              death date of the author, if known
            ========== ================= ===================================

        Use the query tool below to view the data.

        .. activecode:: appendix_a_simple_books_dataset
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM simple_books;
            SELECT * FROM simple_authors;

        To see the **CREATE TABLE** code for a table, you can use the query tool above to query the **sqlite_master** table, e.g.:

        .. code:: sql

                SELECT sql FROM sqlite_master WHERE name = 'simple_books';


扩展图书数据集
--------------------------

**The expanded books dataset**

.. md-tab-set::

    .. md-tab-item:: 中文

        扩展书籍数据集包括 200 本书（在 **books** 表中）及其作者（总共 76 位作者在 **authors** 表中）。**awards** 表列出了一些授予作者的主要奖项，既包括他们的整体作品，也包括特定书籍的奖项。两个交叉引用表将作者与他们的奖项关联起来 (**authors_awards**) 和将特定书籍与它们的奖项关联起来 (**books_awards**)。最后，**editions** 表包含与 J.R.R. 托尔金的四本书相关的出版数据。（仅包含四本书是为了减小数据库文件的大小，文件必须下载并保存在网页浏览器的内存中。）出版数据特别“脏”，因为它包含许多不准确、遗漏和冗余的信息；请参见下面的标题为 `Data collection notes`_ 的部分。

        该数据集在 :numref:`Chapter {number} <joins-chapter>` 中介绍，并在 :numref:`Part {number} <sql-part>` 的其余部分中使用。虽然该数据集代表了书籍的高度简化模型（例如，假设书籍始终只有一个作者），但其模式尝试在展示基本 SQL 数据库概念的同时模拟数据库设计的最佳实践。设计中使用了主键约束（使用合成唯一标识符）、外键约束和实现多对多关系的交叉引用表。

        以下是数据集中每个表的详细描述，包含数据模型的实体关系图（ERD），以及使用乌鸦脚标记法表示表及其关系的逻辑模型。

        .. container:: data-dictionary

            **authors** 表记录了曾撰写书籍的人。每位作者对应数据库中的至少一本书。

            ========== ================= ===================================
            column     type              description
            ========== ================= ===================================
            author_id  integer           作者的唯一标识符
            name       character string  作者的全名
            birth      date              作者的出生日期（如果已知）
            death      date              作者的死亡日期（如果已知）
            ========== ================= ===================================

        .. container:: data-dictionary

            **books** 表记录由单一作者创作的虚构、非虚构、诗歌等作品。每本书对应 **authors** 表中的一位作者，并可能对应 **editions** 表中列出的多本书的版本。

            ================ ================= =================================================
            column           type              description
            ================ ================= =================================================
            book_id          integer           书的唯一标识符
            author_id        integer           书的作者在 **authors** 表中的 author_id
            title            character string  书的标题
            publication_year integer           书首次出版的年份
            ================ ================= =================================================

        .. container:: data-dictionary

            **editions** 表记录一本书的特定出版版本。每个版本对应 **books** 表中的一本书。出于空间原因，**editions** 表仅包含 J.R.R. 托尔金的四本书的数据。

            ================== ================= ====================================================================
            column             type              description
            ================== ================= ====================================================================
            edition_id         integer           版本的唯一标识符
            book_id            integer           作为此版本出版的书（来自 **books** 表）的 book_id
            publication_year   integer           此版本出版的年份
            publisher          character string  出版社的名称
            publisher_location character string  出版社所在地的城市或其他位置
            title              character string  此版本出版时的标题
            pages              integer           此版本的页数
            isbn10             character string  10 位国际标准书号
            isbn13             character string  13 位国际标准书号
            ================== ================= ====================================================================

        .. container:: data-dictionary

            **awards** 表记录各种作者和/或书籍奖项。

            ========= ================= =========================================
            column    type              description
            ========= ================= =========================================
            award_id  integer           奖项的唯一标识符
            name      character string  奖项的名称
            sponsor   character string  授予奖项的组织名称
            criteria  character string  奖项颁发的标准
            ========= ================= =========================================

        .. container:: data-dictionary

            **authors_awards** 表是一个 *交叉引用* 表（在 :numref:`Chapter {number} <joins-chapter>` 中解释），用于关联 **authors** 和 **awards**；表中的每个条目记录某位作者在特定年份获得奖项（而不是针对任何特定书籍）。

            =========== =========== ===========================================
            column      type        description
            =========== =========== ===========================================
            author_id   integer     获奖作者的 author_id
            award_id    integer     获得的奖项的 award_id
            year        integer     奖项颁发的年份
            =========== =========== ===========================================

        .. container:: data-dictionary

            **books_awards** 表是一个交叉引用表，用于关联 **books** 和 **awards**；表中的每个条目记录某位作者因特定书籍在特定年份获得奖项。

            =========== =========== =================================================
            column      type        description
            =========== =========== =================================================
            book_id     integer     该书获得奖项的 book_id
            award_id    integer     获得的奖项的 award_id
            year        integer     奖项颁发的年份
            =========== =========== =================================================

        这是扩展书籍数据集的数据模型，作为 ERD：

        .. image:: books_ERD.svg
            :alt: 书籍数据集的数据模型，给出实体关系图。

        扩展书籍数据集的逻辑模型如下所示。在这个乌鸦脚图中，主键用下划线和粗体显示，而外键用斜体显示。

        .. image:: books_logical.svg
            :alt: 显示书籍数据集逻辑模型的乌鸦脚图。

        使用下面的查询工具查看扩展书籍数据。请注意，查询工具将结果限制为 100 行，但 **books** 和 **editions** 表各自的行数都超过 100 行。

        .. activecode:: appendix_a_expanded_books_dataset
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM authors;
            SELECT * FROM books;
            SELECT * FROM editions;
            SELECT * FROM awards;
            SELECT * FROM authors_awards;
            SELECT * FROM books_awards;

    .. md-tab-item:: 英文

        The expanded books dataset includes information on 200 books (in the **books** table) and their authors (76 authors in total in the **authors** table).  An **awards** table lists some major awards given to authors for their body of work or for specific books.  Two cross-reference tables associate authors with their awards (**authors_awards**) and specific books with their awards (**books_awards**).  Finally, the **editions** table contains publication data related to just four books by author J.R.R. Tolkien.  (Only four books were included to reduce the size of the database file, which must be downloaded and held in the web browser's memory.)  The publication data is particularly "dirty" in the sense that it contains numerous inaccuracies, omissions, and redundancies; see the section title `Data collection notes`_, below.

        This dataset is introduced in :numref:`Chapter {number} <joins-chapter>` and is used throughout much of the rest of :numref:`Part {number} <sql-part>` of the text.  While the dataset represents a highly simplified model of books (e.g., books are assumed to always have a single author), the schema attempts to emulate best practices in database design while illustrating fundamental SQL database concepts.  The design makes use of primary key constraints (using synthetic unique identifiers), foreign key constraints, and cross-reference tables implementing many-to-many relationships.

        We provide below detailed descriptions of each table in the dataset, an entity-relationship diagram (ERD) modeling the data, and a logical model in crow's foot notation showing the tables and their relationships.

        .. container:: data-dictionary

            The **authors** table records persons who have authored books.  Every author corresponds to at least one book in the database.

            ========== ================= ===================================
            column     type              description
            ========== ================= ===================================
            author_id  integer           unique identifier for the author
            name       character string  full name of the author
            birth      date              birth date of the author, if known
            death      date              death date of the author, if known
            ========== ================= ===================================

        .. container:: data-dictionary

            The **books** table records works of fiction, non-fiction, poetry, etc. by a single author.  Each book corresponds to a single author from the **authors** table, and may correspond to many editions of the book listed in the **editions** table.

            ================ ================= =================================================
            column           type              description
            ================ ================= =================================================
            book_id          integer           unique identifier for the book
            author_id        integer           author_id of book's author from **authors** table
            title            character string  the book's title
            publication_year integer           year the book was first published
            ================ ================= =================================================

        .. container:: data-dictionary

            The **editions** table records specific publications of a book.  Each edition corresponds to a single book from the **books** table.  For space reasons, the **editions** table only includes data on four books by J.R.R. Tolkien.

            ================== ================= ====================================================================
            column             type              description
            ================== ================= ====================================================================
            edition_id         integer           unique identifier for the edition
            book_id            integer           book_id of the book (from **books** table) published as this edition
            publication_year   integer           year this edition was published
            publisher          character string  name of the publisher
            publisher_location character string  city or other location(s) where the publisher is located
            title              character string  title this edition was published under
            pages              integer           number of pages in this edition
            isbn10             character string  10-digit international standard book number
            isbn13             character string  13-digit international standard book number
            ================== ================= ====================================================================

        .. container:: data-dictionary

            The **awards** table records various author and/or book awards.

            ========= ================= =========================================
            column    type              description
            ========= ================= =========================================
            award_id  integer           unique identifier for the award
            name      character string  name of the award
            sponsor   character string  name of the organization giving the award
            criteria  character string  what the award is given for
            ========= ================= =========================================

        .. container:: data-dictionary

            The **authors_awards** table is a *cross-reference* table (explained in :numref:`Chapter {number} <joins-chapter>`) relating **authors** and **awards**; each entry in the table records the giving of an award to an author (not for any particular book) in a particular year.

            =========== =========== ===========================================
            column      type        description
            =========== =========== ===========================================
            author_id   integer     author_id of the author receiving the award
            award_id    integer     award_id of the award received
            year        integer     year the award was given
            =========== =========== ===========================================

        .. container:: data-dictionary

            The **books_awards** table is a cross-reference table relating **books** and **awards**; each entry in the table records the giving of an award to an author for a specific book in a particular year.

            =========== =========== =================================================
            column      type        description
            =========== =========== =================================================
            book_id     integer     book_id of the book for which the award was given
            award_id    integer     award_id of the award given
            year        integer     year the award was given
            =========== =========== =================================================

        Here is the data model for the expanded books dataset, as an ERD:

        .. image:: books_ERD.svg
            :alt: A data model of the books dataset given as an entity-relationship diagram.

        A logical model of the expanded books dataset is shown below.  In this crow's foot diagram, primary keys are shown underlined and in boldface, while foreign keys are italicized.

        .. image:: books_logical.svg
            :alt: A crow's foot diagram showing the logical model of the books dataset.

        Use the query tool below to view the expanded books data.  Note that the query tool limits results to 100 rows, but the **books** and **editions** tables have more than 100 rows each.

        .. activecode:: appendix_a_expanded_books_dataset
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM authors;
            SELECT * FROM books;
            SELECT * FROM editions;
            SELECT * FROM awards;
            SELECT * FROM authors_awards;
            SELECT * FROM books_awards;

书店数据集
---------------------

**The bookstore dataset**

.. md-tab-set::

    .. md-tab-item:: 中文

        书店数据集由 **bookstore_inventory** 和 **bookstore_sales** 表组成。这些表模拟了二手书商可能使用的非常简单的数据库。 **bookstore_inventory** 表代表书商正在出售的书籍。该表实际上包括一些已经售出的书籍——当一本书被出售时，会在伴随的 **bookstore_sales** 表中添加一条记录。因此，书商必须查看这两个表，以确定哪些书籍实际上可供出售。书商可以选择定期从表中删除旧记录。

        虽然学生可以随意修改教科书数据库中的任何数据（放心，因为任何更改在他们重新加载浏览器页面时都会被还原），但书店数据集特别设计时考虑到了数据修改。为了避免在引入数据修改查询时出现复杂情况，这些表没有外键约束。然而，所提供的表具有一对一关系： **bookstore_sales** 中的每条记录正好与 **bookstore_inventory** 中的一条记录匹配，而 **bookstore_inventory** 中的每条记录最多与 **bookstore_sales** 中的一条记录匹配。

        该数据集在 :numref:`Chapter {number} <joins-chapter>` 中简要用于说明一对一关系。在 :numref:`Chapter {number} <data-modification-chapter>` 中，表用于演示数据修改查询。在 :numref:`Chapter {number} <grouping-chapter>` 中，表用于分组和聚合的示例。

        .. container:: data-dictionary

            **bookstore_inventory** 表包含有关新书和二手书的信息。

            ============= ================= ==================================================
            column        type              description
            ============= ================= ==================================================
            stock_number  integer           唯一键，用于标识某本书的特定副本
            author        character string  书的作者
            title         character string  书的标题
            condition     character string  书的状态（新书、良好、一般等）
            price         fixed-point       书的价格，以某种货币单位表示
            ============= ================= ==================================================

        .. container:: data-dictionary

            **bookstore_sales** 表提供有关 **bookstore_inventory** 中书籍销售的信息。

            =============== ================= =================================================================
            column          type              description
            =============== ================= =================================================================
            receipt_number  integer           唯一键，用于标识这笔销售
            stock_number    integer           售出的书副本的键（来自 **bookstore_inventory**）
            date_sold       date              书籍售出的日期
            payment         character string  销售中使用的支付方式（现金、信用卡等）
            =============== ================= =================================================================

        使用下面的查询工具查看数据。

        .. activecode:: appendix_a_bookstore_dataset
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM bookstore_inventory;
            SELECT * FROM bookstore_sales;

    .. md-tab-item:: 英文

        The bookstore dataset consists of the tables **bookstore_inventory** and **bookstore_sales**.  These tables simulate a very simple database that a seller of used books might use.  The **bookstore_inventory** table represents books that the bookseller is selling.  The table actually includes some books that have already been sold - when a book is sold, an entry is added to the companion table, **bookstore_sales**.  The bookseller thus has to look at both tables to determine which books are actually available to be sold.  The bookseller may choose to periodically remove old records from the tables.

        While students should feel free to modify any data within the textbook database (secure in the knowledge that any changes will be reverted when they reload the page in their browser), the bookstore dataset was specifically designed with data modification in mind.  To avoid complications in introducing data modification queries, there are no foreign key constraints on the tables.  However, the tables as provided have a one-to-one relationship: each record in **bookstore_sales** matches exactly record in **bookstore_inventory**, while each record in **bookstore_inventory** matches at most one record in **bookstore_sales**.

        This dataset is used briefly to illustrate one-to-one relationships in :numref:`Chapter {number} <joins-chapter>`.  In :numref:`Chapter {number} <data-modification-chapter>`, the tables are used to demonstrate data modification queries.  The tables are used in examples of grouping and aggregation in :numref:`Chapter {number} <grouping-chapter>`.

        .. container:: data-dictionary

            The **bookstore_inventory** table contains information on new and used books for sale.

            ============= ================= ==================================================
            column        type              description
            ============= ================= ==================================================
            stock_number  integer           unique key identifying a particular copy of a book
            author        character string  the author of the book
            title         character string  the title of the book
            condition     character string  the condition of the book (new, good, fair, etc.)
            price         fixed-point       the price of the book, in some unit of currency
            ============= ================= ==================================================

        .. container:: data-dictionary

            The **bookstore_sales** table gives information about the sales of books from **bookstore_inventory**.

            =============== ================= =================================================================
            column          type              description
            =============== ================= =================================================================
            receipt_number  integer           unique key identifying this sale
            stock_number    integer           key of the book copy (from **bookstore_inventory**) that was sold
            date_sold       date              the date on which the books was sold
            payment         character string  the method of payment used in the sale (case, credit card, etc.)
            =============== ================= =================================================================

        Use the query tool below to view the data.

        .. activecode:: appendix_a_bookstore_dataset
            :language: sql
            :dburl: /_static/textbook.sqlite3

            SELECT * FROM bookstore_inventory;
            SELECT * FROM bookstore_sales;

数据库中的其他表
----------------------------

**Other tables in the database**

.. md-tab-set::

    .. md-tab-item:: 中文

        除了上述内容，数据库还包含一些非常小的表，用于在文本中说明各种要点：**fruit_stand**、**s**、**s2**、**s3**、**t**、**t2** 和 **t3**。由于这些表在文本中已有完整给出，因此我们在此不再详细解释。不过，您可以使用下面的交互式查询工具查看数据。

        下载 :download:`数据库文件 <../_static/textbook.sqlite3>`

        .. code-block:: sql

            SELECT * FROM fruit_stand;
            SELECT * FROM s;
            SELECT * FROM s2;
            SELECT * FROM s3;
            SELECT * FROM t;
            SELECT * FROM t2;
            SELECT * FROM t3;

    .. md-tab-item:: 英文

        In addition to the above, the database contains some very small tables which are used to illustrate various points in the text: **fruit_stand**, **s**, **s2**, **s3**, **t**, **t2**, and **t3**.  As these tables are give in full in the text, we do not further explain them here.  However, you can use the interactive query tool below to view the data.

        下载 :download:`数据库文件 <../_static/textbook.sqlite3>`

        .. code-block:: sql
            
            SELECT * FROM fruit_stand;
            SELECT * FROM s;
            SELECT * FROM s2;
            SELECT * FROM s3;
            SELECT * FROM t;
            SELECT * FROM t2;
            SELECT * FROM t3;

数据收集说明
:::::::::::::::::::::

**Data collection notes**

.. md-tab-set::

    .. md-tab-item:: 中文

        简单和扩展书籍数据集中的书籍选择受到几个因素的驱动。首先，教科书的作者是科幻和奇幻的爱好者——因此，这些类型在数据集中可能过于突出。其次，试图包含多样化的作者，以期为全球学生提供一些共同的参考点。（然而，数据集确实存在对英语文学的强烈偏向，反映了教科书作者的背景。）最后，选择偏向于那些获得文学奖项的作者的书籍。为了保持管理的可行性，书籍数量限制在200本。

        作者是根据教科书作者的知识和对主要文学奖项的互联网搜索进行精心挑选的。 `Wikipedia`_ 在收集作者的出生和死亡日期等数据时极为有用。（请注意，数据集于2022年定稿；自数据录入以来，某些作者可能已去世。这种不准确性令人遗憾，但在这种情况下是不可避免的。）

        一些作者仅以一部作品（通常是获奖或至少广受好评的书籍）为代表，而在其他情况下则包括了该作者的多部书籍。对于每位作者包括多少书籍并没有使用一致的决策过程。许多选择是为了支持文本中的特定示例。关于个别书籍的大部分数据是从维基百科和其他免费来源手动收集的。一些出版年份的值则是从免费提供的 `Open Library`_ 数据集中提取的。

        关于作者和书籍奖项的数据是从维基百科和奖项代表网站手动收集的。关于作品的众多版本的数据完全来自 Open Library。

        据作者所知，简单和扩展书籍数据集中的所有数据均属于公共领域。

        书店数据集使用了扩展书籍数据集中的书籍，但其他方面完全是虚构的，水果摊和其他抽象示例表也是如此。

    .. md-tab-item:: 英文

        The selection of books in the simple and expanded books datasets was driven by several interests.  First, the textbook's author is a fan of science fiction and fantasy - these genres are thus perhaps overrepresented in the dataset.  Second, an attempt was made to include a diverse set of authors, in hopes of providing some common points of reference for students everywhere.  (There is nevertheless a strong bias towards English-language literature, reflecting the context of the textbook's author.) Lastly, the selection favored books by authors who have received literary awards.  To keep things manageable, the number of books was capped at 200.

        Authors were handpicked, based on the textbook author's knowledge and on internet searches of major literary awards. `Wikipedia`_ was extremely helpful in collecting data such as authors' birth and death dates.  (Note that the dataset was finalized in 2022; it is very possible that some authors in the dataset have died since the data was entered.  This inaccuracy is regrettable but unavoidable under the circumstances.)

        Some authors are represented by a single work (typically an award winning or at least widely acclaimed book), while in other cases many books by the author were included.  There was no consistent decision process used to decide how many books to include by each author.  Many choices were made in support of specific examples in the text.  Most of the data regarding individual books was hand collected from Wikipedia and other freely available sources on the internet.  Some publication year values were extracted from the freely available `Open Library`_ dataset.

        Data on author and book awards was hand collected from Wikipedia and the websites representing the awards.  Data on the many editions of works comes entirely from the Open Library.

        To the best of the author's knowledge, all of the data in the simple and expanded books datasets is in the public domain.

        The bookstore dataset uses books from the expanded books dataset, but is otherwise entirely fabricated, as are the fruit stand and other abstract example tables.


.. _`Wikipedia`: https://www.wikipedia.org/
.. _`Open Library`: https://openlibrary.org/

获取数据
::::::::::::::::

**Getting the data**

.. md-tab-set::

    .. md-tab-item:: 中文

        本书的 :numref:`Part {number} <sql-part>` 包含交互式元素，允许读者直接与关系数据库进行操作。此功能使学生能够立即在真实数据库系统上尝试示例代码。由于每个页面上可用的数据库实际上是一个固定数据库的副本（在内存中），因此对数据库的更改不会持久保存——刷新浏览器窗口将每次返回数据库到相同的初始状态。这一特性使学生可以安全地尝试破坏性 SQL 命令，因为他们知道没有任何更改是永久的。另一方面，这意味着学生无法将系统用于长期项目。

        本教科书使用的数据库系统是 `SQLite`_ 。虽然 SQLite 是一个功能强大且流行的关系数据库系统，但它缺乏一些行业中常用的客户端-服务器数据库系统的特性。它在许多方面也与 SQL 标准存在显著差异（特别是在动态类型的使用上）。

        基于这些原因，本教科书的用户可能希望自行设置数据库系统。市面上有许多不同的数据库系统，每个系统都有自己的系统要求和安装程序。访问和查询各个数据库系统的方法也有很多。因此，设置和访问不同系统的说明超出了本教科书的范围。不过，为了提供从教科书数据库到用户选择的系统的过渡，我们在下面提供脚本和数据文件，这些文件可以用来在您选择的数据库系统上重建本书的数据库。

    .. md-tab-item:: 英文

        :numref:`Part {number} <sql-part>` of this book includes interactive elements allowing the reader to work directly with a relational database.  This functionality lets students immediately try example code on a real database system.  As the database available on each page is actually a copy (in memory) of a fixed database, changes to the database do not persist over time - refreshing the browser window will return the database to the same initial state each time.  This is useful in that students can safely experiment with destructive SQL commands, knowing that no changes are permanent.  On the other hand, it means that students cannot use the system for longer term projects.

        The database system used in this textbook is `SQLite`_ .  While SQLite is a powerful and popular relational database system, it lacks some features of the client-server database systems commonly used in industry.  It also differs in significant ways from the SQL standard (notably with its use of dynamic typing).

        For these reasons, users of this textbook may wish to set up their own database system.  Many different database systems are available, each with their own system requirements and installation procedures.  There are likewise many ways to access and query each database system.  Instructions for setting up and accessing different systems are therefore out of the scope of this textbook.  However, in the interest of providing a transition from the textbook's database to the users' systems of choice, we provide scripts and data files below, which can be used to recreate the book's database on the database system of your choice.

.. _`SQLite`: https://www.sqlite.org/

SQLite
------

**SQLite**

.. md-tab-set::

    .. md-tab-item:: 中文

        SQLite_ 数据库引擎在本教科书支持的系统中是独特的，因为它的数据库完全存储在单个文件中。SQLite 数据库可以通过简单地复制包含它们的文件来共享。我们在下面提供了本教科书使用的数据库文件。此外，我们还提供了一个 SQL 脚本（以 UTF-8 Unicode 格式的文本文件），其中包含重新从头创建数据库所需的 SQL 命令。如果您只想要一本教科书数据库的副本供自己使用，请使用前者；如果您想在现有的 SQLite 数据库中创建教科书的数据库表，请使用后者。该 SQL 脚本仅包含 **CREATE TABLE** 和 **INSERT** 语句，因此不应替换数据库中现有的表。

        - :download:`textbook.sqlite3` , 教科书的 SQLite 数据库文件
        - :download:`sqlite.sql` , SQL 脚本

        此 SQL 脚本在 Windows 10 上使用版本 3.39.2 的 ``sqlite3.exe`` 程序以及在 Linux 上运行的版本 3.31.1 的 ``sqlite3`` 程序（Linux Mint 20.3，内核版本 5.15.0-41）验证为正确工作。

    .. md-tab-item:: 英文

        The `SQLite`_ database engine is unique (in the set of systems supported by this textbook) in that it works with databases stored entirely in a single file.  SQLite databases can be shared by simply copying the files containing them.  We provide below the database file used by this textbook.  Additionally, we provide a SQL script (a text file in UTF-8 Unicode format) with the SQL commands necessary to re-create the database from scratch.  Use the former if you simply want a copy of the textbook's database for your own use; use the latter if you want to create the textbook's database tables within an existing SQLite database.  The SQL script contains only **CREATE TABLE** and **INSERT** statements, and therefore should not replace existing tables within the database.

        - :download:`textbook.sqlite3`, the textbook's SQLite database file
        - :download:`sqlite.sql`, the SQL script

        This SQL script was verified to work correctly using version 3.39.2 of the ``sqlite3.exe`` program on Windows 10 and with version 3.31.1 of the ``sqlite3`` program running on linux (Linux Mint 20.3 with kernel version 5.15.0-41).

PostgreSQL
----------

**PostgreSQL**

.. _`PostgreSQL`: https://www.postgresql.org/

.. md-tab-set::

    .. md-tab-item:: 中文

        下面的 SQL 脚本可以用于在 `PostgreSQL`_ 数据库中创建与教科书表相当的表。该 SQL 脚本仅包含 **CREATE TABLE** 和 **INSERT** 语句，因此不应替换数据库中现有的表。

        - :download:`postgresql.sql`

        此 SQL 脚本在 Windows 10 上使用版本 12.5 的 ``psql.exe`` 程序以及在 Linux 上运行的版本 12.11 的 ``psql`` 程序（Linux Mint 20.3，内核版本 5.15.0-41）时经过验证，可以正确工作，加载到运行在 Linux 上的 PostgreSQL 版本 12.8 实例中（Linux Mint 20，内核版本 5.4.0-86）。注意: 在 Windows 10 上，您可能需要在加载或查询数据之前，首先在 ``psql`` 命令行中发出命令 ``\encoding utf8``。此设置可能不足以确保查询返回的所有字符都能正确显示，但数据可以正确加载。

        与教科书的显著差异：

        - 正如文本中所述，SQLite 不使用标准 SQL 方法自动生成顺序 ID 值。SQLite 数据库中使用的 **AUTOINCREMENT** 选项（在 **bookstore_sales** 和 **bookstore_inventory** 中）在 PostgreSQL 中不可用，但标准 SQL 的 **GENERATED BY DEFAULT AS IDENTITY** 选项是可用的。因此，PostgreSQL 脚本使用标准方法。这两种选项的行为略有不同。

    .. md-tab-item:: 英文

        The SQL script below can be used to create the equivalent of the textbook's tables in a `PostgreSQL`_ database.  The SQL script contains only **CREATE TABLE** and **INSERT** statements, and therefore should not replace existing tables within the database.

        - :download:`postgresql.sql`

        This SQL script was verified to work correctly using version 12.5 of the ``psql.exe`` program on Windows 10 and with version 12.11 of the ``psql`` program running on linux (Linux Mint 20.3 with kernel version 5.15.0-41), loading into a PostgreSQL version 12.8 instance running on linux (Linux Mint 20 with kernel version 5.4.0-86).  Note: on Windows 10, you may need to first issue the command ``\encoding utf8`` (at the ``psql`` command line) before loading or querying the data.  This setting may not be sufficient to ensure all characters can be viewed correctly when returned by a query, but the data can be loaded correctly.

        Notable differences from the textbook:

        - As described in the text, SQLite does not use a standard SQL approach to automatically generate sequential ID values.  The **AUTOINCREMENT** option used in the SQLite database (in **bookstore_sales** and **bookstore_inventory**) is not available in PostgreSQL, but the standard SQL **GENERATED BY DEFAULT AS IDENTITY** option is.  Accordingly, the PostgreSQL script uses the standard approach.  The two options behave slightly differently.

MySQL
-----

**MySQL**

.. _`MySQL`: https://www.mysql.com/

.. md-tab-set::

    .. md-tab-item:: 中文

        下面的 SQL 脚本可以用于在 `MySQL`_ 数据库中创建与教科书表相当的表。该 SQL 脚本仅包含 **CREATE TABLE** 和 **INSERT** 语句，因此不应替换数据库中现有的表。

        - :download:`mysql.sql`

        此 SQL 脚本在 Windows 10 上使用版本 8.0.29 的 MySQL Shell (``mysqlsh.exe``) 程序以及在 Linux 上运行的版本 8.0.29 的 ``mysql`` 程序（Linux Mint 20.3，内核版本 5.15.0-41）时经过验证，可以正确工作，加载到运行在 Linux 上的 MySQL 版本 8.0.26 实例中（Linux Mint 20，内核版本 5.4.0-86）。

        与教科书的显著差异：

        - 教科书数据库中的 **bookstore_sales** 表具有 **DEFAULT** 子句，用于在未提供列的值时将 **date_sold** 列设置为当前日期。MySQL 不允许为 **DATE** 类型的列设置默认值，但允许为 **TIMESTAMP** 类型设置。因此，MySQL 脚本中的 **date_sold** 列为 **TIMESTAMP** 类型（因此包括时间和日期）。
        - MySQL 的 **AUTO_INCREMENT** 选项与 SQLite 中的 **AUTOINCREMENT** 选项（在 **bookstore_sales** 和 **bookstore_inventory** 中使用）非常相似，但可能具有略微不同的行为。
        - **bookstore_inventory** 表包含一个名为 **condition** 的列。这是 MySQL 中的保留关键字，这意味着像 "SELECT DISTINCT condition FROM bookstore_inventory" 这样的查询将失败，除非您在 "condition" 这个词周围加上反引号。（反引号字符看起来像一个撇号，但倾斜方向相反。）

    .. md-tab-item:: 英文

        The SQL script below can be used to create the equivalent of the textbook's tables in a `MySQL`_ database.  The SQL script contains only **CREATE TABLE** and **INSERT** statements, and therefore should not replace existing tables within the database.

        - :download:`mysql.sql`

        This SQL script was verified to work correctly using version 8.0.29 of the MySQL Shell (``mysqlsh.exe``) program on Windows 10 and with version 8.0.29 of the ``mysql`` program running on linux (Linux Mint 20.3 with kernel version 5.15.0-41), loading into a MySQL version 8.0.26 instance running on linux (Linux Mint 20 with kernel version 5.4.0-86).

        Notable differences from the textbook:

        - The **bookstore_sales** table in the textbook database has a **DEFAULT** clause to set the **date_sold** column to the current date when no value is provided for the column.  MySQL does not permit default setting for columns of type **DATE**, but does allow it for the **TIMESTAMP** type.  Accordingly, the **date_sold** column in the MySQL script is of type **TIMESTAMP** (and thus includes time as well as date).
        - The MySQL **AUTO_INCREMENT** option is very similar to the **AUTOINCREMENT** option in SQLite (used in **bookstore_sales** and **bookstore_inventory**), but may have slightly different behavior.
        - The **bookstore_inventory** table contains a column named **condition**.  This is a reserved keyword in MySQL, which means that queries such as "SELECT DISTINCT condition FROM bookstore_inventory" will fail unless you put backticks around the word "condition".  (The backtick character looks like an apostrophe, but slanting in the opposite direction.)

Oracle
------

**Oracle**

.. md-tab-set::

    .. md-tab-item:: 中文

        下面的 SQL 脚本可以用于在 Oracle 数据库中创建与教科书表相当的表。该 SQL 脚本仅包含 **CREATE TABLE** 和 **INSERT** 语句以及设置临时会话变量的语句，因此不应替换数据库中现有的表。

        - :download:`oracle.sql`

        此 SQL 脚本在 Linux 上使用 Oracle 的 SQLcl 工具（版本 22.2，运行在 Linux Mint 20.3，内核版本 5.15.0-41）与 OpenJDK 版本 11.0.15 时经过验证，可以正确工作，加载到运行在 Linux 上的 Oracle Database XE 18c 实例中（openSUSE Leap 15.2，内核版本 5.3.18）。在 Windows 10 上使用 SQLcl（版本 22.2）时，脚本运行没有报告错误，但某些字符值加载不正确。注意：如果您使用 SQLcl 或 SQL\*Plus 运行此脚本，您 *必须* 取消注释脚本顶部的命令 ``SET DEFINE OFF``。否则，程序将解释任何 \& 字符为变量替换序列，这将停止脚本并导致数据无法正确加载。

        与教科书的显著差异：

        - 如文本中所述，SQLite 不使用标准 SQL 方法自动生成顺序 ID 值。在 SQLite 数据库中使用的 **AUTOINCREMENT** 选项（在 **bookstore_sales** 和 **bookstore_inventory** 中）在 Oracle 中不可用，但标准 SQL 的 **GENERATED BY DEFAULT AS IDENTITY** 选项是可用的。因此，Oracle 脚本使用标准方法。这两个选项的行为略有不同。

    .. md-tab-item:: 英文

        The SQL script below can be used to create the equivalent of the textbook's tables in an Oracle database.  The SQL script contains only **CREATE TABLE** and **INSERT** statements and statements setting temporary session variables, and therefore should not replace existing tables within the database.

        - :download:`oracle.sql`

        This SQL script was verified to work correctly using Oracle's SQLcl utility (release 22.2) running on linux (Linux Mint 20.3 with kernel version 5.15.0-41) with OpenJDK version 11.0.15, loading into an Oracle Database XE 18c instance running on linux (openSUSE Leap 15.2 with kernel version 5.3.18).  On Windows 10 with SQLcl (release 22.2), the script ran without reporting errors, but some character values were loaded incorrectly.  Note: if you run this script with SQLcl or SQL\*Plus, you *must* uncomment the command ``SET DEFINE OFF`` at the top of the script.  Otherwise, the program will interpret any \& characters to imply a variable substitution sequence, which will halt the script and prevent the data from loading correctly.

        Notable differences from the textbook:

        - As described in the text, SQLite does not use a standard SQL approach to automatically generate sequential ID values.  The **AUTOINCREMENT** option used in the SQLite database (in **bookstore_sales** and **bookstore_inventory**) is not available in Oracle, but the standard SQL **GENERATED BY DEFAULT AS IDENTITY** option is.  Accordingly, the Oracle script uses the standard approach.  The two options behave slightly differently.

SQL Server
----------

**SQL Server**

.. md-tab-set::

    .. md-tab-item:: 中文

        下面的 SQL 脚本可以用于在 Microsoft SQL Server 数据库中创建与教科书表相当的表。该 SQL 脚本主要包含 **CREATE TABLE** 和 **INSERT** 语句，不应替换数据库中现有的表。脚本顶部的 **USE** 语句假设数据将被加载到名为 "textbook" 的现有数据库中。该语句在与 ``sqlcmd`` 工具及其他软件一起使用时是必要的，可能需要根据需要编辑以指示正确的数据库。在其他客户端软件中，可能不需要该语句。

        - :download:`sqlserver.sql`

        此 SQL 脚本在 Linux 上使用 ``sqlcmd`` 程序（版本 17.10.0001.1，运行在 Linux Mint 20.3，内核版本 5.15.0-41）时经过验证，可以正确工作，加载到运行在 Linux 上的 SQL Server 2019 实例中（Linux Mint 20，内核版本 5.4.0-86）。在 Windows 10 上使用版本 15.0.2000.5 的 ``sqlcmd.exe`` 时，脚本运行没有报告错误，但某些字符值加载不正确。注意，必须使用支持 UTF8 的排序规则（这可以通过 **ALTER DATABASE** 语句在数据库上设置）；测试系统使用了 "Latin1_General_100_CI_AS_SC_UTF8" 排序规则。

        与教科书的显著差异：

        - SQL Server 为具有 **IDENTITY** 属性的列生成顺序整数值，其行为与标准 SQL 的 **GENERATED BY...** 和 SQLite 的 **AUTO_INCREMENT** 不同。

    .. md-tab-item:: 英文

        The SQL script below can be used to create the equivalent of the textbook's tables in a Microsoft SQL Server database.  The SQL script primarily contains **CREATE TABLE** and **INSERT** statements, and should not replace existing tables within the database.  The **USE** statement at the top of the script assumes that data will be loaded into an existing database named "textbook".  This statement is needed for use with the ``sqlcmd`` utility and possibly other software, and should be edited to indicate the correct database as needed.  The statement may not be needed in other client software programs.

        - :download:`sqlserver.sql`

        This SQL script was verified to work correctly using the ``sqlcmd`` program (version 17.10.0001.1) running on linux (Linux Mint 20.3 with kernel version 5.15.0-41), loading into a SQL Server 2019 instance running on linux (Linux Mint 20 with kernel version 5.4.0-86).  On Windows 10 with version 15.0.2000.5 of ``sqlcmd.exe``, the script ran without reporting errors, but some character values were loaded incorrectly.  Note that a collation supporting UTF8 must be used (this can be set on the database using an **ALTER DATABASE** statement); the test system used the "Latin1_General_100_CI_AS_SC_UTF8" collation.

        Notable differences from the textbook:

        - SQL Server generates sequential integer values for columns with the **IDENTITY** property, which differs in behavior compared to both the standard SQL **GENERATED BY...** and SQLite's **AUTO_INCREMENT**.

原始数据文件
--------------

**Raw data files**

.. md-tab-set::

    .. md-tab-item:: 中文

        如果您希望使用其他数据库，而不是上述列出的数据库，您可以通过文本编辑器的查找/替换功能和一些试错方法，轻松调整上述脚本以适用于您的数据库。或者，您也可以手动创建所需的表，并从下面链接的压缩档案中的数据文件加载数据——大多数数据库系统都提供从格式化文件加载数据的机制。数据文件采用逗号分隔值（CSV）格式，并以 UTF-8 编码。每个文件包含一行标题，标签与教科书数据库中的列名相匹配。如果您的数据库系统不支持此文件格式，您可以尝试用电子表格程序打开文件，然后导出为您的系统支持的格式。

        - :download:`practical_db_data_files.zip`

    .. md-tab-item:: 英文

        If you wish to use a database other than one of those listed above, you can likely adapt one of the above scripts for use with your database, using the find/replace function of a text editor and some trial and error.  Alternatively, you may create the desired tables manually, and load the data from the data files in the zip archive linked below - most database systems provide mechanisms to load data from formatted files.  The data files are in comma-separated value (CSV) format, and are encoded in UTF-8.  Each file includes a header row with labels matching the column names from the textbook database.  If your database system does not support this file format, you may be able to open the files with a spreadsheet program and then export a format that is supported by your system.

        - :download:`practical_db_data_files.zip`


