Title: Vim: Operation on search matches using gn
Date: Wed 26 Dec 10:08:53 CET 2018
Category: Vim
Tags: Vim
The gn command (introduced in Vim 7.4) makes it easy to operate on regions of
text that match the current search pattern. It’s especially useful when used
with a regex that matches text regions of variable length.

Here’s what Vim’s documentation has to say about the gn command (:help gn):
> Search forward for the last used search pattern, like with n, and start
Visual mode to select the match. If the cursor is on the match, visually
selects it. If an operator is pending, operates on the match.

这里有三个步骤：

* Search forward for the last used search pattern.
* Visually select it. (so that operator could apply to the pattern immediately)
* Apply pending operator.

一般的查找下一个(n)，只是做了第一步，如果你的查找是多个单词或者一个区域，例如 "this
is"，正常的查找下一个不会选择全部，而是将光标移动到匹配的开始，也就是在"this"， 
如果你要一起修改"this is", 需要再次选择"this is"，然后替换。

在没有知道这个命令之前，我都是使用q来record多个操作到寄存器。然后重复的应用到下一个匹配的搜索。

'gn'在Operator-pending mode下，可以将所有的操作融合为一个步骤，
这样就可以使用vim的'.'dot指令进行重复，简便很多。例如：
```shell
\this is	#search block "this is"
:cgn these are	#next match pattern, and change it into "these are"
.		#apply the same modification to the next match
```

Reference:  
[Operating on search matches using gn](http://vimcasts.org/episodes/operating-on-search-matches-using-gn/)
