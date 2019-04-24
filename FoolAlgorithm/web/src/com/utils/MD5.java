package com.utils;
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
public class MD5
{
    private long m_buf[];
    private long m_bits[];
    private byte m_in[];
    private char HEX[] = 
    	{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
         'a', 'b', 'c', 'd', 'e', 'f'};

    public MD5()
    {
        m_buf = new long[4];
        m_bits = new long[2];
        m_in = new byte[64];
    }

    /*
     * 加密方法 
     * 调用方式：
     * MD5 md = new MD5();
     * String code = md.toMD5("加密参数");
     * code就是加密后的密文
     */
    public String toMD5(String src)
    {
        byte digest[] = toDigest(src.getBytes());
        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < digest.length; i++)
        {
            sb.append(HEX[(digest[i] & 0xff) / 16]);
            sb.append(HEX[(digest[i] & 0xff) % 16]);
        }

        return sb.toString();
    }

    public byte[] toDigest(byte src[])
    {
        byte digest[] = new byte[16];
        int len = src.length;
        MD5Init();
        MD5Update(src, len);
        MD5Final(digest);
        return digest;
    }

    private void memset(byte des[], int des_offset, byte dat, int len)
    {
        for(int i = 0; i < len; i++)
            des[des_offset + i] = dat;

    }

    private void memset(long des[], int des_offset, long dat, int len)
    {
        for(int i = 0; i < len; i++)
            des[des_offset + i] = dat;

    }

    private void memcpy(byte des[], int des_offset, byte src[], int src_offset, int len)
    {
        for(int i = 0; i < len; i++)
            des[des_offset + i] = src[src_offset + i];

    }

    private long bp2long(byte src[], int offset_lng)
    {
        long ret = 0L;
        ret = (long)src[offset_lng * 4 + 0] & 255L | (long)(src[offset_lng * 4 + 1] << 8) & 65280L | (long)(src[offset_lng * 4 + 2] << 16) & 0xff0000L | (long)(src[offset_lng * 4 + 3] << 24) & 0xff000000L;
        return ret & 0xffffffffL;
    }

    private void MD5Init()
    {
        m_buf[0] = 0x67452301L;
        m_buf[1] = 0xefcdab89L;
        m_buf[2] = 0x98badcfeL;
        m_buf[3] = 0x10325476L;
        m_bits[0] = 0L;
        m_bits[1] = 0L;
    }

    private void MD5Update(byte buf[], int len)
    {
        long t = m_bits[0];
        m_bits[0] = t + (long)(len << 3);
        if(m_bits[0] < t)
            m_bits[1]++;
        m_bits[1] = m_bits[1] + (long)(len >> 29);
        t = t >> 3 & 63L;
        if(t != 0L)
        {
            long p = t;
            t = (long)64 - t & 0xffffffffL;
            if((long)len < t)
            {
                memcpy(m_in, (int)t, buf, 0, len);
                return;
            }
            memcpy(m_in, (int)t, buf, 0, (int)t);
            MD5Transform();
            len = (int)((long)len - t);
        }
        for(; len >= 64; len -= 64)
        {
            memcpy(m_in, 0, buf, (int)t, 64);
            MD5Transform();
            t += 64;
        }

        memcpy(m_in, 0, buf, (int)t, len);
    }

    private void MD5Final(byte digest[])
    {
        long count = m_bits[0] >> 3 & 63L;
        m_in[(int)count] = -128;
        long p = count + (long)1;
        count = (long)63 - count;
        if(count < (long)8)
        {
            memset(m_in, (int)p, (byte)0, (int)count);
            MD5Transform();
            memset(m_in, 0, (byte)0, 56);
        } else
        {
            memset(m_in, (int)p, (byte)0, (int)(count - (long)8));
        }
        m_in[56] = (byte)(int)(m_bits[0] & (long)255);
        m_in[57] = (byte)(int)(m_bits[0] >> 8 & (long)255);
        m_in[58] = (byte)(int)(m_bits[0] >> 16 & (long)255);
        m_in[59] = (byte)(int)(m_bits[0] >> 24 & (long)255);
        m_in[60] = (byte)(int)(m_bits[1] & (long)255);
        m_in[61] = (byte)(int)(m_bits[1] >> 8 & (long)255);
        m_in[62] = (byte)(int)(m_bits[1] >> 16 & (long)255);
        m_in[63] = (byte)(int)(m_bits[1] >> 24 & (long)255);
        MD5Transform();
        for(int i = 0; i < 4; i++)
        {
            digest[i * 4 + 0] = (byte)(int)(m_buf[i] & (long)255);
            digest[i * 4 + 1] = (byte)(int)(m_buf[i] >> 8 & (long)255);
            digest[i * 4 + 2] = (byte)(int)(m_buf[i] >> 16 & (long)255);
            digest[i * 4 + 3] = (byte)(int)(m_buf[i] >> 24 & (long)255);
        }

        MD5Init();
    }

    private long F1(long x, long y, long z)
    {
        return (z ^ x & (y ^ z)) & 0xffffffffL;
    }

    private long F2(long x, long y, long z)
    {
        return F1(z, x, y);
    }

    private long F3(long x, long y, long z)
    {
        return (x ^ y ^ z) & 0xffffffffL;
    }

    private long F4(long x, long y, long z)
    {
        return (y ^ (x | z ^ 0L - 1L)) & 0xffffffffL;
    }

    private long MD5STEP(long w, long f, long x, long y, long z, long data, long s)
    {
        w = w + f + data & 0xffffffffL;
        w = (w << (int)s | w >> (int)((long)32 - s)) & 0xffffffffL;
        w = w + x & 0xffffffffL;
        return w;
    }

    private void MD5Transform()
    {
        long a = m_buf[0];
        long b = m_buf[1];
        long c = m_buf[2];
        long d = m_buf[3];
        a = MD5STEP(a, F1(b, c, d), b, c, d, bp2long(m_in, 0) + 0xd76aa478L, 7L);
        d = MD5STEP(d, F1(a, b, c), a, b, c, bp2long(m_in, 1) + 0xe8c7b756L, 12L);
        c = MD5STEP(c, F1(d, a, b), d, a, b, bp2long(m_in, 2) + 0x242070dbL, 17L);
        b = MD5STEP(b, F1(c, d, a), c, d, a, bp2long(m_in, 3) + 0xc1bdceeeL, 22L);
        a = MD5STEP(a, F1(b, c, d), b, c, d, bp2long(m_in, 4) + 0xf57c0fafL, 7L);
        d = MD5STEP(d, F1(a, b, c), a, b, c, bp2long(m_in, 5) + 0x4787c62aL, 12L);
        c = MD5STEP(c, F1(d, a, b), d, a, b, bp2long(m_in, 6) + 0xa8304613L, 17L);
        b = MD5STEP(b, F1(c, d, a), c, d, a, bp2long(m_in, 7) + 0xfd469501L, 22L);
        a = MD5STEP(a, F1(b, c, d), b, c, d, bp2long(m_in, 8) + 0x698098d8L, 7L);
        d = MD5STEP(d, F1(a, b, c), a, b, c, bp2long(m_in, 9) + 0x8b44f7afL, 12L);
        c = MD5STEP(c, F1(d, a, b), d, a, b, bp2long(m_in, 10) + 0xffff5bb1L, 17L);
        b = MD5STEP(b, F1(c, d, a), c, d, a, bp2long(m_in, 11) + 0x895cd7beL, 22L);
        a = MD5STEP(a, F1(b, c, d), b, c, d, bp2long(m_in, 12) + 0x6b901122L, 7L);
        d = MD5STEP(d, F1(a, b, c), a, b, c, bp2long(m_in, 13) + 0xfd987193L, 12L);
        c = MD5STEP(c, F1(d, a, b), d, a, b, bp2long(m_in, 14) + 0xa679438eL, 17L);
        b = MD5STEP(b, F1(c, d, a), c, d, a, bp2long(m_in, 15) + 0x49b40821L, 22L);
        a = MD5STEP(a, F2(b, c, d), b, c, d, bp2long(m_in, 1) + 0xf61e2562L, 5L);
        d = MD5STEP(d, F2(a, b, c), a, b, c, bp2long(m_in, 6) + 0xc040b340L, 9L);
        c = MD5STEP(c, F2(d, a, b), d, a, b, bp2long(m_in, 11) + 0x265e5a51L, 14L);
        b = MD5STEP(b, F2(c, d, a), c, d, a, bp2long(m_in, 0) + 0xe9b6c7aaL, 20L);
        a = MD5STEP(a, F2(b, c, d), b, c, d, bp2long(m_in, 5) + 0xd62f105dL, 5L);
        d = MD5STEP(d, F2(a, b, c), a, b, c, bp2long(m_in, 10) + 0x2441453L, 9L);
        c = MD5STEP(c, F2(d, a, b), d, a, b, bp2long(m_in, 15) + 0xd8a1e681L, 14L);
        b = MD5STEP(b, F2(c, d, a), c, d, a, bp2long(m_in, 4) + 0xe7d3fbc8L, 20L);
        a = MD5STEP(a, F2(b, c, d), b, c, d, bp2long(m_in, 9) + 0x21e1cde6L, 5L);
        d = MD5STEP(d, F2(a, b, c), a, b, c, bp2long(m_in, 14) + 0xc33707d6L, 9L);
        c = MD5STEP(c, F2(d, a, b), d, a, b, bp2long(m_in, 3) + 0xf4d50d87L, 14L);
        b = MD5STEP(b, F2(c, d, a), c, d, a, bp2long(m_in, 8) + 0x455a14edL, 20L);
        a = MD5STEP(a, F2(b, c, d), b, c, d, bp2long(m_in, 13) + 0xa9e3e905L, 5L);
        d = MD5STEP(d, F2(a, b, c), a, b, c, bp2long(m_in, 2) + 0xfcefa3f8L, 9L);
        c = MD5STEP(c, F2(d, a, b), d, a, b, bp2long(m_in, 7) + 0x676f02d9L, 14L);
        b = MD5STEP(b, F2(c, d, a), c, d, a, bp2long(m_in, 12) + 0x8d2a4c8aL, 20L);
        a = MD5STEP(a, F3(b, c, d), b, c, d, bp2long(m_in, 5) + 0xfffa3942L, 4L);
        d = MD5STEP(d, F3(a, b, c), a, b, c, bp2long(m_in, 8) + 0x8771f681L, 11L);
        c = MD5STEP(c, F3(d, a, b), d, a, b, bp2long(m_in, 11) + 0x6d9d6122L, 16L);
        b = MD5STEP(b, F3(c, d, a), c, d, a, bp2long(m_in, 14) + 0xfde5380cL, 23L);
        a = MD5STEP(a, F3(b, c, d), b, c, d, bp2long(m_in, 1) + 0xa4beea44L, 4L);
        d = MD5STEP(d, F3(a, b, c), a, b, c, bp2long(m_in, 4) + 0x4bdecfa9L, 11L);
        c = MD5STEP(c, F3(d, a, b), d, a, b, bp2long(m_in, 7) + 0xf6bb4b60L, 16L);
        b = MD5STEP(b, F3(c, d, a), c, d, a, bp2long(m_in, 10) + 0xbebfbc70L, 23L);
        a = MD5STEP(a, F3(b, c, d), b, c, d, bp2long(m_in, 13) + 0x289b7ec6L, 4L);
        d = MD5STEP(d, F3(a, b, c), a, b, c, bp2long(m_in, 0) + 0xeaa127faL, 11L);
        c = MD5STEP(c, F3(d, a, b), d, a, b, bp2long(m_in, 3) + 0xd4ef3085L, 16L);
        b = MD5STEP(b, F3(c, d, a), c, d, a, bp2long(m_in, 6) + 0x4881d05L, 23L);
        a = MD5STEP(a, F3(b, c, d), b, c, d, bp2long(m_in, 9) + 0xd9d4d039L, 4L);
        d = MD5STEP(d, F3(a, b, c), a, b, c, bp2long(m_in, 12) + 0xe6db99e5L, 11L);
        c = MD5STEP(c, F3(d, a, b), d, a, b, bp2long(m_in, 15) + 0x1fa27cf8L, 16L);
        b = MD5STEP(b, F3(c, d, a), c, d, a, bp2long(m_in, 2) + 0xc4ac5665L, 23L);
        a = MD5STEP(a, F4(b, c, d), b, c, d, bp2long(m_in, 0) + 0xf4292244L, 6L);
        d = MD5STEP(d, F4(a, b, c), a, b, c, bp2long(m_in, 7) + 0x432aff97L, 10L);
        c = MD5STEP(c, F4(d, a, b), d, a, b, bp2long(m_in, 14) + 0xab9423a7L, 15L);
        b = MD5STEP(b, F4(c, d, a), c, d, a, bp2long(m_in, 5) + 0xfc93a039L, 21L);
        a = MD5STEP(a, F4(b, c, d), b, c, d, bp2long(m_in, 12) + 0x655b59c3L, 6L);
        d = MD5STEP(d, F4(a, b, c), a, b, c, bp2long(m_in, 3) + 0x8f0ccc92L, 10L);
        c = MD5STEP(c, F4(d, a, b), d, a, b, bp2long(m_in, 10) + 0xffeff47dL, 15L);
        b = MD5STEP(b, F4(c, d, a), c, d, a, bp2long(m_in, 1) + 0x85845dd1L, 21L);
        a = MD5STEP(a, F4(b, c, d), b, c, d, bp2long(m_in, 8) + 0x6fa87e4fL, 6L);
        d = MD5STEP(d, F4(a, b, c), a, b, c, bp2long(m_in, 15) + 0xfe2ce6e0L, 10L);
        c = MD5STEP(c, F4(d, a, b), d, a, b, bp2long(m_in, 6) + 0xa3014314L, 15L);
        b = MD5STEP(b, F4(c, d, a), c, d, a, bp2long(m_in, 13) + 0x4e0811a1L, 21L);
        a = MD5STEP(a, F4(b, c, d), b, c, d, bp2long(m_in, 4) + 0xf7537e82L, 6L);
        d = MD5STEP(d, F4(a, b, c), a, b, c, bp2long(m_in, 11) + 0xbd3af235L, 10L);
        c = MD5STEP(c, F4(d, a, b), d, a, b, bp2long(m_in, 2) + 0x2ad7d2bbL, 15L);
        b = MD5STEP(b, F4(c, d, a), c, d, a, bp2long(m_in, 9) + 0xeb86d391L, 21L);
        m_buf[0] += a;
        m_buf[1] += b;
        m_buf[2] += c;
        m_buf[3] += d;
    }
    
  
} 
