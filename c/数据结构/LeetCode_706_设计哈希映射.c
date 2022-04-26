/***
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/design-hashmap/
 * 
 * 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
 * 实现 MyHashMap 类：
 * MyHashMap() 用空映射初始化对象
 * void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
 * int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
 * void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
 * 
 * 示例:
 * 输入: ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
 *       [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
 * 输出: [null, null, null, 1, -1, null, 1, null, -1]
 * 解释：
 * 
 * MyHashMap myHashMap = new MyHashMap();
 * myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
 * myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
 * myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
 * myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
 * myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
 * myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
 * myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
 * myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
***/

#define BUCKET_SIZE 100

typedef struct NewList {
    int key;
    int val;
    struct NewList *next;
} List;

void listPush(List *head, int key, int val) {
    List* tmp = malloc(sizeof(List));
    tmp->key = key;
    tmp->val = val;
    tmp->next = head->next;
    head->next = tmp;
}

void listDelete(List* head, int key) {
    for (List* it = head; it->next; it = it->next) {
        if (it->next->key == key) {
            List* tmp = it->next;
            it->next = tmp->next;
            free(tmp);
            break;
        }
    }
}

List* listFind(List* head, int key) {
    for (List* it = head; it->next; it = it->next) {
        if (it->next->key == key) {
            return it->next;
        }
    }
    return NULL;
}

void listFree(List* head) {
    while (head->next) {
        List* tmp = head->next;
        head->next = tmp->next;
        free(tmp);
    }
}

int hash(int key) {
    return key % BUCKET_SIZE;
}

typedef struct {
    List* bucket;
} MyHashMap;

MyHashMap* myHashMapCreate() {
    MyHashMap* ret = malloc(sizeof(MyHashMap));
    ret->bucket = malloc(sizeof(List) * BUCKET_SIZE);
    for (int i = 0; i < BUCKET_SIZE; i++) {
        ret->bucket[i].key = 0;
        ret->bucket[i].val = 0;
        ret->bucket[i].next = NULL;
    }
    return ret;
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    int h = hash(key);
    List* rec = listFind(&(obj->bucket[h]), key);
    if (rec == NULL) {
        listPush(&(obj->bucket[h]), key, value);
    } else {
        rec->val = value;
    }
}

int myHashMapGet(MyHashMap* obj, int key) {
    int h = hash(key);
    List* rec = listFind(&(obj->bucket[h]), key);
    if (rec == NULL) {
        return -1;
    } else {
        return rec->val;
    }
}

void myHashMapRemove(MyHashMap* obj, int key) {
    int h = hash(key);
    listDelete(&(obj->bucket[h]), key);
}

void myHashMapFree(MyHashMap* obj) {
    for (int i = 0; i < BUCKET_SIZE; i++) {
        listFree(&(obj->bucket[i]));
    }
    free(obj->bucket);
}

/**
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);
 
 * int param_2 = myHashMapGet(obj, key);
 
 * myHashMapRemove(obj, key);
 
 * myHashMapFree(obj);
*/