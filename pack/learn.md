对应表

全休止符 sleep 4 //休止一小节=休止四拍

play 67 == play :G4 //MIDI数值和音符对应c-1=0。c0=12

# 语法
## 设置节奏
    use_bpm 100
    bits per minute， 除以60可以得到每秒几拍，默认为60
## 设置振幅
    play :c2, attack: 0, release: 0.3
    attack振幅上升时间，release振幅下降时间
## 设置旋律
    use_transpose 2 #移调
    play_pattern_timed [:c2, :d2, :e2, :d2], [0.5, 0.25, 0.75, 0.5]
    可精简代码，不用反复使用play和sleep了
    试验时发现＜c4的无法在run后发出声音，仅当后面数字≥4才可行
## 旋律反复
    4.times do
      {code}
    end
    或
    loop do
      {code}
    end
    旋律反复可嵌套使用
## live_loop
    live_loop :{drums} do
      sample :{drum_heavy_kick}
      sleep 1
    end
    drums是live_loop指令的命名。可以随意命名以便区分。
    一个 live_loop 至少要有一个 sleep 指令。
    sample名字对应
        drum_heavy_kick 大鼓
        drum_snare_hard 小鼓
        drum_cymbal_closed 踩镲

    live_loop :{bass} do
      use_synth :{fm}
      sleep 1
    end
    synth名字对应
## 外部采样包sample
    sample后可跟随设置rate倍率，amp幅值，pan声像，cutoff去掉高于给定值的频率，attack，decay，sustain，release(ADSR)振幅控制，start，finish采样起止时间，beat_stretch设置采样文件拍数，rate倍率
        sample :loop_amen, rate: 1.5
        # new_sample_duration = (1 / rate) * sample_duration
        sample :loop_amen, beat_stretch:2
        # new_sample_duration = beat_stretch
        sample :ambi_lunar_land, amp: 0.5
        sample :loop_amen, pan: -1
        sample :drum_cymbal_open, attack: 0.01, sustain: 0, release: 0.1
        sample :loop_amen, start: 0.5, finish: 0.8, rate: -0.2, attack: 0.3, release: 1
        sample "C:/Users/sam/Desktop/my-sound.wav"
        # 外部采样，有时.wav可以省略

    sample "/path/to/my/samples/120_Bb_piano1.wav"
    # /path/to/my/samples/ = "c:/Program Files/Sonic Pi/etc/samples"

    sample "/path/to/my/samples/", 0 
    等价于
    samps = "/path/to/my/samples/"
    sample samps, 0

    手动筛选满足条件120，a#的条目
    samps = "/path/to/my/samples/"
    sample samps, "120", 1
    或者同理
    samps = "/path/to/my/samples/"
    sample samps, "120", "A#" 
    或者同理
    samps = "/path/to/my/samples/"
    sample samps, "120", "Bb", 1, lpf: 70, amp: 2

    等价项目
    sample "/path/to/dir", "100", "C#"
    sample ["/path/to/dir", "100", "C#"]
    sample "/path/to/dir", ["100", "C#"]
    sample ["/path/to/dir", ["100", ["C#"]]]
## 随机化
    随机化搭配循环比较好玩，语法为rrand和choose

    loop do
      play choose([60, 65, 72])
      sleep 1
    end 

    loop do
      play 50, release: 0.1, cutoff: rrand(60, 120)
      sleep 0.125
    end

    loop do
      sample :perc_bell, rate: rrand(0.125, 1.5)
      sleep rrand(0.2, 2)
    end

    loop do
      play 60, amp: rand
      sleep 0.25
    end
    rand默认范围为[0,1)的float，rand_i为int[0,n]
    同理，rrand输出值为float(a,b)，rrand_i为int[a,b]
    dice(n)输出1-n的整数，one_in(6)输出布尔值

    use_random_seed 40
    5.times do
      play rrand(50, 100)
      sleep 0.5
    end
    use_random_seed可以固定随机化旋律，使听到的旋律每一次都相同，改变数字40即可改变旋律
