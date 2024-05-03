CREATE TABLE IF NOT EXISTS voice_setups (
    guild_id BIGINT PRIMARY KEY,
    category_id BIGINT,
    voice_channel_id BIGINT
);