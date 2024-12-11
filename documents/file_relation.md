```mermaid
graph TB
    %% Main entry points
    main[api/src/main.py] -->|imports| routers/chat.py
    main[api/src/main.py] -->|imports| routers/threads.py
    main[api/src/main.py] -->|imports| middleware.py

    %% Routers
    routers/chat.py -->|imports| usecases/chat_gpt/generate_chat_response.py
    routers/chat.py -->|imports| usecases/chat_gpt/streaming_chat_responses.py
    routers/chat.py -->|imports| usecases/chat_message/save_chat_message.py
    routers/chat.py -->|imports| usecases/chat_thread/generate_thread.py
    routers/chat.py -->|imports| usecases/chat_gpt/fetch_and_format_chat_messages.py
    routers/chat.py -->|imports| schemes/chat.py
    routers/chat.py -->|imports| db.py

    %% Usecases
    usecases/chat_gpt/generate_chat_response.py -->|imports| services/openai_service.py
    usecases/chat_gpt/streaming_chat_responses.py -->|imports| services/openai_service.py
    usecases/chat_message/save_chat_message.py -->|imports| repositories/chat_message.py
    usecases/chat_message/save_chat_message.py -->|imports| constants.py
    usecases/chat_thread/generate_thread.py -->|imports| repositories/chat_thread.py
    usecases/chat_thread/generate_thread.py -->|imports| usecases/chat_thread/generate_title.py
    usecases/chat_thread/generate_title.py -->|imports| services/openai_service.py
    usecases/chat_gpt/fetch_and_format_chat_messages.py -->|imports| repositories/chat_message.py
    usecases/chat_gpt/fetch_and_format_chat_messages.py -->|imports| constants.py

    %% Repositories
    repositories/chat_thread.py -->|imports| models/chat_thread.py
    repositories/chat_message.py -->|imports| models/chat_message.py

    %% Models
    models/chat_message.py -->|imports| models/role.py
    models/chat_message.py -->|imports| models/chat_thread.py

    %% Middleware
    middleware.py -->|imports| config.py

    %% Database
    db.py -->|imports| config.py
```