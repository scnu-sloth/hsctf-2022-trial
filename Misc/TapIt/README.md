# TapIt

>  公开 release 和 source部署的网址

## 题目描述

用键盘跟Miku酱唱出同样的歌声吧~

flag格式为r'[0-9a-v]{30}'，提交时用"hsctf{}"包裹

演唱工具：10.10.202.172:52039

## wp

https://c10udlnk.top/p/wpFor-2022SlothTrial/#tapit

## flag

hsctf{l0vemikufor3verdoul1ke7hi5misc}

## hints

1）画面可能会一样，但声音绝对不同。

## 答案

0-9a-v可以呈现32种不同的声音，16种不同的画面，也就是说有两个字符的画面是一种类型的，但是声音不同。

通过画面+声音筛选拿到flag。