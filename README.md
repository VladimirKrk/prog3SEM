---

# Проект "Компьютер-Программа"
  **Создание классов данных:**
   - `Program` - класс, представляющий программу, с полями:
     - `id` - уникальный идентификатор программы;
     - `name` - название программы;
     - `version` - год выпуска программы;
     - `comp_id` - идентификатор компьютера, на котором установлена программа.
   
   - `Computer` - класс, представляющий компьютер, с полями:
     - `id` - уникальный идентификатор компьютера;
     - `model` - модель компьютера.

   - `ProgramComputer` - класс для реализации связи многие-ко-многим между компьютерами и программами:
     - `comp_id` - идентификатор компьютера;
     - `program_id` - идентификатор программы.

