`outbound-trunk.sjon` COMMAND `lk sip outbound create outbound-trunk.json`
SIPTrunkID: ST_rPvW5wTCkUJj

`participant.json` COMMAND `lk sip participant create participant.json`
SIPCallID: SCL_VF87Cpsipn4a
ParticipantID: PA_7pFcZC4eH85d
ParticipantIdentity: sip-test
RoomName: open-room

`sip-participant.json` COMMAND `lk sip participant create sip-participant.json`
SIPCallID: SCL_qkdZT9EHFyxR
ParticipantID: PA_SnvmiqQRg8Yv
ParticipantIdentity: sip-test
RoomName: my-sip-room

RUN COMMAND
`lk dispatch create --new-room --agent-name my-outbound-agent`