import sqlite3

DATABASE_PATH = "/Users/chia-enli/Desktop/Drawer/Tutoring/Monica/Vocabulary/vocabulary.db"

def check_input(input_str):
    confirm = input(f"請確認輸入為：{input_str} (確認請打Y)")
    return confirm

def get_pos(vocab):
    pos_dict = {
    "0": "名詞",
    "1": "動詞",
    "2": "形容詞",
    "3": "副詞",
    "4": "代詞",
    "5": "冠詞",
    "6": "介系詞"
    }
    while True:
        pos_select = input(f"{vocab} 詞性（0:名詞, 1:動詞, 2:形容詞, 3:副詞, 4:代詞, 5:冠詞, 6:介系詞, 7:其他（自行輸入）:\n")
        try:
            pos = pos_dict[pos_select]
            if check_input(pos) == "Y":
                break
        except:
            if pos_select == 7:
                while True:
                    pos = input("請輸入詞性")
                    if check_input(pos) == "YES":
                        break
                break
            else:
                print("輸入無效，請檢查輸入")

    return pos


def get_chinese(vocab):
    while True:
        ch = input(f"{vocab}中文:\n")
        if check_input(ch) == "Y":
            break
    return ch

def get_familiarity(vocab):
    while True:
        f = input(f"{vocab} familiarity: (0~5) \n")
        if check_input(f) == "Y":
            break
    return f

def check_exist(cursor, vocab):
    #If vocab exists in databse, returns the respective row; if not, returns None
    check_query = """SELECT * FROM vocabulary_main WHERE vocab = ? LIMIT 1"""
    cursor.execute(check_query, (vocab,))
    result = cursor.fetchone()
    return result

def get_max_id(cursor):
    query = """SELECT MAX(ID) FROM vocabulary_main"""
    cursor.execute(query)
    row = cursor.fetchone()
    return int(row[0])

def update_vocab(cursor, vocab):
    print(f"Updating {vocab}")
    pos = get_pos(vocab)
    chinese = get_chinese(vocab)
    familiarity = get_familiarity(vocab)

    update_query = """UPDATE vocabulary_main SET part_of_speech = ?, chinese = ?, familiarity = ? WHERE vocab = ?"""
    cursor.execute (update_query, (pos, chinese, familiarity, vocab))
    conn.commit()

def add_vocab(cursor, vocab):
    
    exist_info = check_exist(cursor, vocab)
    if exist_info:
        print(f"{vocab} already exists in database, query result as follows:")
        print(exist_info)
        update_q = input("Do you wish to update the data for this vocab?(Y/N)")
        if update_q == "Y":
            update_vocab(cursor, vocab)

    else:
        pos = get_pos(vocab)
        chinese = get_chinese(vocab)
        id_new = get_max_id(cursor) + 1
        cursor.execute (
            """
            INSERT INTO vocabulary_main (ID, vocab_type, vocab, part_of_speech, chinese, familiarity)
            VALUES (?, ?, ?, ?, ?)
            """,
            (id_new, "not2000", vocab, pos, chinese, 2)
        )

        conn.commit()

def get_vocabs():
    vocab_list = []
    while True:
        in_vocab = input("Please input new vocab (Please type 'end' if all vocabs have been added)")
        if in_vocab == 'end':
            break
        elif check_input(in_vocab) == "Y":
            vocab_list.append(in_vocab)
    print("Added Vocabs:")
    print(vocab_list)
    return vocab_list

def add_vocabs(vocab_list, cursor):

    for vocab in vocab_list:
        print("=======\n")
        add_vocab(cursor, vocab)
        print("========\n")

if __name__== "__main__":
    # Connect to your SQLite database file:
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    vocab_list = get_vocabs()

    add_vocabs(vocab_list, cursor)

    conn.commit()
    conn.close()

    print("Database updated!")