-- Study Dashboards: cloud storage for signed-in users.
-- Run once in Supabase: Dashboard -> SQL Editor -> New query -> paste -> Run.
-- Every row belongs to one user and Row Level Security means a user can only ever see or change their own rows,
-- even though the browser talks to the database directly with the public "anon" key.

create table if not exists public.attempts (
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  id      text not null,                 -- the attempt id created in the browser
  ts      bigint not null,               -- when the quiz was taken (ms since epoch)
  subject text not null,                 -- subject slug or 'mixed'
  data    jsonb not null,                -- the full attempt: rows, marks, scheme, time...
  primary key (user_id, id)
);
create index if not exists attempts_user_ts on public.attempts (user_id, ts desc);

create table if not exists public.user_settings (
  user_id    uuid primary key default auth.uid() references auth.users(id) on delete cascade,
  marking    jsonb,                      -- {"c":2,"w":-1,"u":0}
  updated_at timestamptz not null default now()
);

alter table public.attempts      enable row level security;
alter table public.user_settings enable row level security;

drop policy if exists "own attempts" on public.attempts;
create policy "own attempts" on public.attempts
  for all using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists "own settings" on public.user_settings;
create policy "own settings" on public.user_settings
  for all using (user_id = auth.uid()) with check (user_id = auth.uid());
