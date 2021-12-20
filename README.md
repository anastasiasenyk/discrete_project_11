## Discrete. Computer project
### task №7, group №11
___
worked on the project:
* [Anastasia Beheni](#func2)
* [Anastasia Senyk](#func1)
* [Maksym Koliubinskyi](#func3)
* [Olesia Omelchuk](#func4)
* [Sofia Yamkova](#func5)


---

#### Реалізація проекту:
1.Розподілили функції

2.Під час роботи над проектом збиралися і обговорювали алгоритми, після чого реалізовували функції.

У цьому проекті ми виконали наші знання з дискретної математики про графи, зокрема ізоморфність графів, ейлерів та гамільтонів цикли, дводольність графа, а також розфарбування графів. Також, при перевірці на зв’язність, використали пошук вширину.

---
____read_data__:__ Anastasia Senyk
<a id="func1"></a>

csv file:

|first_v |second_v |
|--- |--- |
1 | 2
2 | 3
3 | 1


Перша функція read_data читає файл з графом і повертає 2 tupples з словниками, де ключем є вершина, а значенням список вершин, з якими зв'язана вершина-ключ. Один словник- для неорієнтовфного графа, а інший- для орієнтованого. Спочатку ми перевіряємо, чи існує такий шлях до файлу. Якщо шлях існує- читаємо рядки файлу і розділяємо їх за пробілом (file.columns[0].split(' ')), тепер проходимось по кожному рядку. Row перетворюємо в список і беремо перший елемент. Перевіряємо, чи в ключах є перша вершина, якщо немає, то створюємо новий ключ.

---
____ifconnected__:__ Anastasia Senyk
<a id="func1"></a>

Друга функція ifconnected перевіряє граф на зв’язність і повертає True/False. Ми використовуємо пошук вширину, проходимось по вершинах першого графа і додаємо їх в список, а потім перевіряємо, чи є якісь вершини, яких немає в списку. Спочатку створюємо 2 списки: відвідані вершини і не відвідані вершини. Беремо першу вершину і проходимось пошуком вширину, поки існує черга(поки список не буде пустим). Після закінчення перевіряємо, чи всі елементи відвідані.

---
____bipartite__:__ Anastasia Senyk
<a id="func1"></a>

Третя функція bipartite перевіряє граф на дводольність і повертає True/False. Тут знову використовуємо пошук вширину. Першу вершину записуємо в перший список, другу в другий список і так по порядку, поки не пройдемося по всіх вершинах. На малюнку показаний приклад(1- перший список з вершинами, 2- другий).

---
__find euler circuit:__ Anastasia Beheni
<a id="func2"></a>

Пошук Ейлерового графу містить 4 функції. Фінальний вивід – список вершин по порядку, в якому треба проходитись. 
Функції euler_circuit_not_directed і euler_circuit_directed повертають цей фінальний вивід, вони викликають в собі функцію, яка перевіряє чи існує ейлерів цикл і, якщо існує, шукає його. 
В функціях is_euler_possible_not_directed і is_euler_possible_directed ми перевіряємо, чи існує ейлерів цикл для неорієнтованих і орієнтованих графів. В функції для неорієнтованих графів ми проходимось по всіх значеннях словника(списках вершин) і записуємо в новостворений список довжину цього списку(тобто степінь кожної вершини графа). Після цього перевіряємо, чи кожен з елементів нового списку ділиться націло на 2(тобто є парним), якщо ні, то функція повертає False, якщо так, то True.
Щодо функції для орієнтованих графів ми робимо подібну процедуру, але ми перевіряємо, чи кількість дуг, які входять в вершину дорівнює кількості дуг, які з неї виходять.
В функціях, де ми вже шукаємо цей ейлерів цикл, ми шукаємо його за таким алгоритмом: “останній прийшов - перший вийде”.

---
__find hamiltonian cycle:__ Anastasia Senyk, Maksym Koliubinskyi
<a id="func3"></a>

Функції pre_hamilton і hamiltonian_cycle шукають чи існує Гамільтоновий шлях і, якщо існує, повертає список вершин, по яких треба проходитись, щоб отримати цей шлях.
Перша функція шукає, чи існує шлях та повертає True/False відповідно, а також в ній ми створюємо елементи для другої функції.
Друга функція приймає наш граф, список, змінну для переходу між ключами і довжину шляху. Проходимось пошуком вшир і після отримання списку перевіряємо, чи початкова і кінцева вершини зв’язані і чи вершина є ключем(особливо важливо для орієнтованих графів). Item(вершину) прирівнюємо до якогось індексу в списку ключа і щоразу рекурсивно збільшуємо цей індекс на 1. Остання рекурсія “повертає назад”.

---
__Function4:__ Olesia Omelchuk
<a id="func6"></a>

---
__Function5:__ Sofia Yamkova
<a id="func7"></a>

---
#### Висновки

Під час виконання комп’ютерного проекту ми поглибили наші знання з дискретної математики з теми графів, а саме:
1.Алгоритм пошуку вшир (перевірка зв’язності та дводольність)

2.Алгоритм пошуку вглиб (Ейлерів цикл)

3.Алгоритм backtracking (Гамільтонів цикл)

4.Перевірка інваріантів ізоморфності графа

А також вдосконалили свої навички з основ програмування, застосовуючи їх на практиці, що пригодиться нам на 2-му курсі.


