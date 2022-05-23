from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import re

dom = xml.dom.minidom.parse('go_obo.xml')
collection = dom.documentElement
terms = collection.getElementsByTagName('term')  # get all terms
print(f'The total number of terms is {terms.length}.')
dic = {}
trans_link = []
for term in terms:
    id = term.getElementsByTagName('id')[0]
    is_a = term.getElementsByTagName('is_a')
    defstr = term.getElementsByTagName('defstr')[0]
    this_GO = id.firstChild.data  # the id of this term
    parent_GO = []
    if re.search('translation', defstr.firstChild.data, re.I):  # check whether translation related
        trans_link.append(this_GO)
    if this_GO not in dic:
        dic[this_GO] = []
    for i in range(is_a.length):
        parent_GO.append(is_a[i].firstChild.data)
        childnodes = []
        if parent_GO[i] not in dic:
            dic[parent_GO[i]] = []
        dic[parent_GO[i]].append(this_GO)  # store this GO as childnode
        dic[parent_GO[i]].append(dic[this_GO])  # store childnodes of this GO as childnodes
# Here a list of this term's childnodes (l1)  is appended to its parentnode's childnode list (l2).
# In this case, if l1 varies, the l1 in l2 will also vary. So as the loop goes, l1 will be appended with its childnodes
# until all childnodes of have been found. So after the loop, l1 in l2 is also completed, but l2 is a nested list.
# So subsequently, we nned to unfold the nested list and get all elements in it.


def unfold(mlist):
    """
    input the list you want to unfold; list
    get every element in the list and append it to another list; the input list is ok to contain multiple lists
    return None
    """
    for node in mlist:
        if type(node) == str:
            final.append(node)
        else:
            unfold(node)


# unfold all the list and store them in the corresponding parentnode in the dictionary
for key, value in dic.items():
    final = []
    unfold(value)
    add = list(set(final))
    dic[key] = add

# draw the boxplot to show the distribution
values = list(dic.values())
childnodes_number = [len(node) for node in values]
trans_link_number = [len(dic[node]) for node in trans_link]
plt.subplot(121)
plt.boxplot(childnodes_number, showmeans=True, meanline=True)
plt.title('distribution of child nodes across all terms')
plt.ylabel('number of child nodes')
plt.xlabel('all terms')

plt.subplot(122)
plt.boxplot(trans_link_number, showmeans=True, meanline=True)
plt.title('distribution of child nodes across terms associated with ‘translation’')
plt.ylabel('number of child nodes')
plt.xlabel('terms associated with ‘translation’')
plt.show()

# compare the average of child node number of the two
childnodes_mean = sum(childnodes_number) / len(childnodes_number)
trans_mean = sum(trans_link_number) / len(trans_link_number)
print(f'the average child node number of the overall Gene Ontology is {childnodes_mean}')
print(f'the average child node number of the ‘translation’ terms is {trans_mean}')
if trans_mean < childnodes_mean:
    print('The ‘translation’ terms contain, on average, smaller number of child nodes than the overall Gene Ontology.')
else:
    print('The ‘translation’ terms contain, on average, greater number of child nodes than the overall Gene Ontology.')
#  The ‘translation’ terms contain, on average, greater number of child nodes than the overall Gene Ontology.
