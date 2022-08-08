## Entity Relationship

```mermaid
erDiagram
    Customer ||--o{ Order : places

    Order ||--|{ LineItem : contains

    Customer {
        String id
        String name
    }
    class Order{
        String id
        OrderStatus status
    }
    class LineItem{
        String code
        String description
        int quantity
        int price
    }
```