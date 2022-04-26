/***
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/design-linked-list/
 * 
 * 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。
 * 如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
 * 
 * 在链表类中实现这些功能：
 * get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
 * addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
 * addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
 * addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。
 * 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
 * deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 * 
 * 示例1:
 * MyLinkedList linkedList = new MyLinkedList();
 * linkedList.addAtHead(1);
 * linkedList.addAtTail(3);
 * linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
 * linkedList.get(1);            //返回2
 * linkedList.deleteAtIndex(1);  //现在链表是1-> 3
 * linkedList.get(1);            //返回3
 *
 * 提示：
 * 所有val值都在 [1, 1000] 之内。
 * 操作次数将在  [1, 1000] 之内。
 * 请不要使用内置的 LinkedList 库。
***/

typedef struct NewListNode{
    int val;
    struct NewListNode * next;
} ListNode;

typedef struct {
    int len;
    ListNode *head;
} MyLinkedList;


MyLinkedList* myLinkedListCreate() {
    MyLinkedList *myLinkedList = (MyLinkedList *)malloc(sizeof(MyLinkedList));
    if (myLinkedList == NULL) {
        return NULL;
    }
    
    memset(myLinkedList, 0, sizeof(MyLinkedList));
    return myLinkedList;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    if (index < 0 || index >= obj->len) {
        return -1;
    }

    ListNode *p = obj->head;
    for (int i = 0; i < index; i++) {
        p = p->next;
    }

    return p->val;
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    myLinkedListAddAtIndex(obj, 0, val);
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    myLinkedListAddAtIndex(obj,obj->len, val);     
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    if (index < 0 || index > obj->len) {
        return;
    }

    ListNode *node = (ListNode *)malloc(sizeof(ListNode));
    if (node == NULL) {
        return;
    }
    node->val = val;

    if (index == 0) {
        node->next = obj->head;
        obj->head = node;
        obj->len += 1; 
        return;
    }

    ListNode *p = obj->head;
    for (int i = 0; i < index - 1; i++) {
        p = p->next;
    }
    node->next = p->next;
    p->next = node;
    obj->len += 1;       
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
   if (index < 0 || index >= obj->len) {
        return;
    }
    
    if (index == 0) {
        obj->head = obj->head->next;
        obj->len -= 1;
        return;
    }
    ListNode *p = obj->head;
    ListNode *pre = obj->head;
    for (int i = 0; i < index; i++) {
        pre = p;
        p = p->next;
    }

    if (index == obj->len - 1) {
        pre->next = NULL;
    } else {
        pre->next = p->next;
    }
    obj->len -= 1; 
}

void FreeWithRecur(ListNode * node)
{
    if (node != NULL && node->next != NULL) {
        FreeWithRecur(node->next);
        node->next = NULL;
    } 

    free(node);
}
void myLinkedListFree(MyLinkedList* obj) {
    FreeWithRecur(obj->head);
    free(obj);
}