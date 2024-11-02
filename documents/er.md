```mermaid
erDiagram

chat_rooms ||--|{ chat_histories : ""

chat_histories {
  uuid id PK
  int role_id
  text message
  timestamp created_at
  timestamp updated_at
}

chat_rooms {
  uuid id PK
  timestamp created_at
  timestamp updated_at
}

```