# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# 账户配额不足，每个腾讯云账户每个地域下最多可创建 20 个 EIP。
ADDRESSQUOTALIMITEXCEEDED = 'AddressQuotaLimitExceeded'

# 申购次数不足，每个腾讯云账户每个地域每天申购次数为配额数*2 次。
ADDRESSQUOTALIMITEXCEEDED_DAILYALLOCATE = 'AddressQuotaLimitExceeded.DailyAllocate'

# CAM签名/鉴权错误。
AUTHFAILURE = 'AuthFailure'

# 内部错误。
INTERNALERROR = 'InternalError'

# 操作内部错误。
INTERNALSERVERERROR = 'InternalServerError'

# 不支持此账户。
INVALIDACCOUNT_NOTSUPPORTED = 'InvalidAccount.NotSupported'

# 指定EIP处于被封堵状态。当EIP处于封堵状态的时候是不能够进行绑定操作的，需要先进行解封。
INVALIDADDRESSID_BLOCKED = 'InvalidAddressId.Blocked'

#  指定的EIP不存在。
INVALIDADDRESSID_NOTFOUND = 'InvalidAddressId.NotFound'

# 指定EIP处于欠费状态。
INVALIDADDRESSIDSTATE_INARREARS = 'InvalidAddressIdState.InArrears'

# 指定 EIP 当前状态不能进行绑定操作。只有 EIP 的状态是 UNBIND 时才能进行绑定操作。
INVALIDADDRESSIDSTATUS_NOTPERMIT = 'InvalidAddressIdStatus.NotPermit'

# 指定EIP的当前状态不允许进行该操作。
INVALIDADDRESSSTATE = 'InvalidAddressState'

# 不被支持的实例。
INVALIDINSTANCE_NOTSUPPORTED = 'InvalidInstance.NotSupported'

# 指定实例已经绑定了EIP。需先解绑当前的EIP才能再次进行绑定操作。
INVALIDINSTANCEID_ALREADYBINDEIP = 'InvalidInstanceId.AlreadyBindEip'

# 无效实例ID。指定的实例ID不存在。
INVALIDINSTANCEID_NOTFOUND = 'InvalidInstanceId.NotFound'

# 指定 NetworkInterfaceId 不存在或指定的PrivateIpAddress不在NetworkInterfaceId上。
INVALIDNETWORKINTERFACEID_NOTFOUND = 'InvalidNetworkInterfaceId.NotFound'

# 参数错误。
INVALIDPARAMETER = 'InvalidParameter'

# 参数不支持同时指定。
INVALIDPARAMETER_COEXIST = 'InvalidParameter.Coexist'

# 指定过滤条件不存在。
INVALIDPARAMETER_FILTERINVALIDKEY = 'InvalidParameter.FilterInvalidKey'

# 指定过滤条件不是键值对。
INVALIDPARAMETER_FILTERNOTDICT = 'InvalidParameter.FilterNotDict'

# 指定过滤选项值不是列表。
INVALIDPARAMETER_FILTERVALUESNOTLIST = 'InvalidParameter.FilterValuesNotList'

# 该过滤规则不合法。
INVALIDPARAMETER_INVALIDFILTER = 'InvalidParameter.InvalidFilter'

# 下一跳类型与下一跳网关不匹配。
INVALIDPARAMETER_NEXTHOPMISMATCH = 'InvalidParameter.NextHopMismatch'

# 指定的两个参数冲突，不能同时存在。 EIP只能绑定在实例上或指定网卡的指定内网 IP 上。
INVALIDPARAMETERCONFLICT = 'InvalidParameterConflict'

# 参数取值错误。
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# 该地址计费方式与其他地址冲突。
INVALIDPARAMETERVALUE_ADDRESSINTERNETCHARGETYPECONFLICT = 'InvalidParameterValue.AddressInternetChargeTypeConflict'

# 该地址不可与此实例申请。
INVALIDPARAMETERVALUE_ADDRESSNOTAPPLICABLE = 'InvalidParameterValue.AddressNotApplicable'

# 该地址不是CalcIP。
INVALIDPARAMETERVALUE_ADDRESSNOTCALCIP = 'InvalidParameterValue.AddressNotCalcIP'

# 带宽超出限制。
INVALIDPARAMETERVALUE_BANDWIDTHOUTOFRANGE = 'InvalidParameterValue.BandwidthOutOfRange'

# 未查询到该带宽包。
INVALIDPARAMETERVALUE_BANDWIDTHPACKAGENOTFOUND = 'InvalidParameterValue.BandwidthPackageNotFound'

# 选择带宽低于可允许的最小范围。
INVALIDPARAMETERVALUE_BANDWIDTHTOOSMALL = 'InvalidParameterValue.BandwidthTooSmall'

# 指定云联网关联黑石私有网络数量达到上限。
INVALIDPARAMETERVALUE_CCNATTACHBMVPCLIMITEXCEEDED = 'InvalidParameterValue.CcnAttachBmvpcLimitExceeded'

# 目的网段不在对端VPC的CIDR范围内。
INVALIDPARAMETERVALUE_CIDRNOTINPEERVPC = 'InvalidParameterValue.CidrNotInPeerVpc'

# 非法入参组合。
INVALIDPARAMETERVALUE_COMBINATION = 'InvalidParameterValue.Combination'

# 入参重复。
INVALIDPARAMETERVALUE_DUPLICATE = 'InvalidParameterValue.Duplicate'

# 缺少参数。
INVALIDPARAMETERVALUE_EMPTY = 'InvalidParameterValue.Empty'

# 该实例的计费方式与其他实例不同。
INVALIDPARAMETERVALUE_INCONSISTENTINSTANCEINTERNETCHARGETYPE = 'InvalidParameterValue.InconsistentInstanceInternetChargeType'

# 该实例不支持AnycastEIP。
INVALIDPARAMETERVALUE_INSTANCEDOESNOTSUPPORTANYCAST = 'InvalidParameterValue.InstanceDoesNotSupportAnycast'

# 该实例已有WanIP。
INVALIDPARAMETERVALUE_INSTANCEHASWANIP = 'InvalidParameterValue.InstanceHasWanIP'

# 该实例没有CalcIP，无法完成请求。
INVALIDPARAMETERVALUE_INSTANCENOCALCIP = 'InvalidParameterValue.InstanceNoCalcIP'

# 该实例没有WanIP，无法完成请求。
INVALIDPARAMETERVALUE_INSTANCENOWANIP = 'InvalidParameterValue.InstanceNoWanIP'

# 由于该IP被禁用，无法绑定该实例。
INVALIDPARAMETERVALUE_INSTANCENORMALPUBLICIPBLOCKED = 'InvalidParameterValue.InstanceNormalPublicIpBlocked'

# 传入的DedicatedClusterId有误。
INVALIDPARAMETERVALUE_INVALIDDEDICATEDCLUSTERID = 'InvalidParameterValue.InvalidDedicatedClusterId'

# 该IP只能绑定小时流量后付费和带宽包实例。
INVALIDPARAMETERVALUE_INVALIDINSTANCEINTERNETCHARGETYPE = 'InvalidParameterValue.InvalidInstanceInternetChargeType'

# 该实例状态无法完成操作。
INVALIDPARAMETERVALUE_INVALIDINSTANCESTATE = 'InvalidParameterValue.InvalidInstanceState'

# 该Tag不合法。
INVALIDPARAMETERVALUE_INVALIDTAG = 'InvalidParameterValue.InvalidTag'

# 负载均衡实例已经绑定了EIP。
INVALIDPARAMETERVALUE_LBALREADYBINDEIP = 'InvalidParameterValue.LBAlreadyBindEip'

# 参数值超出限制。
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# 入参格式不合法。
INVALIDPARAMETERVALUE_MALFORMED = 'InvalidParameterValue.Malformed'

# NAT网关的SNAT规则已经存在。
INVALIDPARAMETERVALUE_NATSNATRULEEXISTS = 'InvalidParameterValue.NatSnatRuleExists'

# 探测目的IP与同一个私有网络内的同一个子网下的其他网络探测的探测目的IP相同。
INVALIDPARAMETERVALUE_NETDETECTSAMEIP = 'InvalidParameterValue.NetDetectSameIp'

# 该操作仅对主网卡支持。
INVALIDPARAMETERVALUE_ONLYSUPPORTEDFORMASTERNETWORKCARD = 'InvalidParameterValue.OnlySupportedForMasterNetworkCard'

# 参数值不在指定范围。
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# 参数值是一个系统保留对象。
INVALIDPARAMETERVALUE_RESERVED = 'InvalidParameterValue.Reserved'

# 该资源不在此带宽包中。
INVALIDPARAMETERVALUE_RESOURCENOTEXISTED = 'InvalidParameterValue.ResourceNotExisted'

# 未查询到该资源。
INVALIDPARAMETERVALUE_RESOURCENOTFOUND = 'InvalidParameterValue.ResourceNotFound'

# 子网CIDR冲突。
INVALIDPARAMETERVALUE_SUBNETCONFLICT = 'InvalidParameterValue.SubnetConflict'

# 子网CIDR不合法。
INVALIDPARAMETERVALUE_SUBNETRANGE = 'InvalidParameterValue.SubnetRange'

# 该标签和值不存在。
INVALIDPARAMETERVALUE_TAGNOTEXISTED = 'InvalidParameterValue.TagNotExisted'

# 无效参数值。参数值太长。
INVALIDPARAMETERVALUE_TOOLONG = 'InvalidParameterValue.TooLong'

# 目的网段和当前VPC的CIDR冲突。
INVALIDPARAMETERVALUE_VPCCIDRCONFLICT = 'InvalidParameterValue.VpcCidrConflict'

# 当前功能不支持此专线网关。
INVALIDPARAMETERVALUE_VPGTYPENOTMATCH = 'InvalidParameterValue.VpgTypeNotMatch'

# 目的网段和当前VPN通道的CIDR冲突。
INVALIDPARAMETERVALUE_VPNCONNCIDRCONFLICT = 'InvalidParameterValue.VpnConnCidrConflict'

# VPN通道探测ip冲突。
INVALIDPARAMETERVALUE_VPNCONNHEALTHCHECKIPCONFLICT = 'InvalidParameterValue.VpnConnHealthCheckIpConflict'

# 参数Zone的值与CDC所在Zone冲突。
INVALIDPARAMETERVALUE_ZONECONFLICT = 'InvalidParameterValue.ZoneConflict'

# 指定弹性网卡的指定内网IP已经绑定了EIP，不能重复绑定。
INVALIDPRIVATEIPADDRESS_ALREADYBINDEIP = 'InvalidPrivateIpAddress.AlreadyBindEip'

# 无效的路由策略ID（RouteId）。
INVALIDROUTEID_NOTFOUND = 'InvalidRouteId.NotFound'

# 无效的路由表,路由表实例ID不合法。
INVALIDROUTETABLEID_MALFORMED = 'InvalidRouteTableId.Malformed'

# 无效的路由表,路由表资源不存在，请再次核实您输入的资源信息是否正确。
INVALIDROUTETABLEID_NOTFOUND = 'InvalidRouteTableId.NotFound'

# 无效的安全组,安全组实例ID不合法。
INVALIDSECURITYGROUPID_MALFORMED = 'InvalidSecurityGroupID.Malformed'

# 无效的安全组,安全组实例ID不存在。
INVALIDSECURITYGROUPID_NOTFOUND = 'InvalidSecurityGroupID.NotFound'

# 无效的VPC,VPC实例ID不合法。
INVALIDVPCID_MALFORMED = 'InvalidVpcId.Malformed'

# 无效的VPC,VPC资源不存在。
INVALIDVPCID_NOTFOUND = 'InvalidVpcId.NotFound'

# 无效的VPN网关,VPN实例ID不合法。
INVALIDVPNGATEWAYID_MALFORMED = 'InvalidVpnGatewayId.Malformed'

# 无效的VPN网关,VPN实例不存在，请再次核实您输入的资源信息是否正确。
INVALIDVPNGATEWAYID_NOTFOUND = 'InvalidVpnGatewayId.NotFound'

# 超过配额限制。
LIMITEXCEEDED = 'LimitExceeded'

# 分配IP地址数量达到上限。
LIMITEXCEEDED_ADDRESS = 'LimitExceeded.Address'

# 租户申请的弹性IP超过上限。
LIMITEXCEEDED_ADDRESSQUOTALIMITEXCEEDED = 'LimitExceeded.AddressQuotaLimitExceeded'

# VPC分配网段数量达到上限。
LIMITEXCEEDED_CIDRBLOCK = 'LimitExceeded.CidrBlock'

# 租户每天申请的弹性IP超过上限。
LIMITEXCEEDED_DAILYALLOCATEADDRESSQUOTALIMITEXCEEDED = 'LimitExceeded.DailyAllocateAddressQuotaLimitExceeded'

# 私有网络创建的NAT网关超过上限。
LIMITEXCEEDED_NATGATEWAYPERVPCLIMITEXCEEDED = 'LimitExceeded.NatGatewayPerVpcLimitExceeded'

# NAT网关绑定的弹性IP超过上限。
LIMITEXCEEDED_PUBLICIPADDRESSPERNATGATEWAYLIMITEXCEEDED = 'LimitExceeded.PublicIpAddressPerNatGatewayLimitExceeded'

# 安全组规则数量超过上限。
LIMITEXCEEDED_SECURITYGROUPPOLICYSET = 'LimitExceeded.SecurityGroupPolicySet'

# 子网分配子网段数量达到上限。
LIMITEXCEEDED_SUBNETCIDRBLOCK = 'LimitExceeded.SubnetCidrBlock'

# 缺少参数错误。
MISSINGPARAMETER = 'MissingParameter'

# 资源被占用。
RESOURCEINUSE = 'ResourceInUse'

# 指定IP地址已经在使用中。
RESOURCEINUSE_ADDRESS = 'ResourceInUse.Address'

# 资源不足。
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# 网段资源不足。
RESOURCEINSUFFICIENT_CIDRBLOCK = 'ResourceInsufficient.CidrBlock'

# 资源不存在。
RESOURCENOTFOUND = 'ResourceNotFound'

# 资源不可用。
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# 未授权操作。
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# 绑定关系不存在。
UNAUTHORIZEDOPERATION_ATTACHMENTNOTFOUND = 'UnauthorizedOperation.AttachmentNotFound'

# 账号未实名。
UNAUTHORIZEDOPERATION_NOREALNAMEAUTHENTICATION = 'UnauthorizedOperation.NoRealNameAuthentication'

# 主IP不支持指定操作。
UNAUTHORIZEDOPERATION_PRIMARYIP = 'UnauthorizedOperation.PrimaryIp'

# 未知参数错误。
UNKNOWNPARAMETER = 'UnknownParameter'

# 参数无法识别，可以尝试相似参数代替。
UNKNOWNPARAMETER_WITHGUESS = 'UnknownParameter.WithGuess'

# 操作不支持。
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# 接口不存在。
UNSUPPORTEDOPERATION_ACTIONNOTFOUND = 'UnsupportedOperation.ActionNotFound'

# 资源不在指定的AppId下。
UNSUPPORTEDOPERATION_APPIDMISMATCH = 'UnsupportedOperation.AppIdMismatch'

# 绑定关系已存在。
UNSUPPORTEDOPERATION_ATTACHMENTALREADYEXISTS = 'UnsupportedOperation.AttachmentAlreadyExists'

# 绑定关系不存在。
UNSUPPORTEDOPERATION_ATTACHMENTNOTFOUND = 'UnsupportedOperation.AttachmentNotFound'

# 当前云联网还有预付费带宽未到期，不支持主动删除。
UNSUPPORTEDOPERATION_BANDWIDTHNOTEXPIRED = 'UnsupportedOperation.BandwidthNotExpired'

# 已绑定EIP。
UNSUPPORTEDOPERATION_BINDEIP = 'UnsupportedOperation.BindEIP'

# 指定VPC CIDR范围不支持私有网络和基础网络设备互通。
UNSUPPORTEDOPERATION_CIDRUNSUPPORTEDCLASSICLINK = 'UnsupportedOperation.CIDRUnSupportedClassicLink'

# 实例已关联CCN。
UNSUPPORTEDOPERATION_CCNATTACHED = 'UnsupportedOperation.CcnAttached'

# 实例未关联CCN。
UNSUPPORTEDOPERATION_CCNNOTATTACHED = 'UnsupportedOperation.CcnNotAttached'

# 指定的路由表不存在。
UNSUPPORTEDOPERATION_CCNROUTETABLENOTEXIST = 'UnsupportedOperation.CcnRouteTableNotExist'

# CDC子网不支持创建非本地网关类型的路由。
UNSUPPORTEDOPERATION_CDCSUBNETNOTSUPPORTUNLOCALGATEWAY = 'UnsupportedOperation.CdcSubnetNotSupportUnLocalGateway'

# 实例已经和VPC绑定。
UNSUPPORTEDOPERATION_CLASSICINSTANCEIDALREADYEXISTS = 'UnsupportedOperation.ClassicInstanceIdAlreadyExists'

# 公网Clb不支持该规则。
UNSUPPORTEDOPERATION_CLBPOLICYLIMIT = 'UnsupportedOperation.ClbPolicyLimit'

# 与该VPC下的TKE容器的网段重叠。
UNSUPPORTEDOPERATION_CONFLICTWITHDOCKERROUTE = 'UnsupportedOperation.ConflictWithDockerRoute'

# 指定的VPC未发现专线网关。
UNSUPPORTEDOPERATION_DCGATEWAYSNOTFOUNDINVPC = 'UnsupportedOperation.DcGatewaysNotFoundInVpc'

# 专线网关正在更新BGP Community属性。
UNSUPPORTEDOPERATION_DIRECTCONNECTGATEWAYISUPDATINGCOMMUNITY = 'UnsupportedOperation.DirectConnectGatewayIsUpdatingCommunity'

# 指定的路由策略已发布至云联网，请先撤销。
UNSUPPORTEDOPERATION_DISABLEDNOTIFYCCN = 'UnsupportedOperation.DisabledNotifyCcn'

# 安全组规则重复。
UNSUPPORTEDOPERATION_DUPLICATEPOLICY = 'UnsupportedOperation.DuplicatePolicy'

# 不支持ECMP。
UNSUPPORTEDOPERATION_ECMP = 'UnsupportedOperation.Ecmp'

# 和云联网的路由形成ECMP。
UNSUPPORTEDOPERATION_ECMPWITHCCNROUTE = 'UnsupportedOperation.EcmpWithCcnRoute'

# 和用户自定义的路由形成ECMP。
UNSUPPORTEDOPERATION_ECMPWITHUSERROUTE = 'UnsupportedOperation.EcmpWithUserRoute'

# 用户配置的实例和路由表不匹配。
UNSUPPORTEDOPERATION_INSTANCEANDRTBNOTMATCH = 'UnsupportedOperation.InstanceAndRtbNotMatch'

# 账户余额不足。
UNSUPPORTEDOPERATION_INSUFFICIENTFUNDS = 'UnsupportedOperation.InsufficientFunds'

# 无效的实例状态。
UNSUPPORTEDOPERATION_INVALIDINSTANCESTATE = 'UnsupportedOperation.InvalidInstanceState'

# 资源状态不合法。
UNSUPPORTEDOPERATION_INVALIDSTATE = 'UnsupportedOperation.InvalidState'

# 关联当前云联网的实例的账号存在不是金融云账号。
UNSUPPORTEDOPERATION_ISNOTFINANCEACCOUNT = 'UnsupportedOperation.IsNotFinanceAccount'

# 指定的CDC已存在本地网关。
UNSUPPORTEDOPERATION_LOCALGATEWAYALREADYEXISTS = 'UnsupportedOperation.LocalGateWayAlreadyExists'

# 资源互斥操作任务正在执行。
UNSUPPORTEDOPERATION_MUTEXOPERATIONTASKRUNNING = 'UnsupportedOperation.MutexOperationTaskRunning'

# NAT网关类型不支持SNAT规则。
UNSUPPORTEDOPERATION_NATGATEWAYTYPENOTSUPPORTSNAT = 'UnsupportedOperation.NatGatewayTypeNotSupportSNAT'

# 指定的子网不支持创建本地网关类型的路由。
UNSUPPORTEDOPERATION_NORMALSUBNETNOTSUPPORTLOCALGATEWAY = 'UnsupportedOperation.NormalSubnetNotSupportLocalGateway'

# 当前云联网实例未处于申请中状态，无法进行操作。
UNSUPPORTEDOPERATION_NOTPENDINGCCNINSTANCE = 'UnsupportedOperation.NotPendingCcnInstance'

# 当前云联网为非后付费类型，无法进行此操作。
UNSUPPORTEDOPERATION_NOTPOSTPAIDCCNOPERATION = 'UnsupportedOperation.NotPostpaidCcnOperation'

# 指定的路由策略不支持发布或撤销至云联网。
UNSUPPORTEDOPERATION_NOTIFYCCN = 'UnsupportedOperation.NotifyCcn'

# 预付费云联网只支持地域间限速。
UNSUPPORTEDOPERATION_PREPAIDCCNONLYSUPPORTINTERREGIONLIMIT = 'UnsupportedOperation.PrepaidCcnOnlySupportInterRegionLimit'

# 指定的值是主IP。
UNSUPPORTEDOPERATION_PRIMARYIP = 'UnsupportedOperation.PrimaryIp'

# Nat网关至少存在一个弹性IP，弹性IP不能解绑。
UNSUPPORTEDOPERATION_PUBLICIPADDRESSDISASSOCIATE = 'UnsupportedOperation.PublicIpAddressDisassociate'

# 绑定NAT网关的弹性IP不是BGP性质的IP。
UNSUPPORTEDOPERATION_PUBLICIPADDRESSISNOTBGPIP = 'UnsupportedOperation.PublicIpAddressIsNotBGPIp'

# 绑定NAT网关的弹性IP不存在。
UNSUPPORTEDOPERATION_PUBLICIPADDRESSISNOTEXISTED = 'UnsupportedOperation.PublicIpAddressIsNotExisted'

# 绑定NAT网关的弹性IP不是按流量计费的。
UNSUPPORTEDOPERATION_PUBLICIPADDRESSNOTBILLEDBYTRAFFIC = 'UnsupportedOperation.PublicIpAddressNotBilledByTraffic'

# 输入的资源ID与IP绑定的资源不匹配，请检查。
UNSUPPORTEDOPERATION_RESOURCEMISMATCH = 'UnsupportedOperation.ResourceMismatch'

# 指定的终端节点服务所创建的终端节点不支持绑定安全组。
UNSUPPORTEDOPERATION_SPECIALENDPOINTSERVICE = 'UnsupportedOperation.SpecialEndPointService'

# 系统路由，禁止操作。
UNSUPPORTEDOPERATION_SYSTEMROUTE = 'UnsupportedOperation.SystemRoute'

# 账号ID不存在。
UNSUPPORTEDOPERATION_UINNOTFOUND = 'UnsupportedOperation.UinNotFound'

# 不支持跨境。
UNSUPPORTEDOPERATION_UNABLECROSSBORDER = 'UnsupportedOperation.UnableCrossBorder'

# 当前云联网无法关联金融云实例。
UNSUPPORTEDOPERATION_UNABLECROSSFINANCE = 'UnsupportedOperation.UnableCrossFinance'

# 未分配IPv6网段。
UNSUPPORTEDOPERATION_UNASSIGNCIDRBLOCK = 'UnsupportedOperation.UnassignCidrBlock'

# 未绑定EIP。
UNSUPPORTEDOPERATION_UNBINDEIP = 'UnsupportedOperation.UnbindEIP'

# 账户还有未支付订单，请先完成付款。
UNSUPPORTEDOPERATION_UNPAIDORDERALREADYEXISTS = 'UnsupportedOperation.UnpaidOrderAlreadyExists'

# 指定机型不支持弹性网卡。
UNSUPPORTEDOPERATION_UNSUPPORTEDINSTANCEFAMILY = 'UnsupportedOperation.UnsupportedInstanceFamily'

# 当前用户付费类型不支持创建所选付费类型的云联网。
UNSUPPORTEDOPERATION_USERANDCCNCHARGETYPENOTMATCH = 'UnsupportedOperation.UserAndCcnChargeTypeNotMatch'

# 指定安全组规则版本号和当前最新版本不一致。
UNSUPPORTEDOPERATION_VERSIONMISMATCH = 'UnsupportedOperation.VersionMismatch'

# 资源不属于同一个VPC。
UNSUPPORTEDOPERATION_VPCMISMATCH = 'UnsupportedOperation.VpcMismatch'

# 指定资源在不同的可用区。
UNSUPPORTEDOPERATION_ZONEMISMATCH = 'UnsupportedOperation.ZoneMismatch'

# 已经达到指定区域vpc资源申请数量上限。
VPCLIMITEXCEEDED = 'VpcLimitExceeded'
