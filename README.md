# DoDo - Server
This repo can be seen as the Server application of my [DoDo Android application](https://github.com/MapManagement/DoDo).
It's not absolutely necessary but surely improves your experience with it. I'm planning on a server program which
can be connected with clients to save and sync data (todos and notes in my case) on multiple devices. Therefore, this
repository will give you the opportunity to host the program on your own server. Further explanations and overviews are
already in the making.

# Features
**work in progress**

# Database
Most of the data will be stored in a relational database, and I chose [MariaDB](https://mariadb.org/) for this project.
Why, you might ask, and the answer is nearly as simple as the question itself. In the past I worked mainly with MariaDB
and MySQL and since the stored data will only contain some todo and note information like content, color, creation date
and so on, any database should work fine anyway. You can find more information about my data model adn the stored data
[here](/information/database.md).

# Connection
The communication between client and server will be based on [gRPC](https://grpc.io/). It will sync the local data on
your device with the data stored on the server. How and when the data will be synced is not decided yet but as always
I will update [this file](/information/connection.md) as soon as something should change.