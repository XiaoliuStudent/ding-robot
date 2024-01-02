use `ding-robot`;
create table help_docs
(
    doc_id        varchar(100) not null primary key,
    doc_name      varchar(100) not null,
    father_doc_id varchar(100) not null,
    doc_comment   varchar(255) not null,
    state         tinyint(1)   not null,
    create_time   datetime     not null,
    doc_type      varchar(100) null,
    work_type     int          null
);