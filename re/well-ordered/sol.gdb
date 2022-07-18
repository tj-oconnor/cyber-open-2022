set width 0
set height 0
set verbose off

break before
commands 1
    printf "CALLED (('%c', %d), ('%c', %d))\n",$rsi,$rdx,$rcx,$r8
    continue
end

break exit
commands 2
    set $pc = *(long long *)$rsp
    set $rsp = $rsp + 4
    continue
end

run
