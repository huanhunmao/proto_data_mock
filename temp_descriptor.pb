
�
freeze-skill-admin.protoesport_admin_logic"�
CoachDetail
uid (Ruid
ttid (	Rttid
nickname (	Rnickname$
esport_er_type (ResportErType
guild_id (RguildId

guild_name (	R	guildName$
obtain_role_ts (RobtainRoleTs"�
SkillDetail
game_id (RgameId
	game_name (	RgameName?
freeze_type (2.esport_admin_logic.FreezeTypeR
freezeType$
freeze_stop_ts (RfreezeStopTs

is_deleted (R	isDeleted
rank (Rrank"I
GetCoachSkillInfoRequest
uid (Ruid
	is_freeze (RisFreeze"[
GetCoachSkillInfoResponse>

skill_list (2.esport_admin_logic.SkillDetailR	skillList"F
FreezeCoachSkill
uid (Ruid 
game_id_list (R
gameIdList"�
BatFreezeCoachSkillRequestE
freeze_list (2$.esport_admin_logic.FreezeCoachSkillR
freezeList?
freeze_type (2.esport_admin_logic.FreezeTypeR
freezeType$
freeze_stop_ts (RfreezeStopTs#
freeze_reason (	RfreezeReason
op_user (	RopUser"8
BatFreezeCoachSkillResponse
err_list (	RerrList"h
UnfreezeCoachSkillRequest
uid (Ruid 
game_id_list (R
gameIdList
op_user (	RopUser"
UnfreezeCoachSkillResponse"�
GetCoachSkillInfoListRequest
page (Rpage
	page_size (RpageSize
uid_list (RuidList
guild_id (RguildId"�
GetCoachSkillInfoListResponseU
coach_skill_info_list (2".esport_admin_logic.CoachSkillInfoRcoachSkillInfoList
total (Rtotal"�
CoachSkillInfoB
coach_detail (2.esport_admin_logic.CoachDetailRcoachDetail>

skill_list (2.esport_admin_logic.SkillDetailR	skillList"�
"GetSkillFreezeOperationListRequest
page (Rpage
	page_size (RpageSize
uid_list (RuidList
guild_id (RguildId
game_id (RgameId"�
#GetSkillFreezeOperationListResponseO
operation_list (2(.esport_admin_logic.SkillFreezeOperationRoperationList
total (Rtotal"�
SkillFreezeOperationB
coach_detail (2.esport_admin_logic.CoachDetailRcoachDetail>

skill_list (2.esport_admin_logic.SkillDetailR	skillList?
freeze_type (2.esport_admin_logic.FreezeTypeR
freezeType$
freeze_stop_ts (RfreezeStopTs#
freeze_reason (	RfreezeReason
op_user (	RopUser
op_ts (RopTs*X

FreezeType
FREEZE_TYPE_UNFREEZE 
FREEZE_TYPE_FOREVER
FREEZE_TYPE_TO_TIME2�
FreezeSkillAdminp
GetCoachSkillInfo,.esport_admin_logic.GetCoachSkillInfoRequest-.esport_admin_logic.GetCoachSkillInfoResponsev
BatFreezeCoachSkill..esport_admin_logic.BatFreezeCoachSkillRequest/.esport_admin_logic.BatFreezeCoachSkillResponses
UnfreezeCoachSkill-.esport_admin_logic.UnfreezeCoachSkillRequest..esport_admin_logic.UnfreezeCoachSkillResponse|
GetCoachSkillInfoList0.esport_admin_logic.GetCoachSkillInfoListRequest1.esport_admin_logic.GetCoachSkillInfoListResponse�
GetSkillFreezeOperationList6.esport_admin_logic.GetSkillFreezeOperationListRequest7.esport_admin_logic.GetSkillFreezeOperationListResponseB6Z4golang.52tt.com/protocol/services/esport_admin_logicbproto3