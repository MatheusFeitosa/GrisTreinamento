Create database GRIS;

use GRIS;

create table alunos (
nome varchar(48) not null,
dre int not null,
curso varchar(48) not null,
email varchar(48) not null,
datanasc date not null,
telegra varchar(48) not null,
notebook bool not null,
primary key (dre)
);

create table tags (
conteudo varchar(200) not null,
assunto varchar(100) not null,
datadatag date not null,
idtg int not null auto_increment,
primary key (idtg)
);

create table professores (
DaUFRJ bool not null,
nome varchar(48) not null,
cpf int not null,
contato1 varchar(48) not null,
contato2 varchar(48),
primary key (cpf)
);

create table ava (
tag int not null,
candidato int not null,
nota int not null,
professor int not null,
idava int not null auto_increment,
foreign key (tag) references tags(idtg),
foreign key (candidato) references alunos(dre),
foreign key (professor) references professores(cpf),
primary key (idava)

);