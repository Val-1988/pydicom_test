# pydicom_test

Входные данные находятся в данном репозитории в директории src
Ссылка на документацию pydicom - https://pydicom.github.io/pydicom/stable
Выполнить преобразования входных данных, используя модуль pydicom. Необходимо сделать следующее:

    удалить информацию хранящуюся в ключе PatientName (анонимизировать файлы)

    используя информацию в ключах StudyInstanceUID, SeriesInstanceUID, SOPInstanceUID преобразовать структуру хранения файлов к следующей:
        на первом уровне StudyInstanceUID
        на втором уровне SeriesInstanceUID
        именем файла будет значение SOPInstanceUID с расширением .dcm

    Таким образом, путь к каждому файлу будет выглядеть так: $StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm

    дополнительно, нужно создать файл, в котором путь к каждому файлу исходной структуры сопоставлен пути к файлу в конечной структуре.

Выходные данные

Результат работы:

    директория с полученной структурой;
    файл со списком соответствия путей;
    код скрипта.
