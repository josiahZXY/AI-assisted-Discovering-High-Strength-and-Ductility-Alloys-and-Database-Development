# AI-assisted-Discovering-High-Strength-and-Ductility-Alloys-and-Database-Development
请将本文件解压放置在D盘下面
Please unzip this file and place it under the D drive

本文件一共分为4个part，database，deep_learning,machine_learning,user_interface.在使用之前可以先阅读根目录下的论文，以便于获得对该数据集更加清晰的认识。
This document is divided into 4 parts, database, deep_learning, machine_learning, user_interface. Before using, you can read the papers in the root directory to get a clearer understanding of the data set.

在使用user_interface之前，请先确保安装了numpy,scipty,scikit_learn,matplotlib,matminer,pymatgen,pandas,pilow,request,beautifulsoup等python第三方库。
Before using user_interface, please make sure to install numpy, scipty, scikit_learn, matplotlib, matminer, pymatgen, pandas, pilow, request, beautifulsoup and other python third-party libraries.

database中包含有从materialsproject下获得的带有弹性性质的材料数据，分为给linear regression、random forest的数据以及给automatminer使用的数据，都已做好标记。以及从Matweb上通过爬虫爬取的数据集，共有大概61个各种合金的csv文件，同时AMbasicdata中提供了作者已经处理好的，可供Automatminer使用的总体数据集(因为时间关系并没有全部处理完)。同时database中还有爬取matweb网站的爬虫代码web_crawler_code，其中version2.0中的爬虫代码只需要简单修改便可以爬取matweb最新数据。同时我们还在pictures文件夹中提供了项目中所有路径实现后的图像。
The database contains material data with elastic properties obtained from materialsproject, which is divided into data for linear regression, random forest, and data for automatminer,  and the data set crawled through the crawler from Matweb. There are about 61 csv files of various alloys, at the same time, AMbasicdata provides the overall data set that the author has processed and can be used by Automatminer. Meanwhile, there is a crawler code web_crawler_code that crawls the matweb website in the database. The crawler code in version2.0 only needs to be modified to crawl the latest data of matweb. We also provide images of all paths in the project in the pictures folder.


deep_learning中包含有建立需要的整体数据文件的代码以及结果绘图代码，并且我们提供了CGCNN和mt_cgcnn两种预测模型搭建文件。在其中的data文件夹下有供cgcnn和mt-cgcnn使用的5种属性数据集。
'deep_learning' contains the code for building the overall data file needed and the result drawing code, and we provide two prediction model building files, CGCNN and mt_cgcnn. There are 5 kinds of attribute data sets for cgcnn and mt-cgcnn under the data folder.

machine_learning中包含有构建linear regression和random forest预测模型的基础代码以及构建automatminer预测模型的基础代码。
'machine_learning' contains the basic code for building linear regression and random forest prediction models and the basic code for building automatminer prediction models.

User_interface整合了完整的机器学习和深度学习预测路径，应力应变曲线绘制以及数据库搜索。每一项功能模块都有相关的user guidebook提供，只需要在成功运行程序之后点击"help"，即可一步步实现预测模型搭建以及应力应变曲线预测。
User_interface integrates complete machine learning and deep learning prediction paths, stress-strain curve drawing and database search. Each functional module is provided by the relevant user guidebook. You only need to click "help" after successfully running the program to realize the step-by-step prediction model construction and stress-strain curve prediction.

祝各位使用愉快！如果使用过程中有问题欢迎加我的微信询问:13568930634.
I wish you all a happy use! If you have any questions during use, please add my WeChat : 13568930634.

2020/5/3
