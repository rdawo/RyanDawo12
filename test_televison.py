import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power: False, Channel: 0, Volume: 0"

def test_power_toggle():
    tv = Television()
    assert str(tv).startswith("Power: False")
    tv.power()
    assert str(tv).startswith("Power: True")
    tv.power()
    assert str(tv).startswith("Power: False")

def test_mute_unmute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power: True, Channel: 0, Volume: 0"  # muted volume
    tv.mute()
    assert "Volume: 0" in str(tv)  # volume doesn't restore, still 0
    assert "Power: True" in str(tv)

def test_channel_up():
    tv = Television()
    tv.power()
    for _ in range(4):  # cycle through all channels
        tv.channel_up()
    assert str(tv).startswith("Power: True, Channel: 0")

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert "Channel: 3" in str(tv)
    tv.channel_down()
    assert "Channel: 2" in str(tv)

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert "Volume: 1" in str(tv)
    tv.volume_up()
    assert "Volume: 2" in str(tv)
    tv.volume_up()  # should stay at MAX_VOLUME
    assert "Volume: 2" in str(tv)

def test_volume_up_unmutes():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert "Volume: 1" in str(tv)

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert "Volume: 1" in str(tv)
    tv.volume_down()
    assert "Volume: 0" in str(tv)
    tv.volume_down()  # should stay muted and at 0
    assert "Volume: 0" in str(tv)

def test_volume_down_mutes():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert "Volume: 0" in str(tv)
