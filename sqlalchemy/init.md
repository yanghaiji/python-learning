# 常用的数据类型映射

| SQLAlchemy    | Python               | SQL                             |
| :------------ | :------------------- | :------------------------------ |
| `BigInteger`  | `int`                | `BIGINT`                        |
| `Boolean`     | `bool`               | `BOOLEAN` or `SMALLINT`         |
| `Date`        | `datetime.date`      | `DATE` (SQLite: `STRING`)       |
| `DateTime`    | `datetime.datetime`  | `DATETIME` (SQLite: `STRING`)   |
| `Enum`        | `str`                | `ENUM` or `VARCHAR`             |
| `Float`       | `float` or `Decimal` | `FLOAT` or `REAL`               |
| `Integer`     | `int`                | `INTEGER`                       |
| `Interval`    | `datetime.timedelta` | `INTERVAL` or `DATE from epoch` |
| `LargeBinary` | `byte`               | `BLOB` or `BYTEA`               |
| `Numeric`     | `decimal.Decimal`    | `NUMERIC` or `DECIMAL`          |
| `Unicode`     | `unicode`            | `UNICODE` or `VARCHAR`          |
| `Text`        | `str`                | `CLOB` or `TEXT`                |
| `Time`        | `datetime.time`      | `DATETIME`                      |

