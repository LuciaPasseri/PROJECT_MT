# Master thesis project

This project has the aim to build an ontology with a bottom up approach, starting from a relational database (csv files of tables are uploaded).

At first for the mapping part is used the project [r2rml](https://github.com/chrdebru/r2rml), that maps all the tables inside the database into triples.

Then the libraries _rdflib_ and _pyvis.network_ are used to read and visualize the ontology (ttl file format), saved in [this file](https://github.com/LuciaPasseri/master_thesis/blob/main/ontology.html).
