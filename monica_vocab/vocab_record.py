import sqlite3
from db_utils import VocabDB
from setting import DATABASE_PATH
from vocab_config import Vocab_Obj

def check_input(input_str):
    confirm = input(f"請確認輸入為：{input_str} (確認請打Y)")
    return confirm

def check_input(input_str):
        confirm = input(f"請確認輸入為：{input_str} (確認請打Y)")
        return confirm        

def get_chinese(vocab):
    while True:
        ch = input(f"{vocab}中文:\n")
        if check_input(ch) == "Y":
            break
    return ch
    
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
            if pos_select == "7":
                while True:
                    pos = input("請輸入詞性")
                    if check_input(pos) == "YES":
                        break
                break
            else:
                print("輸入無效，請檢查輸入")

    return pos

def get_familiarity(vocab):
    while True:
        f = input(f"{vocab} familiarity: (0~5) \n")
        if check_input(f) == "Y":
            break
    return f

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

def add_vocabs(vocab_list:list, db:VocabDB):
    for vocab in vocab_list:
        print(f"\n==============={vocab}==============\n")
        v = Vocab_Obj(vocab)
        existing = db.check_vocab_exist(v.vocab)
        if existing is None:
            v.pos = get_pos(vocab)
            v.chinese = get_chinese(vocab)
            v.familiarity = get_familiarity(vocab)
            v.print_info()
            db.insert_vocab("not2000", v.vocab, v.pos, v.chinese, v.familiarity)

        else:
            print("Vocabulary already exists in database:")
            id, vocab_type, vocab, v.pos, v.chinese, v.familiarity = existing #pass in current information
            v.print_info()
            update = input("Do you wish to update it? (Y/N)")
            if update == "Y":
                v.pos = get_pos(vocab)
                v.chinese = get_chinese(vocab)
                v.familiarity = get_familiarity(vocab)
                print("Update Entry:")
                v.print_info()
                db.update_vocab(vocab, v.pos, v.chinese, v.familiarity)

def main():
    db = VocabDB(DATABASE_PATH)
    vocab_list = get_vocabs()
    add_vocabs(vocab_list, db)
    db.close()

if __name__== "__main__":
    
    main() 