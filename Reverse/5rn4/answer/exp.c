// sm4 code from https://blog.csdn.net/weixin_42700740/article/details/102667012

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/******************************定义系统参数FK的取值****************************************/
const unsigned long TBL_SYS_PARAMS[4] = {
    0xa3b1bac6,
    0x56aa3350,
    0x677d9197,
    0xb27022dc
};

/******************************定义固定参数CK的取值****************************************/
const unsigned long TBL_FIX_PARAMS[32] = {
    0x00070e15,0x1c232a31,0x383f464d,0x545b6269,
    0x70777e85,0x8c939aa1,0xa8afb6bd,0xc4cbd2d9,
    0xe0e7eef5,0xfc030a11,0x181f262d,0x343b4249,
    0x50575e65,0x6c737a81,0x888f969d,0xa4abb2b9,
    0xc0c7ced5,0xdce3eaf1,0xf8ff060d,0x141b2229,
    0x30373e45,0x4c535a61,0x686f767d,0x848b9299,
    0xa0a7aeb5,0xbcc3cad1,0xd8dfe6ed,0xf4fb0209,
    0x10171e25,0x2c333a41,0x484f565d,0x646b7279
};

/******************************SBox参数列表****************************************/
const unsigned char TBL_SBOX[256] = {
    0xd6,0x90,0xe9,0xfe,0xcc,0xe1,0x3d,0xb7,0x16,0xb6,0x14,0xc2,0x28,0xfb,0x2c,0x05,
    0x2b,0x67,0x9a,0x76,0x2a,0xbe,0x04,0xc3,0xaa,0x44,0x13,0x26,0x49,0x86,0x06,0x99,
    0x9c,0x42,0x50,0xf4,0x91,0xef,0x98,0x7a,0x33,0x54,0x0b,0x43,0xed,0xcf,0xac,0x62,
    0xe4,0xb3,0x1c,0xa9,0xc9,0x08,0xe8,0x95,0x80,0xdf,0x94,0xfa,0x75,0x8f,0x3f,0xa6,
    0x47,0x07,0xa7,0xfc,0xf3,0x73,0x17,0xba,0x83,0x59,0x3c,0x19,0xe6,0x85,0x4f,0xa8,
    0x68,0x6b,0x81,0xb2,0x71,0x64,0xda,0x8b,0xf8,0xeb,0x0f,0x4b,0x70,0x56,0x9d,0x35,
    0x1e,0x24,0x0e,0x5e,0x63,0x58,0xd1,0xa2,0x25,0x22,0x7c,0x3b,0x01,0x21,0x78,0x87,
    0xd4,0x00,0x46,0x57,0x9f,0xd3,0x27,0x52,0x4c,0x36,0x02,0xe7,0xa0,0xc4,0xc8,0x9e,
    0xea,0xbf,0x8a,0xd2,0x40,0xc7,0x38,0xb5,0xa3,0xf7,0xf2,0xce,0xf9,0x61,0x15,0xa1,
    0xe0,0xae,0x5d,0xa4,0x9b,0x34,0x1a,0x55,0xad,0x93,0x32,0x30,0xf5,0x8c,0xb1,0xe3,
    0x1d,0xf6,0xe2,0x2e,0x82,0x66,0xca,0x60,0xc0,0x29,0x23,0xab,0x0d,0x53,0x4e,0x6f,
    0xd5,0xdb,0x37,0x45,0xde,0xfd,0x8e,0x2f,0x03,0xff,0x6a,0x72,0x6d,0x6c,0x5b,0x51,
    0x8d,0x1b,0xaf,0x92,0xbb,0xdd,0xbc,0x7f,0x11,0xd9,0x5c,0x41,0x1f,0x10,0x5a,0xd8,
    0x0a,0xc1,0x31,0x88,0xa5,0xcd,0x7b,0xbd,0x2d,0x74,0xd0,0x12,0xb8,0xe5,0xb4,0xb0,
    0x89,0x69,0x97,0x4a,0x0c,0x96,0x77,0x7e,0x65,0xb9,0xf1,0x09,0xc5,0x6e,0xc6,0x84,
    0x18,0xf0,0x7d,0xec,0x3a,0xdc,0x4d,0x20,0x79,0xee,0x5f,0x3e,0xd7,0xcb,0x39,0x48
};

//4字节无符号数组转无符号long型
void four_uCh2uLong(unsigned char* in, unsigned long* out)
{
    int i = 0;
    *out = 0;
    for (i = 0; i < 4; i++)
        *out = ((unsigned long)in[i] << (24 - i * 8)) ^ *out;
}

//无符号long型转4字节无符号数组
void uLong2four_uCh(unsigned long in, unsigned char* out)
{
    int i = 0;
    //从32位unsigned long的高位开始取
    for (i = 0; i < 4; i++)
        *(out + i) = (unsigned long)(in >> (24 - i * 8));
}

//左移，保留丢弃位放置尾部
unsigned long move(unsigned long data, int length)
{
    unsigned long result = 0;
    result = (data << length) ^ (data >> (32 - length));

    return result;
}

//秘钥处理函数,先使用Sbox进行非线性变化，再将线性变换L置换为L'
unsigned long func_key(unsigned long input)
{
    int i = 0;
    unsigned long ulTmp = 0;
    unsigned char ucIndexList[4] = { 0 };
    unsigned char ucSboxValueList[4] = { 0 };
    uLong2four_uCh(input, ucIndexList);
    for (i = 0; i < 4; i++)
    {
        ucSboxValueList[i] = TBL_SBOX[ucIndexList[i]];
    }
    four_uCh2uLong(ucSboxValueList, &ulTmp);
    ulTmp = ulTmp ^ move(ulTmp, 13) ^ move(ulTmp, 23);

    return ulTmp;
}

//加解密数据处理函数,先使用Sbox进行非线性变化，再进行线性变换L
unsigned long func_data(unsigned long input)
{
    int i = 0;
    unsigned long ulTmp = 0;
    unsigned char ucIndexList[4] = { 0 };
    unsigned char ucSboxValueList[4] = { 0 };
    uLong2four_uCh(input, ucIndexList);
    for (i = 0; i < 4; i++)
    {
        ucSboxValueList[i] = TBL_SBOX[ucIndexList[i]];
    }
    four_uCh2uLong(ucSboxValueList, &ulTmp);
    ulTmp = ulTmp ^ move(ulTmp, 2) ^ move(ulTmp, 10) ^ move(ulTmp, 18) ^ move(ulTmp, 24);

    return ulTmp;
}

//解密函数（与加密函数基本一致，只是秘钥使用的顺序不同，即把钥匙反着用就是解密）
//len:数据长度 key:密钥 input:输入的加密后数据 output:输出的解密后数据
void decode_fun(unsigned char len, unsigned char* key, unsigned char* input, unsigned char* output)
{
    int i = 0, j = 0;
    unsigned long ulKeyTmpList[4] = { 0 };//存储密钥的unsigned long数据
    unsigned long ulKeyList[36] = { 0 };  //用于密钥扩展算法与系统参数FK运算后的结果存储
    unsigned long ulDataList[36] = { 0 }; //用于存放加密数据

    /*开始生成子秘钥*/
    four_uCh2uLong(key, &(ulKeyTmpList[0]));
    four_uCh2uLong(key + 4, &(ulKeyTmpList[1]));
    four_uCh2uLong(key + 8, &(ulKeyTmpList[2]));
    four_uCh2uLong(key + 12, &(ulKeyTmpList[3]));

    ulKeyList[0] = ulKeyTmpList[0] ^ TBL_SYS_PARAMS[0];
    ulKeyList[1] = ulKeyTmpList[1] ^ TBL_SYS_PARAMS[1];
    ulKeyList[2] = ulKeyTmpList[2] ^ TBL_SYS_PARAMS[2];
    ulKeyList[3] = ulKeyTmpList[3] ^ TBL_SYS_PARAMS[3];

    for (i = 0; i < 32; i++)             //32次循环迭代运算
    {
        //5-36为32个子秘钥
        ulKeyList[i + 4] = ulKeyList[i] ^ func_key(ulKeyList[i + 1] ^ ulKeyList[i + 2] ^ ulKeyList[i + 3] ^ TBL_FIX_PARAMS[i]);
    }
    /*生成32轮32位长子秘钥结束*/

    for (j = 0; j < len / 16; j++)  //进行循环加密,并将加密后数据保存
    {
        /*开始处理解密数据*/
        four_uCh2uLong(input + 16 * j, &(ulDataList[0]));
        four_uCh2uLong(input + 16 * j + 4, &(ulDataList[1]));
        four_uCh2uLong(input + 16 * j + 8, &(ulDataList[2]));
        four_uCh2uLong(input + 16 * j + 12, &(ulDataList[3]));

        //解密
        for (i = 0; i < 32; i++)
        {
            ulDataList[i + 4] = ulDataList[i] ^ func_data(ulDataList[i + 1] ^ ulDataList[i + 2] ^ ulDataList[i + 3] ^ ulKeyList[35 - i]);//与加密唯一不同的就是轮密钥的使用顺序
        }
        /*将解密后数据输出*/
        uLong2four_uCh(ulDataList[35], output + 16 * j);
        uLong2four_uCh(ulDataList[34], output + 16 * j + 4);
        uLong2four_uCh(ulDataList[33], output + 16 * j + 8);
        uLong2four_uCh(ulDataList[32], output + 16 * j + 12);
    }
}

unsigned char byte_40B000[32] = {
    0xF6, 0x66, 0xAE, 0xF4, 0xFE, 0x17, 0xAE, 0x18, 0xAE, 0x68, 0xC7, 0x81, 0x18, 0x86, 0xC1, 0x9B, 
    0xF5, 0xEA, 0xE6, 0x22, 0x8F, 0x42, 0xCF, 0xF0, 0xD0, 0x15, 0x2A, 0xB7, 0xDC, 0xB3, 0x68, 0x4F
};

int main() {
    unsigned char i, len;
    unsigned char rslt[32] = { 0 };
    unsigned char key[20] = "746573746f766572";
    for (int i = 0; i <= 512; i++) { // 做了513次交换，其实就是做了一次交换，魔改密文
        byte_40B000[23] ^= byte_40B000[24];
        byte_40B000[24] ^= byte_40B000[23];
        byte_40B000[23] ^= byte_40B000[24];
    }
    decode_fun(32, key, byte_40B000, rslt);
    for (int i = 0; i < 32; i++) {
        printf("%c", rslt[i]);
    }
    return 0;
}