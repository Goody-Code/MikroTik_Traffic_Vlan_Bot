:global vlanData ""
/interface vlan print detail without-paging do={
    :set vlanData ($vlanData . $"name" . " - " . $"tx-byte" . " - " . $"rx-byte" . "\n")
}
:log info $vlanData
