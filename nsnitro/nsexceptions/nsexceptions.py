from collections import defaultdict


class NSNitroError(Exception):
    """ Custom exception class """
    def __init__(self, value, code=0):
        self.message = value
        self.code = code

    def __str__(self):
        return repr(self.message)


class NSNitroBaseErrors(NSNitroError):
    """
        Base exception class NSNitroBaseErrors
    """
    pass


class NSNitroNserrNotrunning(NSNitroBaseErrors):
    """
        Nitro error code 256
        NetScaler not running
    """
    pass


class NSNitroNserrPerm(NSNitroBaseErrors):
    """
        Nitro error code 257
        Operation not permitted
    """
    pass


class NSNitroNserrNoent(NSNitroBaseErrors):
    """
        Nitro error code 258
        No such resource
    """
    pass


class NSNitroNserrSrch(NSNitroBaseErrors):
    """
        Nitro error code 259
        No such process
    """
    pass


class NSNitroNserrIntr(NSNitroBaseErrors):
    """
        Nitro error code 260
        Interrupted system call
    """
    pass


class NSNitroNserrIo(NSNitroBaseErrors):
    """
        Nitro error code 261
        Input/output error
    """
    pass


class NSNitroNserrNxio(NSNitroBaseErrors):
    """
        Nitro error code 262
        Device not configured
    """
    pass


class NSNitroNserr2big(NSNitroBaseErrors):
    """
        Nitro error code 263
        Argument list too long
    """
    pass


class NSNitroNserrNoexec(NSNitroBaseErrors):
    """
        Nitro error code 264
        Exec format error
    """
    pass


class NSNitroNserrBadf(NSNitroBaseErrors):
    """
        Nitro error code 265
        Bad file descriptor
    """
    pass


class NSNitroNserrChild(NSNitroBaseErrors):
    """
        Nitro error code 266
        No child processes
    """
    pass


class NSNitroNserrDeadlk(NSNitroBaseErrors):
    """
        Nitro error code 267
        Resource deadlock avoided
    """
    pass


class NSNitroNserrNomem(NSNitroBaseErrors):
    """
        Nitro error code 268
        Cannot allocate memory
    """
    pass


class NSNitroNserrAcces(NSNitroBaseErrors):
    """
        Nitro error code 269
        Permission denied
    """
    pass


class NSNitroNserrFault(NSNitroBaseErrors):
    """
        Nitro error code 270
        Bad address
    """
    pass


class NSNitroNserrNotblk(NSNitroBaseErrors):
    """
        Nitro error code 271
        Block device required
    """
    pass


class NSNitroNserrBusy(NSNitroBaseErrors):
    """
        Nitro error code 272
        Device busy
    """
    pass


class NSNitroNserrExist(NSNitroBaseErrors):
    """
        Nitro error code 273
        Resource already exists
    """
    pass


class NSNitroNserrXdev(NSNitroBaseErrors):
    """
        Nitro error code 274
        Cross-device link
    """
    pass


class NSNitroNserrNodev(NSNitroBaseErrors):
    """
        Nitro error code 275
        Operation not supported by device
    """
    pass


class NSNitroNserrNotdir(NSNitroBaseErrors):
    """
        Nitro error code 276
        Not a directory
    """
    pass


class NSNitroNserrIsdir(NSNitroBaseErrors):
    """
        Nitro error code 277
        Is a directory
    """
    pass


class NSNitroNserrInval(NSNitroBaseErrors):
    """
        Nitro error code 278
        Invalid argument
    """
    pass


class NSNitroNserrNfile(NSNitroBaseErrors):
    """
        Nitro error code 279
        Too many open files in system
    """
    pass


class NSNitroNserrMfile(NSNitroBaseErrors):
    """
        Nitro error code 280
        Too many open files
    """
    pass


class NSNitroNserrNotty(NSNitroBaseErrors):
    """
        Nitro error code 281
        Inappropriate ioctl for device
    """
    pass


class NSNitroNserrTxtbsy(NSNitroBaseErrors):
    """
        Nitro error code 282
        Text file busy
    """
    pass


class NSNitroNserrFbig(NSNitroBaseErrors):
    """
        Nitro error code 283
        File too large
    """
    pass


class NSNitroNserrNospace(NSNitroBaseErrors):
    """
        Nitro error code 284
        No space left on device
    """
    pass


class NSNitroNserrSpipe(NSNitroBaseErrors):
    """
        Nitro error code 285
        Illegal seek
    """
    pass


class NSNitroNserrRofs(NSNitroBaseErrors):
    """
        Nitro error code 286
        Read-only file system
    """
    pass


class NSNitroNserrMlink(NSNitroBaseErrors):
    """
        Nitro error code 287
        Too many links
    """
    pass


class NSNitroNserrPipe(NSNitroBaseErrors):
    """
        Nitro error code 288
        Broken pipe
    """
    pass


class NSNitroNserrDom(NSNitroBaseErrors):
    """
        Nitro error code 289
        Numerical argument out of domain
    """
    pass


class NSNitroNserrRange(NSNitroBaseErrors):
    """
        Nitro error code 290
        Result too large
    """
    pass


class NSNitroNserrAgain(NSNitroBaseErrors):
    """
        Nitro error code 291
        Resource temporarily unavailable
    """
    pass


class NSNitroNserrInprogress(NSNitroBaseErrors):
    """
        Nitro error code 292
        Operation now in progress
    """
    pass


class NSNitroNserrAlready(NSNitroBaseErrors):
    """
        Nitro error code 293
        Operation already in progress
    """
    pass


class NSNitroNserrNotsock(NSNitroBaseErrors):
    """
        Nitro error code 294
        Socket operation on non-socket
    """
    pass


class NSNitroNserrDestaddrreq(NSNitroBaseErrors):
    """
        Nitro error code 295
        Destination address required
    """
    pass


class NSNitroNserrMsgsize(NSNitroBaseErrors):
    """
        Nitro error code 296
        Message too long
    """
    pass


class NSNitroNserrPrototype(NSNitroBaseErrors):
    """
        Nitro error code 297
        Protocol wrong type for socket
    """
    pass


class NSNitroNserrNoprotoopt(NSNitroBaseErrors):
    """
        Nitro error code 298
        Protocol not available
    """
    pass


class NSNitroNserrProtonosupport(NSNitroBaseErrors):
    """
        Nitro error code 299
        Protocol not supported
    """
    pass


class NSNitroNserrSocktnosupport(NSNitroBaseErrors):
    """
        Nitro error code 300
        Socket type not supported
    """
    pass


class NSNitroNserrOpnotsupp(NSNitroBaseErrors):
    """
        Nitro error code 301
        Operation not supported
    """
    pass


class NSNitroNserrPfnosupport(NSNitroBaseErrors):
    """
        Nitro error code 302
        Protocol family not supported
    """
    pass


class NSNitroNserrAfnosupport(NSNitroBaseErrors):
    """
        Nitro error code 303
        Address family not supported by protocol family
    """
    pass


class NSNitroNserrAddrinuse(NSNitroBaseErrors):
    """
        Nitro error code 304
        Address already in use
    """
    pass


class NSNitroNserrAddrnotavail(NSNitroBaseErrors):
    """
        Nitro error code 305
        Can't assign requested address
    """
    pass


class NSNitroNserrNetdown(NSNitroBaseErrors):
    """
        Nitro error code 306
        Network is down
    """
    pass


class NSNitroNserrNetunreach(NSNitroBaseErrors):
    """
        Nitro error code 307
        Network is unreachable
    """
    pass


class NSNitroNserrNetreset(NSNitroBaseErrors):
    """
        Nitro error code 308
        Network dropped connection on reset
    """
    pass


class NSNitroNserrConnaborted(NSNitroBaseErrors):
    """
        Nitro error code 309
        Software caused connection abort
    """
    pass


class NSNitroNserrConnreset(NSNitroBaseErrors):
    """
        Nitro error code 310
        Connection reset by peer
    """
    pass


class NSNitroNserrNobufs(NSNitroBaseErrors):
    """
        Nitro error code 311
        No buffer space available
    """
    pass


class NSNitroNserrIsconn(NSNitroBaseErrors):
    """
        Nitro error code 312
        Socket is already connected
    """
    pass


class NSNitroNserrNotconn(NSNitroBaseErrors):
    """
        Nitro error code 313
        Socket is not connected
    """
    pass


class NSNitroNserrShutdown(NSNitroBaseErrors):
    """
        Nitro error code 314
        Can't send after socket shutdown
    """
    pass


class NSNitroNserrToomanyrefs(NSNitroBaseErrors):
    """
        Nitro error code 315
        Resource in use
    """
    pass


class NSNitroNserrTimedout(NSNitroBaseErrors):
    """
        Nitro error code 316
        Operation timed out
    """
    pass


class NSNitroNserrConnrefused(NSNitroBaseErrors):
    """
        Nitro error code 317
        Connection refused
    """
    pass


class NSNitroNserrLoop(NSNitroBaseErrors):
    """
        Nitro error code 318
        Too many levels of symbolic links
    """
    pass


class NSNitroNserrNametoolong(NSNitroBaseErrors):
    """
        Nitro error code 319
        File name too long
    """
    pass


class NSNitroNserrHostdown(NSNitroBaseErrors):
    """
        Nitro error code 320
        Host is down
    """
    pass


class NSNitroNserrHostunreach(NSNitroBaseErrors):
    """
        Nitro error code 321
        No route to host
    """
    pass


class NSNitroNserrNotempty(NSNitroBaseErrors):
    """
        Nitro error code 322
        Directory not empty
    """
    pass


class NSNitroNserrProclim(NSNitroBaseErrors):
    """
        Nitro error code 323
        Too many processes
    """
    pass


class NSNitroNserrUsers(NSNitroBaseErrors):
    """
        Nitro error code 324
        Too many users
    """
    pass


class NSNitroNserrDquot(NSNitroBaseErrors):
    """
        Nitro error code 325
        Disc quota exceeded
    """
    pass


class NSNitroNserrStale(NSNitroBaseErrors):
    """
        Nitro error code 326
        Stale NFS file handle
    """
    pass


class NSNitroNserrRemote(NSNitroBaseErrors):
    """
        Nitro error code 327
        Too many levels of remote in path
    """
    pass


class NSNitroNserrBadrpc(NSNitroBaseErrors):
    """
        Nitro error code 328
        RPC struct is bad
    """
    pass


class NSNitroNserrRpcmismatch(NSNitroBaseErrors):
    """
        Nitro error code 329
        RPC version wrong
    """
    pass


class NSNitroNserrProgunavail(NSNitroBaseErrors):
    """
        Nitro error code 330
        RPC prog. not avail
    """
    pass


class NSNitroNserrProgmismatch(NSNitroBaseErrors):
    """
        Nitro error code 331
        Program version wrong
    """
    pass


class NSNitroNserrProcunavail(NSNitroBaseErrors):
    """
        Nitro error code 332
        Bad procedure for program
    """
    pass


class NSNitroNserrNolck(NSNitroBaseErrors):
    """
        Nitro error code 333
        No locks available
    """
    pass


class NSNitroNserrNosys(NSNitroBaseErrors):
    """
        Nitro error code 334
        System Call not supported; Possible Reason: NetScaler is not
        running
    """
    pass


class NSNitroNserrFtype(NSNitroBaseErrors):
    """
        Nitro error code 335
        Inappropriate file type or format
    """
    pass


class NSNitroNserrAuth(NSNitroBaseErrors):
    """
        Nitro error code 336
        Authentication error
    """
    pass


class NSNitroNserrNeedauth(NSNitroBaseErrors):
    """
        Nitro error code 337
        Need authenticator
    """
    pass


class NSNitroNserrWouldblock(NSNitroBaseErrors):
    """
        Nitro error code 338
        Operation would block
    """
    pass


class NSNitroNserrNocode(NSNitroBaseErrors):
    """
        Nitro error code 339
        Feature is not implemented
    """
    pass


class NSNitroNserrNotsuser(NSNitroBaseErrors):
    """
        Nitro error code 340
        Not super-user
    """
    pass


class NSNitroNserrBigdata(NSNitroBaseErrors):
    """
        Nitro error code 341
        Data size is too big
    """
    pass


class NSNitroNserrSmalldata(NSNitroBaseErrors):
    """
        Nitro error code 342
        Data size is too small
    """
    pass


class NSNitroNserrNomorent(NSNitroBaseErrors):
    """
        Nitro error code 343
        No more entry in table
    """
    pass


class NSNitroNserrNoservice(NSNitroBaseErrors):
    """
        Nitro error code 344
        No Service
    """
    pass


class NSNitroNserrOserror(NSNitroBaseErrors):
    """
        Nitro error code 345
        Operating system error
    """
    pass


class NSNitroNserrNonexpcmd(NSNitroBaseErrors):
    """
        Nitro error code 346
        Unexpected command
    """
    pass


class NSNitroNserrCmdpropfail(NSNitroBaseErrors):
    """
        Nitro error code 347
        Command propagation failed
    """
    pass


class NSNitroNserrToomanynodes(NSNitroBaseErrors):
    """
        Nitro error code 348
        Too many nodes
    """
    pass


class NSNitroNserrSecondaryfail(NSNitroBaseErrors):
    """
        Nitro error code 349
        Command failed on secondary node,  but succeeded on primary
        node. Configuration will be synchronized to ensure secondary and
        primary have same configuration.
    """
    pass


class NSNitroNserrInvalbackup(NSNitroBaseErrors):
    """
        Nitro error code 350
        Invalid backup vserver
    """
    pass


class NSNitroNserrNoserver(NSNitroBaseErrors):
    """
        Nitro error code 351
        No such server
    """
    pass


class NSNitroNserrLoginreqd(NSNitroBaseErrors):
    """
        Nitro error code 352
        Login is required
    """
    pass


class NSNitroNserrRpcinval(NSNitroBaseErrors):
    """
        Nitro error code 353
        RPC invalid argument
    """
    pass


class NSNitroNserrNouser(NSNitroBaseErrors):
    """
        Nitro error code 354
        Invalid username or password
    """
    pass


class NSNitroNserrInvalpasswd(NSNitroBaseErrors):
    """
        Nitro error code 355
        Invalid username or password
    """
    pass


class NSNitroNserrLicense(NSNitroBaseErrors):
    """
        Nitro error code 356
        Feature(s) not licensed
    """
    pass


class NSNitroNserrDeferred(NSNitroBaseErrors):
    """
        Nitro error code 357
        The command is stored for later execution
    """
    pass


class NSNitroNserrPropauthfail(NSNitroBaseErrors):
    """
        Nitro error code 358
        Command propagation failed due to user authentication problems
    """
    pass


class NSNitroNserrNodelsuser(NSNitroBaseErrors):
    """
        Nitro error code 359
        The superuser cannot be removed
    """
    pass


class NSNitroNserrNomodsuser(NSNitroBaseErrors):
    """
        Nitro error code 360
        Permissions for the superuser cannot be modified
    """
    pass


class NSNitroNserrInvalnodeid(NSNitroBaseErrors):
    """
        Nitro error code 362
        Invalid node ID specified
    """
    pass


class NSNitroNserrNotopha(NSNitroBaseErrors):
    """
        Nitro error code 363
        Operation not permitted on stand-alone node
    """
    pass


class NSNitroNserrNooppeerbad(NSNitroBaseErrors):
    """
        Nitro error code 364
        Operation not possible due to invalid peer state. Rectify and
        retry.
    """
    pass


class NSNitroNserrNoopbad(NSNitroBaseErrors):
    """
        Nitro error code 365
        Operation not possible as system state is invalid. Use show node
        for more information.
    """
    pass


class NSNitroNserrNopnow(NSNitroBaseErrors):
    """
        Nitro error code 366
        Operation not possible now. Please wait for system to stabilize
        before retrying.
    """
    pass


class NSNitroNserrNooppri(NSNitroBaseErrors):
    """
        Nitro error code 367
        Operation permitted only on secondary node.
    """
    pass


class NSNitroNserrNoopsec(NSNitroBaseErrors):
    """
        Nitro error code 368
        Operation permitted only on primary node.
    """
    pass


class NSNitroNserrRedirect(NSNitroBaseErrors):
    """
        Nitro error code 369
        Redirect request (VIP down)
    """
    pass


class NSNitroNserrBufoverflow(NSNitroBaseErrors):
    """
        Nitro error code 370
        Buffer overflow occurred
    """
    pass


class NSNitroNserrNouserpolicy(NSNitroBaseErrors):
    """
        Nitro error code 371
        No command policy defined,  permission denied
    """
    pass


class NSNitroNserrNosysgroup(NSNitroBaseErrors):
    """
        Nitro error code 372
        System group does not exist
    """
    pass


class NSNitroNserrNosyscmdpol(NSNitroBaseErrors):
    """
        Nitro error code 373
        System command policy does not exist
    """
    pass


class NSNitroNserrHaipv6pt(NSNitroBaseErrors):
    """
        Nitro error code 374
        IPV6 Feature cannot be disabled while HA is running over IPv6.
    """
    pass


class NSNitroNserrHansipv6(NSNitroBaseErrors):
    """
        Nitro error code 375
        IPv6 NSIP cannot be changed while HA is running over IPv6.
    """
    pass


class NSNitroNserrNsipv6active(NSNitroBaseErrors):
    """
        Nitro error code 376
        IPv6 NSIP is not in ACTIVE state,  rectify and retry.
    """
    pass


class NSNitroNserrRtmonStandalone(NSNitroBaseErrors):
    """
        Nitro error code 377
        Unbind all route monitors before making node standalone.
    """
    pass


class NSNitroNserrIpv6featDisabled(NSNitroBaseErrors):
    """
        Nitro error code 378
        IPv6 Feature Disabled
    """
    pass


class NSNitroNserrIprangenotallowd(NSNitroBaseErrors):
    """
        Nitro error code 394
        Range not allowed for wildcard IP
    """
    pass


class NSNitroNserrIvalidiprange(NSNitroBaseErrors):
    """
        Nitro error code 395
        Invalid range value
    """
    pass


class NSNitroNserrIprangemaxlimit(NSNitroBaseErrors):
    """
        Nitro error code 396
        Range value greater than maximum limit 254
    """
    pass


class NSNitroNserrIpNotExist(NSNitroBaseErrors):
    """
        Nitro error code 397
        IP does not exist
    """
    pass


class NSNitroNserrToomanyrules(NSNitroBaseErrors):
    """
        Nitro error code 398
        Maximum number of ACLs on the system has been exceeded
    """
    pass


class NSNitroNserrPasswdLenMin8(NSNitroBaseErrors):
    """
        Nitro error code 399
        Password too short - minimum length is 8 characters
    """
    pass


class NSNitroNserrSyncDisabled(NSNitroBaseErrors):
    """
        Nitro error code 410
        Synchronization disabled
    """
    pass


class NSNitroNserrNodeDisabled(NSNitroBaseErrors):
    """
        Nitro error code 411
        Node disabled
    """
    pass


class NSNitroNserrSyncProgress(NSNitroBaseErrors):
    """
        Nitro error code 412
        Synchronization is in progress
    """
    pass


class NSNitroNserrAdnsPerm(NSNitroBaseErrors):
    """
        Nitro error code 413
        Operation not permitted on ADNS service
    """
    pass


class NSNitroNserrNoincIpsamesubnet(NSNitroBaseErrors):
    """
        Nitro error code 414
        Peer IP should be on the NSIP subnet if INC mode is disabled
    """
    pass


class NSNitroNserrInvalidPeerip(NSNitroBaseErrors):
    """
        Nitro error code 415
        Not a valid peer IP
    """
    pass


class NSNitroNserrRedirect307(NSNitroBaseErrors):
    """
        Nitro error code 416
        Redirect request (send 307 temporary redirect
    """
    pass


class NSNitroNserrInvalhostname(NSNitroBaseErrors):
    """
        Nitro error code 417
        Invalid hostname
    """
    pass


class NSNitroNserrRewriteNotSupported(NSNitroBaseErrors):
    """
        Nitro error code 418
        Port rewrite not supported on this vserver type
    """
    pass


class NSNitroNserrIpchgDeny(NSNitroBaseErrors):
    """
        Nitro error code 419
        IP address change not permitted on this entity
    """
    pass


class NSNitroNserrIpchgGslb(NSNitroBaseErrors):
    """
        Nitro error code 420
        GSLB local service IP cannot be changed. Please change the
        corresponding vserver's IP
    """
    pass


class NSNitroNserrGslbIpchg(NSNitroBaseErrors):
    """
        Nitro error code 421
        corresponding GSLB service IP has also been changed.
    """
    pass


class NSNitroNserrNoauditsrvc(NSNitroBaseErrors):
    """
        Nitro error code 422
        No audit service running on the specified port
    """
    pass


class NSNitroNserrLacpkeyNotset(NSNitroBaseErrors):
    """
        Nitro error code 423
        LACP key not set
    """
    pass


class NSNitroNserrChannelInusebylacp(NSNitroBaseErrors):
    """
        Nitro error code 424
        Channel in use by LACP
    """
    pass


class NSNitroNserrLacpenabled(NSNitroBaseErrors):
    """
        Nitro error code 425
        LACP enabled interface cannot be bound manually to a channel
    """
    pass


class NSNitroNserrIfacemanuallybound(NSNitroBaseErrors):
    """
        Nitro error code 426
        LACP cannot be enabled,  interface manually bound to a channel
    """
    pass


class NSNitroNserrIntrecinuse(NSNitroBaseErrors):
    """
        Nitro error code 427
        Domain name for the reverse domain name already exists
    """
    pass


class NSNitroNserrIpportVipConflict(NSNitroBaseErrors):
    """
        Nitro error code 428
        IP,  port conflict with another entity bound to the same vserver
    """
    pass


class NSNitroNserrIpportVipBound(NSNitroBaseErrors):
    """
        Nitro error code 429
        IP,  port conflict with an entity already bound to the vserver
    """
    pass


class NSNitroNserrNoBackupVip(NSNitroBaseErrors):
    """
        Nitro error code 430
        No such backup vserver
    """
    pass


class NSNitroNserrReqSetArgs(NSNitroBaseErrors):
    """
        Nitro error code 431
        No arguments to set
    """
    pass


class NSNitroNserrSvcgrpMemberNameconflict(NSNitroBaseErrors):
    """
        Nitro error code 432
        Name conflicts with an existing service or service group member
        name
    """
    pass


class NSNitroNserrServerNameExist(NSNitroBaseErrors):
    """
        Nitro error code 433
        Server name already exists
    """
    pass


class NSNitroNserrMaxServiceBindingOnVserver(NSNitroBaseErrors):
    """
        Nitro error code 434
        Maximum services bound to vserver exceeded
    """
    pass


class NSNitroNserrMaxSvcEntityBindingOnSvcgroup(NSNitroBaseErrors):
    """
        Nitro error code 435
        Maximum services bound to service group exceeded
    """
    pass


class NSNitroNserrFsmall(NSNitroBaseErrors):
    """
        Nitro error code 436
        File too small
    """
    pass


class NSNitroNserrIntoflow(NSNitroBaseErrors):
    """
        Nitro error code 437
        Integer overflow
    """
    pass


class NSNitroNserrAsyncBlocked(NSNitroBaseErrors):
    """
        Nitro error code 438
        PI has blocked for body accumulation
    """
    pass


class NSNitroNserrSaclClearpending(NSNitroBaseErrors):
    """
        Nitro error code 439
        Clear in progress
    """
    pass


class NSNitroNserrSaclNameExists(NSNitroBaseErrors):
    """
        Nitro error code 440
        An ACL with the same name exists
    """
    pass


class NSNitroNserrSaclSupersetExists(NSNitroBaseErrors):
    """
        Nitro error code 441
        Operation not permitted. (An overlapping rule already exists)
    """
    pass


class NSNitroNserrSaclSubsetExists(NSNitroBaseErrors):
    """
        Nitro error code 442
        Operation not permitted. (A rule which is subset of this rule
        already exists)
    """
    pass


class NSNitroNserrNoincRoutemonitor(NSNitroBaseErrors):
    """
        Nitro error code 443
        Route monitors should be added only if INC mode is enabled
    """
    pass


class NSNitroNserrSessionExpired(NSNitroBaseErrors):
    """
        Nitro error code 444
        Session expired or killed. Please login again
    """
    pass


class NSNitroNserrSessionExceeded(NSNitroBaseErrors):
    """
        Nitro error code 445
        Session limit exceeded
    """
    pass


class NSNitroNserrCfeConnExceeded(NSNitroBaseErrors):
    """
        Nitro error code 446
        Connection limit to CFE exceeded
    """
    pass


class NSNitroNserrCfeConnPerSessExceeded(NSNitroBaseErrors):
    """
        Nitro error code 447
        Connection limit per session exceeded
    """
    pass


class NSNitroNserrCfeKillself(NSNitroBaseErrors):
    """
        Nitro error code 449
        Invalid session id. Current session cannot be killed
    """
    pass


class NSNitroNserrCfeIncompletesession(NSNitroBaseErrors):
    """
        Nitro error code 450
        Invalid session. Response/challenge is incomplete
    """
    pass


class NSNitroNserrCfeInvalidsession(NSNitroBaseErrors):
    """
        Nitro error code 451
        Invalid session. Please login again
    """
    pass


class NSNitroNserrCfeSessionNoexist(NSNitroBaseErrors):
    """
        Nitro error code 452
        Session does not exist
    """
    pass


class NSNitroNserrSysgroupUserExists(NSNitroBaseErrors):
    """
        Nitro error code 453
        User already bound to system group
    """
    pass


class NSNitroNserrSysgroupPolicyExists(NSNitroBaseErrors):
    """
        Nitro error code 454
        Policy already bound to system group
    """
    pass


class NSNitroNserrSleep(NSNitroBaseErrors):
    """
        Nitro error code 455
        Sleep process sleep
    """
    pass


class NSNitroNserrPpedie(NSNitroBaseErrors):
    """
        Nitro error code 456
        Your PPE is no more
    """
    pass


class NSNitroNserrNoconnCmdpropfail(NSNitroBaseErrors):
    """
        Nitro error code 457
        Unable to establish connection with the secondary. Command
        propagation failed
    """
    pass


class NSNitroNserrTimeoutSecondary(NSNitroBaseErrors):
    """
        Nitro error code 458
        There is no response from the secondary. Propagation timed out
    """
    pass


class NSNitroNserrRpcTimeout(NSNitroBaseErrors):
    """
        Nitro error code 459
        RPC timeout
    """
    pass


class NSNitroNserrNotSupported(NSNitroBaseErrors):
    """
        Nitro error code 460
        Feature not supported in this release
    """
    pass


class NSNitroNserrNoentVserver(NSNitroBaseErrors):
    """
        Nitro error code 461
        No such Vserver
    """
    pass


class NSNitroNserrNoentSvc(NSNitroBaseErrors):
    """
        Nitro error code 462
        No such service
    """
    pass


class NSNitroNserrNoentSvcSvcgrp(NSNitroBaseErrors):
    """
        Nitro error code 463
        No such service/serviceGroup
    """
    pass


class NSNitroNserrHaNov4Netmask(NSNitroBaseErrors):
    """
        Nitro error code 464
        IPv4 netmask is not required for IPv6
    """
    pass


class NSNitroNserrMaxVsevrverBindingsToService(NSNitroBaseErrors):
    """
        Nitro error code 465
        Maximum vservers bound to a service exceeded
    """
    pass


class NSNitroNserrSacl6Clearpending(NSNitroBaseErrors):
    """
        Nitro error code 466
        Simple ACL6 Clear in progress
    """
    pass


class NSNitroNserrSacl6NameExists(NSNitroBaseErrors):
    """
        Nitro error code 467
        Simple ACL6 with the same name exists
    """
    pass


class NSNitroNserrSacl6SupersetExists(NSNitroBaseErrors):
    """
        Nitro error code 468
        Operation not permitted. (An overlapping rule already exists)
    """
    pass


class NSNitroNserrSacl6SubsetExists(NSNitroBaseErrors):
    """
        Nitro error code 469
        Operation not permitted. (A rule which is subset of this rule
        already exists)
    """
    pass


class NSNitroNserrNoBackupVipBound(NSNitroBaseErrors):
    """
        Nitro error code 470
        No backupVserver bound
    """
    pass


class NSNitroNserrVserverTypeMismatch(NSNitroBaseErrors):
    """
        Nitro error code 471
        Vserver type mismatch.
    """
    pass


class NSNitroNserrSessionExpiredRedirect(NSNitroBaseErrors):
    """
        Nitro error code 472
        Session expired,  Please login again
    """
    pass


class NSNitroCaconfErrors(NSNitroError):
    """
        Base exception class NSNitroCaconfErrors
    """
    pass


class NSNitroNserrCaconfCnflHeurexpRelexp(NSNitroCaconfErrors):
    """
        Nitro error code 480
        Conflicting arguments,  heurExpiryParam and relExpiry
    """
    pass


class NSNitroNserrCaconfCnflHeurexpRelexpmili(NSNitroCaconfErrors):
    """
        Nitro error code 481
        Conflicting arguments,  heurExpiryParam and relExpiryMilliSec
    """
    pass


class NSNitroNserrCaconfCnflRelexpRelexpmili(NSNitroCaconfErrors):
    """
        Nitro error code 482
        Conflicting arguments,  relExpiry and relExpiryMiliSec
    """
    pass


class NSNitroNserrCaconfCnflAbsexpHeurexp(NSNitroCaconfErrors):
    """
        Nitro error code 483
        Conflicting arguments,  absExpiry and heurExpiryParam
    """
    pass


class NSNitroNserrCaconfCnflAbsexpRelexpmili(NSNitroCaconfErrors):
    """
        Nitro error code 484
        Conflicting arguments,  absExpiry and relExpiryMilliSec
    """
    pass


class NSNitroNserrCaconfCnflAbsexpgmtHeruexp(NSNitroCaconfErrors):
    """
        Nitro error code 485
        Conflicting arguments,  absExpiryGMT and heurExpiryParam
    """
    pass


class NSNitroNserrCaconfCnflAbsexpAbsexpgmt(NSNitroCaconfErrors):
    """
        Nitro error code 486
        Conflicting arguments,  absExpiry and absExpiryGMT
    """
    pass


class NSNitroNserrCaconfCnflAbsexpgmtRelexpmili(NSNitroCaconfErrors):
    """
        Nitro error code 487
        Conflicting arguments,  absExpiryGMT and relExpiryMilliSec
    """
    pass


class NSNitroNserrCaconfCnflHitparamsHitslctr(NSNitroCaconfErrors):
    """
        Nitro error code 488
        Conflicting arguments,  hitParams and hitSelector
    """
    pass


class NSNitroNserrCaconfCnflInvalparamsHitslctr(NSNitroCaconfErrors):
    """
        Nitro error code 489
        Conflicting arguments,  invalParams and hitSelector
    """
    pass


class NSNitroNserrCaconfCnflHitparamsInvlslctr(NSNitroCaconfErrors):
    """
        Nitro error code 490
        Conflicting arguments,  hitParams and invalSelector
    """
    pass


class NSNitroNserrCaconfCnflInvalparamsInvlslctr(NSNitroCaconfErrors):
    """
        Nitro error code 491
        Conflicting arguments,  invalParams and invalSelector
    """
    pass


class NSNitroNserrCaconfCnflHitslctrMatchcooky(NSNitroCaconfErrors):
    """
        Nitro error code 492
        Conflicting arguments,  hitSelector and matchCookies
    """
    pass


class NSNitroNserrCaconfCnflHitslctrInvalrest2host(NSNitroCaconfErrors):
    """
        Nitro error code 493
        Conflicting arguments,  hitSelector and invalRestrictedToHost
    """
    pass


class NSNitroNserrCaconfCnflHitslctrIgnrparamvalcase(NSNitroCaconfErrors):
    """
        Nitro error code 494
        Conflicting arguments,  hitSelector and ignoreParamValueCase
    """
    pass


class NSNitroNserrCaconfCnflInvalslctrMatchcooky(NSNitroCaconfErrors):
    """
        Nitro error code 495
        Conflicting arguments,  invalSelector and matchCookies
    """
    pass


class NSNitroNserrCaconfCnflInvalslctrInvalrest2host(NSNitroCaconfErrors):
    """
        Nitro error code 496
        Conflicting arguments,  invalSelector and invalRestrictedToHost
    """
    pass


class NSNitroNserrCaconfCnflInvalslctrIgnrparamvalcase(NSNitroCaconfErrors):
    """
        Nitro error code 497
        Conflicting arguments,  invalSelector and ignoreParamValueCase
    """
    pass


class NSNitroNserrCaconfCnflPosrelexpRelexp(NSNitroCaconfErrors):
    """
        Nitro error code 498
        Conflicting arguments,  weekPosRelExpiry and relExpiry
    """
    pass


class NSNitroNserrCaconfCnflPosrelexpRelexpmili(NSNitroCaconfErrors):
    """
        Nitro error code 499
        Conflicting arguments,  weekPosRelExpiry and relExpiryMiliSec
    """
    pass


class NSNitroNserrCaconfCnflAbsexpPosrelexp(NSNitroCaconfErrors):
    """
        Nitro error code 500
        Conflicting arguments,  absExpiry and weekPosRelExpiry
    """
    pass


class NSNitroNserrCaconfCnflAbsexpgmtPosrelexp(NSNitroCaconfErrors):
    """
        Nitro error code 501
        Conflicting arguments,  absExpiryGMT and weekPosRelExpiry
    """
    pass


class NSNitroNserrCaconfCnflIgnrparamvalcaseHitparams(NSNitroCaconfErrors):
    """
        Nitro error code 502
        Invalid arguments,  ignoreParamValueCase is set while hitParams
        is 0
    """
    pass


class NSNitroNserrCaconfCnflHitInvalparamsMatchcuky(NSNitroCaconfErrors):
    """
        Nitro error code 503
        Invalid arguments,  matchCookies is set while both hitParams and
        invalParams are 0
    """
    pass


class NSNitroNserrCaconfCnflInvalrest2hostInvalparam(NSNitroCaconfErrors):
    """
        Nitro error code 504
        Invalid arguments,  invalRestrictedToHost is set while
        invalParams is 0
    """
    pass


class NSNitroNserrCaconfCnflPrefetchPrefetchsec(NSNitroCaconfErrors):
    """
        Nitro error code 505
        Invalid arguments,  prefetchPeriod is set while prefetch is
        disabled
    """
    pass


class NSNitroNserrCaconfCnflPrefetchPrefetchmili(NSNitroCaconfErrors):
    """
        Nitro error code 506
        Invalid arguments,  prefetchPeriodMilliSec is set while prefetch
        is disabled
    """
    pass


class NSNitroNserrCaconfCnflPrefetchmiliPrefetchsec(NSNitroCaconfErrors):
    """
        Nitro error code 507
        Conflicting arguments,  prefetchPeriodMilliSec and
        prefetchPeriod
    """
    pass


class NSNitroNserrCaconfArgLeMinVal(NSNitroCaconfErrors):
    """
        Nitro error code 508
        Invalid arguments,  given value is less than the minimum value
    """
    pass


class NSNitroNserrCaconfArgGeMaxVal(NSNitroCaconfErrors):
    """
        Nitro error code 509
        Invalid arguments,  given value is more than the maximum value
    """
    pass


class NSNitroCrErrors(NSNitroError):
    """
        Base exception class NSNitroCrErrors
    """
    pass


class NSNitroNserrPxyCacheHmg(NSNitroCrErrors):
    """
        Nitro error code 512
        All caches in a content group should be of the same type
    """
    pass


class NSNitroNserrPxyRmLastMemt(NSNitroCrErrors):
    """
        Nitro error code 513
        Cannot remove last map entry from the table; remove the map
        table instead
    """
    pass


class NSNitroNserrCswInsInvalPfx(NSNitroCrErrors):
    """
        Nitro error code 514
        Invalid prefix specified in the URL
    """
    pass


class NSNitroNserrPengExprIvalName(NSNitroCrErrors):
    """
        Nitro error code 515
        Invalid expression name
    """
    pass


class NSNitroNserrCswBigUrl(NSNitroCrErrors):
    """
        Nitro error code 516
        URL specified is too long - maximum is 208,  including . and *
    """
    pass


class NSNitroNserrCswBigPfx(NSNitroCrErrors):
    """
        Nitro error code 517
        Prefix specified is too long - maximum is 199,  excluding *
    """
    pass


class NSNitroNserrCswBigSfx(NSNitroCrErrors):
    """
        Nitro error code 518
        Extension specified is too long,  maximum is 8
    """
    pass


class NSNitroNserrCswInvalSfx(NSNitroCrErrors):
    """
        Nitro error code 519
        Extension is invalid
    """
    pass


class NSNitroNserrExprNomethod(NSNitroCrErrors):
    """
        Nitro error code 520
        Invalid method name
    """
    pass


class NSNitroNserrExprNourltokens(NSNitroCrErrors):
    """
        Nitro error code 521
        Invalid HTTP URL tokens
    """
    pass


class NSNitroNserrExprNoversion(NSNitroCrErrors):
    """
        Nitro error code 522
        Invalid HTTP version
    """
    pass


class NSNitroNserrExprNohdr(NSNitroCrErrors):
    """
        Nitro error code 523
        Invalid HTTP header
    """
    pass


class NSNitroNserrExprNocacntl(NSNitroCrErrors):
    """
        Nitro error code 524
        Invalid cache-control value
    """
    pass


class NSNitroNserrExprNoprag(NSNitroCrErrors):
    """
        Nitro error code 525
        Invalid pragma value
    """
    pass


class NSNitroNserrExprNoquery(NSNitroCrErrors):
    """
        Nitro error code 526
        Invalid query string
    """
    pass


class NSNitroNserrExprNoqual(NSNitroCrErrors):
    """
        Nitro error code 527
        Invalid qualifier
    """
    pass


class NSNitroNserrActionInuse(NSNitroCrErrors):
    """
        Nitro error code 528
        Action name is already in use
    """
    pass


class NSNitroNserrActionHdrInval(NSNitroCrErrors):
    """
        Nitro error code 529
        Invalid header
    """
    pass


class NSNitroNserrUrlqInval(NSNitroCrErrors):
    """
        Nitro error code 530
        
    """
    pass


class NSNitroNserrUndefAction(NSNitroCrErrors):
    """
        Nitro error code 531
        Action directive or qualifier is not valid
    """
    pass


class NSNitroNserrCpeInuse(NSNitroCrErrors):
    """
        Nitro error code 532
        Policy name is already in use
    """
    pass


class NSNitroNserrCpeReqactInval(NSNitroCrErrors):
    """
        Nitro error code 533
        Request action is not valid
    """
    pass


class NSNitroNserrCpeRspactInval(NSNitroCrErrors):
    """
        Nitro error code 534
        Response action is not valid
    """
    pass


class NSNitroNserrCpeReqruleInval(NSNitroCrErrors):
    """
        Nitro error code 535
        Request rule is not valid
    """
    pass


class NSNitroNserrCpeRspruleInval(NSNitroCrErrors):
    """
        Nitro error code 536
        Response rule is not valid
    """
    pass


class NSNitroNserrActionDefinval(NSNitroCrErrors):
    """
        Nitro error code 537
        Default actions cannot be removed
    """
    pass


class NSNitroNserrActionNotpresent(NSNitroCrErrors):
    """
        Nitro error code 538
        Action does not exist
    """
    pass


class NSNitroNserrPxyInvalServicetype(NSNitroCrErrors):
    """
        Nitro error code 539
        Invalid service type for virtual server
    """
    pass


class NSNitroNserrCachepolicyInuse(NSNitroCrErrors):
    """
        Nitro error code 540
        Caching policy name is already in use
    """
    pass


class NSNitroNserrCachegroupInternal(NSNitroCrErrors):
    """
        Nitro error code 543
        Built-in content groups cannot be removed
    """
    pass


class NSNitroNserrCpeInval(NSNitroCrErrors):
    """
        Nitro error code 544
        Policy name is invalid
    """
    pass


class NSNitroNserrExprNolen(NSNitroCrErrors):
    """
        Nitro error code 545
        URL length is not valid
    """
    pass


class NSNitroNserrDnswait(NSNitroCrErrors):
    """
        Nitro error code 546
        
    """
    pass


class NSNitroNserrGwTimeout(NSNitroCrErrors):
    """
        Nitro error code 547
        
    """
    pass


class NSNitroNserrCswdmnInuse(NSNitroCrErrors):
    """
        Nitro error code 548
        Domain is already hosted by another server
    """
    pass


class NSNitroNserrCswdmnPlcyExist(NSNitroCrErrors):
    """
        Nitro error code 549
        
    """
    pass


class NSNitroNserrActionNomodHdr(NSNitroCrErrors):
    """
        Nitro error code 550
        Action has missing argument
    """
    pass


class NSNitroNserrExprInvalOperator(NSNitroCrErrors):
    """
        Nitro error code 551
        Invalid operator for the qualifier
    """
    pass


class NSNitroNserrExprDefRemInval(NSNitroCrErrors):
    """
        Nitro error code 552
        Default expression cannot be removed
    """
    pass


class NSNitroNserrExprToomany(NSNitroCrErrors):
    """
        Nitro error code 553
        Expression limit reached
    """
    pass


class NSNitroNserrActionToomany(NSNitroCrErrors):
    """
        Nitro error code 554
        Action limit reached
    """
    pass


class NSNitroNserrCswpolicyToomany(NSNitroCrErrors):
    """
        Nitro error code 555
        CS policy limit reached
    """
    pass


class NSNitroNserrCrdpolicyToomany(NSNitroCrErrors):
    """
        Nitro error code 556
        CR policy limit reached
    """
    pass


class NSNitroNserrMappolicyToomany(NSNitroCrErrors):
    """
        Nitro error code 557
        Map policy limit reached
    """
    pass


class NSNitroNserrFiltpolicyToomany(NSNitroCrErrors):
    """
        Nitro error code 558
        Filter policy limit reached
    """
    pass


class NSNitroNserrCachepolicyToomany(NSNitroCrErrors):
    """
        Nitro error code 559
        Integrated cache policy limit reached
    """
    pass


class NSNitroNserrCachegroupToomany(NSNitroCrErrors):
    """
        Nitro error code 560
        Integrated cache content group limit reached
    """
    pass


class NSNitroNserrCacheparamMemallocFailed(NSNitroCrErrors):
    """
        Nitro error code 561
        Unable to allocate specified amount of memory
    """
    pass


class NSNitroNserrCachegroupInuse(NSNitroCrErrors):
    """
        Nitro error code 562
        Content group name is already in use
    """
    pass


class NSNitroNserrCachegroupExpconflict(NSNitroCrErrors):
    """
        Nitro error code 563
        Expiry times conflict
    """
    pass


class NSNitroNserrCacheparamInval(NSNitroCrErrors):
    """
        Nitro error code 564
        Cache parameter is invalid
    """
    pass


class NSNitroNserrCachegroupParamInval(NSNitroCrErrors):
    """
        Nitro error code 565
        Invalid invalidation parameter
    """
    pass


class NSNitroNserrCachegroupQueryInval(NSNitroCrErrors):
    """
        Nitro error code 566
        Invalid query string
    """
    pass


class NSNitroNserrActionInval(NSNitroCrErrors):
    """
        Nitro error code 567
        Action name is invalid
    """
    pass


class NSNitroNserrExprDefSetInval(NSNitroCrErrors):
    """
        Nitro error code 568
        Default expression cannot be set
    """
    pass


class NSNitroNserrCachegroupResszMinGtMax(NSNitroCrErrors):
    """
        Nitro error code 569
        Minimum response size cannot exceed the maximum response size
    """
    pass


class NSNitroNserrFiltacionInvalrespcode(NSNitroCrErrors):
    """
        Nitro error code 570
        Invalid HTTP response code
    """
    pass


class NSNitroNserrCachegroupHostReq(NSNitroCrErrors):
    """
        Nitro error code 576
        Host required for a group with invalidation restricted to host
    """
    pass


class NSNitroNserrCachegroupHostNreq(NSNitroCrErrors):
    """
        Nitro error code 577
        Host not required
    """
    pass


class NSNitroNserrCachegroupDyngrpNexp(NSNitroCrErrors):
    """
        Nitro error code 578
        Cannot expire a parameterized content group
    """
    pass


class NSNitroNserrCachegroupOneGrpReq(NSNitroCrErrors):
    """
        Nitro error code 579
        Only one content group required
    """
    pass


class NSNitroNserrCachegroupOneAllReq(NSNitroCrErrors):
    """
        Nitro error code 580
        ALL should be the only content group specified
    """
    pass


class NSNitroNserrCachegroupMatchParamInval(NSNitroCrErrors):
    """
        Nitro error code 581
        Invalid request hit parameter
    """
    pass


class NSNitroNserrCachegroupDynResCache(NSNitroCrErrors):
    """
        Nitro error code 582
        Cannot specify a parameterized group with a response time CACHE
        action
    """
    pass


class NSNitroNserrExprInvalValue(NSNitroCrErrors):
    """
        Nitro error code 583
        Invalid expression value
    """
    pass


class NSNitroNserrCachegroupPrefetchConflict(NSNitroCrErrors):
    """
        Nitro error code 584
        Prefetch periods conflict
    """
    pass


class NSNitroNserrCachegroupPrefetchEnable(NSNitroCrErrors):
    """
        Nitro error code 585
        Enable prefetch to set prefetch period
    """
    pass


class NSNitroNserrCachegroupCchUnknown(NSNitroCrErrors):
    """
        Nitro error code 586
        Unknown cache-control header
    """
    pass


class NSNitroNserrCachegroupRelexpX10ms(NSNitroCrErrors):
    """
        Nitro error code 587
        Relative expiry milliseconds must be multiples of 10
    """
    pass


class NSNitroNserrCachegroupPrefetchX10ms(NSNitroCrErrors):
    """
        Nitro error code 588
        Prefetch period milliseconds must be multiples of 10
    """
    pass


class NSNitroNserrCachegroupStaticToDynamic(NSNitroCrErrors):
    """
        Nitro error code 589
         This content group cannot be made parameterized
    """
    pass


class NSNitroNserrPlcyDefRemInval(NSNitroCrErrors):
    """
        Nitro error code 591
        Default policy cannot be removed
    """
    pass


class NSNitroNserrCachegroupPrefetchRelNreq(NSNitroCrErrors):
    """
        Nitro error code 592
        Relative expiry and prefetch period should both be seconds or
        milliseconds
    """
    pass


class NSNitroNserrExprSetInvalFlowtype(NSNitroCrErrors):
    """
        Nitro error code 593
        Flow type cannot be changed
    """
    pass


class NSNitroNserrExprTooBig(NSNitroCrErrors):
    """
        Nitro error code 594
        Expression too long - maximum length is 1500,  in fully-
        qualified form
    """
    pass


class NSNitroNserrCpeInvalidIdrange(NSNitroCrErrors):
    """
        Nitro error code 595
        Priority should be between 0 and 64000 (inclusive)
    """
    pass


class NSNitroNserrExprTooBigExt(NSNitroCrErrors):
    """
        Nitro error code 596
        Expression too long - maximum length is 800,  in fully-qualified
        form
    """
    pass


class NSNitroNserrCachegroupMatchcookieDynReq(NSNitroCrErrors):
    """
        Nitro error code 597
        Match cookies argument allowed only with parameterized groups
    """
    pass


class NSNitroNserrCachegroupMatchcookieNreq(NSNitroCrErrors):
    """
        Nitro error code 598
        Cannot modify match cookies
    """
    pass


class NSNitroNserrCachefwpxyPresent(NSNitroCrErrors):
    """
        Nitro error code 599
        Forward proxy is already present
    """
    pass


class NSNitroNserrCachePrefetchReevalNreq(NSNitroCrErrors):
    """
        Nitro error code 600
        Cannot configure a content group to both prefetch and evaluate
        every miss
    """
    pass


class NSNitroNserrCachefwpxyToomany(NSNitroCrErrors):
    """
        Nitro error code 601
        Forward proxy limit reached
    """
    pass


class NSNitroNserrCachePetFcNreq(NSNitroCrErrors):
    """
        Nitro error code 602
        Cannot enable both 'Poll Every Time' and 'Flash Cache'
    """
    pass


class NSNitroNserrSaveconfigInProgress(NSNitroCrErrors):
    """
        Nitro error code 603
        Configuration is being saved,  please try again later
    """
    pass


class NSNitroNserrGwsubnetNotExist(NSNitroCrErrors):
    """
        Nitro error code 604
        The gateway is not directly reachable
    """
    pass


class NSNitroNserrGwReqSubnet(NSNitroCrErrors):
    """
        Nitro error code 605
        An existing route relies on the presence of this subnet
    """
    pass


class NSNitroNserrUrlpolNoPri(NSNitroCrErrors):
    """
        Nitro error code 606
        Priority cannot be specified for URL-based content switching
        policy
    """
    pass


class NSNitroNserrBadCrAttribs(NSNitroCrErrors):
    """
        Nitro error code 607
        Bad cache redirection VIP attributes given
    """
    pass


class NSNitroNserrMacNotSupported(NSNitroCrErrors):
    """
        Nitro error code 608
        MAC redirection not supported
    """
    pass


class NSNitroNserrPolicyNotSupported(NSNitroCrErrors):
    """
        Nitro error code 609
        Policy redirection not supported with NNTP
    """
    pass


class NSNitroNserrCacheabilityNotSupported(NSNitroCrErrors):
    """
        Nitro error code 610
        Cannot set cacheability on cache
    """
    pass


class NSNitroNserrHostRtNotAllowed(NSNitroCrErrors):
    """
        Nitro error code 611
        Host route advertisement not permitted for this IP
    """
    pass


class NSNitroNserrRoutingNotAllowed(NSNitroCrErrors):
    """
        Nitro error code 612
        Routing protocols can run only on SNIP's or NSIP
    """
    pass


class NSNitroNserrConfigNotsaved(NSNitroCrErrors):
    """
        Nitro error code 613
        Configuration is not saved
    """
    pass


class NSNitroNserrExprmismatch(NSNitroCrErrors):
    """
        Nitro error code 624
        
    """
    pass


class NSNitroNserrNoHost(NSNitroCrErrors):
    """
        Nitro error code 627
        No host header and default not set
    """
    pass


class NSNitroNserrNoDflt(NSNitroCrErrors):
    """
        Nitro error code 628
        Host header present,  no match,  and default not set
    """
    pass


class NSNitroNserrDfltdmnFirst(NSNitroCrErrors):
    """
        Nitro error code 629
        No default domain translation entry
    """
    pass


class NSNitroNserrPxyConfLoop(NSNitroCrErrors):
    """
        Nitro error code 630
        Source and target domains cannot be the same
    """
    pass


class NSNitroNserrPxyMeDup(NSNitroCrErrors):
    """
        Nitro error code 632
        Duplicate map entry
    """
    pass


class NSNitroNserrPxyIvalTgt(NSNitroCrErrors):
    """
        Nitro error code 633
        Target is invalid during map entry addition
    """
    pass


class NSNitroNserrConnected(NSNitroCrErrors):
    """
        Nitro error code 634
        Proxy connection established
    """
    pass


class NSNitroNserrAuthenticate(NSNitroCrErrors):
    """
        Nitro error code 635
        Authentication required
    """
    pass


class NSNitroNserrLargeDomain(NSNitroCrErrors):
    """
        Nitro error code 636
        Domain length overflow
    """
    pass


class NSNitroNserrPxyIvalUrl(NSNitroCrErrors):
    """
        Nitro error code 640
        Source/destination URL or the combination is not valid
    """
    pass


class NSNitroNserrPxyMeUse(NSNitroCrErrors):
    """
        Nitro error code 641
        Map entry is already in use
    """
    pass


class NSNitroNserrPxyMtType(NSNitroCrErrors):
    """
        Nitro error code 642
        Map entries in a table should be homogeneous
    """
    pass


class NSNitroNserrPxyMtUse(NSNitroCrErrors):
    """
        Nitro error code 643
        Map table is in use
    """
    pass


class NSNitroNserrPxyMbInval(NSNitroCrErrors):
    """
        Nitro error code 644
        Invalid map bind operation
    """
    pass


class NSNitroNserrPxyMbUse(NSNitroCrErrors):
    """
        Nitro error code 645
        You can bind only one table to a vserver
    """
    pass


class NSNitroNserrPxySetdcdn(NSNitroCrErrors):
    """
        Nitro error code 646
        Invalid DCDN configuration
    """
    pass


class NSNitroNserrPxySetdflt(NSNitroCrErrors):
    """
        Nitro error code 647
        Invalid default domain specification
    """
    pass


class NSNitroNserrPxyDfltNotset(NSNitroCrErrors):
    """
        Nitro error code 648
        Removing default without setting it
    """
    pass


class NSNitroNserrPxyFwdIval(NSNitroCrErrors):
    """
        Nitro error code 649
        Invalid FWD PXY map entry
    """
    pass


class NSNitroNserrPxyMtxProt(NSNitroCrErrors):
    """
        Nitro error code 656
        PXY and cache protocol should be the same
    """
    pass


class NSNitroNserrPxyMtxTra(NSNitroCrErrors):
    """
        Nitro error code 657
        Invalid cache type on service
    """
    pass


class NSNitroNserrPxyMtxFwd(NSNitroCrErrors):
    """
        Nitro error code 658
        Forward Pxy matrix
    """
    pass


class NSNitroNserrPxyMtxRev(NSNitroCrErrors):
    """
        Nitro error code 659
        Reverse Pxy Matrix
    """
    pass


class NSNitroNserrPxyAddTraNonhttp(NSNitroCrErrors):
    """
        Nitro error code 660
        transparent non-HTTP policy is invalid
    """
    pass


class NSNitroNserrPxyAddTraOther(NSNitroCrErrors):
    """
        Nitro error code 661
        transparent non-HTTP map/via should not be specified
    """
    pass


class NSNitroNserrPxyOptInval(NSNitroCrErrors):
    """
        Nitro error code 662
        ARP/ghost options invalid for REV/FWD proxy
    """
    pass


class NSNitroNserrPxyAddSvrOther(NSNitroCrErrors):
    """
        Nitro error code 663
        Simple content based no proxy attribs
    """
    pass


class NSNitroNserrPxyMbDup(NSNitroCrErrors):
    """
        Nitro error code 664
        Bind entry already exists
    """
    pass


class NSNitroNserrPxyDfltDup(NSNitroCrErrors):
    """
        Nitro error code 665
        Default already exists
    """
    pass


class NSNitroNserrSelInuse(NSNitroCrErrors):
    """
        Nitro error code 672
        Selector already exists
    """
    pass


class NSNitroNserrSelParseFailed(NSNitroCrErrors):
    """
        Nitro error code 673
        Error in selector expression syntax
    """
    pass


class NSNitroNserrNoselector(NSNitroCrErrors):
    """
        Nitro error code 674
        No such selector
    """
    pass


class NSNitroNserrSelToomany(NSNitroCrErrors):
    """
        Nitro error code 675
        Selector limit reached
    """
    pass


class NSNitroNserrCachegroupNoselparam(NSNitroCrErrors):
    """
        Nitro error code 677
        Cannot change param-based content group to selector-based (or
        vice-versa)
    """
    pass


class NSNitroNserrNocachegroup(NSNitroCrErrors):
    """
        Nitro error code 678
        Content group does not exist
    """
    pass


class NSNitroNserrNonreqSel(NSNitroCrErrors):
    """
        Nitro error code 679
        Selector expression is not request based
    """
    pass


class NSNitroNserrInvalarg(NSNitroCrErrors):
    """
        Nitro error code 680
        The action qualifier and the specified argument(s) do not match
    """
    pass


class NSNitroNserrNowildAllowed(NSNitroCrErrors):
    """
        Nitro error code 681
        Wildcard not allowed with BETWEEN operator
    """
    pass


class NSNitroNserrDateIncompat(NSNitroCrErrors):
    """
        Nitro error code 682
        Time arguments incompatible
    """
    pass


class NSNitroNserrTimedateInvalid(NSNitroCrErrors):
    """
        Nitro error code 683
        Date/time value invalid
    """
    pass


class NSNitroNserrContentgroupCookieReqParam(NSNitroCrErrors):
    """
        Nitro error code 684
        Hit parameters or inval parameters needed to enable cookie
        matching
    """
    pass


class NSNitroNserrContentgroupIgnorecaseReqHitparam(NSNitroCrErrors):
    """
        Nitro error code 685
        Hit parameters needed to enable case-insensitive param value
        matching
    """
    pass


class NSNitroNserrContentgroupInvalparamReq(NSNitroCrErrors):
    """
        Nitro error code 686
        Inval parameters needed to enable host-based invalidation
    """
    pass


class NSNitroNserrClisecExpTooLong(NSNitroCrErrors):
    """
        Nitro error code 687
        Client security expression too long
    """
    pass


class NSNitroNserrNonhttpCswBindHttpSslPolicy(NSNitroCrErrors):
    """
        Nitro error code 688
        HTTP/SSL protocol based policies can be bound only to HTTP/SSL
        CS vserver
    """
    pass


class NSNitroNserrNonhttpCswBindDomainPolicy(NSNitroCrErrors):
    """
        Nitro error code 689
        Domain based policies can be bound only to HTTP/SSL CS vserver
    """
    pass


class NSNitroNserrNonhttpCswBindUrlPolicy(NSNitroCrErrors):
    """
        Nitro error code 690
        URL based policies can be bound only to HTTP/SSL CS vserver
    """
    pass


class NSNitroNserrPolboundtoTooManyVsvrs(NSNitroCrErrors):
    """
        Nitro error code 691
        Domain cannot be set - policy bound to more than one vserver.
    """
    pass


class NSNitroNserrPiCswUrlDomain(NSNitroCrErrors):
    """
        Nitro error code 692
        Domain/URL options disallowed along with advanced expressions
    """
    pass


class NSNitroNserrPiToPeCsw(NSNitroCrErrors):
    """
        Nitro error code 693
        Advanced expressions based  policies cannot be bound to a
        classic CS vserver.
    """
    pass


class NSNitroNserrPeToPiCsw(NSNitroCrErrors):
    """
        Nitro error code 694
        Classic expression policies cannot be bound to a advanced CS
        vserver.
    """
    pass


class NSNitroNserrPriorityCompPiCsw(NSNitroCrErrors):
    """
        Nitro error code 695
        Priority is mandatory for advanced expressions.
    """
    pass


class NSNitroNserrPiTcpcsw(NSNitroCrErrors):
    """
        Nitro error code 696
        Advanced expressions can not be bound to non-HTTP CS Vserver.
    """
    pass


class NSNitroNserrPeGoto(NSNitroCrErrors):
    """
        Nitro error code 697
        Priority Jump expression cannot be bound with a classic
        expression based policy.
    """
    pass


class NSNitroNserrPiToPePolCsw(NSNitroCrErrors):
    """
        Nitro error code 698
        Advanced expression based policy cannot be converted to a
        classic expression based policy and vice versa.
    """
    pass


class NSNitroNserrCacheobjectEvict(NSNitroCrErrors):
    """
        Nitro error code 699
        Cached object removed on expiry.
    """
    pass


class NSNitroNserrDnsfail(NSNitroCrErrors):
    """
        Nitro error code 700
        DNS request failed
    """
    pass


class NSNitroNserrHcRetTypeChange(NSNitroCrErrors):
    """
        Nitro error code 701
        Cannot change http callout return type.
    """
    pass


class NSNitroNserrHcNotHttpVs(NSNitroCrErrors):
    """
        Nitro error code 702
        Not a HTTP vserver.
    """
    pass


class NSNitroNserrHcReqConfigXor(NSNitroCrErrors):
    """
        Nitro error code 703
        Full request expression and other request attributes cannot be
        set at the same time.
    """
    pass


class NSNitroNserrHcServiceConfigXor(NSNitroCrErrors):
    """
        Nitro error code 704
         and vserver cannot be set at the same time.
    """
    pass


class NSNitroNserrHcRetTypeReqd(NSNitroCrErrors):
    """
        Nitro error code 705
        Return type needs to be configured first.
    """
    pass


class NSNitroNserrRtspCswBindIpPolicy(NSNitroCrErrors):
    """
        Nitro error code 706
        Only IP based policies can be bound to RTSP CS vserver
    """
    pass


class NSNitroNserrCswBindIncompatTgt(NSNitroCrErrors):
    """
        Nitro error code 707
        The target vserver is not compatible with the cs verver.
    """
    pass


class NSNitroNserrAsBadXmlnamespacePrefix(NSNitroCrErrors):
    """
        Nitro error code 708
        Invalid XML-Namespace prefix.
    """
    pass


class NSNitroNserrInvalidSipExpr(NSNitroCrErrors):
    """
        Nitro error code 709
        The SourceIP Expression specified is invalid.
    """
    pass


class NSNitroNserrNoBackendvserver(NSNitroCrErrors):
    """
        Nitro error code 710
        No backend LB vserver found.
    """
    pass


class NSNitroNserrContentGroupToomany(NSNitroCrErrors):
    """
        Nitro error code 711
        ContentGroup limit reached
    """
    pass


class NSNitroNserrCacheMemSizeChanged(NSNitroCrErrors):
    """
        Nitro error code 712
        To use new Integrated Cache memory limit,  save the
        configuration and restart the NetScalar.
    """
    pass


class NSNitroNserrCacheMemSizeZero(NSNitroCrErrors):
    """
        Nitro error code 713
        No memory limit is configured for Integrated Cache. Use set
        cache parameter command to set the memory limit.
    """
    pass


class NSNitroNserrL2connNotAllowed(NSNitroCrErrors):
    """
        Nitro error code 714
        l2conn feature is supported only for ncore.
    """
    pass


class NSNitroNserrSqlNotAllowed(NSNitroCrErrors):
    """
        Nitro error code 715
        Database feature is supported only on nCore
    """
    pass


class NSNitroNserrIpsecNotAllowed(NSNitroCrErrors):
    """
        Nitro error code 716
        IPSec feature is not supported
    """
    pass


class NSNitroNserrCswBindIncompatBkup(NSNitroCrErrors):
    """
        Nitro error code 717
        The backup vserver of the target vserver is not compatible with
        the CS vserver.
    """
    pass


class NSNitro0x300Errors(NSNitroError):
    """
        Base exception class NSNitro0x300Errors
    """
    pass


class NSNitroNserrRnatInv(NSNitro0x300Errors):
    """
        Nitro error code 769
        Reverse NAT not applicable for default route.
    """
    pass


class NSNitroNserrInvalidIf(NSNitro0x300Errors):
    """
        Nitro error code 770
        Invalid interface name/number.
    """
    pass


class NSNitroNserrMgrlimitReached(NSNitro0x300Errors):
    """
        Nitro error code 771
        Maximum manager limit reached.
    """
    pass


class NSNitroNserrSpInvaldTable(NSNitro0x300Errors):
    """
        Nitro error code 772
        SP table entries should be in increasing order.
    """
    pass


class NSNitroNserrRnatNatipExists(NSNitro0x300Errors):
    """
        Nitro error code 773
        RNAT to the target network with specified NAT IP already exists.
    """
    pass


class NSNitroNserrRnatExists(NSNitro0x300Errors):
    """
        Nitro error code 774
        RNAT to the target network already exists.
    """
    pass


class NSNitroNserrRnatNotExists(NSNitro0x300Errors):
    """
        Nitro error code 775
        RNAT to the target network does not exist.
    """
    pass


class NSNitroNserrRnatNatipNotExists(NSNitro0x300Errors):
    """
        Nitro error code 776
        RNAT to the target network with specified NAT IP doesn't exist.
    """
    pass


class NSNitroNserrRnatInvalidNatip(NSNitro0x300Errors):
    """
        Nitro error code 777
        NAT IP is not valid.
    """
    pass


class NSNitroNserrArpDisabled(NSNitro0x300Errors):
    """
        Nitro error code 784
        IP has arp disabled.
    """
    pass


class NSNitroNserrArpSecNotOwnedip(NSNitro0x300Errors):
    """
        Nitro error code 785
        Secondary can not arp for this IP.
    """
    pass


class NSNitroNserrCpeRuleInval(NSNitro0x300Errors):
    """
        Nitro error code 786
        Invalid rule.
    """
    pass


class NSNitroNserrInvalFlowtype(NSNitro0x300Errors):
    """
        Nitro error code 787
        Only authorization,  audit,  VPN session and traffic policies
        can be bound to aaa user or group.
    """
    pass


class NSNitroNserrInvalPolicyType(NSNitro0x300Errors):
    """
        Nitro error code 788
        Response rule is invalid in an authorization policy.
    """
    pass


class NSNitroNserrCpeRuleActionInval(NSNitro0x300Errors):
    """
        Nitro error code 789
        Request action is valid only for request rule.
    """
    pass


class NSNitroNserrCpeDefSetInval(NSNitro0x300Errors):
    """
        Nitro error code 790
        Default policy cannot be set.
    """
    pass


class NSNitroNserrInvalForcecleanup(NSNitro0x300Errors):
    """
        Nitro error code 791
        Invalid forcecleanup value.
    """
    pass


class NSNitroNserrInvalAaaGroup(NSNitro0x300Errors):
    """
        Nitro error code 792
        Invalid authorizationgroup value.
    """
    pass


class NSNitroNserrInvalProxy(NSNitro0x300Errors):
    """
        Nitro error code 793
        Invalid allprotocolproxy value.
    """
    pass


class NSNitroNserrInvalHtttpproxy(NSNitro0x300Errors):
    """
        Nitro error code 800
        Invalid HTTP proxy value.
    """
    pass


class NSNitroNserrInvalFtpproxy(NSNitro0x300Errors):
    """
        Nitro error code 801
        Invalid FTP proxy value.
    """
    pass


class NSNitroNserrInvalSockproxy(NSNitro0x300Errors):
    """
        Nitro error code 802
        Invalid SOCKS proxy value.
    """
    pass


class NSNitroNserrInvalGopherproxy(NSNitro0x300Errors):
    """
        Nitro error code 803
        Invalid GOPHER proxy value.
    """
    pass


class NSNitroNserrInvalSslproxy(NSNitro0x300Errors):
    """
        Nitro error code 804
        Invalid SSL proxy value.
    """
    pass


class NSNitroNserrInvalAaagrpMax(NSNitro0x300Errors):
    """
        Nitro error code 805
        Max 5 groups can be specified in authorizationgroup.
    """
    pass


class NSNitroNserrInvalMaxPortNum(NSNitro0x300Errors):
    """
        Nitro error code 806
        Maximum 16 ports can be specified in httpport.
    """
    pass


class NSNitroNserrInvalHttpport(NSNitro0x300Errors):
    """
        Nitro error code 807
        Invalid port.
    """
    pass


class NSNitroNserrInvalVpnvsererPoltype(NSNitro0x300Errors):
    """
        Nitro error code 808
        Only authentication and traffic policies can be bound to a VPN
        vserver.
    """
    pass


class NSNitroNserrInvalVpnglobalPoltype(NSNitro0x300Errors):
    """
        Nitro error code 809
        Only authentication and traffic policies can be bound to VPN
        global.
    """
    pass


class NSNitroNserrCpeRemInuse(NSNitro0x300Errors):
    """
        Nitro error code 810
        Bound policy cannot be removed.
    """
    pass


class NSNitroNserrProxyConflict(NSNitro0x300Errors):
    """
        Nitro error code 811
        Proxy server for all protocols already configured.
    """
    pass


class NSNitroNserrProxyInval(NSNitro0x300Errors):
    """
        Nitro error code 812
        Domain names allowed only if proxy type is browser
    """
    pass


class NSNitroNserrPxyexcptInval(NSNitro0x300Errors):
    """
        Nitro error code 813
        Proxy exception allowed only if proxy type is browser
    """
    pass


class NSNitroNserrCpePoltypeNoCse(NSNitro0x300Errors):
    """
        Nitro error code 814
        Policy type does not support client security expressions in rule
    """
    pass


class NSNitroNserrSessactCseIncompatible(NSNitro0x300Errors):
    """
        Nitro error code 815
        Session action and rule are incompatible
    """
    pass


class NSNitroNserrNomemCse(NSNitro0x300Errors):
    """
        Nitro error code 816
        Not enough memory while adding client security expressions
    """
    pass


class NSNitroNserrIncompatFsRule(NSNitro0x300Errors):
    """
        Nitro error code 817
        File system expressions supported in authorization policy only
    """
    pass


class NSNitroNserrIncompatFsMix(NSNitro0x300Errors):
    """
        Nitro error code 818
        Incompatible expressions mixed with file system expressions in
        rule
    """
    pass


class NSNitroNserrDrEnable(NSNitro0x300Errors):
    """
        Nitro error code 819
        Dynamic routing can be enabled on only one IP per subnet
    """
    pass


class NSNitroNserrMaxDistance(NSNitro0x300Errors):
    """
        Nitro error code 820
        Only null interface routes can have distance equal to 255
    """
    pass


class NSNitroNserrNullRouteDistance(NSNitro0x300Errors):
    """
        Nitro error code 821
        It is not possible to set the administrative distance/cost
        metric for a null interface route
    """
    pass


class NSNitroNserrBadActionTcpProfileType(NSNitro0x300Errors):
    """
        Nitro error code 822
        TCP profile cannot be set to this service type
    """
    pass


class NSNitroNserrBadActionHttpProfileType(NSNitro0x300Errors):
    """
        Nitro error code 823
        HTTP profile cannot be set to this service type
    """
    pass


class NSNitroNserrSpInvalidThreshold(NSNitro0x300Errors):
    """
        Nitro error code 824
        Invalid base threshold value
    """
    pass


class NSNitroNserrVipRouteExists(NSNitro0x300Errors):
    """
        Nitro error code 825
        VIP exists for this host route
    """
    pass


class NSNitroAclErrors(NSNitroError):
    """
        Base exception class NSNitroAclErrors
    """
    pass


class NSNitroNserrAclNotExists(NSNitroAclErrors):
    """
        Nitro error code 864
        ACL rule does not exist
    """
    pass


class NSNitroNserrAclExists(NSNitroAclErrors):
    """
        Nitro error code 865
        IP address has existing ACL rule
    """
    pass


class NSNitroNserrAclpipWosrcdst(NSNitroAclErrors):
    """
        Nitro error code 866
        Peer IP can't be given without src/dst flag
    """
    pass


class NSNitroNserrAclSameipPip(NSNitroAclErrors):
    """
        Nitro error code 867
        IP address and peer IP can't be same
    """
    pass


class NSNitroNserrAclInvalPeerip(NSNitroAclErrors):
    """
        Nitro error code 868
        Invalid peer IP
    """
    pass


class NSNitroNserrAclIppipExists(NSNitroAclErrors):
    """
        Nitro error code 869
        ACL with identical parameter specification already exists
    """
    pass


class NSNitroNserrXacldelerror(NSNitroAclErrors):
    """
        Nitro error code 870
        ACL has already been removed
    """
    pass


class NSNitroNserrXacladderror(NSNitroAclErrors):
    """
        Nitro error code 871
        Port can be specified only if protocol is TCP (6) or UDP (17)
    """
    pass


class NSNitroNserrXaclPriorityExists(NSNitroAclErrors):
    """
        Nitro error code 872
        ACL with this priority already exists
    """
    pass


class NSNitroNserrXaclIcmpReqd(NSNitroAclErrors):
    """
        Nitro error code 873
        ICMP type / code can be specified only if protocol is ICMP(1)
    """
    pass


class NSNitroNserrNoloopback(NSNitroAclErrors):
    """
        Nitro error code 874
        ACL cannot be configured on the loopback interface
    """
    pass


class NSNitroNserrInvicmptype(NSNitroAclErrors):
    """
        Nitro error code 875
        Invalid ICMP type
    """
    pass


class NSNitroNserrInvicmpcode(NSNitroAclErrors):
    """
        Nitro error code 876
        Invalid ICMP code
    """
    pass


class NSNitroNserrXaclrnatdel(NSNitroAclErrors):
    """
        Nitro error code 877
        ACL is bounded to RNAT, cannot be removed
    """
    pass


class NSNitroNserrXaclmodcfginfo(NSNitroAclErrors):
    """
        Nitro error code 880
        ACL modified,  apply ACLs to activate change
    """
    pass


class NSNitroAcl6Errors(NSNitroError):
    """
        Base exception class NSNitroAcl6Errors
    """
    pass


class NSNitroNserrAcl6IppipExists(NSNitroAcl6Errors):
    """
        Nitro error code 896
        ACL6 with identical parameter specification already exists
    """
    pass


class NSNitroNserrAcl6Delerror(NSNitroAcl6Errors):
    """
        Nitro error code 897
        ACL6 has already been removed
    """
    pass


class NSNitroNserrAcl6Adderror(NSNitroAcl6Errors):
    """
        Nitro error code 898
        Port can be specified only if protocol is TCP (6) or UDP (17)
    """
    pass


class NSNitroNserrAcl6PriorityExists(NSNitroAcl6Errors):
    """
        Nitro error code 899
        ACL6 with this priority already exists
    """
    pass


class NSNitroNserrAcl6IcmpReqd(NSNitroAcl6Errors):
    """
        Nitro error code 900
        ICMPv6 type/code can be specified only if protocol is ICMPv6
        (58)
    """
    pass


class NSNitroNserrAcl6Unspecaddr(NSNitroAcl6Errors):
    """
        Nitro error code 901
        unspecified address (::) can not be configured in ACL6
    """
    pass


class NSNitroNserrAcl6Modcfginfo(NSNitroAcl6Errors):
    """
        Nitro error code 902
        ACL6 modified,  apply ACLs6 to activate change
    """
    pass


class NSNitroNserrAcl6Prefixlen(NSNitroAcl6Errors):
    """
        Nitro error code 903
        Prefix length should not be configured in ACL6. (Use range
        instead)
    """
    pass


class NSNitroPbrErrors(NSNitroError):
    """
        Base exception class NSNitroPbrErrors
    """
    pass


class NSNitroNserrPbrNexthopNotdirect(NSNitroPbrErrors):
    """
        Nitro error code 912
        PBR Nexthop should be direct
    """
    pass


class NSNitroNserrPbrNoloopback(NSNitroPbrErrors):
    """
        Nitro error code 913
        PBR cannot be configured on the loopback interface
    """
    pass


class NSNitroNserrPbrdelerror(NSNitroPbrErrors):
    """
        Nitro error code 914
        This PBR has already been removed
    """
    pass


class NSNitroNserrPbrIppipExists(NSNitroPbrErrors):
    """
        Nitro error code 915
        PBR with identical parameter specification already exists
    """
    pass


class NSNitroNserrPbrPriorityExists(NSNitroPbrErrors):
    """
        Nitro error code 916
        PBR with this priority already exists
    """
    pass


class NSNitroNserrPbrmodcfginfo(NSNitroPbrErrors):
    """
        Nitro error code 918
        PBR modified,  use 'apply pbrs' to commit this operation
    """
    pass


class NSNitroNserrPbrNexthopReqd(NSNitroPbrErrors):
    """
        Nitro error code 919
        PBR Nexthop is required
    """
    pass


class NSNitroNserrPbrL2ConfigInfo(NSNitroPbrErrors):
    """
        Nitro error code 920
        L2 based PBRs work only for routed traffic
    """
    pass


class NSNitroNserrPbrmodcfgL2Info(NSNitroPbrErrors):
    """
        Nitro error code 921
        L2 based PBRs work only for routed traffic: PBR modified,  use
        'apply pbrs' to commit this operation
    """
    pass


class NSNitroNserrPbrNoMonitorGateway(NSNitroPbrErrors):
    """
        Nitro error code 922
        Monitor can't be configured when nexthop is configured as
        gateway name
    """
    pass


class NSNitroNserrPbrInvalidIporgateway(NSNitroPbrErrors):
    """
        Nitro error code 923
        Invalid Nexthop IPaddress/Gateway name
    """
    pass


class NSNitroNserrPbrMaxRuleExceeded(NSNitroPbrErrors):
    """
        Nitro error code 924
        Number of PBRs on the system exceeds Maximum
    """
    pass


class NSNitroCliErrors(NSNitroError):
    """
        Base exception class NSNitroCliErrors
    """
    pass


class NSNitroNserrTcpconnfail(NSNitroCliErrors):
    """
        Nitro error code 1024
        Connection failed
    """
    pass


class NSNitroNserrLoginfail(NSNitroCliErrors):
    """
        Nitro error code 1025
        Login failed
    """
    pass


class NSNitroNserrNologin(NSNitroCliErrors):
    """
        Nitro error code 1026
        Not logged in
    """
    pass


class NSNitroNserrAuthtimeout(NSNitroCliErrors):
    """
        Nitro error code 1027
        Not logged in or connection timed out
    """
    pass


class NSNitroNserrNotPrimary(NSNitroCliErrors):
    """
        Nitro error code 1028
        You are connected to a secondary node; configuration changes
        made in this session will not be propagated to,  or saved on,
        other nodes
    """
    pass


class NSNitroNserrRemoteop(NSNitroCliErrors):
    """
        Nitro error code 1029
        Operation cannot be performed from remote login
    """
    pass


class NSNitroNserrConnlost(NSNitroCliErrors):
    """
        Nitro error code 1030
        Connection with NetScaler lost
    """
    pass


class NSNitroNserrRpcdatamismatch(NSNitroCliErrors):
    """
        Nitro error code 1031
        Communication error (RPC data-size mismatch)
    """
    pass


class NSNitroNserrRpcbadreply(NSNitroCliErrors):
    """
        Nitro error code 1032
        Communication error (bad RPC reply)
    """
    pass


class NSNitroNserrUnabletoprompt(NSNitroCliErrors):
    """
        Nitro error code 1033
        Unable to display secondary prompt
    """
    pass


class NSNitroNserrUserabort(NSNitroCliErrors):
    """
        Nitro error code 1040
        User requested abort
    """
    pass


class NSNitroNserrEof(NSNitroCliErrors):
    """
        Nitro error code 1041
        EOF
    """
    pass


class NSNitroNserrInterrupt(NSNitroCliErrors):
    """
        Nitro error code 1042
        Interrupted
    """
    pass


class NSNitroNserrInternal(NSNitroCliErrors):
    """
        Nitro error code 1043
        Internal error
    """
    pass


class NSNitroNserrStrmaxlen255(NSNitroCliErrors):
    """
        Nitro error code 1048
        String length exceeds maximum. Allowed maximum length is 255
        bytes.
    """
    pass


class NSNitroNserrStrmaxlen32(NSNitroCliErrors):
    """
        Nitro error code 1049
        String length exceeds maximum. Allowed maximum length is 32.
    """
    pass


class NSNitroNserrNoresponse(NSNitroCliErrors):
    """
        Nitro error code 1056
        No response from NetScaler
    """
    pass


class NSNitroNserrIoerror(NSNitroCliErrors):
    """
        Nitro error code 1057
        I/O error
    """
    pass


class NSNitroNserrEnv(NSNitroCliErrors):
    """
        Nitro error code 1058
        Environment error
    """
    pass


class NSNitroNserrCmdsfailed(NSNitroCliErrors):
    """
        Nitro error code 1059
        Some commands failed
    """
    pass


class NSNitroNserrAllcmdsfailed(NSNitroCliErrors):
    """
        Nitro error code 1060
        All commands failed
    """
    pass


class NSNitroNserrInvalidTcpOptionType(NSNitroCliErrors):
    """
        Nitro error code 1061
        Invalid tcp option type value. Allowed type values are 0 to 255
    """
    pass


class NSNitroNserrLicexpired(NSNitroCliErrors):
    """
        Nitro error code 1066
        Features(s) license expired
    """
    pass


class NSNitroNserrFeatdisabled(NSNitroCliErrors):
    """
        Nitro error code 1067
        Feature(s) not enabled
    """
    pass


class NSNitroNserrMaxlimit(NSNitroCliErrors):
    """
        Nitro error code 1072
        Maximum resource limit reached
    """
    pass


class NSNitroNserrSetNosupport(NSNitroCliErrors):
    """
        Nitro error code 1073
        Set operation not supported
    """
    pass


class NSNitroNserrInvalidvalue(NSNitroCliErrors):
    """
        Nitro error code 1074
        Invalid value
    """
    pass


class NSNitroNserrInvalidname(NSNitroCliErrors):
    """
        Nitro error code 1075
        Invalid name; names must begin with an alphanumeric character or
        underscore and must contain only alphanumerics,  '_',  '#',
        '.',  ' ',  ':',  '@',  '=' or '-'
    """
    pass


class NSNitroNserrNosuchcmd(NSNitroCliErrors):
    """
        Nitro error code 1088
        No such command
    """
    pass


class NSNitroNserrCmdambiguous(NSNitroCliErrors):
    """
        Nitro error code 1089
        Ambiguous command name
    """
    pass


class NSNitroNserrNosucharg(NSNitroCliErrors):
    """
        Nitro error code 1090
        No such argument
    """
    pass


class NSNitroNserrArgvalmissing(NSNitroCliErrors):
    """
        Nitro error code 1091
        Required argument value missing
    """
    pass


class NSNitroNserrArgsmutex(NSNitroCliErrors):
    """
        Nitro error code 1092
        Arguments cannot both be specified
    """
    pass


class NSNitroNserrArgprereq(NSNitroCliErrors):
    """
        Nitro error code 1093
        Argument pre-requisite missing
    """
    pass


class NSNitroNserrArgstoofew(NSNitroCliErrors):
    """
        Nitro error code 1094
        Too few arguments
    """
    pass


class NSNitroNserrArgmissing(NSNitroCliErrors):
    """
        Nitro error code 1095
        Required argument missing
    """
    pass


class NSNitroNserrArgorder(NSNitroCliErrors):
    """
        Nitro error code 1096
        Argument(s) out of order
    """
    pass


class NSNitroNserrArgvalbad(NSNitroCliErrors):
    """
        Nitro error code 1097
        Invalid argument value
    """
    pass


class NSNitroNserrArgvalseq(NSNitroCliErrors):
    """
        Nitro error code 1098
        Arguments cannot have the same value
    """
    pass


class NSNitroNserrArgambiguous(NSNitroCliErrors):
    """
        Nitro error code 1099
        Ambiguous argument name
    """
    pass


class NSNitroNserrSyncgslbconfig(NSNitroCliErrors):
    """
        Nitro error code 1100
        Please confirm whether you want to sync-config (Y/N)? [N]:
    """
    pass


class NSNitroNserrSyncgslbconfigWarn(NSNitroCliErrors):
    """
        Nitro error code 1101
        Syncing config may cause configuration loss on other site.
    """
    pass


class NSNitroNserrArgvalsneq(NSNitroCliErrors):
    """
        Nitro error code 1104
        Arguments must have the same value
    """
    pass


class NSNitroNserrArgvalambiguous(NSNitroCliErrors):
    """
        Nitro error code 1105
        Ambiguous argument value
    """
    pass


class NSNitroNserrStrmaxlen(NSNitroCliErrors):
    """
        Nitro error code 1106
        String length exceeds maximum
    """
    pass


class NSNitroNserrStrminlen(NSNitroCliErrors):
    """
        Nitro error code 1107
        String too short
    """
    pass


class NSNitroNserrIntmaxval(NSNitroCliErrors):
    """
        Nitro error code 1108
        Integer value exceeds maximum
    """
    pass


class NSNitroNserrIntminval(NSNitroCliErrors):
    """
        Nitro error code 1109
        Integer value below minimum
    """
    pass


class NSNitroNserrInvalidip(NSNitroCliErrors):
    """
        Nitro error code 1110
        Invalid IP address
    """
    pass


class NSNitroNserrInvalidnetmask(NSNitroCliErrors):
    """
        Nitro error code 1111
        Invalid netmask
    """
    pass


class NSNitroNserrToomanyvals(NSNitroCliErrors):
    """
        Nitro error code 1112
        Argument has too many values
    """
    pass


class NSNitroNserrBadrange(NSNitroCliErrors):
    """
        Nitro error code 1113
        Range minimum exceeds range maximum
    """
    pass


class NSNitroNserrExprquotes(NSNitroCliErrors):
    """
        Nitro error code 1114
        Expression must be enclosed in quotes
    """
    pass


class NSNitroNserrBadquotes(NSNitroCliErrors):
    """
        Nitro error code 1115
        Unmatched quote
    """
    pass


class NSNitroNserrInvalidrange(NSNitroCliErrors):
    """
        Nitro error code 1116
        Invalid range specification
    """
    pass


class NSNitroNserrMismatchranges(NSNitroCliErrors):
    """
        Nitro error code 1117
        Ranges are different sizes
    """
    pass


class NSNitroNserrMultiranges(NSNitroCliErrors):
    """
        Nitro error code 1118
        Only one range allowed per argument
    """
    pass


class NSNitroNserrNomatchchar(NSNitroCliErrors):
    """
        Nitro error code 1119
        Unmatched character
    """
    pass


class NSNitroNserrNeedreboot(NSNitroCliErrors):
    """
        Nitro error code 1120
        The configuration must be saved and the system rebooted for
        these settings to take effect
    """
    pass


class NSNitroNsqSaveconfig(NSNitroCliErrors):
    """
        Nitro error code 1121
        Do you want to save the new configuration?
    """
    pass


class NSNitroNserrNotsaved(NSNitroCliErrors):
    """
        Nitro error code 1122
        The configuration changes were not saved - they will be lost on
        the next reboot
    """
    pass


class NSNitroNserrCmdexec(NSNitroCliErrors):
    """
        Nitro error code 1123
        Error(s) occurred - some or all changes may not be applied
    """
    pass


class NSNitroNsqReboot(NSNitroCliErrors):
    """
        Nitro error code 1124
        Do you want to reboot the system now?
    """
    pass


class NSNitroNserrNoreboot(NSNitroCliErrors):
    """
        Nitro error code 1125
        The configuration changes will not take effect until the system
        is rebooted
    """
    pass


class NSNitroNserrPgmfailed(NSNitroCliErrors):
    """
        Nitro error code 1126
        External program failed
    """
    pass


class NSNitroNserrCtxmode(NSNitroCliErrors):
    """
        Nitro error code 1127
        Contextual CLI mode
    """
    pass


class NSNitroNserrCmdincomplete(NSNitroCliErrors):
    """
        Nitro error code 1128
        Incomplete command
    """
    pass


class NSNitroNserrCmdoutofctx(NSNitroCliErrors):
    """
        Nitro error code 1129
        Command not valid here
    """
    pass


class NSNitroNserrConfigsaved(NSNitroCliErrors):
    """
        Nitro error code 1130
        The running configuration has been saved
    """
    pass


class NSNitroNserrConfigcleared(NSNitroCliErrors):
    """
        Nitro error code 1131
        The running configuration has been cleared
    """
    pass


class NSNitroNserrRebooting(NSNitroCliErrors):
    """
        Nitro error code 1132
        NetScaler is rebooting now
    """
    pass


class NSNitroNserrNoconfigsave(NSNitroCliErrors):
    """
        Nitro error code 1133
        The running configuration has not changed
    """
    pass


class NSNitroNserrRegexnoanchor(NSNitroCliErrors):
    """
        Nitro error code 1135
        First character of regular expression must be '^'
    """
    pass


class NSNitroNserrRegexnomatch(NSNitroCliErrors):
    """
        Nitro error code 1136
        Regular expression does not match
    """
    pass


class NSNitroNserrRegexinvalid(NSNitroCliErrors):
    """
        Nitro error code 1137
        Invalid regular expression
    """
    pass


class NSNitroNserrRegexnotallowed(NSNitroCliErrors):
    """
        Nitro error code 1138
        Regular expression not allowed
    """
    pass


class NSNitroNserrRegexnocmd(NSNitroCliErrors):
    """
        Nitro error code 1139
        No matches
    """
    pass


class NSNitroNserrInvalidipv6Format(NSNitroCliErrors):
    """
        Nitro error code 1140
        Invalid IPv6 address
    """
    pass


class NSNitroNserrInvalidipv6TwoDoubecolon(NSNitroCliErrors):
    """
        Nitro error code 1141
        Double-colon can appear only once in an IPv6 address
    """
    pass


class NSNitroNserrInvalidipv6NoprefixLength(NSNitroCliErrors):
    """
        Nitro error code 1142
        Prefix length must be given with an IPv6 address
    """
    pass


class NSNitroNserrInvalidipv6PrefixValue(NSNitroCliErrors):
    """
        Nitro error code 1143
        Prefix length must be in the range of 0-128
    """
    pass


class NSNitroNserrTermnameinvalid(NSNitroCliErrors):
    """
        Nitro error code 1144
        Invalid term name
    """
    pass


class NSNitroNserrTerminvalid(NSNitroCliErrors):
    """
        Nitro error code 1145
        Invalid syntax in term
    """
    pass


class NSNitroNserrForcefailover(NSNitroCliErrors):
    """
        Nitro error code 1146
        Please confirm whether you want force-failover (Y/N)? [N]:
    """
    pass


class NSNitroNserrForcefailHealthWarn(NSNitroCliErrors):
    """
        Nitro error code 1147
        Force Failover may cause configuration loss,  peer health not
        optimum. Reason(s):
    """
    pass


class NSNitroNserrHellotimeMultiple(NSNitroCliErrors):
    """
        Nitro error code 1148
        Invalid value. Hellotime Interval must be a multiple of 200
    """
    pass


class NSNitroNserrForcesyncsave(NSNitroCliErrors):
    """
        Nitro error code 1149
        Do you want to save the config after sync (Y/N)? [Y]:
    """
    pass


class NSNitroNserrErroutfilename(NSNitroCliErrors):
    """
        Nitro error code 1150
        Character '/' not allowed in outfilename
    """
    pass


class NSNitroNserrRnatipdel(NSNitroCliErrors):
    """
        Nitro error code 1151
        address is bound to rnat config,  can not be removed
    """
    pass


class NSNitroNserrInvalidalias(NSNitroCliErrors):
    """
        Nitro error code 1152
        Invalid alias
    """
    pass


class NSNitroNserrNosuchalias(NSNitroCliErrors):
    """
        Nitro error code 1153
        No such alias
    """
    pass


class NSNitroNserrAliasexists(NSNitroCliErrors):
    """
        Nitro error code 1154
        Alias already exists
    """
    pass


class NSNitroNserrNosuchfile(NSNitroCliErrors):
    """
        Nitro error code 1155
        No such file
    """
    pass


class NSNitroNserrNotregfile(NSNitroCliErrors):
    """
        Nitro error code 1156
        Not a file
    """
    pass


class NSNitroNserrDeprcmd(NSNitroCliErrors):
    """
        Nitro error code 1157
        Command deprecated
    """
    pass


class NSNitroNserrDeprarg(NSNitroCliErrors):
    """
        Nitro error code 1158
        Argument deprecated
    """
    pass


class NSNitroNserrNotlogfile(NSNitroCliErrors):
    """
        Nitro error code 1159
        Not a NetScaler log file
    """
    pass


class NSNitroNserrNoplenforipv6range(NSNitroCliErrors):
    """
        Nitro error code 1160
        Prefix length cannot be specified for an IPv6 range
    """
    pass


class NSNitroNserrInvalidint(NSNitroCliErrors):
    """
        Nitro error code 1161
        Integer not in range
    """
    pass


class NSNitroNserrCmdambiguousUsecompletionsoptions(NSNitroCliErrors):
    """
        Nitro error code 1162
        Ambiguous (use cmd completion for options)
    """
    pass


class NSNitroNserrMetadataInvalEntitytype(NSNitroCliErrors):
    """
        Nitro error code 1163
        Invalid Entity Type
    """
    pass


class NSNitroNserrSetnotexist(NSNitroCliErrors):
    """
        Nitro error code 1164
        set operation does not exist
    """
    pass


class NSNitroNserrSetargnotexist(NSNitroCliErrors):
    """
        Nitro error code 1165
        set operation for one of the modified argument does not exist
    """
    pass


class NSNitroNserrInvalidDs(NSNitroCliErrors):
    """
        Nitro error code 1166
        Invalid datasource
    """
    pass


class NSNitroNserrNosuchcounter(NSNitroCliErrors):
    """
        Nitro error code 1167
        No such counter
    """
    pass


class NSNitroNserrInvalidipmask(NSNitroCliErrors):
    """
        Nitro error code 1168
        Invalid IP address mask
    """
    pass


class NSNitroNserrInvalidippat(NSNitroCliErrors):
    """
        Nitro error code 1169
        Invalid IP address pattern
    """
    pass


class NSNitroNserrBadrc(NSNitroCliErrors):
    """
        Nitro error code 1170
        Unexpected return code
    """
    pass


class NSNitroNserrInvalidrangetype(NSNitroCliErrors):
    """
        Nitro error code 1171
        Inappropriate range values for value type
    """
    pass


class NSNitroNserrInvalidrangeval(NSNitroCliErrors):
    """
        Nitro error code 1172
        Invalid range value
    """
    pass


class NSNitroNserrInvalidipv6PrefixLength(NSNitroCliErrors):
    """
        Nitro error code 1173
        Prefix length must not be given
    """
    pass


class NSNitroNserrEntitydeleteFail(NSNitroCliErrors):
    """
        Nitro error code 1174
        Can not delete active entity
    """
    pass


class NSNitroNserrIncompatibleip(NSNitroCliErrors):
    """
        Nitro error code 1181
        Private IP and public IP must be either IPv4 or IPv6
    """
    pass


class NSNitroNserrTranscrIp(NSNitroCliErrors):
    """
        Nitro error code 1182
        For transparent CR vserver,  you cannot specify IP address
    """
    pass


class NSNitroNserrPasswordMismatch(NSNitroCliErrors):
    """
        Nitro error code 1183
        Passwords entered do not match
    """
    pass


class NSNitroCfeErrors(NSNitroError):
    """
        Base exception class NSNitroCfeErrors
    """
    pass


class NSNitroNserrNosuchioctl(NSNitroCfeErrors):
    """
        Nitro error code 1184
        Command not implemented on server
    """
    pass


class NSNitroNserrNotargets(NSNitroCfeErrors):
    """
        Nitro error code 1185
        No configured targets
    """
    pass


class NSNitroNserrCantrecover(NSNitroCfeErrors):
    """
        Nitro error code 1186
        Configuration possibly inconsistent.  Please check with the
        \"show configstatus\" command or reboot.
    """
    pass


class NSNitroNserrIgnoredioctl(NSNitroCfeErrors):
    """
        Nitro error code 1187
        The command was ignored.
    """
    pass


class NSNitroNserrRemoteclose(NSNitroCfeErrors):
    """
        Nitro error code 1188
        The remote side closed the connection.
    """
    pass


class NSNitroNserrInvalidTarget(NSNitroCfeErrors):
    """
        Nitro error code 1189
        The specified target does not exist
    """
    pass


class NSNitroNserrFileError(NSNitroCfeErrors):
    """
        Nitro error code 1190
        File operation failed
    """
    pass


class NSNitroNserrCommentDropped(NSNitroCfeErrors):
    """
        Nitro error code 1191
        Failed to retain all comments
    """
    pass


class NSNitroNserrAggreqTimeout(NSNitroCfeErrors):
    """
        Nitro error code 1192
        Request to Aggregator timed out
    """
    pass


class NSNitroNserrAggread(NSNitroCfeErrors):
    """
        Nitro error code 1193
        Failed to read data from Aggregator
    """
    pass


class NSNitroNserrRpcCmdDup(NSNitroCfeErrors):
    """
        Nitro error code 1194
        Found unexpected RPC duplicate command
    """
    pass


class NSNitroNserrRpcCmdNondup(NSNitroCfeErrors):
    """
        Nitro error code 1195
        Found unexpected RPC command
    """
    pass


class NSNitroNserrCfePeComm(NSNitroCfeErrors):
    """
        Nitro error code 1196
        Communication error with the packet engine
    """
    pass


class NSNitroNserrAggConfail(NSNitroCfeErrors):
    """
        Nitro error code 1197
        Failed to connect to the aggregator
    """
    pass


class NSNitroNserrCfePeTimout(NSNitroCfeErrors):
    """
        Nitro error code 1198
        No response from the packet engine
    """
    pass


class NSNitroNserrAggInvalidresponse(NSNitroCfeErrors):
    """
        Nitro error code 1199
        Invalid response from the aggregator
    """
    pass


class NSNitroNserrNontpsvr(NSNitroCfeErrors):
    """
        Nitro error code 1200
        Cannot enable ntpd when there is no ntp server configured
    """
    pass


class NSNitroNserrAggSendfail(NSNitroCfeErrors):
    """
        Nitro error code 1201
        Failed to send to aggregator
    """
    pass


class NSNitroNserrCfeAslearnComm(NSNitroCfeErrors):
    """
        Nitro error code 1202
        Communication error with aslearn
    """
    pass


class NSNitroNitroErrors(NSNitroError):
    """
        Base exception class NSNitroNitroErrors
    """
    pass


class NSNitroNserrNitroInvalidObjectname(NSNitroNitroErrors):
    """
        Nitro error code 1232
        Invalid object name
    """
    pass


class NSNitroNserrNitroInvalidJsonInput(NSNitroNitroErrors):
    """
        Nitro error code 1233
        Invalid JSON input
    """
    pass


class NSNitroNserrNitroInvalidJsonDatatype(NSNitroNitroErrors):
    """
        Nitro error code 1234
        Invalid JSON data type
    """
    pass


class NSNitroNserrNitroInvalidXmlInput(NSNitroNitroErrors):
    """
        Nitro error code 1235
        Invalid XML input
    """
    pass


class NSNitroNserrNitroInvalidDatatype(NSNitroNitroErrors):
    """
        Nitro error code 1236
        Invalid NITRO data type
    """
    pass


class NSNitroNserrNitroInvalidMethod(NSNitroNitroErrors):
    """
        Nitro error code 1237
        Invalid method name. It should be either post,  put,  get,  stat
        or delete
    """
    pass


class NSNitroNserrNitroParseError(NSNitroNitroErrors):
    """
        Nitro error code 1238
        NITRO parse error
    """
    pass


class NSNitroNserrNitroCmdexecFailed(NSNitroNitroErrors):
    """
        Nitro error code 1239
        NITRO command Execution failed
    """
    pass


class NSNitroNserrNitroInvalidAction(NSNitroNitroErrors):
    """
        Nitro error code 1240
        Invalid nitro action or operation
    """
    pass


class NSNitroNserrNsappTemplateExists(NSNitroNitroErrors):
    """
        Nitro error code 1248
        Template already exists
    """
    pass


class NSNitroNserrNsappInvalidTemplate(NSNitroNitroErrors):
    """
        Nitro error code 1249
        Invalid Template
    """
    pass


class NSNitroNserrNsappDirError(NSNitroNitroErrors):
    """
        Nitro error code 1250
        Couldnot open directory
    """
    pass


class NSNitroNserrNsappFileError(NSNitroNitroErrors):
    """
        Nitro error code 1251
        Can not open the file
    """
    pass


class NSNitroNserrNsappInvalidAppInput(NSNitroNitroErrors):
    """
        Nitro error code 1252
        Invalid Application input
    """
    pass


class NSNitroNserrNsappExceededFilelength(NSNitroNitroErrors):
    """
        Nitro error code 1253
        File length exceeded 256 characters
    """
    pass


class NSNitroNserrNsappEndpointInuse(NSNitroNitroErrors):
    """
        Nitro error code 1254
        Public endpoint in use
    """
    pass


class NSNitroNserrNsappProtocolMismatch(NSNitroNitroErrors):
    """
        Nitro error code 1255
        Protocol mismatch with existing configuration
    """
    pass


class NSNitroNserrNsappInvalidVarname(NSNitroNitroErrors):
    """
        Nitro error code 1256
        Invalid variable name
    """
    pass


class NSNitroNserrNsappZipFile(NSNitroNitroErrors):
    """
        Nitro error code 1257
        Error in zip format
    """
    pass


class NSNitroNserrNsappMaxepReached(NSNitroNitroErrors):
    """
        Nitro error code 1258
        Only one endpoint can be configured
    """
    pass


class NSNitroNserrNsappNotExist(NSNitroNitroErrors):
    """
        Nitro error code 1259
        Application does not exist
    """
    pass


class NSNitroNserrNsappInvalidServicetype(NSNitroNitroErrors):
    """
        Nitro error code 1260
        Invalid servicetype - HTTP/HTTPS/SSL are only allowed
    """
    pass


class NSNitroNserrNsappTemplateFormatError(NSNitroNitroErrors):
    """
        Nitro error code 1261
        Template format error
    """
    pass


class NSNitroNserrNsappAppWithoutAppunits(NSNitroNitroErrors):
    """
        Nitro error code 1262
        Application without appunits can not be exported
    """
    pass


class NSNitroNserrNsappServicrgroupExists(NSNitroNitroErrors):
    """
        Nitro error code 1263
        Service group with this name already exists
    """
    pass


class NSNitroLbErrors(NSNitroError):
    """
        Base exception class NSNitroLbErrors
    """
    pass


class NSNitroNserrSlesslbLbmethodNotsupported(NSNitroLbErrors):
    """
        Nitro error code 1280
        Incompatible LB method for sessionless vserver
    """
    pass


class NSNitroNserrSlesslbPersistNotsupported(NSNitroLbErrors):
    """
        Nitro error code 1281
        Incompatible persistence method for sessionless vserver
    """
    pass


class NSNitroNserrSlesslbTypeNotsupported(NSNitroLbErrors):
    """
        Nitro error code 1282
        Sessionless vserver must be of type ANY,  DNS or UDP
    """
    pass


class NSNitroNserrSlesslbModeNotsupported(NSNitroLbErrors):
    """
        Nitro error code 1283
        Sessionless vserver must have MAC or IPTUNNEL mode set
    """
    pass


class NSNitroNserrSlesslbSvcUsipnotset(NSNitroLbErrors):
    """
        Nitro error code 1284
        Service bound to a sessionless vserver must have UseSourceIP
        mode enabled
    """
    pass


class NSNitroNserrWildcardvipLbmethodInval(NSNitroLbErrors):
    """
        Nitro error code 1286
        Invalid LB method for a wildcard vserver
    """
    pass


class NSNitroNserrWildcardvipPersistInval(NSNitroLbErrors):
    """
        Nitro error code 1287
        Invalid persistence policy for a wildcard vserver
    """
    pass


class NSNitroNserrLbSoThreshold(NSNitroLbErrors):
    """
        Nitro error code 1288
        Spill-over threshold should be a non-zero value
    """
    pass


class NSNitroNserrConnfailoverUsip(NSNitroLbErrors):
    """
        Nitro error code 1289
        Service must have Use Source IP option set in order to be bound
        to a connection failover enabled virtual server
    """
    pass


class NSNitroNserrConnfailoverService(NSNitroLbErrors):
    """
        Nitro error code 1290
        Connection failover can only be enabled on a virtual server of
        service type ANY
    """
    pass


class NSNitroNserrLbSoDynamicconThreshold(NSNitroLbErrors):
    """
        Nitro error code 1291
        Spill-over threshold cannot be set for dynamic connection spill-
        over method
    """
    pass


class NSNitroNserrLbSoAddrvip(NSNitroLbErrors):
    """
        Nitro error code 1292
        DYNAMICCONNECTION spill-over cannot be set on a non-LB vserver
    """
    pass


class NSNitroNserrConnfailoverNotforSless(NSNitroLbErrors):
    """
        Nitro error code 1293
        Connection Failover is not supported for sessionless lb
        vserver\n
    """
    pass


class NSNitroNserrSipNocallid(NSNitroLbErrors):
    """
        Nitro error code 1296
        Missing Call-ID header field
    """
    pass


class NSNitroNserrSipNovia(NSNitroLbErrors):
    """
        Nitro error code 1297
        Missing Via header field
    """
    pass


class NSNitroNserrSipNocseq(NSNitroLbErrors):
    """
        Nitro error code 1298
        Missing CSeq header field
    """
    pass


class NSNitroNserrSipNoto(NSNitroLbErrors):
    """
        Nitro error code 1299
        Missing To header field
    """
    pass


class NSNitroNserrSipNofrom(NSNitroLbErrors):
    """
        Nitro error code 1300
        Missing From header field
    """
    pass


class NSNitroNserrSipNomaxForwards(NSNitroLbErrors):
    """
        Nitro error code 1301
        Missing Max-Forwards header field
    """
    pass


class NSNitroNserrSipServiceUnavailable(NSNitroLbErrors):
    """
        Nitro error code 1302
        Service unavailable
    """
    pass


class NSNitroNserrSvcNotBound(NSNitroLbErrors):
    """
        Nitro error code 1303
        Service not bound to Vserver
    """
    pass


class NSNitroNserrSvctypeMismatch(NSNitroLbErrors):
    """
        Nitro error code 1304
        Service type mismatch between the vserver and service
    """
    pass


class NSNitroNserrChConNotAllowed(NSNitroLbErrors):
    """
        Nitro error code 1305
        CONNECTION header cannot be set
    """
    pass


class NSNitroNserrChIncompleteHdr(NSNitroLbErrors):
    """
        Nitro error code 1312
        Custom Header string should end with CRLF
    """
    pass


class NSNitroNserrSpilloverdisabled(NSNitroLbErrors):
    """
        Nitro error code 1313
        No spillover on the vserver due to max client setting '0' on a
        bound service
    """
    pass


class NSNitroNserrMaxtimeexceeded(NSNitroLbErrors):
    """
        Nitro error code 1314
        Maximum time value for interval or responsetimeout or downtime
        is exceeded,  rounding to maximum
    """
    pass


class NSNitroNserrScinvalproto(NSNitroLbErrors):
    """
        Nitro error code 1315
        Cannot bind SC policy to non-HTTP service or vserver
    """
    pass


class NSNitroNserrRootrec(NSNitroLbErrors):
    """
        Nitro error code 1316
        Atleast one nameserver record should exist for the root domain
    """
    pass


class NSNitroNserrRootGluerec(NSNitroLbErrors):
    """
        Nitro error code 1317
        Root domain nameserver address record should have atleast one ip
        address
    """
    pass


class NSNitroNserrVipinsertNotSupported(NSNitroLbErrors):
    """
        Nitro error code 1356
        Vserver IP and port header insertion option not supported on
        this vserver.
    """
    pass


class NSNitroNserrVsvrAlrdyBound(NSNitroLbErrors):
    """
        Nitro error code 1318
        This vserver is already bound to a WLM
    """
    pass


class NSNitroNserrInvalidWlmBinding(NSNitroLbErrors):
    """
        Nitro error code 1319
        Only LB vservers are allowed to bound to WLM
    """
    pass


class NSNitroNserrVsvrNotBound(NSNitroLbErrors):
    """
        Nitro error code 1320
        Vserver not bound to WLM
    """
    pass


class NSNitroNserrWlmExists(NSNitroLbErrors):
    """
        Nitro error code 1321
        WLM already configured on this IP,  port
    """
    pass


class NSNitroNserrInvalidTimeout(NSNitroLbErrors):
    """
        Nitro error code 1322
        Invalid persistence timeout: default timeout assigned
    """
    pass


class NSNitroNserrConnfailoverIncmode(NSNitroLbErrors):
    """
        Nitro error code 1323
        Stateful connection failover cannot be enabled in INC mode
    """
    pass


class NSNitroNserrConnfailoverTcpb(NSNitroLbErrors):
    """
        Nitro error code 1324
        Stateful connection failover cannot be enabled on a vserver that
        binds services with TCP buffering enabled
    """
    pass


class NSNitroNserrConnfailoverTcpbSvcBind(NSNitroLbErrors):
    """
        Nitro error code 1326
        Service with TCP buffering enabled cannot be bound to a vserver
        with stateful connection failover enabled
    """
    pass


class NSNitroNserrConnfailoverTcpbSvcParam(NSNitroLbErrors):
    """
        Nitro error code 1327
        TCP buffering cannot be enabled on a service bound to a vserver
        with stateful connection failover enabled
    """
    pass


class NSNitroNserrConnfailoverServiceStatefull(NSNitroLbErrors):
    """
        Nitro error code 1328
        Stateful connection failover cannot be enabled on a vserver of
        this service type
    """
    pass


class NSNitroNserrConnfailoverSslSvcBind(NSNitroLbErrors):
    """
        Nitro error code 1329
        SSL TCP service cannot be bound to a TCP vserver with stateful
        connection failover enabled
    """
    pass


class NSNitroNserrConnfailoverHaIncNode(NSNitroLbErrors):
    """
        Nitro error code 1330
        Ha node with INC mode enabled cannot be added to the system that
        has vserver(s) with stateful connection failover enabled
    """
    pass


class NSNitroNserrConnfailoverSslSvc(NSNitroLbErrors):
    """
        Nitro error code 1331
        Stateful connection failover cannot be enabled on a vserver that
        binds services of type SSL_TCP
    """
    pass


class NSNitroNserrInvalidPersistence(NSNitroLbErrors):
    """
        Nitro error code 1332
        Invalid Persistence type
    """
    pass


class NSNitroNserrRtspsessionInvalid(NSNitroLbErrors):
    """
        Nitro error code 1333
        Invalid RTSP session entry
    """
    pass


class NSNitroNserrLbMethodSameasBackupMethod(NSNitroLbErrors):
    """
        Nitro error code 1334
        Backup load balancing method cannot be the same as the primary
        load balancing method
    """
    pass


class NSNitroNserrServerExist(NSNitroLbErrors):
    """
        Nitro error code 1335
        Server already exists
    """
    pass


class NSNitroNserrLbSoHealth(NSNitroLbErrors):
    """
        Nitro error code 1336
        HEALTH spill-over cannot be set on a non-LB vserver
    """
    pass


class NSNitroNserrReqRuleMissing(NSNitroLbErrors):
    """
        Nitro error code 1337
        Request Rule is required,  when Response rule is specified.
    """
    pass


class NSNitroNserrConnfailoverBindlo(NSNitroLbErrors):
    """
        Nitro error code 1338
        Loopback service cannot be bound to vserver with connection
        failover enabled \n
    """
    pass


class NSNitroNserrConnfailoverSetwithlo(NSNitroLbErrors):
    """
        Nitro error code 1339
        Connection Failover cannot be set to STATEFUL/STATELESS on
        vserver with bound loopback service\n
    """
    pass


class NSNitroNserrRedirectUrlNotApplicable(NSNitroLbErrors):
    """
        Nitro error code 1340
        Redirect URL cannot be configured on this vserver.
    """
    pass


class NSNitroNserrStatefulConnfailoverIpv6(NSNitroLbErrors):
    """
        Nitro error code 1341
        Stateful connection failover cannot be enabled on an IPv6
        vserver
    """
    pass


class NSNitroNserrConnfailoverNotSupported(NSNitroLbErrors):
    """
        Nitro error code 1342
        Connection Failover is not supported for pattern based vservers
    """
    pass


class NSNitroNserrNobindOnpush(NSNitroLbErrors):
    """
        Nitro error code 1343
        Bindings not allowed on push vserver
    """
    pass


class NSNitroNserrPushVsvr(NSNitroLbErrors):
    """
        Nitro error code 1344
        Option cannot be set on push vserver
    """
    pass


class NSNitroNserrOnlyHttpssl(NSNitroLbErrors):
    """
        Nitro error code 1345
        Option can only be set on http/ ssl vserver
    """
    pass


class NSNitroNserrPushBindExists(NSNitroLbErrors):
    """
        Nitro error code 1346
        A push vserver is already bound. Unbind before binding new
        vserver
    """
    pass


class NSNitroNserrSetPushvsOnly(NSNitroLbErrors):
    """
        Nitro error code 1347
        Push vserver should be of type push or ssl_push only
    """
    pass


class NSNitroNserrSlessNoSupport(NSNitroLbErrors):
    """
        Nitro error code 1348
        Not supported for sessionless vservers
    """
    pass


class NSNitroNserrConnfailoverV6service(NSNitroLbErrors):
    """
        Nitro error code 1349
        Connection Failover cannot be set to STATEFUL/STATELESS on
        vserver with IPv6 services bound
    """
    pass


class NSNitroNserrConnfailoverVserver(NSNitroLbErrors):
    """
        Nitro error code 1350
        IPV6 service cannot be bound to vserver with connection failover
        set to STATEFUL/STATELESS
    """
    pass


class NSNitroNserrNoListenPolicyForDummyvs(NSNitroLbErrors):
    """
        Nitro error code 1352
        Cannot bind listen policy to dummy vservers
    """
    pass


class NSNitroNserrNormalVsNoneListenpol(NSNitroLbErrors):
    """
        Nitro error code 1355
        The vserver already has None Listen Policy\n
    """
    pass


class NSNitroNserrNoLispriForNoneLispol(NSNitroLbErrors):
    """
        Nitro error code 1357
        None listenpolicy doesnot have listen priority\n
    """
    pass


class NSNitroNserrInvalidPolicyString(NSNitroLbErrors):
    """
        Nitro error code 1358
        Invalid listenpolicy entered\n
    """
    pass


class NSNitroNserrNodatalenoffforvs(NSNitroLbErrors):
    """
        Nitro error code 1359
        Dataoffset and datalength are not requied for this vserver\n
    """
    pass


class NSNitroNserrLbgrppersiswithrdp(NSNitroLbErrors):
    """
        Nitro error code 1285
        Persistency is not applicable for RDP vserver or LB group which
        has RDP vserver part of it
    """
    pass


class NSNitroPqErrors(NSNitroError):
    """
        Base exception class NSNitroPqErrors
    """
    pass


class NSNitroNserrPqBindvip(NSNitroPqErrors):
    """
        Nitro error code 1360
        Cannot bind same priority policy to VIP
    """
    pass


class NSNitroNserrPqInvalprio(NSNitroPqErrors):
    """
        Nitro error code 1361
        Invalid priority value
    """
    pass


class NSNitroNserrPq2bigrule(NSNitroPqErrors):
    """
        Nitro error code 1362
        Rule argument too big
    """
    pass


class NSNitroNserrPqInvalwt(NSNitroPqErrors):
    """
        Nitro error code 1363
        Invalid weight value
    """
    pass


class NSNitroNserrPqPolexist(NSNitroPqErrors):
    """
        Nitro error code 1364
        Policy name already in use
    """
    pass


class NSNitroNserrPqNopol(NSNitroPqErrors):
    """
        Nitro error code 1365
        No such PQ policy exists
    """
    pass


class NSNitroNserrPq2manyref(NSNitroPqErrors):
    """
        Nitro error code 1366
        Cannot remove a policy which is bound to VIP
    """
    pass


class NSNitroNserrPqNolbvip(NSNitroPqErrors):
    """
        Nitro error code 1367
        No such LB vserver exists
    """
    pass


class NSNitroNserrPqPhsconfig(NSNitroPqErrors):
    """
        Nitro error code 1368
        Cannot configure PQ on VIP if physical service has PQ
        configuration
    """
    pass


class NSNitroNserrPqNobind(NSNitroPqErrors):
    """
        Nitro error code 1369
        Cannot unbind PQ Policy which is not bound
    """
    pass


class NSNitroSslErrors(NSNitroError):
    """
        Base exception class NSNitroSslErrors
    """
    pass


class NSNitroNserrSslCert(NSNitroSslErrors):
    """
        Nitro error code 1536
        Invalid certificate
    """
    pass


class NSNitroNserrSslPkey(NSNitroSslErrors):
    """
        Nitro error code 1537
        Invalid private key,  or PEM pass phrase required for this
        private key
    """
    pass


class NSNitroNserrSslNomatch(NSNitroSslErrors):
    """
        Nitro error code 1538
        Certificate and private key do not match
    """
    pass


class NSNitroNserrSslCerttype(NSNitroSslErrors):
    """
        Nitro error code 1539
        Invalid cetificate type
    """
    pass


class NSNitroNserrSslNocert(NSNitroSslErrors):
    """
        Nitro error code 1540
        Certificate does not exist
    """
    pass


class NSNitroNserrSslRefext(NSNitroSslErrors):
    """
        Nitro error code 1541
        Certificate is referenced by a CRL,  OCSP responder,  vserver,
        service,  another certificate,  or a policy expression using
        XML_ENCRYPT() or XML_DECRYPT()
    """
    pass


class NSNitroNserrSslBind(NSNitroSslErrors):
    """
        Nitro error code 1542
        Certificate binding does not exist
    """
    pass


class NSNitroNserrSslLink(NSNitroSslErrors):
    """
        Nitro error code 1543
        Certificate can't be linked to the same certificate
    """
    pass


class NSNitroNserrSslNeedSslproto(NSNitroSslErrors):
    """
        Nitro error code 1544
        Object's protocol type is not SSL
    """
    pass


class NSNitroNserrSslNolink(NSNitroSslErrors):
    """
        Nitro error code 1545
        Certificate does not have any CA link
    """
    pass


class NSNitroNserrSslBindor(NSNitroSslErrors):
    """
        Nitro error code 1546
        Current certificate replaces the previous binding
    """
    pass


class NSNitroNserrSslNosvrcert(NSNitroSslErrors):
    """
        Nitro error code 1547
        Certificate is not a server certificate
    """
    pass


class NSNitroNserrSslIssubmis(NSNitroSslErrors):
    """
        Nitro error code 1548
        Issuer certificate mismatch
    """
    pass


class NSNitroNserrSslCrl(NSNitroSslErrors):
    """
        Nitro error code 1549
        Invalid CRL
    """
    pass


class NSNitroNserrSslNocrl(NSNitroSslErrors):
    """
        Nitro error code 1550
        CRL does not exist
    """
    pass


class NSNitroNserrSslDhcount(NSNitroSslErrors):
    """
        Nitro error code 1551
        DH Refresh count should be 0 or >=500
    """
    pass


class NSNitroNserrSslSessto(NSNitroSslErrors):
    """
        Nitro error code 1552
        Session timeout should be > 0
    """
    pass


class NSNitroNserrSslErsacount(NSNitroSslErrors):
    """
        Nitro error code 1553
        eRSA Refresh count should be 0 or >=500
    """
    pass


class NSNitroNserrSslDhSize(NSNitroSslErrors):
    """
        Nitro error code 1554
        DH params of size greater than 2048 bits not supported
    """
    pass


class NSNitroNserrDhpath(NSNitroSslErrors):
    """
        Nitro error code 1555
        DH file path mandatory if DH enabled
    """
    pass


class NSNitroNserrCertheader(NSNitroSslErrors):
    """
        Nitro error code 1556
        Cert header tag mandatory if cert enabled
    """
    pass


class NSNitroNserrSessheader(NSNitroSslErrors):
    """
        Nitro error code 1557
        Sess header tag mandatory if sess enabled
    """
    pass


class NSNitroNserrCipherPerm(NSNitroSslErrors):
    """
        Nitro error code 1558
        Default ciphers/aliases cannot be added or removed
    """
    pass


class NSNitroNserrSslErsadisabled(NSNitroSslErrors):
    """
        Nitro error code 1559
        Setting eRSA count when eRSA is disabled
    """
    pass


class NSNitroNserrSslDhdisabled(NSNitroSslErrors):
    """
        Nitro error code 1560
        Setting DH count when DH is disabled
    """
    pass


class NSNitroNserrSslSessdisabled(NSNitroSslErrors):
    """
        Nitro error code 1561
        Setting session timeout when session reuse is disabled
    """
    pass


class NSNitroNserrSslPkeySize(NSNitroSslErrors):
    """
        Nitro error code 1562
        Certificate with key size greater than RSA4096 or DSA2048 bits
        not supported
    """
    pass


class NSNitroNserrSslNotApplicable(NSNitroSslErrors):
    """
        Nitro error code 1563
        Option is not applicable for this SSL protocol
    """
    pass


class NSNitroNserrSslInternalerr(NSNitroSslErrors):
    """
        Nitro error code 1567
        Internal Error
    """
    pass


class NSNitroNserrSslNocacert(NSNitroSslErrors):
    """
        Nitro error code 1568
        cacert does not exists
    """
    pass


class NSNitroNserrSslRefreshdis(NSNitroSslErrors):
    """
        Nitro error code 1569
        crl refresh disabled
    """
    pass


class NSNitroNserrSslSvrportneeded(NSNitroSslErrors):
    """
        Nitro error code 1570
        Server/port information is needed for enabling auto refresh
    """
    pass


class NSNitroNserrSslBaseobjneeded(NSNitroSslErrors):
    """
        Nitro error code 1571
        baseDN is required for enabling auto refresh
    """
    pass


class NSNitroNserrSslCipherRedirect(NSNitroSslErrors):
    """
        Nitro error code 1572
        Send Internal Cipher mismatch error page
    """
    pass


class NSNitroNserrSslNodsa(NSNitroSslErrors):
    """
        Nitro error code 1573
        Loading of certificate and key of type DSA(DSS) is not supported
        with FIPS
    """
    pass


class NSNitroNserrSslFipsrefext(NSNitroSslErrors):
    """
        Nitro error code 1574
        The FIPS key is referenced by a certificate
    """
    pass


class NSNitroNserrSslNofipskey(NSNitroSslErrors):
    """
        Nitro error code 1575
        No such FIPS key
    """
    pass


class NSNitroNserrNofipscard(NSNitroSslErrors):
    """
        Nitro error code 1576
        Operation not permitted - no FIPS card present in the system
    """
    pass


class NSNitroNserrFipscardnotconf(NSNitroSslErrors):
    """
        Nitro error code 1577
        Operation not permitted - FIPS card is not configured
    """
    pass


class NSNitroNserrSslSslv2Redirect(NSNitroSslErrors):
    """
        Nitro error code 1578
        Send Internal SSL protocol mismatch error page
    """
    pass


class NSNitroNserrSslModsize64(NSNitroSslErrors):
    """
        Nitro error code 1579
        Modulus size in bytes should be multiple of 64
    """
    pass


class NSNitroNserrSslNonfipskey(NSNitroSslErrors):
    """
        Nitro error code 1580
        Configuration of non-FIPS key on FIPS system not allowed
    """
    pass


class NSNitroNserrNfipsFipsUpd(NSNitroSslErrors):
    """
        Nitro error code 1581
        Cannot update a non-FIPS certificate with a FIPS certificate
    """
    pass


class NSNitroNserrFipsNfipsUpd(NSNitroSslErrors):
    """
        Nitro error code 1582
        Cannot update a FIPS certificate with a non-FIPS certificate
    """
    pass


class NSNitroNserrSslIssuerNotinGlbcertlist(NSNitroSslErrors):
    """
        Nitro error code 1583
        Unable to find the CA certificate for the CRL
    """
    pass


class NSNitroNserrSslCrlsigcheckFail(NSNitroSslErrors):
    """
        Nitro error code 1584
        Signature check on the CRL failed
    """
    pass


class NSNitroNserrSslPortrewrite(NSNitroSslErrors):
    """
        Nitro error code 1585
        SSL port rewrite can be enabled only when SSL redirect is
        enabled
    """
    pass


class NSNitroNserrSslSslv2RenegClientCert(NSNitroSslErrors):
    """
        Nitro error code 1586
        Send Internal error page for SSLv2 protocol and client
        authentication with session renegotiation
    """
    pass


class NSNitroNserrSslBrklink(NSNitroSslErrors):
    """
        Nitro error code 1587
        All incompatible CA links/Cert bindings were broken during the
        update operation
    """
    pass


class NSNitroNserrSslCertNotYetValid(NSNitroSslErrors):
    """
        Nitro error code 1588
        The specified certificate is not yet valid
    """
    pass


class NSNitroNserrSslCertExpired(NSNitroSslErrors):
    """
        Nitro error code 1589
        The certificate has expired
    """
    pass


class NSNitroNserrSslExpiredBrklink(NSNitroSslErrors):
    """
        Nitro error code 1590
        All incompatible CA links were broken during the update
        operation. (Note: the certificate has expired)
    """
    pass


class NSNitroNserrSslNyvalidBrklink(NSNitroSslErrors):
    """
        Nitro error code 1591
        All incompatible CA links were broken during the update
        operation. (Note: the certificate is not yet valid)
    """
    pass


class NSNitroNserrSslOcspRespcert(NSNitroSslErrors):
    """
        Nitro error code 1592
        No such responder certificate.
    """
    pass


class NSNitroNserrSslOcspSigncert(NSNitroSslErrors):
    """
        Nitro error code 1593
        No such signing certificate.
    """
    pass


class NSNitroNserrSslOcspAia(NSNitroSslErrors):
    """
        Nitro error code 1600
        Invalid AIA value
    """
    pass


class NSNitroSsl2Errors(NSNitroError):
    """
        Base exception class NSNitroSsl2Errors
    """
    pass


class NSNitroNserrSslFipscardlocked(NSNitroSsl2Errors):
    """
        Nitro error code 3584
        FIPS card locked due to three unsuccessful login attempts
    """
    pass


class NSNitroNserrSslDomincompat(NSNitroSsl2Errors):
    """
        Nitro error code 3585
        Certificate is registered to a different domain; use the 'no
        domain check' option to force the operation
    """
    pass


class NSNitroNserrSslNomthdchange(NSNitroSsl2Errors):
    """
        Nitro error code 3586
        Cannot change refresh method of CRL
    """
    pass


class NSNitroNserrSslUrlsrvrneeded(NSNitroSsl2Errors):
    """
        Nitro error code 3587
        Either URL or server-IP required on CRL
    """
    pass


class NSNitroNserrSslInvalidUrl(NSNitroSsl2Errors):
    """
        Nitro error code 3588
        Invalid URL
    """
    pass


class NSNitroNserrSslMixparams(NSNitroSsl2Errors):
    """
        Nitro error code 3589
        LDAP and HTTP parameters cannot both be specified
    """
    pass


class NSNitroNserrSslPkeyMinsize(NSNitroSsl2Errors):
    """
        Nitro error code 3590
        Certificate of size smaller than 512 bits not supported
    """
    pass


class NSNitroNserrSslSyncinprogress(NSNitroSsl2Errors):
    """
        Nitro error code 3591
        Another synchronization is already in process,  please try again
        later
    """
    pass


class NSNitroNserrSslSyncfailed(NSNitroSsl2Errors):
    """
        Nitro error code 3592
        Synchronization failed,  please try again
    """
    pass


class NSNitroNserrSslCiphgrpRefcnt(NSNitroSsl2Errors):
    """
        Nitro error code 3593
        Cipher group referenced by an SSL vserver or service
    """
    pass


class NSNitroNserrSslCvmNodsa(NSNitroSsl2Errors):
    """
        Nitro error code 3594
        Loading DSA(DSS) certificate and key not supported on this
        platform
    """
    pass


class NSNitroNserrCerthashheader(NSNitroSsl2Errors):
    """
        Nitro error code 3595
        CertHash header tag mandatory if certHash is enabled
    """
    pass


class NSNitroNserrSslCrlinrefresh(NSNitroSsl2Errors):
    """
        Nitro error code 3596
        CRL refresh in progress,  details cannot be displayed
    """
    pass


class NSNitroNserrSslCrlmemExceeds(NSNitroSsl2Errors):
    """
        Nitro error code 3597
        CRL memory exhausted. Cannot load any more CRL's
    """
    pass


class NSNitroNserrSslCrlindeletion(NSNitroSsl2Errors):
    """
        Nitro error code 3598
        CRL deletion in progress,  details cannot be displayed
    """
    pass


class NSNitroNserrSslIndeleteNorefresh(NSNitroSsl2Errors):
    """
        Nitro error code 3599
        CRL deletion in progress,  cannot be refreshed
    """
    pass


class NSNitroNserrSslInrefreshNodelete(NSNitroSsl2Errors):
    """
        Nitro error code 3600
        CRL refresh in progress,  cannot be removed
    """
    pass


class NSNitroNserrNomix(NSNitroSsl2Errors):
    """
        Nitro error code 3601
        Cannot specify both HTTP data insertion and SSL actions
    """
    pass


class NSNitroNserrNopolicyNontrsvc(NSNitroSsl2Errors):
    """
        Nitro error code 3602
        Cannot bind SSL policy to SSL backend service
    """
    pass


class NSNitroNserrSslSslpolBindConst(NSNitroSsl2Errors):
    """
        Nitro error code 3603
        Cannot bind non-SSL policy to SSL vserver/service
    """
    pass


class NSNitroNserrSslNoUsableCiphers(NSNitroSsl2Errors):
    """
        Nitro error code 3604
        No usable ciphers configured on the SSL vserver/service
    """
    pass


class NSNitroNserrSslCertNotCa(NSNitroSsl2Errors):
    """
        Nitro error code 3605
        Not a CA certificate
    """
    pass


class NSNitroNserrSslCacertNoCrlsign(NSNitroSsl2Errors):
    """
        Nitro error code 3606
        Specified certificate is either not a CA cert,  or does not have
        privileges to issue CRLs
    """
    pass


class NSNitroNserrSslCrlExpired(NSNitroSsl2Errors):
    """
        Nitro error code 3607
        CRL has expired
    """
    pass


class NSNitroNserrSslCrlNotyetValid(NSNitroSsl2Errors):
    """
        Nitro error code 3608
        CRL is not yet valid
    """
    pass


class NSNitroNserrSslParsingDeltaCrlExtn(NSNitroSsl2Errors):
    """
        Nitro error code 3609
        Parsing of Delta-CRL extension failed
    """
    pass


class NSNitroNserrSslDeltaCrlMissingBaseCrl(NSNitroSsl2Errors):
    """
        Nitro error code 3610
        Base-CRL for the specified Delta-CRL is missing
    """
    pass


class NSNitroNserrNofipscipher(NSNitroSsl2Errors):
    """
        Nitro error code 3611
        Specified cipher/cipher-alias is not FIPS-approved
    """
    pass


class NSNitroNserrNofipsciphergrp(NSNitroSsl2Errors):
    """
        Nitro error code 3612
        Cipher group does not contain all FIPS-approved ciphers
    """
    pass


class NSNitroNserrNonfipsciphertogrp(NSNitroSsl2Errors):
    """
        Nitro error code 3613
        Cannot add non FIPS approved cipher to cipher group
    """
    pass


class NSNitroNserrNonfipsaliastogrp(NSNitroSsl2Errors):
    """
        Nitro error code 3614
        Cannot add non FIPS approved cipher alias to cipher group
    """
    pass


class NSNitroNserrNonfipsgrouptogrp(NSNitroSsl2Errors):
    """
        Nitro error code 3615
        Cannot add non FIPS cipher group to another cipher group
    """
    pass


class NSNitroNserrSslImportFipskeyNameMismatch(NSNitroSsl2Errors):
    """
        Nitro error code 3616
        Specified FIPS key name does not match with the exported FIPS
        key name
    """
    pass


class NSNitroNserrSslPkeySizeCa(NSNitroSsl2Errors):
    """
        Nitro error code 3617
        CA certificate of size greater than 4096 bits not supported
    """
    pass


class NSNitroNserrSslCrlPortMismatch(NSNitroSsl2Errors):
    """
        Nitro error code 3618
        Port specified in URL does not match -port parameter
    """
    pass


class NSNitroNserrSslPkeySizeVpx(NSNitroSsl2Errors):
    """
        Nitro error code 3619
        Certificate with key size greater than RSA512 or DSA512 bits not
        supported
    """
    pass


class NSNitroNserrSslDhSizeVpx(NSNitroSsl2Errors):
    """
        Nitro error code 3620
        DH params of size greater than 512 bits not supported
    """
    pass


class NSNitroNserrNoentCipher(NSNitroSsl2Errors):
    """
        Nitro error code 3621
        No such cipher/cipherAlias/cipherGroup
    """
    pass


class NSNitroNserrFipsfwwrongmajor(NSNitroSsl2Errors):
    """
        Nitro error code 3622
        The current firmware's major version is not supported for update
        operation
    """
    pass


class NSNitroNserrFipsfwwrongminor(NSNitroSsl2Errors):
    """
        Nitro error code 3623
        The current firmware's minor version is not supported for update
        operation
    """
    pass


class NSNitroNserrFipsfwupdated(NSNitroSsl2Errors):
    """
        Nitro error code 3624
        The current firmware is already updated to 4.6.1
    """
    pass


class NSNitroNserrSslPendingCmds(NSNitroSsl2Errors):
    """
        Nitro error code 3625
        Other commands (card health monitoring/traffic) are pending to
        FIPS card. Please try the firmware update command after some
        time
    """
    pass


class NSNitroNserrFipsfwupdatedoreboot(NSNitroSsl2Errors):
    """
        Nitro error code 3626
        Operation not permitted - FIPS card firmware update done,
        please reboot the system
    """
    pass


class NSNitroNserrSslSniNotenable(NSNitroSsl2Errors):
    """
        Nitro error code 3627
        SNI feature not enabled on the vserver/service
    """
    pass


class NSNitroNserrSslNoCn(NSNitroSsl2Errors):
    """
        Nitro error code 3628
        CommonName not present in certificate,  it is must for a
        certificate to use for SNI
    """
    pass


class NSNitroNserrSslDupSnicert(NSNitroSsl2Errors):
    """
        Nitro error code 3629
        Trying to bind SNI certificate with duplicate CommonName,
        operation failed
    """
    pass


class NSNitroNserrSslSniNotvalidServ(NSNitroSsl2Errors):
    """
        Nitro error code 3630
        Operation not permitted - SNI feature not supported on SSL
        backend service
    """
    pass


class NSNitroNserrOcspReferences(NSNitroSsl2Errors):
    """
        Nitro error code 3632
        OCSP responder is bound to a vserver/certkey pair.  Use unbind
        ssl certkey.
    """
    pass


class NSNitroNserrOcspSignerNokey(NSNitroSsl2Errors):
    """
        Nitro error code 3633
        Signing certificate must also have a private key.
    """
    pass


class NSNitroNserrSslNotSupported(NSNitroSsl2Errors):
    """
        Nitro error code 3634
        OCSP responder must be an HTTP server; SSL is not supported.
    """
    pass


class NSNitroNserrOcspTooManyResponders(NSNitroSsl2Errors):
    """
        Nitro error code 3635
        Too many OCSP responders configured to add another.  Please
        delete some and try again.
    """
    pass


class NSNitroNserrOcspNoDnsServerConfigured(NSNitroSsl2Errors):
    """
        Nitro error code 3636
        Unable to resolve DNS name.
    """
    pass


class NSNitroNserrSslDupSnicertBrklink(NSNitroSsl2Errors):
    """
        Nitro error code 3637
        Some of the existing SNI cert bindings are broken due to
        presence of certificate with duplicate Common Name.
    """
    pass


class NSNitroNserrSslNoCnBrllink(NSNitroSsl2Errors):
    """
        Nitro error code 3638
        All exitsing SNI Cert bindings are broken during update
        operation due to missing Common Name.
    """
    pass


class NSNitroNserrNgfipsresetreboot(NSNitroSsl2Errors):
    """
        Nitro error code 3639
        Operation not permitted - FIPS card was reset,  please reboot
        the system
    """
    pass


class NSNitroNserrNgfipsinitreboot(NSNitroSsl2Errors):
    """
        Nitro error code 3640
        Operation not permitted - FIPS card was initialized,  please
        reboot the system
    """
    pass


class NSNitroNserrFipscmdtimeout(NSNitroSsl2Errors):
    """
        Nitro error code 3641
        Operation timedout on the FIPS card,  please try again
    """
    pass


class NSNitroNserrSslSimtimeout(NSNitroSsl2Errors):
    """
        Nitro error code 3642
        Operation timed out or repeated,  please wait for 10 mins and
        redo the SIM/HA configuration steps.
    """
    pass


class NSNitroNserrSslNgfipsQfull(NSNitroSsl2Errors):
    """
        Nitro error code 3643
        FIPS card command queue full. Please try again later
    """
    pass


class NSNitroNserrSslNomemVsvrsrvlistnode(NSNitroSsl2Errors):
    """
        Nitro error code 3644
        Failed to allocate memory for CertkeyVserverServList Node.
    """
    pass


class NSNitroNserrSslCertkeySize64(NSNitroSsl2Errors):
    """
        Nitro error code 3645
        Certificate with key size (modulus) that is not multiple of 512
        bits is not supported
    """
    pass


class NSNitroNserrSniAtk(NSNitroSsl2Errors):
    """
        Nitro error code 3646
        Host header field in the HTTP request does not match with the
        SNI domain name
    """
    pass


class NSNitroNserrSniNohosthdr(NSNitroSsl2Errors):
    """
        Nitro error code 3647
        Host header missing in the HTTP header for SNI enabled session
    """
    pass


class NSNitroNserrCrlShmemAllocFail(NSNitroSsl2Errors):
    """
        Nitro error code 3648
        Crl node allocation in the shared mem is failed
    """
    pass


class NSNitroNserrSslCertMissingParam(NSNitroSsl2Errors):
    """
        Nitro error code 3655
        Required parameters missing in the certificate. Please check the
        certificate for completeness
    """
    pass


class NSNitroNserrSslNomemCertkeyOcsprespListnode(NSNitroSsl2Errors):
    """
        Nitro error code 3656
        Failed to allocate memory for CertkeyOCSPRespList Node.
    """
    pass


class NSNitroNserrSslBundleIcFileExists(NSNitroSsl2Errors):
    """
        Nitro error code 3657
        Certificate file for intermediate certificate already exists.
    """
    pass


class NSNitroNserrSslBundleScertMissing(NSNitroSsl2Errors):
    """
        Nitro error code 3658
        Server certificate must be placed first in certificate bundle
        file.
    """
    pass


class NSNitroNserrSslBundleCertMissing(NSNitroSsl2Errors):
    """
        Nitro error code 3659
        No certificates present in the certificate bundle file.
    """
    pass


class NSNitroNserrSslBundleFailed(NSNitroSsl2Errors):
    """
        Nitro error code 3660
        Processing of certificate bundle file failed.
    """
    pass


class NSNitroNserrSslBundleParseErr(NSNitroSsl2Errors):
    """
        Nitro error code 3661
        Unable to parse the certificate bundle file.
    """
    pass


class NSNitroNserrSslBundleMaxCert(NSNitroSsl2Errors):
    """
        Nitro error code 3662
        Exceeded maximum Intermediate certificates limit of 9.
    """
    pass


class NSNitroNserrSslBundleMaxKey(NSNitroSsl2Errors):
    """
        Nitro error code 3663
        Only one private-key is allowed in the certificate bundle file.
    """
    pass


class NSNitroNserrSslBundleIcFileCreateFailed(NSNitroSsl2Errors):
    """
        Nitro error code 3664
        Intermediate certificate file creation failed.
    """
    pass


class NSNitroNserrSslIssuerMismatch(NSNitroSsl2Errors):
    """
        Nitro error code 3668
        Certificate Issuer mismatch
    """
    pass


class NSNitroGentoolErrors(NSNitroError):
    """
        Base exception class NSNitroGentoolErrors
    """
    pass


class NSNitroNserrSslConffile(NSNitroGentoolErrors):
    """
        Nitro error code 1601
        Error in SSL conf file
    """
    pass


class NSNitroNserrSslNoconffile(NSNitroGentoolErrors):
    """
        Nitro error code 1602
        Unable to load SSL configuration info
    """
    pass


class NSNitroNserrSslSigfail(NSNitroGentoolErrors):
    """
        Nitro error code 1603
        Signing operation failed
    """
    pass


class NSNitroNserrSslInvalformat(NSNitroGentoolErrors):
    """
        Nitro error code 1604
        Invalid format
    """
    pass


class NSNitroNserrSslOutfile(NSNitroGentoolErrors):
    """
        Nitro error code 1605
        Problem in writing output file
    """
    pass


class NSNitroNserrSslVerifyFail(NSNitroGentoolErrors):
    """
        Nitro error code 1606
        Signature verification failed
    """
    pass


class NSNitroNserrSslFilecreate(NSNitroGentoolErrors):
    """
        Nitro error code 1607
        Unable to create output file
    """
    pass


class NSNitroNserrSslMinkeysize(NSNitroGentoolErrors):
    """
        Nitro error code 1608
        Key size is less than the minimum value 512
    """
    pass


class NSNitroNserrSslInvalidReq(NSNitroGentoolErrors):
    """
        Nitro error code 1609
        Invalid certificate request
    """
    pass


class NSNitroNserrSslGentool(NSNitroGentoolErrors):
    """
        Nitro error code 1610
        Internal failure in SSL cert/key generation tool
    """
    pass


class NSNitroNserrSslPemOnly(NSNitroGentoolErrors):
    """
        Nitro error code 1611
        Only PEM format private key can be encrypted
    """
    pass


class NSNitroNserrSslPassmismatch(NSNitroGentoolErrors):
    """
        Nitro error code 1612
        Password verification failed
    """
    pass


class NSNitroNserrSslPassreq(NSNitroGentoolErrors):
    """
        Nitro error code 1613
        Password required for private key
    """
    pass


class NSNitroNserrSslInvalpass(NSNitroGentoolErrors):
    """
        Nitro error code 1614
        Invalid password
    """
    pass


class NSNitroNserrSslMaxkeysize(NSNitroGentoolErrors):
    """
        Nitro error code 1615
        Maximum allowed key size is 2048
    """
    pass


class NSNitroNserrSslGntoolargMissing(NSNitroGentoolErrors):
    """
        Nitro error code 1616
        Required argument missing
    """
    pass


class NSNitroNserrSslInvalPubexp(NSNitroGentoolErrors):
    """
        Nitro error code 1617
        Invalid public exponent value
    """
    pass


class NSNitroNserrSslInvalidValue(NSNitroGentoolErrors):
    """
        Nitro error code 1618
        Invalid value
    """
    pass


class NSNitroNserrSslMissingKval(NSNitroGentoolErrors):
    """
        Nitro error code 1619
         Value missing for the argument
    """
    pass


class NSNitroNserrSslInvalDhgen(NSNitroGentoolErrors):
    """
        Nitro error code 1620
        Invalid DH generator value
    """
    pass


class NSNitroNserrSslNofileCertreq(NSNitroGentoolErrors):
    """
        Nitro error code 1621
        No such certificate request file exists
    """
    pass


class NSNitroNserrSslReqNomatch(NSNitroGentoolErrors):
    """
        Nitro error code 1622
        Certificate Request (CSR) and private key do not match
    """
    pass


class NSNitroNserrSslPkcs12(NSNitroGentoolErrors):
    """
        Nitro error code 1623
        Problem in input PKCS12 file
    """
    pass


class NSNitroNserrSslNofileCapvtkey(NSNitroGentoolErrors):
    """
        Nitro error code 1624
        No such CA key file present
    """
    pass


class NSNitroNserrSslNofileCacert(NSNitroGentoolErrors):
    """
        Nitro error code 1625
        No such CA certificate file exists
    """
    pass


class NSNitroNserrSslNofileSerial(NSNitroGentoolErrors):
    """
        Nitro error code 1626
        No such serial file exists
    """
    pass


class NSNitroNserrSslNofilePkcs12(NSNitroGentoolErrors):
    """
        Nitro error code 1627
        No such PKCS12 file exists
    """
    pass


class NSNitroNserrSslReadCacert(NSNitroGentoolErrors):
    """
        Nitro error code 1628
        In reading input CA certficate file
    """
    pass


class NSNitroNserrReadCert(NSNitroGentoolErrors):
    """
        Nitro error code 1629
        Error in reading input certficate file
    """
    pass


class NSNitroNserrImpExpNotTogether(NSNitroGentoolErrors):
    """
        Nitro error code 1630
        Import and export can not be specified together
    """
    pass


class NSNitroNserrNofileCert(NSNitroGentoolErrors):
    """
        Nitro error code 1631
        No such certificate file exists
    """
    pass


class NSNitroNserrNofileKey(NSNitroGentoolErrors):
    """
        Nitro error code 1632
        No such key file exists
    """
    pass


class NSNitroNserrCacertpkeyMismatch(NSNitroGentoolErrors):
    """
        Nitro error code 1633
        CA certificate not matching with CA private-key
    """
    pass


class NSNitroNserrWrongRevEntry(NSNitroGentoolErrors):
    """
        Nitro error code 1634
        Invalid revocation entry in CA's database
    """
    pass


class NSNitroNserrWrongRevDate(NSNitroGentoolErrors):
    """
        Nitro error code 1635
        Invalid revocation data in CA's database
    """
    pass


class NSNitroNserrWrongSerialNo(NSNitroGentoolErrors):
    """
        Nitro error code 1636
        Invalid serial number in CA's database
    """
    pass


class NSNitroNserrCreateDatabaseEntry(NSNitroGentoolErrors):
    """
        Nitro error code 1637
        Revocation entry creation failed
    """
    pass


class NSNitroNserrAlreadyRevkd(NSNitroGentoolErrors):
    """
        Nitro error code 1638
        Certificate already revoked
    """
    pass


class NSNitroNserrLoadPkey(NSNitroGentoolErrors):
    """
        Nitro error code 1639
        Private key loading failed
    """
    pass


class NSNitroNserrCertpkeyNeeded(NSNitroGentoolErrors):
    """
        Nitro error code 1640
        Both certificate and private key are needed for export
    """
    pass


class NSNitroNserrPkcs12Needed(NSNitroGentoolErrors):
    """
        Nitro error code 1641
        PKCS12 file missing for import
    """
    pass


class NSNitroNserrErrFileexists(NSNitroGentoolErrors):
    """
        Nitro error code 1642
        Cannot create output file. File already exists
    """
    pass


class NSNitroNserrFipskeyKeyfileOption(NSNitroGentoolErrors):
    """
        Nitro error code 1643
        Both -keyFileName and -fipsKeyName cannot be specified
    """
    pass


class NSNitroNserrOutfilelenbig(NSNitroGentoolErrors):
    """
        Nitro error code 1644
        Output file name too long
    """
    pass


class NSNitroNserrSslDefpath(NSNitroGentoolErrors):
    """
        Nitro error code 1645
        Output filepath should be under the default directory
        /nsconfig/ssl/
    """
    pass


class NSNitroNserrSslCrlDefpath(NSNitroGentoolErrors):
    """
        Nitro error code 1646
        Output CRL filepath should be under the default directory
        /var/netscaler/ssl/
    """
    pass


class NSNitroNserrSslDeflocation(NSNitroGentoolErrors):
    """
        Nitro error code 1647
        Input file(s) not present under the default directory
        /nsconfig/ssl/
    """
    pass


class NSNitroNserrDhreqd(NSNitroGentoolErrors):
    """
        Nitro error code 1791
        DH required
    """
    pass


class NSNitroNserrSslCrlDeflocation(NSNitroGentoolErrors):
    """
        Nitro error code 1650
        Input CRL file not present under the default directory
        /var/netscaler/ssl/
    """
    pass


class NSNitroNserrSslNofipsKey(NSNitroGentoolErrors):
    """
        Nitro error code 1651
        No such FIPS key
    """
    pass


class NSNitroNserrSslImproperSerialfile(NSNitroGentoolErrors):
    """
        Nitro error code 1652
        Invalid serial file
    """
    pass


class NSNitroNserrSslSerialNumRevoked(NSNitroGentoolErrors):
    """
        Nitro error code 1653
        Certificate serial number match with another certificate already
        revoked in the CRL
    """
    pass


class NSNitroNserrSslMaxrsakeysize(NSNitroGentoolErrors):
    """
        Nitro error code 1654
        Maximum allowed key size is 4096
    """
    pass


class NSNitroNserrSslMustbepem(NSNitroGentoolErrors):
    """
        Nitro error code 1655
        The input file must be in PEM or SIM format.
    """
    pass


class NSNitroNserrSslCantbepem(NSNitroGentoolErrors):
    """
        Nitro error code 1656
        The input file cannot be in PEM format.
    """
    pass


class NSNitroNserrSslBadLabel(NSNitroGentoolErrors):
    """
        Nitro error code 1657
        The keylabel cannot be 'public' or 'private'.
    """
    pass


class NSNitroGslbErrors(NSNitroError):
    """
        Base exception class NSNitroGslbErrors
    """
    pass


class NSNitroNserrBadDnsOption(NSNitroGslbErrors):
    """
        Nitro error code 1792
        Invalid DNS option specified
    """
    pass


class NSNitroNserrDnsBadCachetype(NSNitroGslbErrors):
    """
        Nitro error code 1793
        Only forward cache type can bind to DNS vserver
    """
    pass


class NSNitroNserrDnsNotavail(NSNitroGslbErrors):
    """
        Nitro error code 1794
        No such DNS vserver exists
    """
    pass


class NSNitroNserrDnsBadVstype(NSNitroGslbErrors):
    """
        Nitro error code 1795
        DNS vserver can only be address-based
    """
    pass


class NSNitroNserrGslbSitelkupFailed(NSNitroGslbErrors):
    """
        Nitro error code 1796
        GSLB site not found
    """
    pass


class NSNitroNserrNoarec(NSNitroGslbErrors):
    """
        Nitro error code 1801
        Address record for host name not available
    """
    pass


class NSNitroNserrInvalttl(NSNitroGslbErrors):
    """
        Nitro error code 1806
        Invalid TTL value
    """
    pass


class NSNitroNserrCnameexists(NSNitroGslbErrors):
    """
        Nitro error code 1807
        Alias name record exists for the host name
    """
    pass


class NSNitroNserrInvalSvcoption(NSNitroGslbErrors):
    """
        Nitro error code 1808
        Option not applicable for this service
    """
    pass


class NSNitroNserrGslbbindExists(NSNitroGslbErrors):
    """
        Nitro error code 1809
        GSLB binding exists for the given host
    """
    pass


class NSNitroNserrNotLocalremote(NSNitroGslbErrors):
    """
        Nitro error code 1810
        Site information must be specified for a GSLB service
    """
    pass


class NSNitroNserrCountMismatch(NSNitroGslbErrors):
    """
        Nitro error code 1811
        Address record count does not match the number of services bound
        to the GSLB vserver
    """
    pass


class NSNitroNserrIpMismatch(NSNitroGslbErrors):
    """
        Nitro error code 1812
        IP addresses of bound GSLB services and the address records do
        not match
    """
    pass


class NSNitroNserrSvcipRepeat(NSNitroGslbErrors):
    """
        Nitro error code 1813
        A GSLB service with the same IP address is already bound to the
        GSLB vserver
    """
    pass


class NSNitroNserrNotRemote(NSNitroGslbErrors):
    """
        Nitro error code 1814
        Service bound to GSLB VIP with -gslb remote is a local service
    """
    pass


class NSNitroNserrNotLocal(NSNitroGslbErrors):
    """
        Nitro error code 1815
        Service bound to GSLB VIP with -gslb local is not a local
        service
    """
    pass


class NSNitroNserrProxyRec(NSNitroGslbErrors):
    """
        Nitro error code 1816
        A proxy record cannot be assigned to the domain
    """
    pass


class NSNitroNserrNoproxyArec(NSNitroGslbErrors):
    """
        Nitro error code 1817
        Proxy address records cannot be bound to a GSLB vserver
    """
    pass


class NSNitroNserrSvcGslbbindExists(NSNitroGslbErrors):
    """
        Nitro error code 1819
        GSLB binding exists - unbind the GSLB vserver first
    """
    pass


class NSNitroNserrSvctypemismatch(NSNitroGslbErrors):
    """
        Nitro error code 1820
        Service type mismatch with existing service/vserver
    """
    pass


class NSNitroNserrInvalidPubipOption(NSNitroGslbErrors):
    """
        Nitro error code 1822
        The public IP and public port are valid only for GSLB local
        service
    """
    pass


class NSNitroNserrInvalNameSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1823
        Invalid domain name syntax
    """
    pass


class NSNitroNserrGslbBackup(NSNitroGslbErrors):
    """
        Nitro error code 1824
        Backup VIP is backup of other GSLB VIP. Please unset the
        existing association and try again
    """
    pass


class NSNitroNserrIsBackup(NSNitroGslbErrors):
    """
        Nitro error code 1825
        Backup VIP is backup of other VIP. Please unset the existing
        association and try again
    """
    pass


class NSNitroNserrGslbHasBackup(NSNitroGslbErrors):
    """
        Nitro error code 1826
        GSLB VIP has a backup. Please unset the backup and try the
        operation again
    """
    pass


class NSNitroNserrGslbRequiresIndependentBackup(NSNitroGslbErrors):
    """
        Nitro error code 1827
        Backup VIP to GSLB VIP must not be backup of any other VIP.
        Please unset the backup and try the operation again
    """
    pass


class NSNitroNserrGslbNoqualifier(NSNitroGslbErrors):
    """
        Nitro error code 1828
        At least one qualifier should be given for the location
    """
    pass


class NSNitroNserrGslbNoname(NSNitroGslbErrors):
    """
        Nitro error code 1829
        The qualifier does not exist in the repository
    """
    pass


class NSNitroNserrGslbCustomNospace(NSNitroGslbErrors):
    """
        Nitro error code 1830
        Too many custom locations
    """
    pass


class NSNitroNserrGslbStaticNospace(NSNitroGslbErrors):
    """
        Nitro error code 1836
        Too many static locations
    """
    pass


class NSNitroNserrGslbsitenameExists(NSNitroGslbErrors):
    """
        Nitro error code 1831
        A GSLB site with the same name exists
    """
    pass


class NSNitroNserrGslbsiteipExists(NSNitroGslbErrors):
    """
        Nitro error code 1832
        A GSLB site with the same IP address exists
    """
    pass


class NSNitroNserrNoGslbsite(NSNitroGslbErrors):
    """
        Nitro error code 1833
        The GSLB site does not exist
    """
    pass


class NSNitroNserrLocalExists(NSNitroGslbErrors):
    """
        Nitro error code 1834
        The local site already exists
    """
    pass


class NSNitroNserrNoGslbsvc(NSNitroGslbErrors):
    """
        Nitro error code 1835
        The GSLB service does not exist
    """
    pass


class NSNitroNserrNoGslbvip(NSNitroGslbErrors):
    """
        Nitro error code 1837
        The GSLB vserver does not exist
    """
    pass


class NSNitroNserrNoDmn(NSNitroGslbErrors):
    """
        Nitro error code 1839
        The domain does not exist
    """
    pass


class NSNitroNserrDmnNotbound(NSNitroGslbErrors):
    """
        Nitro error code 1840
        The domain is not bound to this VIP
    """
    pass


class NSNitroNserrGslbdomainBound(NSNitroGslbErrors):
    """
        Nitro error code 1842
        The domain is already bound to a GSLB vserver
    """
    pass


class NSNitroNserrNotGslbent(NSNitroGslbErrors):
    """
        Nitro error code 1844
        Operation not permitted on a non-GSLB entity
    """
    pass


class NSNitroNserrGslbdomainPerm(NSNitroGslbErrors):
    """
        Nitro error code 1845
        Operation not permitted on a GSLB-configured domain
    """
    pass


class NSNitroNserrGslbMaxqual(NSNitroGslbErrors):
    """
        Nitro error code 1846
        Maximum qualifiers allowed is six
    """
    pass


class NSNitroNserrGslbMaxloclength(NSNitroGslbErrors):
    """
        Nitro error code 1847
        Maximum allowed location length is 256 characters
    """
    pass


class NSNitroNserrGslbvipPerm(NSNitroGslbErrors):
    """
        Nitro error code 1848
        Operation not permitted on a GSLB vserver
    """
    pass


class NSNitroNserrGslbsvcPerm(NSNitroGslbErrors):
    """
        Nitro error code 1849
        Operation not permitted on a GSLB service
    """
    pass


class NSNitroNserrGslbMaxsites(NSNitroGslbErrors):
    """
        Nitro error code 1850
        Maximum number of sites is 32
    """
    pass


class NSNitroNserrGslbQualtoolong(NSNitroGslbErrors):
    """
        Nitro error code 1851
        The qualifier is too long
    """
    pass


class NSNitroNserrGslbPersistidexists(NSNitroGslbErrors):
    """
        Nitro error code 1852
        The persistence ID is already being used by a GSLB vserver
    """
    pass


class NSNitroNserrGslbInvldLdnstoIntvl(NSNitroGslbErrors):
    """
        Nitro error code 1854
        Minimum LDNS entry timeout interval is 30 secs
    """
    pass


class NSNitroNserrVipBackupIsgslb(NSNitroGslbErrors):
    """
        Nitro error code 1856
        GSLB vserver cannot be backup of a non-GSLB vserver
    """
    pass


class NSNitroNserrGslbPubipPubportExists(NSNitroGslbErrors):
    """
        Nitro error code 1857
        The public IP and public port are being used by another GSLB
        service
    """
    pass


class NSNitroNserrGslblocalsvcEnadisNotallowed(NSNitroGslbErrors):
    """
        Nitro error code 1858
        GSLB local service status not changed - please enable or disable
        the corresponding LB vserver instead
    """
    pass


class NSNitroNserrGslblocalsvrEnadisNotallowed(NSNitroGslbErrors):
    """
        Nitro error code 1859
        Server status not changed - the server has a GSLB local service
    """
    pass


class NSNitroNserrInvalidPersistid(NSNitroGslbErrors):
    """
        Nitro error code 1860
        Invalid persistence ID
    """
    pass


class NSNitroNserrPermPersistid(NSNitroGslbErrors):
    """
        Nitro error code 1861
        The persistence ID is required for persistence or spillover-
        persistency to be set
    """
    pass


class NSNitroNserrInvalidLocalsiteip(NSNitroGslbErrors):
    """
        Nitro error code 1862
        Invalid GSLB local site IP address
    """
    pass


class NSNitroNserrInvalidRemotesiteip(NSNitroGslbErrors):
    """
        Nitro error code 1863
        Invalid GSLB remote site IP address
    """
    pass


class NSNitroNserrInvalidSitetype(NSNitroGslbErrors):
    """
        Nitro error code 1864
        Invalid GSLB site type
    """
    pass


class NSNitroNserrInvalidBackupip(NSNitroGslbErrors):
    """
        Nitro error code 1865
        Invalid backup IP for the GSLB domain
    """
    pass


class NSNitroNserrGslbvipMaxsvc(NSNitroGslbErrors):
    """
        Nitro error code 1866
        Cannot bind more than 32 services to a GSLB vserver
    """
    pass


class NSNitroNserrInvalidJitter(NSNitroGslbErrors):
    """
        Nitro error code 1867
        RTT tolerance value must be between 1 and 100
    """
    pass


class NSNitroNserrGslblocsvcDisNotallowd(NSNitroGslbErrors):
    """
        Nitro error code 1868
        Cannot add GSLB local service with state set to DISABLED
    """
    pass


class NSNitroNserrDummybkupNotallowd(NSNitroGslbErrors):
    """
        Nitro error code 1869
        A backup vserver with no IP address and port must be of type
        GSLB
    """
    pass


class NSNitroNserrGslbsvcBindNotallowd(NSNitroGslbErrors):
    """
        Nitro error code 1870
        Cannot bind GSLB service to a vserver with valid IP and port
    """
    pass


class NSNitroNserrNsmapVersion(NSNitroGslbErrors):
    """
        Nitro error code 1871
        Unrecognized NetScaler file version
    """
    pass


class NSNitroNserrNsmapFormat(NSNitroGslbErrors):
    """
        Nitro error code 1872
        Unrecognized file format specified
    """
    pass


class NSNitroNserrNsmapEof(NSNitroGslbErrors):
    """
        Nitro error code 1873
        End of file has been reached
    """
    pass


class NSNitroNserrNsmapParse(NSNitroGslbErrors):
    """
        Nitro error code 1874
        File parsing error
    """
    pass


class NSNitroNserrNsmapRead(NSNitroGslbErrors):
    """
        Nitro error code 1875
        Error reading file
    """
    pass


class NSNitroNserrNsmapWrite(NSNitroGslbErrors):
    """
        Nitro error code 1876
        Error writing file
    """
    pass


class NSNitroNserrNsmapIoctl(NSNitroGslbErrors):
    """
        Nitro error code 1877
        Error occurred while transferring information to NetScaler
    """
    pass


class NSNitroNserrNsmapOutputfile(NSNitroGslbErrors):
    """
        Nitro error code 1878
        Error opening output file for writing
    """
    pass


class NSNitroNserrNsmapInputfile(NSNitroGslbErrors):
    """
        Nitro error code 1879
        Error opening input file for reading
    """
    pass


class NSNitroNserrNsmapRequiredField(NSNitroGslbErrors):
    """
        Nitro error code 1880
        Required field missing
    """
    pass


class NSNitroNserrNsmapDbfile(NSNitroGslbErrors):
    """
        Nitro error code 1881
        Error opening database file
    """
    pass


class NSNitroNserrNsmapDbinsert(NSNitroGslbErrors):
    """
        Nitro error code 1882
        Error inserting entry into the database
    """
    pass


class NSNitroNserrNsmapDbsearch(NSNitroGslbErrors):
    """
        Nitro error code 1883
        Error searching the database
    """
    pass


class NSNitroNserrGslbproxmLicenceAbsent(NSNitroGslbErrors):
    """
        Nitro error code 1884
        Cannot set proximity methods without GSLB proximity license
    """
    pass


class NSNitroNserrGslbSitepersistenceHttponly(NSNitroGslbErrors):
    """
        Nitro error code 1885
        Site persistence is valid only for HTTP or SSL GSLB services
    """
    pass


class NSNitroNserrGslbNositepfx(NSNitroGslbErrors):
    """
        Nitro error code 1886
        Site prefix compulsory if site persistence is HTTPRedirect
    """
    pass


class NSNitroNserrGslbSiteprefixSize(NSNitroGslbErrors):
    """
        Nitro error code 1888
        Site prefix size exceeds maximum
    """
    pass


class NSNitroNserrGslbSitedomainSize(NSNitroGslbErrors):
    """
        Nitro error code 1889
        Site domain cannot be created - name length exceeds maximum
    """
    pass


class NSNitroNserrGslbSitedomainSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1890
        Site domain cannot be created - name is invalid
    """
    pass


class NSNitroNserrGslbSitedomainRefers(NSNitroGslbErrors):
    """
        Nitro error code 1891
        Site domain cannot be deleted - it has external DNS references
    """
    pass


class NSNitroNserrGslbdomainRefers(NSNitroGslbErrors):
    """
        Nitro error code 1892
        GSLB domain cannot be deleted - it has external DNS references
    """
    pass


class NSNitroNserrGslbArecordExists(NSNitroGslbErrors):
    """
        Nitro error code 1893
        GSLB record cannot be created - another A record is configured
        with the same name
    """
    pass


class NSNitroNserrGslbSitecookieTimeoutRange(NSNitroGslbErrors):
    """
        Nitro error code 1894
        Invalid GSLB site cookie timeout
    """
    pass


class NSNitroNserrGslbdomainSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1895
        GSLB domain cannot be created - name is invalid
    """
    pass


class NSNitroNserrGslbSoPerm(NSNitroGslbErrors):
    """
        Nitro error code 1896
        Spill-over cannot be set on a GSLB vserver
    """
    pass


class NSNitroNserrGslbDeprcookietout(NSNitroGslbErrors):
    """
        Nitro error code 1897
        Ignored deprecated cookietimeout setting since it has been made
        a per-domain configuration
    """
    pass


class NSNitroNserrDnsNamesvrSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1898
        Invalid name server syntax
    """
    pass


class NSNitroNserrDnsOrigsvrSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1899
        Invalid origin server syntax
    """
    pass


class NSNitroNserrDnsContactSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1900
        Invalid contact name syntax
    """
    pass


class NSNitroNserrDnsMxSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1901
        Invalid mail exchange syntax
    """
    pass


class NSNitroNserrDnsCnameSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1902
        Invalid canonical name syntax
    """
    pass


class NSNitroNserrDnsAliasSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1904
        Invalid alias name syntax
    """
    pass


class NSNitroNserrGslbNolocalvip(NSNitroGslbErrors):
    """
        Nitro error code 1905
        Cannot create GSLB local service - add the local vserver first
    """
    pass


class NSNitroNserrGslbLocalsvcexists(NSNitroGslbErrors):
    """
        Nitro error code 1906
        Cannot delete the vserver - corresponding GSLB local service
        still exists
    """
    pass


class NSNitroNserrGslblocalsvcPerm(NSNitroGslbErrors):
    """
        Nitro error code 1907
        Operation not permitted on GSLB local service
    """
    pass


class NSNitroNserrDnsInvalRevdomnameSyntax(NSNitroGslbErrors):
    """
        Nitro error code 1908
        Invalid reverse domain name syntax
    """
    pass


class NSNitroNserrDnsAliasrec(NSNitroGslbErrors):
    """
        Nitro error code 1909
        Alias name cannot have any record
    """
    pass


class NSNitroNserrGslblocsvcDelayedcleanNotallowd(NSNitroGslbErrors):
    """
        Nitro error code 1910
        Down state flush cannot be set on GSLB local service
    """
    pass


class NSNitroNserrNoBkpVip(NSNitroGslbErrors):
    """
        Nitro error code 1911
        Set a backup Vserver,  to enable it.
    """
    pass


class NSNitroNserrGslbNosuchLdnsentry(NSNitroGslbErrors):
    """
        Nitro error code 1912
        LDNS entry not present
    """
    pass


class NSNitroNserrMaxDnsView(NSNitroGslbErrors):
    """
        Nitro error code 1913
        Number of DNS views exceeds limit
    """
    pass


class NSNitroNserrGslbSiteIpExists(NSNitroGslbErrors):
    """
        Nitro error code 1914
        GSLB Site IP already exists
    """
    pass


class NSNitroNserrGslbLastMip(NSNitroGslbErrors):
    """
        Nitro error code 1915
        MIP is not removed. At least one MIP is required
    """
    pass


class NSNitroNserrRmGslbSite(NSNitroGslbErrors):
    """
        Nitro error code 1916
        IP cannot be removed as it is being used by the GSLB local site
    """
    pass


class NSNitroNserrGslbIprmLastMip(NSNitroGslbErrors):
    """
        Nitro error code 1917
        GSLB Site IP removed. MIP is not removed. At least one MIP is
        required
    """
    pass


class NSNitroNserrGslbSvcPubPortErr(NSNitroGslbErrors):
    """
        Nitro error code 1918
        Cannot modify public port for remote GSLB service
    """
    pass


class NSNitroNserrRecHasRef(NSNitroGslbErrors):
    """
        Nitro error code 1919
        DNS record has references
    """
    pass


class NSNitroNserrDnsViewRef(NSNitroGslbErrors):
    """
        Nitro error code 1920
        The dns view cannot be removed as it has dependencies
    """
    pass


class NSNitroNserrGslbSitePersistenceMatch(NSNitroGslbErrors):
    """
        Nitro error code 1921
        Mismatch in gslb site persistence type with other bound services
    """
    pass


class NSNitroNserrGslbSitePersistenceConflicts(NSNitroGslbErrors):
    """
        Nitro error code 1922
        Site persistence  conflicts with other services bound to the
        gslb vip(s)
    """
    pass


class NSNitroNserrDnsPolicyInval(NSNitroGslbErrors):
    """
        Nitro error code 1923
        Invalid DNS policy
    """
    pass


class NSNitroNserrGslbvipCnameMismatch(NSNitroGslbErrors):
    """
        Nitro error code 1924
        GSLB vserver cannot be bound with cname based and ip based
        services at the same time
    """
    pass


class NSNitroNserrGslbvipCnameUnsupportedLbmethods(NSNitroGslbErrors):
    """
        Nitro error code 1925
        GSLB vserver having cname services cannot have dynamic load
        balancing methods
    """
    pass


class NSNitroNserrGslbServiceMonNoipport(NSNitroGslbErrors):
    """
        Nitro error code 1926
        Cannot bind monitor with zero ip or  port to a cname gslb
        service
    """
    pass


class NSNitroNserrGslbServiceMonSetNoipport(NSNitroGslbErrors):
    """
        Nitro error code 1927
        Cannot set ip or port to zero when monitor is bound to a cname
        gslb service.
    """
    pass


class NSNitroNserrGslbCnameServiceSet(NSNitroGslbErrors):
    """
        Nitro error code 1928
        Setting of these parameters on cname gslb service is not allowed
    """
    pass


class NSNitroNserrGslbCnameVserverSet(NSNitroGslbErrors):
    """
        Nitro error code 1929
        Setting of these parameters on gslb vserver having cname
        services is not allowed
    """
    pass


class NSNitroNserrGslbvipCnameUnsupportedBkupLbmethods(NSNitroGslbErrors):
    """
        Nitro error code 1930
        GSLB vserver having cname services cannot have dynamic backup
        load balancing methods
    """
    pass


class NSNitroNserrGslbvipCnameUnsupportedEdr(NSNitroGslbErrors):
    """
        Nitro error code 1931
        GSLB vserver having cname services cannot have empty down
        response disabled
    """
    pass


class NSNitroNserrGslbvipCnameUnsupportedMir(NSNitroGslbErrors):
    """
        Nitro error code 1932
        GSLB vserver having cname services cannot have multiple ip
        response enabled
    """
    pass


class NSNitroNserrGslbsvcViewNexist(NSNitroGslbErrors):
    """
        Nitro error code 1933
        View is not bound to the GSLB service
    """
    pass


class NSNitroNserrDnsTtlMoreThanMaxAllowed(NSNitroGslbErrors):
    """
        Nitro error code 1934
        DNS RECORD TTL value greater than max TTL allowed
    """
    pass


class NSNitroNserrGslbLbMaxsites(NSNitroGslbErrors):
    """
        Nitro error code 1935
        Maximum number of LB sites is 1024
    """
    pass


class NSNitroNserrGslbHaschildren(NSNitroGslbErrors):
    """
        Nitro error code 1936
        Cannot remove site that has child site(s)
    """
    pass


class NSNitroNserrGslbParentischild(NSNitroGslbErrors):
    """
        Nitro error code 1937
        Parent site cannot be a child to another site
    """
    pass


class NSNitroNserrMaxRltSelectors(NSNitroGslbErrors):
    """
        Nitro error code 1938
        Number of limit selectors exceeds limit
    """
    pass


class NSNitroNserrMaxRltIdentifers(NSNitroGslbErrors):
    """
        Nitro error code 1939
        Number of limit identifiers exceeds limit
    """
    pass


class NSNitroNserrNoSuchSelector(NSNitroGslbErrors):
    """
        Nitro error code 1940
        The given selector does not exist
    """
    pass


class NSNitroNserrNoSuchIdentifier(NSNitroGslbErrors):
    """
        Nitro error code 1941
        The given identifier does not exist
    """
    pass


class NSNitroNserrRltTimesliceInvalidVal(NSNitroGslbErrors):
    """
        Nitro error code 1942
        Time slice should be a multiple of 10
    """
    pass


class NSNitroNserrIllegalSubnetMask(NSNitroGslbErrors):
    """
        Nitro error code 1943
        Incorrect subnet mask value
    """
    pass


class NSNitroNserrRltSelectorInuse(NSNitroGslbErrors):
    """
        Nitro error code 1944
        The selector is being referenced by one or more limit
        identifiers
    """
    pass


class NSNitroNserrRltIdentifierInuse(NSNitroGslbErrors):
    """
        Nitro error code 1945
        The identifier is being referenced by one or more policies
    """
    pass


class NSNitroNserrRltSelectorCannotChangeAttribType(NSNitroGslbErrors):
    """
        Nitro error code 1946
        Cannot change request type selector to response type
    """
    pass


class NSNitroNserrGslbIgnTrigmon(NSNitroGslbErrors):
    """
        Nitro error code 1947
        Trigger monitor setting assumed ALWAYS for GSLB local site
    """
    pass


class NSNitroNserrRltSelectorNotMoreThan2Ipv6Exp(NSNitroGslbErrors):
    """
        Nitro error code 1948
        Cannot exceed more than two IPV6 expressions in a selector
    """
    pass


class NSNitroNserrRepeatedMonitors(NSNitroGslbErrors):
    """
        Nitro error code 1949
        Monitors cannot be repeated
    """
    pass


class NSNitroNserrAllMonitorsDisabled(NSNitroGslbErrors):
    """
        Nitro error code 1950
        All monitors in selected list are disabled.
    """
    pass


class NSNitroNserrGslbAaaarecordExists(NSNitroGslbErrors):
    """
        Nitro error code 1951
        GSLB record cannot be created - another AAAA record is
        configured with the same name
    """
    pass


class NSNitroNserrGslbvipHeterogeneousServiceIpversion(NSNitroGslbErrors):
    """
        Nitro error code 1952
        Heterogeneous service binding is not allowed for GSLB vserver
    """
    pass


class NSNitroNserrViewipIpv6(NSNitroGslbErrors):
    """
        Nitro error code 1953
        View IP setting is not allowed for IPv6 GSLB service.
    """
    pass


class NSNitroNserrBackupipIpv6(NSNitroGslbErrors):
    """
        Nitro error code 1954
        IPv4 backup IP setting is not allowed for IPv6 GSLB vserver.
    """
    pass


class NSNitroNserrBackupVipMismatch(NSNitroGslbErrors):
    """
        Nitro error code 1955
        Different ip versions for primary and backup vservers.
    """
    pass


class NSNitroNserrGslbDomainConversion(NSNitroGslbErrors):
    """
        Nitro error code 1956
        Cannot associate gslb domain to the service.
    """
    pass


class NSNitroNserrGslbIpv4Backupip(NSNitroGslbErrors):
    """
        Nitro error code 1957
        IPv6 service binding is not allowed along with IPv4 backup IP.
    """
    pass


class NSNitroNserrRltCannotAddSelector(NSNitroGslbErrors):
    """
        Nitro error code 1958
        Cannot set a new selector when the limit identifier with no
        selector is bound to a policy.
    """
    pass


class NSNitroNserrRltSelConflictingAttributes(NSNitroGslbErrors):
    """
        Nitro error code 1959
        Conflicting attributes in the new and current selector sets.
    """
    pass


class NSNitroNserrGslbvipCnameBackupip(NSNitroGslbErrors):
    """
        Nitro error code 1960
        GSLB vserver having cname services cannot have backup IP
    """
    pass


class NSNitroNserrGslbHeterogeneousSiteip(NSNitroGslbErrors):
    """
        Nitro error code 1961
        Heterogeneous IPv6 and IPv4 GSLB site IPs not allowed.
    """
    pass


class NSNitroNserrGslbUnused1(NSNitroGslbErrors):
    """
        Nitro error code 1962
        ####### USE ME ##########
    """
    pass


class NSNitroNserrGslbUnused2(NSNitroGslbErrors):
    """
        Nitro error code 1963
        ####### USE ME ##########
    """
    pass


class NSNitroNserrAaaaRecordExists(NSNitroGslbErrors):
    """
        Nitro error code 1964
        AAAA record cannot be created - another AAAA record is
        configured with the same name
    """
    pass


class NSNitroNserrGslbRectypeService(NSNitroGslbErrors):
    """
        Nitro error code 1965
        Cannot set the record type while services bound to the GSLB
        vserver.
    """
    pass


class NSNitroNserrGslbRectypeDomain(NSNitroGslbErrors):
    """
        Nitro error code 1966
        Cannot set the record type while domains bound to the GSLB
        vserver.
    """
    pass


class NSNitroNserrGslbRectypeBackupVip(NSNitroGslbErrors):
    """
        Nitro error code 1967
        Cannot set the record type while GSLB vserver has backup
        vserver.
    """
    pass


class NSNitroNserrGslbBkpvipRectype(NSNitroGslbErrors):
    """
        Nitro error code 1968
        Cannot set the record type while GSLB vserver is a backup
        vserver.
    """
    pass


class NSNitroNserrGslbUnused3(NSNitroGslbErrors):
    """
        Nitro error code 1969
        ###### USE ME ########
    """
    pass


class NSNitroNserrBackupipIpv4(NSNitroGslbErrors):
    """
        Nitro error code 1970
        IPv6 backup IP setting is not allowed for IPv4 GSLB vserver.
    """
    pass


class NSNitroNserrGslbIpv6Backupip(NSNitroGslbErrors):
    """
        Nitro error code 1971
        IPv4 service binding is not allowed along with IPv6 backup IP.
    """
    pass


class NSNitroNserrGslbDbReqTooBig(NSNitroGslbErrors):
    """
        Nitro error code 1972
        Static proximity Database request is too big.
    """
    pass


class NSNitroNserrGslbDbQueueMaxed(NSNitroGslbErrors):
    """
        Nitro error code 1973
        Static proximity Database queue is full.
    """
    pass


class NSNitroNserrGslbDbServer(NSNitroGslbErrors):
    """
        Nitro error code 1974
        Static proximity database server is not running.
    """
    pass


class NSNitroNserrGslbDbTimeout(NSNitroGslbErrors):
    """
        Nitro error code 1975
        Static proximity database server is not responding.
    """
    pass


class NSNitroNserrGslbDbClosed(NSNitroGslbErrors):
    """
        Nitro error code 1976
        Connection to static proximity database server is closed.
    """
    pass


class NSNitroNserrGslbCoordinates(NSNitroGslbErrors):
    """
        Nitro error code 1977
        Both longitude and latitude should be specified or not.
    """
    pass


class NSNitroNserrInvalidIpv6Prefixlen(NSNitroGslbErrors):
    """
        Nitro error code 1978
        Invalid IPv6 prefix length.
    """
    pass


class NSNitroNserrGslbdomainCanmeRecordExists(NSNitroGslbErrors):
    """
        Nitro error code 1979
        Cname record can't be created. Another record exists for the
        configured domain.
    """
    pass


class NSNitroNserrGslbdomainAaaaCnameExists(NSNitroGslbErrors):
    """
        Nitro error code 1980
        Cname record exists for the configured domain.
    """
    pass


class NSNitroNserrGslbNonParentRemotesite(NSNitroGslbErrors):
    """
        Nitro error code 1981
        Cannot have a gslb remote site,  other than the parent site,
        configured on an LB node
    """
    pass


class NSNitroNserrZoneExists(NSNitroGslbErrors):
    """
        Nitro error code 1982
        Zone already configured.
    """
    pass


class NSNitroNserrInvalKeyflags(NSNitroGslbErrors):
    """
        Nitro error code 1983
        Invalid flags value in DNSKEY
    """
    pass


class NSNitroNserrDnskeyNonexists(NSNitroGslbErrors):
    """
        Nitro error code 1984
        Zone has no DNSKEY's
    """
    pass


class NSNitroNserrNorecsInZone(NSNitroGslbErrors):
    """
        Nitro error code 1985
        No records in zone
    """
    pass


class NSNitroNserrSignfailed(NSNitroGslbErrors):
    """
        Nitro error code 1986
        RSA Sign operation returned error
    """
    pass


class NSNitroNserrDigestinitFailed(NSNitroGslbErrors):
    """
        Nitro error code 1987
        Digest init before RSA Sign operation returned error
    """
    pass


class NSNitroNserrDigestupdateFailed(NSNitroGslbErrors):
    """
        Nitro error code 1988
        Digest update before RSA Sign operation returned error
    """
    pass


class NSNitroNserrKeyexists(NSNitroGslbErrors):
    """
        Nitro error code 1989
        The DNSKEY is already added for this zone
    """
    pass


class NSNitroNserrNopasvkeys(NSNitroGslbErrors):
    """
        Nitro error code 1990
        No Passive DNSKEY's in zone
    """
    pass


class NSNitroNserrDnsMaxkeysize(NSNitroGslbErrors):
    """
        Nitro error code 1991
        Maximum allowed public key size is 1024 and private key size is
        4096
    """
    pass


class NSNitroNserrNodataToSign(NSNitroGslbErrors):
    """
        Nitro error code 1992
        No data to sign the record
    """
    pass


class NSNitroNserrCnameSiteNotexists(NSNitroGslbErrors):
    """
        Nitro error code 1993
        Site name must be specified for cname based GSLB service.
    """
    pass


class NSNitroNserrDnsNosoaNons(NSNitroGslbErrors):
    """
        Nitro error code 1994
        No SOA or NS records for the zone
    """
    pass


class NSNitroNserrDnsProxyZone(NSNitroGslbErrors):
    """
        Nitro error code 1995
        Cannot sign/unsign a proxy zone
    """
    pass


class NSNitroNserrNoactvkeys(NSNitroGslbErrors):
    """
        Nitro error code 1996
        No active DNSKEY's in zone
    """
    pass


class NSNitroNserrNotifyperiod(NSNitroGslbErrors):
    """
        Nitro error code 1997
        Notification period must be less than the expiry period
    """
    pass


class NSNitroNserrLoadPubkey(NSNitroGslbErrors):
    """
        Nitro error code 1998
        Public key loading failed
    """
    pass


class NSNitroNserrDnskeygenUnsupportedAlgo(NSNitroGslbErrors):
    """
        Nitro error code 1999
        Unsupported algorithm
    """
    pass


class NSNitroNserrDnskeygenErrPubfileOpen(NSNitroGslbErrors):
    """
        Nitro error code 2000
        Error opening public key file
    """
    pass


class NSNitroNserrDnskeygenErrPrivfileOpen(NSNitroGslbErrors):
    """
        Nitro error code 2001
        Error opening private key file
    """
    pass


class NSNitroNserrDnskeygenErrDsfileOpen(NSNitroGslbErrors):
    """
        Nitro error code 2002
        Error opening delegation signer (DS) file
    """
    pass


class NSNitroNserrGslbOptNotsupported(NSNitroGslbErrors):
    """
        Nitro error code 2003
        gslb option is not supported,  GSLB site is mandatory for GSLB
        services
    """
    pass


class NSNitroNserrGslbGfsNotSupported(NSNitroGslbErrors):
    """
        Nitro error code 2004
        Graceful shutdown is not supported for GSLB services.
    """
    pass


class NSNitroNserrNsmapImportfile(NSNitroGslbErrors):
    """
        Nitro error code 2005
        Error reading the imported file. See /var/log/ns.log file for
        more details.
    """
    pass


class NSNitroNserrDnsCnameloop(NSNitroGslbErrors):
    """
        Nitro error code 2006
        Addition of this CNAME record leads to a CNAME loop
    """
    pass


class NSNitroSvpnErrors(NSNitroError):
    """
        Base exception class NSNitroSvpnErrors
    """
    pass


class NSNitroNscfgInfo(NSNitroSvpnErrors):
    """
        Nitro error code 2049
        Sending the /cfg information
    """
    pass


class NSNitroNscsInfo(NSNitroSvpnErrors):
    """
        Nitro error code 2050
        Backend server info exists
    """
    pass


class NSNitroNscsprobeInfo(NSNitroSvpnErrors):
    """
        Nitro error code 2051
        Probe to backend server pending
    """
    pass


class NSNitroNsappprobeInfo(NSNitroSvpnErrors):
    """
        Nitro error code 2052
        Client side connection being closed
    """
    pass


class NSNitroNscfgMpInfo(NSNitroSvpnErrors):
    """
        Nitro error code 2112
        Sending the /mp_cfg Information
    """
    pass


class NSNitroNserrNointranetip(NSNitroSvpnErrors):
    """
        Nitro error code 2113
        No Intranet IP available
    """
    pass


class NSNitroNserrAlreadylogedin(NSNitroSvpnErrors):
    """
        Nitro error code 2114
        The user is already logged-in
    """
    pass


class NSNitroNserrUrlinuse(NSNitroSvpnErrors):
    """
        Nitro error code 2115
        Bound URL/bookmark cannot be removed.
    """
    pass


class NSNitroNserrVpnappinuse(NSNitroSvpnErrors):
    """
        Nitro error code 2116
        Bound VPN application cannot be removed.
    """
    pass


class NSNitroNserrNotsuppTransIntercpt(NSNitroSvpnErrors):
    """
        Nitro error code 2117
        Transparent interception is not yet supported.
    """
    pass


class NSNitroNserrNotsuppProtUdp(NSNitroSvpnErrors):
    """
        Nitro error code 2118
        UDP protocol is not yet supported
    """
    pass


class NSNitroNserrDefaultcmdplcy(NSNitroSvpnErrors):
    """
        Nitro error code 2119
        Default command policy cannot be removed
    """
    pass


class NSNitroNserrClntCertReqd(NSNitroSvpnErrors):
    """
        Nitro error code 2120
        Client SSL certificate is required
    """
    pass


class NSNitroNserrInvalCertfield(NSNitroSvpnErrors):
    """
        Nitro error code 2121
        Invalid certificate field
    """
    pass


class NSNitroNserrVpnappProxyIprange(NSNitroSvpnErrors):
    """
        Nitro error code 2064
        Proxy interception does not support IP ranges
    """
    pass


class NSNitroNserrVpnappProxyNetmask(NSNitroSvpnErrors):
    """
        Nitro error code 2065
        Proxy interception does not support netmasks
    """
    pass


class NSNitroNserrVpnappProxyDstportRange(NSNitroSvpnErrors):
    """
        Nitro error code 2066
        Proxy interception does not support destination port ranges
    """
    pass


class NSNitroNserrVpnappProxyProtocol(NSNitroSvpnErrors):
    """
        Nitro error code 2067
        Proxy interception supports only TCP
    """
    pass


class NSNitroNserrVpnappProxyHostname(NSNitroSvpnErrors):
    """
        Nitro error code 2068
        Proxy interception does not support hostname interception
    """
    pass


class NSNitroNserrVpnappTransSrcip(NSNitroSvpnErrors):
    """
        Nitro error code 2069
        Transparent interception does not support source IP
    """
    pass


class NSNitroNserrVpnappTransSrcport(NSNitroSvpnErrors):
    """
        Nitro error code 2070
        Transparent interception does not support source port
    """
    pass


class NSNitroNserrVpnappNoInterceptionType(NSNitroSvpnErrors):
    """
        Nitro error code 2071
        Intranet application requires an interception type
    """
    pass


class NSNitroNserrVpnappCliappPort(NSNitroSvpnErrors):
    """
        Nitro error code 2072
        Both client application name and destination port cannot be
        specified
    """
    pass


class NSNitroNserrVpnappCliappProto(NSNitroSvpnErrors):
    """
        Nitro error code 2073
        Protocol can not be specified when client application name is
        present
    """
    pass


class NSNitroNserrVpnappProxyCliapp(NSNitroSvpnErrors):
    """
        Nitro error code 2074
        Proxy interception does not support client application based
        interception
    """
    pass


class NSNitroNserrVpnappMissingProto(NSNitroSvpnErrors):
    """
        Nitro error code 2075
        Protocol must be specified
    """
    pass


class NSNitroNserrVpnappMissingArg(NSNitroSvpnErrors):
    """
        Nitro error code 2076
        One of destIP,  IPRange,  hostname or clientApplication has to
        be specified
    """
    pass


class NSNitroNserrVpnappTooManyArg(NSNitroSvpnErrors):
    """
        Nitro error code 2077
        At most one of destIP,  IPRange,  hostname or clientApplication
        may be specified
    """
    pass


class NSNitroNserrFsAuthfail(NSNitroSvpnErrors):
    """
        Nitro error code 2078
        
    """
    pass


class NSNitroNserrNsipv6notpresent(NSNitroSvpnErrors):
    """
        Nitro error code 2079
        No IPV6 Netscaler IP has been configured
    """
    pass


class NSNitroNserrRemoveSession(NSNitroSvpnErrors):
    """
        Nitro error code 2096
        No IPV6 Netscaler IP has been configured
    """
    pass


class NSNitroNserrStawiExist(NSNitroSvpnErrors):
    """
        Nitro error code 3250
        A STA or WI DBS configuration exists. Unset it first
    """
    pass


class NSNitroNserrInvalidSsoAction(NSNitroSvpnErrors):
    """
        Nitro error code 2099
        Invalid sso action
    """
    pass


class NSNitroNserrInvalidTmtrafficAction(NSNitroSvpnErrors):
    """
        Nitro error code 2100
        Invalid tm traffic action
    """
    pass


class NSNitroNserrInvalfsso(NSNitroSvpnErrors):
    """
        Nitro error code 2101
        SSO should be turned on for setting formsso action
    """
    pass


class NSNitroNserrInvalidurl(NSNitroSvpnErrors):
    """
        Nitro error code 2102
        Action url should be root relative url
    """
    pass


class NSNitroPolErrors(NSNitroError):
    """
        Base exception class NSNitroPolErrors
    """
    pass


class NSNitroNserrInvalidpol(NSNitroPolErrors):
    """
        Nitro error code 2053
        Binding invalid policy
    """
    pass


class NSNitroNserrNopol(NSNitroPolErrors):
    """
        Nitro error code 2054
        No such policy exists
    """
    pass


class NSNitroNserrRuleurl(NSNitroPolErrors):
    """
        Nitro error code 2055
        Rule or URL required
    """
    pass


class NSNitroNserrDelmc(NSNitroPolErrors):
    """
        Nitro error code 2056
        Delay or maxConn argument required
    """
    pass


class NSNitroNserrAcp(NSNitroPolErrors):
    """
        Nitro error code 2057
        Alternate content path not required
    """
    pass


class NSNitroNserrAcs(NSNitroPolErrors):
    """
        Nitro error code 2058
        Alternate content service not required
    """
    pass


class NSNitroNserrNosetCexp(NSNitroPolErrors):
    """
        Nitro error code 2059
        No support to set compound expression value
    """
    pass


class NSNitroNserrCexpDepth(NSNitroPolErrors):
    """
        Nitro error code 2060
        Maximum recursive depth reached
    """
    pass


class NSNitroNserrNovpnapp(NSNitroPolErrors):
    """
        Nitro error code 2061
        No such intranet application exists
    """
    pass


class NSNitroNserrNosetCse(NSNitroPolErrors):
    """
        Nitro error code 2062
        No support to set client security expression value
    """
    pass


class NSNitroNserrInvalPolname(NSNitroPolErrors):
    """
        Nitro error code 2063
        Invalid policy Name
    """
    pass


class NSNitroNserrUnbindInvalidpol(NSNitroPolErrors):
    """
        Nitro error code 2097
        Policy not bound
    """
    pass


class NSNitroNserrExceedMaxPolLimit(NSNitroPolErrors):
    """
        Nitro error code 2098
        32 authentication policies are already bound
    """
    pass


class NSNitroNserrInternalPiError(NSNitroPolErrors):
    """
        Nitro error code 2103
        Internal policy error
    """
    pass


class NSNitroVlanErrors(NSNitroError):
    """
        Base exception class NSNitroVlanErrors
    """
    pass


class NSNitroNserrInterfacebound(NSNitroVlanErrors):
    """
        Nitro error code 2080
        Interface is already bound to this VLAN
    """
    pass


class NSNitroNserrIfaceNoUnbind(NSNitroVlanErrors):
    """
        Nitro error code 2081
        Untagged interface cannot be removed from default VLAN. To
        remove,  bind to other VLAN.
    """
    pass


class NSNitroNserrIfaceMaxVlans(NSNitroVlanErrors):
    """
        Nitro error code 2082
        Maximum number of tagged VLANs bound to the interface exceeded.
    """
    pass


class NSNitro0x850Errors(NSNitroError):
    """
        Base exception class NSNitro0x850Errors
    """
    pass


class NSNitroNserrMonitorInterval(NSNitro0x850Errors):
    """
        Nitro error code 2128
        Monitor interval must be greater than response timeout
    """
    pass


class NSNitroNserrMonitorDestip(NSNitro0x850Errors):
    """
        Nitro error code 2129
        Destination IP must be specified for transparent,  tunneled or
        tos monitors
    """
    pass


class NSNitroNserrMonitorCodes(NSNitro0x850Errors):
    """
        Nitro error code 2130
        Too many response codes,  only 16 allowed
    """
    pass


class NSNitroNserrMonitorRef(NSNitro0x850Errors):
    """
        Nitro error code 2131
        Monitor must be unbound before it can be deleted
    """
    pass


class NSNitroNserrMonitorBuiltin(NSNitro0x850Errors):
    """
        Nitro error code 2132
        Built-in monitors cannot be deleted
    """
    pass


class NSNitroNserrMonitorBound(NSNitro0x850Errors):
    """
        Nitro error code 2133
        The monitor is already bound to the service
    """
    pass


class NSNitroNserrMonitorType(NSNitro0x850Errors):
    """
        Nitro error code 2134
        Invalid monitor type
    """
    pass


class NSNitroNserrMonitorLocal(NSNitro0x850Errors):
    """
        Nitro error code 2135
        Monitor object cannot be bound to local service
    """
    pass


class NSNitroNserrTimeoutRange(NSNitro0x850Errors):
    """
        Nitro error code 2136
        Timeout value out of range; enter a value between 2 minutes and
        1440 minutes
    """
    pass


class NSNitroNserrInvalidhashlen(NSNitro0x850Errors):
    """
        Nitro error code 2137
        Hashlength should be between 1 and 4096 (inclusive)
    """
    pass


class NSNitroNserrNotauthorized(NSNitro0x850Errors):
    """
        Nitro error code 2138
        Not authorized to execute this command
    """
    pass


class NSNitroNserrMonitorDefault(NSNitro0x850Errors):
    """
        Nitro error code 2139
        No operations allowed with the default monitor
    """
    pass


class NSNitroNserrMonitorLdnsAddPerm(NSNitro0x850Errors):
    """
        Nitro error code 2140
        Cannot add monitor of ldns type
    """
    pass


class NSNitroNserrMonitorLdnsBindPerm(NSNitro0x850Errors):
    """
        Nitro error code 2141
        Cannot bind ldns monitor
    """
    pass


class NSNitroNserrBackupLoop(NSNitro0x850Errors):
    """
        Nitro error code 2144
        The VIP is already a backup in the chain
    """
    pass


class NSNitroNserrSecureUdp(NSNitro0x850Errors):
    """
        Nitro error code 2154
        Secure mode not supported for this protocol
    """
    pass


class NSNitroNserrMonitorWrongType(NSNitro0x850Errors):
    """
        Nitro error code 2155
        Existing monitor is of different type than given
    """
    pass


class NSNitroNserrLrtmPerm(NSNitro0x850Errors):
    """
        Nitro error code 2156
        Enabling LRTM on this monitor type is not permitted
    """
    pass


class NSNitroNserrMonitorScriptname(NSNitro0x850Errors):
    """
        Nitro error code 2157
        Invalid script name for user monitor
    """
    pass


class NSNitroNserrMonitorDispatcherip(NSNitro0x850Errors):
    """
        Nitro error code 2159
        Invalid dispatcher IP for user monitor
    """
    pass


class NSNitroNserrMonitorUserperm(NSNitro0x850Errors):
    """
        Nitro error code 2160
        Operation not permitted for a user monitor
    """
    pass


class NSNitroNserrMonitorNocodes(NSNitro0x850Errors):
    """
        Nitro error code 2161
        A response code is required for this monitor type
    """
    pass


class NSNitroNserrInvalMon(NSNitro0x850Errors):
    """
        Nitro error code 2162
        Attempt to bind invalid monitor type
    """
    pass


class NSNitroNserrTypeExists(NSNitro0x850Errors):
    """
        Nitro error code 2163
        Only one monitor of this type can be bound to a service
    """
    pass


class NSNitroNserrMonitorUnbindDefault(NSNitro0x850Errors):
    """
        Nitro error code 2164
        Default monitor cannot be unbound from a service
    """
    pass


class NSNitroNserrMonitorBindDefault(NSNitro0x850Errors):
    """
        Nitro error code 2165
        Default monitor cannot be bound explicitly to a service
    """
    pass


class NSNitroNserrMonitorDisableDefault(NSNitro0x850Errors):
    """
        Nitro error code 2166
        Default monitor cannot be disabled or enabled
    """
    pass


class NSNitroNserrDrtmPerm(NSNitro0x850Errors):
    """
        Nitro error code 2167
        Dynamic response timeout is not permitted on this monitor type
    """
    pass


class NSNitroNserrMonDtrmDeviation(NSNitro0x850Errors):
    """
        Nitro error code 2168
        Response timeout of the monitor has been changed to interval - 1
    """
    pass


class NSNitroNserrMonitorInvalidValue(NSNitro0x850Errors):
    """
        Nitro error code 2169
        Time parameter must be a multiple of 10
    """
    pass


class NSNitroNserrMonitorNotBound(NSNitro0x850Errors):
    """
        Nitro error code 2170
        Monitor not bound to service
    """
    pass


class NSNitroNserrInvalidMonitor(NSNitro0x850Errors):
    """
        Nitro error code 2171
        Monitor does not exist
    """
    pass


class NSNitroNserrMonitorNoSuchipaddr(NSNitro0x850Errors):
    """
        Nitro error code 2172
        Some IP addresses were not present
    """
    pass


class NSNitroNserrMonitorScriptArgSize(NSNitro0x850Errors):
    """
        Nitro error code 2173
        Combined argument size too long
    """
    pass


class NSNitroNserrMetrictableNoent(NSNitro0x850Errors):
    """
        Nitro error code 2174
        Metric table does not exist
    """
    pass


class NSNitroNserrMetrictableExist(NSNitro0x850Errors):
    """
        Nitro error code 2175
        Metric table exists
    """
    pass


class NSNitroNserrDelMetrictablePermanent(NSNitro0x850Errors):
    """
        Nitro error code 2176
        Permanent metric table cannot be deleted
    """
    pass


class NSNitroNserrMaxMetricBinding(NSNitro0x850Errors):
    """
        Nitro error code 2177
        Maximum of 10 SNMP type metric can be bound to the monitor
    """
    pass


class NSNitroNserrMetricNoent(NSNitro0x850Errors):
    """
        Nitro error code 2178
        Metric does not exist
    """
    pass


class NSNitroNserrMetricExists(NSNitro0x850Errors):
    """
        Nitro error code 2179
        Metric exists
    """
    pass


class NSNitroNserrOidExist(NSNitro0x850Errors):
    """
        Nitro error code 2180
        SNMP OID exists
    """
    pass


class NSNitroNserrSnmpOidInval(NSNitro0x850Errors):
    """
        Nitro error code 2181
        SNMP OID is invalid
    """
    pass


class NSNitroNserrMetrictableRdonly(NSNitro0x850Errors):
    """
        Nitro error code 2182
        No operations allowed on read only metric table
    """
    pass


class NSNitroNserrThresholdZero(NSNitro0x850Errors):
    """
        Nitro error code 2183
        This metric will not be used for CUSTOM LB as its threshold
        value is zero
    """
    pass


class NSNitroNserrLdapMonitorIncomplete(NSNitro0x850Errors):
    """
        Nitro error code 2184
        bindDN or baseDN must be specified before LDAP monitor can be
        used
    """
    pass


class NSNitroNserrMysqlMonitorIncomplete(NSNitro0x850Errors):
    """
        Nitro error code 2185
        userName or database must be specified before MYSQL monitor can
        be used
    """
    pass


class NSNitroNserrPop3MonitorIncomplete(NSNitro0x850Errors):
    """
        Nitro error code 2186
        userName must be specified before POP3 monitor can be used
    """
    pass


class NSNitroNserrNntpMonitorIncomplete(NSNitro0x850Errors):
    """
        Nitro error code 2187
        group must be specified before NNTP monitor can be used
    """
    pass


class NSNitroNserrFtpextendedMonitorIncomplete(NSNitro0x850Errors):
    """
        Nitro error code 2188
        fileName must be specified before FTP-EXTENDED monitor can be
        used
    """
    pass


class NSNitroNserrSnmpMonitorIncomplete(NSNitro0x850Errors):
    """
        Nitro error code 2189
        snmpOID or snmpCommunity must be specified before SNMP monitor
        can be used
    """
    pass


class NSNitroNserrCitrixXmlService(NSNitro0x850Errors):
    """
        Nitro error code 2190
        application must be specified before CITRIX-XML-SERVICE monitor
        can be used
    """
    pass


class NSNitroNserrCitrixWebInterface(NSNitro0x850Errors):
    """
        Nitro error code 2191
        sitePath must be specified before CITRIX-WEB-INTERFACE monitor
        can be used
    """
    pass


class NSNitroNserrLdnsMonCantDisable(NSNitro0x850Errors):
    """
        Nitro error code 2192
        Atleast one ldns monitor needs to be enabled
    """
    pass


class NSNitroNserrResRetryOnIpSvr(NSNitro0x850Errors):
    """
        Nitro error code 2193
        Resolve retry can be set only on domain based servers
    """
    pass


class NSNitroNserrIpOnDbsSvr(NSNitro0x850Errors):
    """
        Nitro error code 2194
        IP Address cannot be set on a domain based server
    """
    pass


class NSNitroNserrMonitorAlertretries(NSNitro0x850Errors):
    """
        Nitro error code 2195
        Monitor retries must be greater than SNMP alert retries
    """
    pass


class NSNitroNserrMonitorFailureretries(NSNitro0x850Errors):
    """
        Nitro error code 2196
        Monitor retries must be greater than monitor failureRetries
    """
    pass


class NSNitroNserrMonitorAlertfailureretries(NSNitro0x850Errors):
    """
        Nitro error code 2197
        Monitor failureRetries must be greater than SNMP alertRetries
    """
    pass


class NSNitroNserrMonitorIp(NSNitro0x850Errors):
    """
        Nitro error code 2198
        The server/monitor destination ip address is not appropriate for
        this monitor
    """
    pass


class NSNitroNserrMonitorSubnet(NSNitro0x850Errors):
    """
        Nitro error code 2199
        The server/monitor destination ip address should be in a
        directly connected subnet for this monitor
    """
    pass


class NSNitroNserrMonitorStatic(NSNitro0x850Errors):
    """
        Nitro error code 2200
        A static/permanent entry is configured for the server/monitor
        destination ip address
    """
    pass


class NSNitroNserrTosidNotSet(NSNitro0x850Errors):
    """
        Nitro error code 2201
        Tos id must be specified for tos enabled vserver/monitor
    """
    pass


class NSNitroNserrFailureretriesNotSupported(NSNitro0x850Errors):
    """
        Nitro error code 2202
        The failure retries is not supported for this monitor type.
        Resetting the value of failure retries to 0(Disabled).
    """
    pass


class NSNitroNserrSuccessretriesNotSupported(NSNitro0x850Errors):
    """
        Nitro error code 2203
        The success retries is not supported for this monitor type.
        Resetting the value of success entries to 1(Disabled).
    """
    pass


class NSNitroNserrSetvsInvalMysqlparams(NSNitro0x850Errors):
    """
        Nitro error code 2204
        This parameter is only applicable to a MYSQL vserver.
    """
    pass


class NSNitroNserrSetvsInvalProtocolParams(NSNitro0x850Errors):
    """
        Nitro error code 2205
        The parameters are only applicable to  HTTP or SSL vservers.
    """
    pass


class NSNitroNserrSetvsInvalProtocolsParams(NSNitro0x850Errors):
    """
        Nitro error code 2206
        The parameters are only applicable to  HTTP ,  SSL or RTSP
        vservers.
    """
    pass


class NSNitroNserrDdcValidateCredRequired(NSNitro0x850Errors):
    """
        Nitro error code 2207
        Username,  password and ddc domain are required for Xen Desktop
        monitor\n
    """
    pass


class NSNitroNserrCitrixWiExtendedMonitorIncomplete(NSNitro0x850Errors):
    """
        Nitro error code 2208
        userName,  password,  sitepath and domain must be specified
        before CITRIX-WI-EXTENDED monitor can be used
    """
    pass


class NSNitro0x900Errors(NSNitroError):
    """
        Base exception class NSNitro0x900Errors
    """
    pass


class NSNitroNserrSvcporttype(NSNitro0x900Errors):
    """
        Nitro error code 2305
        Service exists with the same port and service type
    """
    pass


class NSNitroNserrVipInGroup(NSNitro0x900Errors):
    """
        Nitro error code 2306
        vserver is bound to a group. Set persistence parameters on group
        to change them for all vservers in group or unbind vserver from
        group and set on individual vserver.
    """
    pass


class NSNitroNserrUnsupportedBkp(NSNitro0x900Errors):
    """
        Nitro error code 2307
        This backup/primary persistence combination is not supported
    """
    pass


class NSNitroNserrNonhttpsslVipingrp(NSNitro0x900Errors):
    """
        Nitro error code 2308
        Cookie persistence cannot be applied - group has non HTTP/SSL
        type of vserver
    """
    pass


class NSNitroNserrNonhttpVipingrp(NSNitro0x900Errors):
    """
        Nitro error code 2309
        Cookie persistence cannot be applied - group has non-HTTP type
        of vserver
    """
    pass


class NSNitroNserrUseProperRmCmd(NSNitro0x900Errors):
    """
        Nitro error code 2310
        Use remove IP option instead
    """
    pass


class NSNitroNserrLbmethodNotSupported(NSNitro0x900Errors):
    """
        Nitro error code 2321
        LB method not supported for LLB/PBR
    """
    pass


class NSNitroNserrPersistenceNotSupported(NSNitro0x900Errors):
    """
        Nitro error code 2322
        Persistence not supported for LLB/PBR
    """
    pass


class NSNitroNserrVserverParameters(NSNitro0x900Errors):
    """
        Nitro error code 2323
        Vserver arguments not valid for LLB/PBR VIP
    """
    pass


class NSNitroNserrServiceParameters(NSNitro0x900Errors):
    """
        Nitro error code 2324
        Service parameters are invalid for LLB/PBR VIP
    """
    pass


class NSNitroNserrLbvipDelete(NSNitro0x900Errors):
    """
        Nitro error code 2325
        Vserver cannot be removed with out removing LB/PBR route
    """
    pass


class NSNitroNserrCachepolicyRespactionInval(NSNitro0x900Errors):
    """
        Nitro error code 2326
        Integrated caching action cannot be applied on a response
    """
    pass


class NSNitroNserrCachelicenseFailed(NSNitro0x900Errors):
    """
        Nitro error code 2327
        The license for Integrated Caching feature was not enabled due
        to an internal error
    """
    pass


class NSNitroNserrLbvipMultiroutes(NSNitro0x900Errors):
    """
        Nitro error code 2328
        VIP can't be associated with multiple LB/PBR routes
    """
    pass


class NSNitroNserrLbmacInval(NSNitro0x900Errors):
    """
        Nitro error code 2329
        MAC/IPTUNNEL mode can be set only for a VIP with wildcard IP or
        with service type ANY or for a sessionless VIP
    """
    pass


class NSNitroNserrCachestatsObjNotpresent(NSNitro0x900Errors):
    """
        Nitro error code 2336
        No object in cache matching the specified attributes
    """
    pass


class NSNitroNserrCachepolicyNotactive(NSNitro0x900Errors):
    """
        Nitro error code 2337
        Integrated caching policy is not active
    """
    pass


class NSNitroNserrCacheBuiltinsNotSourced(NSNitro0x900Errors):
    """
        Nitro error code 2338
        Failed sourcing cache builtins,  Disabling IC
    """
    pass


class NSNitroNserrCachepolicyPriorityInval(NSNitro0x900Errors):
    """
        Nitro error code 2339
        Invalid priority
    """
    pass


class NSNitroNserrRoute6DefaultOnly(NSNitro0x900Errors):
    """
        Nitro error code 2340
        Only default route configuration supported
    """
    pass


class NSNitroNserrRoute6DefaultExists(NSNitro0x900Errors):
    """
        Nitro error code 2341
        Configured route already exists
    """
    pass


class NSNitroNserrRoute6InvalidGateway(NSNitro0x900Errors):
    """
        Nitro error code 2342
        Invalid gateway
    """
    pass


class NSNitroNserrRoute6Max(NSNitro0x900Errors):
    """
        Nitro error code 2343
        Already maximum number of routes configured
    """
    pass


class NSNitroNserrRoute6NotExist(NSNitro0x900Errors):
    """
        Nitro error code 2344
        Route does not exist
    """
    pass


class NSNitroNserrIpv6InvalidAddr(NSNitro0x900Errors):
    """
        Nitro error code 2345
        Incorrect IPv6 address type
    """
    pass


class NSNitroNserrLbvipIpv6tov4(NSNitro0x900Errors):
    """
        Nitro error code 2352
        Changing IP from IPv6 to IPv4 not permitted
    """
    pass


class NSNitroNserrIpv6Nsiptovip(NSNitro0x900Errors):
    """
        Nitro error code 2353
        Configuring NSIP as VIP not permitted
    """
    pass


class NSNitroNserrIpv6Viptonsip(NSNitro0x900Errors):
    """
        Nitro error code 2354
        Configuring VIP as NSIP not permitted
    """
    pass


class NSNitroNserrIpv6Scope(NSNitro0x900Errors):
    """
        Nitro error code 2355
        Incorrect IPv6 address scope. (Default: global)
    """
    pass


class NSNitroNserrLbvipIpv4tov6(NSNitro0x900Errors):
    """
        Nitro error code 2356
        Changing IP from IPv4 to IPv6 not permitted
    """
    pass


class NSNitroNserrIpv6Linklocaltovip(NSNitro0x900Errors):
    """
        Nitro error code 2357
        Configuring Link-Local address as VIP or SNIP not permitted
    """
    pass


class NSNitroNserrIpv6Mapiponnsip(NSNitro0x900Errors):
    """
        Nitro error code 2358
        Mapped IP should not be configured for NSIP (Ignoring mapped ip)
    """
    pass


class NSNitroNserrSecureipportaddrinuse(NSNitro0x900Errors):
    """
        Nitro error code 2359
        Internal secure service exists with the same port and service
        type. Please use this for secure access
    """
    pass


class NSNitroNserrIpv6InvalidPrefix(NSNitro0x900Errors):
    """
        Nitro error code 2360
        Link-local prefix length is not equal to 64
    """
    pass


class NSNitroNserrNd6LinklocalVlan(NSNitro0x900Errors):
    """
        Nitro error code 2361
        Vlan is necessary with IPv6 Link-local address
    """
    pass


class NSNitroNserrNd6VlanIntf(NSNitro0x900Errors):
    """
        Nitro error code 2368
        Interface not a member of given vlan
    """
    pass


class NSNitroNserrPersistTimeoutToDefault(NSNitro0x900Errors):
    """
        Nitro error code 2369
        Unsetting Persistency,  changing timeout to default
    """
    pass


class NSNitroNserrLbGroupNotExist(NSNitro0x900Errors):
    """
        Nitro error code 2370
        LB group does not exist
    """
    pass


class NSNitroNserrLbVserverAlreadyBound(NSNitro0x900Errors):
    """
        Nitro error code 2371
        Vserver is already bound to a LB group
    """
    pass


class NSNitroInternalNameserverErrors(NSNitroError):
    """
        Base exception class NSNitroInternalNameserverErrors
    """
    pass


class NSNitroNserrNameSvrExists(NSNitroInternalNameserverErrors):
    """
        Nitro error code 2561
        Name server already exists.
    """
    pass


class NSNitroNserrNameSvrIdnsNempty(NSNitroInternalNameserverErrors):
    """
        Nitro error code 2562
        Name servers already configured.
    """
    pass


class NSNitroNserrNameSvrIvalpolicy(NSNitroInternalNameserverErrors):
    """
        Nitro error code 2563
        Invalid LB method for vserver-based name server.
    """
    pass


class NSNitroNserrNameSvrIvalproto(NSNitroInternalNameserverErrors):
    """
        Nitro error code 2564
        Invalid service type for vserver-based name server.
    """
    pass


class NSNitroNserrNameSvrAddNexistVip(NSNitroInternalNameserverErrors):
    """
        Nitro error code 2565
        vserver does not exist.
    """
    pass


class NSNitroNserrNameSvrNexist(NSNitroInternalNameserverErrors):
    """
        Nitro error code 2566
        Name server does not exist.
    """
    pass


class NSNitroNserrNameSvrIdnsPerm(NSNitroInternalNameserverErrors):
    """
        Nitro error code 2567
        Operation on internal entity not permitted
    """
    pass


class NSNitroNserrNameSvrIpExists(NSNitroInternalNameserverErrors):
    """
        Nitro error code 2568
        Name server exists with this IP address
    """
    pass


class NSNitroSslvpnAaaErrors(NSNitroError):
    """
        Base exception class NSNitroSslvpnAaaErrors
    """
    pass


class NSNitroNserrErrAaaLicense(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2624
        MaxAAAUsers value not allowed by license
    """
    pass


class NSNitroNserrUsrNointraip(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2625
        No intranet IP bound to user
    """
    pass


class NSNitroNserrUsrNotconfigured(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2626
        User does not exist
    """
    pass


class NSNitroNserrInvalAaaGrp(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2627
        Group does not exist
    """
    pass


class NSNitroNserrInvalCombnation(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2628
        NONE and ALL cannot be used simultaneously
    """
    pass


class NSNitroNserrInvalMipIip(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2629
        Both Mapped IP and Intranet IP must be specified
    """
    pass


class NSNitroNserrInvalMipoffIipoff(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2630
        Mapped IP and Intranet IP cannot be OFF at the same time
    """
    pass


class NSNitroNserrUserexist(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2631
        User already exists
    """
    pass


class NSNitroNserrGroupexist(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2632
        Group already exists
    """
    pass


class NSNitroNserrUseralreadybound(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2633
        User is already bound to the group
    """
    pass


class NSNitroNserrUsernotbound(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2640
        User is not bound to the group
    """
    pass


class NSNitroNserrEntitynotbound(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2641
        Entity not bound
    """
    pass


class NSNitroNserrGroupnotexist(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2642
        Group does not exist
    """
    pass


class NSNitroNserrInvalidloglevel(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2643
        NONE cannot be combined with other options
    """
    pass


class NSNitroNserrDhMisconfig(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2644
        The first hop and second hop can not be enabled on the same
        vserver
    """
    pass


class NSNitroNserrDhIpport(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2645
        The SG second hop ip and port are required
    """
    pass


class NSNitroNserrDhinuse(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2646
        Bound double hop server cannot be removed
    """
    pass


class NSNitroNserrInvalAaaglobalPoltype(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2647
        Only preauthentication policies can be bound to AAA global
    """
    pass


class NSNitroNserrNoIp(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2648
        ServerIP not configured for the authentication type
    """
    pass


class NSNitroNserrAaatmLic(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2649
        Feature not licensed [AAA]
    """
    pass


class NSNitroNserrAaatmDisabled(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2650
        Feature(s) not enabled [AAA]
    """
    pass


class NSNitroNserrNoAuthHost(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2651
        No Authentication Host specified
    """
    pass


class NSNitroNserrAuthOn(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2652
        Turn authentication off first
    """
    pass


class NSNitroNserrKillpending(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2653
        Another kill command in progress
    """
    pass


class NSNitroNserrAaatmNoAuthVs(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2654
        No Authentication vserver name specified
    """
    pass


class NSNitroNserrAaatm401authOn(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2655
        Turn off 401 based authentication first
    """
    pass


class NSNitroNserrUnauthrzed(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2656
        Unauthorized
    """
    pass


class NSNitroNserrKillInprogress(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2657
        A kill session command is in progress. Try again later
    """
    pass


class NSNitroNserrWiFrmNotexist(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2658
        Farm does not exist
    """
    pass


class NSNitroNserrWiFrmLast(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2659
        At least one Farm should be configured: can not remove last farm
    """
    pass


class NSNitroNserrWiNotinst(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2660
        Web interface not installed
    """
    pass


class NSNitroNserrWiGenfailed(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2661
        Unable to generate website
    """
    pass


class NSNitroNserrWiSiteExist(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2662
        Site already exists
    """
    pass


class NSNitroNserrWiSiteNotexist(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2663
        Site does not exist
    """
    pass


class NSNitroNserrWiSiteInvalAgurl(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2664
        Invalid agURL
    """
    pass


class NSNitroNserrWiSiteInvalStaurl(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2665
        Invalid staURL
    """
    pass


class NSNitroNserrWiSiteOnlyMpx(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2666
        WI can only be installed on NetScaler nCore builds
    """
    pass


class NSNitroNserrWiInstfailed(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2667
        Installation failed. Please check the log file
        /var/log/wicmd.log
    """
    pass


class NSNitroNserrWiMaxsiteExcd(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2668
        Maximum number of WI Sites exceeded. Please check the log file
        /var/log/wicmd.log
    """
    pass


class NSNitroNserrWiStawithoutagurl(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2669
        STAUrl cannot be specified without AGUrl.
    """
    pass


class NSNitroNserrWiAgurlwithoutsta(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2670
        AGUrl cannot be specified without STAUrl.
    """
    pass


class NSNitroNserrWiRelwithoutagurl(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2671
        SessionReliability cannot be ON without AGUrl.
    """
    pass


class NSNitroNserrWiAuthwithoutagurl(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2672
        AuthenticationPoint cannot be specified without AGUrl.
    """
    pass


class NSNitroNserrWiTwotktwithoutrel(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2673
        UseTwoTickets cannot be ON without SessionReliability.
    """
    pass


class NSNitroNserrWiTwotktwithoutsecsta(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2674
        UseTwoTickets cannot be ON without SecondSTAUrl.
    """
    pass


class NSNitroNserrWiSecstasame(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2675
        SecondSTAUrl should be different from StaURL.
    """
    pass


class NSNitroNserrWiLicense(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2676
        Web Interface on NS Feature not licensed.
    """
    pass


class NSNitroNserrWiSecstawithoutsta(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2677
        SecondSTAUrl cannot be specified without STAUrl.
    """
    pass


class NSNitroNserrAuthNegotiate(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2678
        Negotiate authentication required
    """
    pass


class NSNitroNserrWiInstsitesreduced(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2679
        Memory available is not sufficient for the passed maxSites value
    """
    pass


class NSNitroNserrWiIncompatibleauthpoint(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2680
        WI Authentication methods can not be specified unless
        authentication point is WI
    """
    pass


class NSNitroNserrWiSiteWithinSite(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2681
        One WI site can not be completely within another WI site
    """
    pass


class NSNitroNserrTmInvalidPersConfig(NSNitroSslvpnAaaErrors):
    """
        Nitro error code 2686
        Please specify both persistentCookie and
        persistentCookieValidity parameters
    """
    pass


class NSNitroRewriteErrors(NSNitroError):
    """
        Base exception class NSNitroRewriteErrors
    """
    pass


class NSNitroNserrRwActInval(NSNitroRewriteErrors):
    """
        Nitro error code 2817
        Invalid rewrite action
    """
    pass


class NSNitroNserrRwUndefactInval(NSNitroRewriteErrors):
    """
        Nitro error code 2818
        Invalid action for undefined event
    """
    pass


class NSNitroNserrActflowmismatch(NSNitroRewriteErrors):
    """
        Nitro error code 2819
        Flow types of target and string expression are incompatible
    """
    pass


class NSNitroNserrRonlyTarExpr(NSNitroRewriteErrors):
    """
        Nitro error code 2820
        Cannot modify target
    """
    pass


class NSNitroNserrPatsetBindfail(NSNitroRewriteErrors):
    """
        Nitro error code 2821
        Unable to bind the pattern to patset
    """
    pass


class NSNitroNserrPatsetUnbindfail(NSNitroRewriteErrors):
    """
        Nitro error code 2822
        Pattern does not exist in patset
    """
    pass


class NSNitroNserrPatsetNotpresent(NSNitroRewriteErrors):
    """
        Nitro error code 2823
        Patset does not exist
    """
    pass


class NSNitroNserrRspActInval(NSNitroRewriteErrors):
    """
        Nitro error code 2824
        Invalid responder action
    """
    pass


class NSNitroNserrRspPolicyFlowtypeReq(NSNitroRewriteErrors):
    """
        Nitro error code 2825
        Responder policy must be a request policy
    """
    pass


class NSNitroNserrTarFlowtypeNres(NSNitroRewriteErrors):
    """
        Nitro error code 2826
        Flow type of target should not be response type
    """
    pass


class NSNitroNserrRspConfigLock(NSNitroRewriteErrors):
    """
        Nitro error code 2827
        Responder configuration is temporarily disabled
    """
    pass


class NSNitroNserrRspActMustBeNoop(NSNitroRewriteErrors):
    """
        Nitro error code 2828
        Non-terminating policy must have NOOP action
    """
    pass


class NSNitroNserrPatsetInvalidRegex(NSNitroRewriteErrors):
    """
        Nitro error code 2829
        Patset contains invalid regex.
    """
    pass


class NSNitroNserrPatsetBindfailDupIndex(NSNitroRewriteErrors):
    """
        Nitro error code 2830
        Pattern index already in use,  try using other index
    """
    pass


class NSNitroNserrPatsetBindfailIndexNotGiven(NSNitroRewriteErrors):
    """
        Nitro error code 2831
        Index not specified : Index for this patset mandatory
    """
    pass


class NSNitroNserrPatsetBindfailIndexNotRequired(NSNitroRewriteErrors):
    """
        Nitro error code 2832
        Index not required : Index for this patset autogenerated
    """
    pass


class NSNitroNserrPatsetBindfailPatlenLtWuMinlen(NSNitroRewriteErrors):
    """
        Nitro error code 2833
        Adding shorter patterns not allowed
    """
    pass


class NSNitroNserrTargetNotAllowedInRule(NSNitroRewriteErrors):
    """
        Nitro error code 2834
        Expression involving Target not allowed in rule.
    """
    pass


class NSNitroNserrRwTargetNotAllowedInStrbuilder(NSNitroRewriteErrors):
    """
        Nitro error code 2835
        Expression involving Target not allowed in StringBuilder
        expression.
    """
    pass


class NSNitroNserrPitInval(NSNitroRewriteErrors):
    """
        Nitro error code 2836
        Invalid Packet data
    """
    pass


class NSNitroNserrInvalInvokepoint(NSNitroRewriteErrors):
    """
        Nitro error code 2837
        Invalid invoke point
    """
    pass


class NSNitroNserrPitMaxPacket(NSNitroRewriteErrors):
    """
        Nitro error code 2838
        Packet size exceeds maximum size
    """
    pass


class NSNitroNserrRefineSearchInvalid(NSNitroRewriteErrors):
    """
        Nitro error code 2839
        Regular expression for patterns not allowed when refine search
        is specified
    """
    pass


class NSNitroNserrExtendInvalid(NSNitroRewriteErrors):
    """
        Nitro error code 2840
        Extend not allowed for non-body expressions
    """
    pass


class NSNitroNserrNonExtendExpr(NSNitroRewriteErrors):
    """
        Nitro error code 2841
        Non extend expressions are not allowed
    """
    pass


class NSNitroNserrExtendInvalPirl(NSNitroRewriteErrors):
    """
        Nitro error code 2842
        Extend not allowed in the string builder expression
    """
    pass


class NSNitroNserrInvalTarExpr(NSNitroRewriteErrors):
    """
        Nitro error code 2843
        Invalid target expression
    """
    pass


class NSNitroNserrInvalPatternSearchSet(NSNitroRewriteErrors):
    """
        Nitro error code 2844
        Cannot set both pattern and search
    """
    pass


class NSNitroNserrInvalSearchArgs(NSNitroRewriteErrors):
    """
        Nitro error code 2845
        Invalid argument: search supports text,  xpath,  xpath_json,
        regex and patset
    """
    pass


class NSNitroNserrRspActMustBeResetDrop(NSNitroRewriteErrors):
    """
        Nitro error code 2846
        Policy action must be DROP|RESET
    """
    pass


class NSNitroNserrInvalSearchSyntax(NSNitroRewriteErrors):
    """
        Nitro error code 2847
        Invalid search syntax
    """
    pass


class NSNitroNserrInvalSearchXpathSyntax(NSNitroRewriteErrors):
    """
        Nitro error code 2848
        Invalid xpath syntax
    """
    pass


class NSNitroNserrInvalSearchPatsetSyntax(NSNitroRewriteErrors):
    """
        Nitro error code 2849
        Invalid patset syntax
    """
    pass


class NSNitroNserrInvalSearchRegexSyntax(NSNitroRewriteErrors):
    """
        Nitro error code 2850
        Invalid regex syntax
    """
    pass


class NSNitroNserrRwReqBodyNotAllowed(NSNitroRewriteErrors):
    """
        Nitro error code 2851
        Request body based expression is not allowed
    """
    pass


class NSNitroNserrRenameNotsupported(NSNitroRewriteErrors):
    """
        Nitro error code 2852
        Renaming this entity is not supported as entity based expression
        is configured
    """
    pass


class NSNitroNserrEntityRemovalNotallowed(NSNitroRewriteErrors):
    """
        Nitro error code 2853
        Removing this entity is not allowed as entity based expression
        is configured
    """
    pass


class NSNitroNserrPiEntityExists(NSNitroRewriteErrors):
    """
        Nitro error code 2854
        Advanced expression entity with same name already exists.
    """
    pass


class NSNitroNserrIncompatibleCalloutChange(NSNitroRewriteErrors):
    """
        Nitro error code 2855
        Incompatible callout change for in-use callout.
    """
    pass


class NSNitroNserrStringmapNotpresent(NSNitroRewriteErrors):
    """
        Nitro error code 2856
        String map does not exist
    """
    pass


class NSNitroUrltransErrors(NSNitroError):
    """
        Base exception class NSNitroUrltransErrors
    """
    pass


class NSNitroNserrUrltransMaxEntities(NSNitroUrltransErrors):
    """
        Nitro error code 2960
        Number of URL Transformation entities exceeds limit
    """
    pass


class NSNitroNserrUrltransInvalProfile(NSNitroUrltransErrors):
    """
        Nitro error code 2962
        Invalid URL Transformation profile
    """
    pass


class NSNitroNserrUrltransActionInuse(NSNitroUrltransErrors):
    """
        Nitro error code 2963
        Action name is already in use
    """
    pass


class NSNitroNserrUrltransPriorityExists(NSNitroUrltransErrors):
    """
        Nitro error code 2964
        An object with this priority already exists
    """
    pass


class NSNitroNserrUrltransReqPcreErr(NSNitroUrltransErrors):
    """
        Nitro error code 2965
        Invalid PCRE expression under 'reqUrlFrom'
    """
    pass


class NSNitroNserrUrltransRespPcreErr(NSNitroUrltransErrors):
    """
        Nitro error code 2966
        Invalid PCRE expression under 'resUrlFrom'
    """
    pass


class NSNitroNserrUrltransReqIntoErr(NSNitroUrltransErrors):
    """
        Nitro error code 2967
        Invalid expression under 'reqUrlInto'
    """
    pass


class NSNitroNserrUrltransRespIntoErr(NSNitroUrltransErrors):
    """
        Nitro error code 2968
        Invalid expression under 'resUrlInto'
    """
    pass


class NSNitroNserrUrltransCookieIntoErr(NSNitroUrltransErrors):
    """
        Nitro error code 2969
        Invalid expression under 'cookieDomainInto'
    """
    pass


class NSNitroNserrUrltransCookiePcreErr(NSNitroUrltransErrors):
    """
        Nitro error code 2970
        Invalid PCRE expression under 'cookieDomainFrom'
    """
    pass


class NSNitroNserrUrltransTooManyBackrefs(NSNitroUrltransErrors):
    """
        Nitro error code 2971
        More than 5 back references in PCRE expression
    """
    pass


class NSNitroNserrUrltransMissingFrom(NSNitroUrltransErrors):
    """
        Nitro error code 2972
        Each 'Into' expression must have a corresponding 'From' pattern
    """
    pass


class NSNitroPiErrors(NSNitroError):
    """
        Base exception class NSNitroPiErrors
    """
    pass


class NSNitroNserrPiLongvsvrname(NSNitroPiErrors):
    """
        Nitro error code 3040
        The name of the label must be less than 32 characters
    """
    pass


class NSNitroNserrPiPriorityExists(NSNitroPiErrors):
    """
        Nitro error code 3041
        A policy is already bound to the specified priority
    """
    pass


class NSNitroNserrInvalpiexpr(NSNitroPiErrors):
    """
        Nitro error code 3073
        Invalid expression
    """
    pass


class NSNitroNserrInvalintop(NSNitroPiErrors):
    """
        Nitro error code 3074
        Expecting numeric arguments in this context for '-',  '+',  '*'
        or '/'
    """
    pass


class NSNitroNserrInvalcompare(NSNitroPiErrors):
    """
        Nitro error code 3075
        Invalid arguments to compare operation
    """
    pass


class NSNitroNserrInvalboolop(NSNitroPiErrors):
    """
        Nitro error code 3076
        The '!',  '||' and '&&' operators can have only boolean
        argument(s)
    """
    pass


class NSNitroNserrArgneg(NSNitroPiErrors):
    """
        Nitro error code 3077
        Argument cannot be negative
    """
    pass


class NSNitroNserrArgexceed(NSNitroPiErrors):
    """
        Nitro error code 3078
        Argument exceeds maximum allowed value
    """
    pass


class NSNitroNserrArgzero(NSNitroPiErrors):
    """
        Nitro error code 3079
        Argument should be non-zero
    """
    pass


class NSNitroNserrMaxheader(NSNitroPiErrors):
    """
        Nitro error code 3080
        Number of custom header exceeds limit
    """
    pass


class NSNitroNserrInvalpicexpr(NSNitroPiErrors):
    """
        Nitro error code 3081
        Compound expression syntax error
    """
    pass


class NSNitroNserrCexprlimit(NSNitroPiErrors):
    """
        Nitro error code 3082
        Compound expression too long
    """
    pass


class NSNitroNserrExprlimit(NSNitroPiErrors):
    """
        Nitro error code 3083
        Expression too long
    """
    pass


class NSNitroNserrSexprlimit(NSNitroPiErrors):
    """
        Nitro error code 3084
        String expression too long
    """
    pass


class NSNitroNserrInvalpisexpr(NSNitroPiErrors):
    """
        Nitro error code 3085
        String expression syntax error
    """
    pass


class NSNitroNserrNobidi(NSNitroPiErrors):
    """
        Nitro error code 3086
        Bi-directional expression not allowed
    """
    pass


class NSNitroNserrNolab(NSNitroPiErrors):
    """
        Nitro error code 3087
        Policy Label does not exist
    """
    pass


class NSNitroNserrInternalLabelRm(NSNitroPiErrors):
    """
        Nitro error code 3088
        Default Policy labels cannot be removed
    """
    pass


class NSNitroNserrPolicyFlowtypeNone(NSNitroPiErrors):
    """
        Nitro error code 3089
        Policy should either be a request or response policy
    """
    pass


class NSNitroNserrInvalPriority(NSNitroPiErrors):
    """
        Nitro error code 3090
        Priority should be non-zero
    """
    pass


class NSNitroNserrNumericexpr(NSNitroPiErrors):
    """
        Nitro error code 3091
        Expression should evaluate to numeric value
    """
    pass


class NSNitroNserrBoolexpr(NSNitroPiErrors):
    """
        Nitro error code 3092
        Expression should evaluate to true or false
    """
    pass


class NSNitroNserrNotbound(NSNitroPiErrors):
    """
        Nitro error code 3093
        Cannot unbind a policy that is not bound
    """
    pass


class NSNitroNserrPolicyInuse(NSNitroPiErrors):
    """
        Nitro error code 3094
        Policy name already in use
    """
    pass


class NSNitroNserrPolicySetNotallowed(NSNitroPiErrors):
    """
        Nitro error code 3095
        Invalid rule/action for bound policy
    """
    pass


class NSNitroNserrInvalidBind(NSNitroPiErrors):
    """
        Nitro error code 3096
        Policy cannot be bound to specified policy label
    """
    pass


class NSNitroNserrUseInvokeResult(NSNitroPiErrors):
    """
        Nitro error code 3097
        USE_INVOCATION_RESULT can be used only with invoke
    """
    pass


class NSNitroNserrInvalUnbind(NSNitroPiErrors):
    """
        Nitro error code 3104
        Policy not bound to specified policy label
    """
    pass


class NSNitroNserrRegexInvalid(NSNitroPiErrors):
    """
        Nitro error code 3105
        Invalid regular expression
    """
    pass


class NSNitroNserrRegexBackref(NSNitroPiErrors):
    """
        Nitro error code 3106
        Backreference in regular expression
    """
    pass


class NSNitroNserrRegexRecursive(NSNitroPiErrors):
    """
        Nitro error code 3107
        Recursive regular expression present
    """
    pass


class NSNitroNserrPixlExprUnsafe(NSNitroPiErrors):
    """
        Nitro error code 3108
        Input expression is unsafe
    """
    pass


class NSNitroNserrPiActionMaxRefReached(NSNitroPiErrors):
    """
        Nitro error code 3109
        Cannot create policy. Binding limit for action reached (65536)
    """
    pass


class NSNitroNserrPiInvalidUnset(NSNitroPiErrors):
    """
        Nitro error code 3110
        Cannot unset rule or action. No changes done
    """
    pass


class NSNitroNserrEmptyString(NSNitroPiErrors):
    """
        Nitro error code 3111
        Zero length string not allowed
    """
    pass


class NSNitroNserrInvalBtwArgs(NSNitroPiErrors):
    """
        Nitro error code 3112
        Arguments to BETWEEN are incorrect
    """
    pass


class NSNitroNserrInvalArgSpecified(NSNitroPiErrors):
    """
        Nitro error code 3113
        GotoPriorityExpression,  flowtype and invoke apply only to
        rewrite,  responder and cache policies
    """
    pass


class NSNitroNserrInvalArgCspl(NSNitroPiErrors):
    """
        Nitro error code 3854
        Target vserver cannot be specified along with
        GotoPriorityExpression and invoke.
    """
    pass


class NSNitroNserrFlowtypeNotApplicable(NSNitroPiErrors):
    """
        Nitro error code 3114
        Flowtype applies only to rewrite,  responder and cache policies
    """
    pass


class NSNitroNserrInvalArgSpecifiedCs(NSNitroPiErrors):
    """
        Nitro error code 3115
        Flowtype and invoke apply only to PI policies.
    """
    pass


class NSNitroNserrInvalGotoexprCs(NSNitroPiErrors):
    """
        Nitro error code 3116
        GotoPriorityExpression applies only to advanced content
        switching policy expressions like rewrite,  responder and cache
        policies.
    """
    pass


class NSNitroNserrRebindFailed(NSNitroPiErrors):
    """
        Nitro error code 3117
        Rebinding of policy with new bind parameters failed. The policy
        is unbound.
    """
    pass


class NSNitroNserrSecondBind(NSNitroPiErrors):
    """
        Nitro error code 3118
        A policy can be bound only once
    """
    pass


class NSNitroNserrNonhttpVs(NSNitroPiErrors):
    """
        Nitro error code 3119
        Specified policy can be bound only to HTTP/SSL vserver
    """
    pass


class NSNitroNserrInvalXpathExpr(NSNitroPiErrors):
    """
        Nitro error code 3858
        XPath Expression Compilation Failed
    """
    pass


class NSNitroNserrXpathExprNotSupported(NSNitroPiErrors):
    """
        Nitro error code 3859
        Unsupported XPath
    """
    pass


class NSNitroNserrTargetInval(NSNitroPiErrors):
    """
        Nitro error code 3860
        Target Vserver cannot be specified for this policy
    """
    pass


class NSNitroNserrNonRespHttpVsList(NSNitroPiErrors):
    """
        Nitro error code 3861
        Specified policy can be bound only to
        HTTP/SSL/TCP/SSL_BRIDGE/FTP/DNS_TCP/RTSP/SSL_TCP/NNTP vserver
    """
    pass


class NSNitroNserrInvalVserverBind(NSNitroPiErrors):
    """
        Nitro error code 3862
        Policy can be bound only to LB/CS vserver types
    """
    pass


class NSNitroNserrAppFreedNsb(NSNitroPiErrors):
    """
        Nitro error code 3863
        Application reset/drop connection and freed nsb
    """
    pass


class NSNitroNserrMultBindInval(NSNitroPiErrors):
    """
        Nitro error code 3864
        CSW/CVPN/DNS/URL-transformation Policies cannot be bound to
        multiple entities
    """
    pass


class NSNitroNserrInvalidKeyvalue(NSNitroPiErrors):
    """
        Nitro error code 3905
        The keyvalue argument is incorrect.
    """
    pass


class NSNitroAsErrors(NSNitroError):
    """
        Base exception class NSNitroAsErrors
    """
    pass


class NSNitroNserrAsNostarturl(NSNitroAsErrors):
    """
        Nitro error code 3120
        No such StartURL check
    """
    pass


class NSNitroNserrAsExistStarturl(NSNitroAsErrors):
    """
        Nitro error code 3121
        The StartURL check is already in use
    """
    pass


class NSNitroNserrAsNodenyurl(NSNitroAsErrors):
    """
        Nitro error code 3122
        No such DenyURL check
    """
    pass


class NSNitroNserrAsExistDenyurl(NSNitroAsErrors):
    """
        Nitro error code 3123
        The DenyURL check is already in use
    """
    pass


class NSNitroNserrAsNocookieconsistency(NSNitroAsErrors):
    """
        Nitro error code 3124
        No such CookieConsistency check
    """
    pass


class NSNitroNserrAsExistCookieconsistency(NSNitroAsErrors):
    """
        Nitro error code 3125
        The CookieConsistency check is already in use
    """
    pass


class NSNitroNserrAsNofieldconsistency(NSNitroAsErrors):
    """
        Nitro error code 3126
        No such FieldConsistency check
    """
    pass


class NSNitroNserrAsExistFieldconsistency(NSNitroAsErrors):
    """
        Nitro error code 3127
        The FieldConsistency check is already in use
    """
    pass


class NSNitroNserrAsNoxss(NSNitroAsErrors):
    """
        Nitro error code 3128
        No such CrossSiteScripting check
    """
    pass


class NSNitroNserrAsExistXss(NSNitroAsErrors):
    """
        Nitro error code 3129
        The CrossSiteScripting check is already in use
    """
    pass


class NSNitroNserrAsNosql(NSNitroAsErrors):
    """
        Nitro error code 3130
        No such SQLInjection check
    """
    pass


class NSNitroNserrAsExistSql(NSNitroAsErrors):
    """
        Nitro error code 3131
        The SQLInjection check is already in use
    """
    pass


class NSNitroNserrAsNofieldformat(NSNitroAsErrors):
    """
        Nitro error code 3132
        No such FieldFormat check
    """
    pass


class NSNitroNserrAsExistFieldformat(NSNitroAsErrors):
    """
        Nitro error code 3133
        The FieldFormat check is already in use
    """
    pass


class NSNitroNserrAsNoobjectexpression(NSNitroAsErrors):
    """
        Nitro error code 3134
        No such SafeObject check
    """
    pass


class NSNitroNserrAsExistObjectexpression(NSNitroAsErrors):
    """
        Nitro error code 3135
        The SafeObject check is already in use
    """
    pass


class NSNitroNserrAsNofieldtype(NSNitroAsErrors):
    """
        Nitro error code 3136
        No such FieldType. See /var/log/ns.log for more details.
    """
    pass


class NSNitroNserrAsBadActionStarturl(NSNitroAsErrors):
    """
        Nitro error code 3138
        Invalid StartURL Action
    """
    pass


class NSNitroNserrAsBadActionDenyurl(NSNitroAsErrors):
    """
        Nitro error code 3139
        Invalid DenyURL Action
    """
    pass


class NSNitroNserrAsBadActionCookieconsistency(NSNitroAsErrors):
    """
        Nitro error code 3140
        Invalid CookieConsistency Action
    """
    pass


class NSNitroNserrAsBadActionFieldconsistency(NSNitroAsErrors):
    """
        Nitro error code 3141
        Invalid FieldConsistency Action
    """
    pass


class NSNitroNserrAsBadActionXss(NSNitroAsErrors):
    """
        Nitro error code 3142
        Invalid CrossSiteScripting Action
    """
    pass


class NSNitroNserrAsBadActionSql(NSNitroAsErrors):
    """
        Nitro error code 3143
        Invalid SQLInjection Action
    """
    pass


class NSNitroNserrAsBadActionFieldformat(NSNitroAsErrors):
    """
        Nitro error code 3144
        Invalid FieldFormat Action
    """
    pass


class NSNitroNserrAsBadActionObjectexpression(NSNitroAsErrors):
    """
        Nitro error code 3145
        Invalid SafeObject Action
    """
    pass


class NSNitroNserrAsBadActionBufferoverflow(NSNitroAsErrors):
    """
        Nitro error code 3146
        Invalid BufferOverflow Action
    """
    pass


class NSNitroNserrAsBadActionCcard(NSNitroAsErrors):
    """
        Nitro error code 3147
        Invalid CreditCard Action
    """
    pass


class NSNitroNserrAsFieldformatMinGtMax(NSNitroAsErrors):
    """
        Nitro error code 3148
        Minimum FieldFormat length cannot exceed maximum FieldFormat
        length
    """
    pass


class NSNitroNserrAsFieldtypeBadNameLen(NSNitroAsErrors):
    """
        Nitro error code 3149
        Invalid FieldType name length
    """
    pass


class NSNitroNserrAsBadCommentLen(NSNitroAsErrors):
    """
        Nitro error code 3150
        Invalid comment length
    """
    pass


class NSNitroNserrAsFieldtypeBadRegexLen(NSNitroAsErrors):
    """
        Nitro error code 3151
        Invalid regex length
    """
    pass


class NSNitroNserrAsSecurityCheckRequired(NSNitroAsErrors):
    """
        Nitro error code 3152
        Security check required
    """
    pass


class NSNitroNserrAsFieldtypeBuiltin(NSNitroAsErrors):
    """
        Nitro error code 3153
        Built-in FieldTypes cannot be modified or deleted
    """
    pass


class NSNitroNserrAsMaxEntities(NSNitroAsErrors):
    """
        Nitro error code 3154
        Number of Application Firewall entities exceeds limit
    """
    pass


class NSNitroNserrAsBadDefaultCharset(NSNitroAsErrors):
    """
        Nitro error code 3155
        Invalid default character set
    """
    pass


class NSNitroNserrAsBadCookieconsistencyName(NSNitroAsErrors):
    """
        Nitro error code 3156
        Invalid Cookie name
    """
    pass


class NSNitroNserrAsBadErrorurl(NSNitroAsErrors):
    """
        Nitro error code 3157
        Invalid ErrorURL
    """
    pass


class NSNitroNserrAsBadEncodingUrl(NSNitroAsErrors):
    """
        Nitro error code 3158
        Invalid encoding for URL
    """
    pass


class NSNitroNserrAsBadEncodingFieldname(NSNitroAsErrors):
    """
        Nitro error code 3159
        Invalid encoding for field name
    """
    pass


class NSNitroNserrAsBadEncodingCookiename(NSNitroAsErrors):
    """
        Nitro error code 3160
        Invalid encoding for cookie name
    """
    pass


class NSNitroNserrAsBadEncodingObjectexpressionName(NSNitroAsErrors):
    """
        Nitro error code 3161
        Invalid encoding for SafeObject name
    """
    pass


class NSNitroNserrAsBadEncodingExpression(NSNitroAsErrors):
    """
        Nitro error code 3162
        Invalid encoding for expression
    """
    pass


class NSNitroNserrAsBadEncodingRegex(NSNitroAsErrors):
    """
        Nitro error code 3163
        Invalid encoding for regex
    """
    pass


class NSNitroNserrAsModifiedUrl(NSNitroAsErrors):
    """
        Nitro error code 3164
        Replaced character that is not printable ASCII with escaped
        equivalent in URL
    """
    pass


class NSNitroNserrAsModifiedObjectexpression(NSNitroAsErrors):
    """
        Nitro error code 3165
        Replaced character that is not printable ASCII with escaped
        equivalent in expression
    """
    pass


class NSNitroNserrAsCffieldBadFieldnameLen(NSNitroAsErrors):
    """
        Nitro error code 3166
        Invalid confidential form field name length
    """
    pass


class NSNitroNserrAsCffieldBadUrlLen(NSNitroAsErrors):
    """
        Nitro error code 3167
        Invalid confidential form field URL length
    """
    pass


class NSNitroNserrAsNocffield(NSNitroAsErrors):
    """
        Nitro error code 3168
        No such confidential form field
    """
    pass


class NSNitroNserrAsBadCffName(NSNitroAsErrors):
    """
        Nitro error code 3169
        Name may not contain leading/trailing spaces.
    """
    pass


class NSNitroNserrAsBadCffUrl(NSNitroAsErrors):
    """
        Nitro error code 3170
        URL may not contain leading/trailing spaces.
    """
    pass


class NSNitroNserrAsCffDup(NSNitroAsErrors):
    """
        Nitro error code 3171
        The confidential field is already in use.
    """
    pass


class NSNitroNserrAsBadActionXdos(NSNitroAsErrors):
    """
        Nitro error code 3172
        Invalid XML Dos Action
    """
    pass


class NSNitroNserrAsExistXmlDosUrl(NSNitroAsErrors):
    """
        Nitro error code 3173
        The XML DoS URL check is already in use.
    """
    pass


class NSNitroNserrXmlUrlNotSupported(NSNitroAsErrors):
    """
        Nitro error code 3174
        Only .* is supported for XML checks.
    """
    pass


class NSNitroNserrAsNoXdosUrl(NSNitroAsErrors):
    """
        Nitro error code 3175
        No such URL exist for XDOS check.
    """
    pass


class NSNitroNserrAsInvalidXmlDosConf(NSNitroAsErrors):
    """
        Nitro error code 3176
        Invalid configuration: xmlMaxFileSize can not be less than
        xmlMinFileSize when both checks are enabled.
    """
    pass


class NSNitroNserrAsBadActionXmlSqlinjection(NSNitroAsErrors):
    """
        Nitro error code 3177
        Invalid XML - SQLInjection Action.
    """
    pass


class NSNitroNserrAsBadActionXmlXss(NSNitroAsErrors):
    """
        Nitro error code 3178
        Invalid XML - CrossSiteScripting Action.
    """
    pass


class NSNitroNserrAsBadActionXmlWellformedness(NSNitroAsErrors):
    """
        Nitro error code 3179
        Invalid XML - Format Action.
    """
    pass


class NSNitroNserrAsBadActionProfileType(NSNitroAsErrors):
    """
        Nitro error code 3180
        Invalid Appsecure Profile Type.
    """
    pass


class NSNitroNserrAsModifiedFieldname(NSNitroAsErrors):
    """
        Nitro error code 3181
        Replaced character that is not printable ASCII with escaped
        equivalent in form field name
    """
    pass


class NSNitroNserrAsBadActionWsi(NSNitroAsErrors):
    """
        Nitro error code 3182
        Invalid XML WS-I Action.
    """
    pass


class NSNitroNserrAsExistXmlWsiUrl(NSNitroAsErrors):
    """
        Nitro error code 3183
        The XML WS-I URL check is already in use.
    """
    pass


class NSNitroNserrAsNoWsiUrl(NSNitroAsErrors):
    """
        Nitro error code 3184
        No such URL exist for WS-I check.
    """
    pass


class NSNitroNserrAsInvalidXmlWsiConf(NSNitroAsErrors):
    """
        Nitro error code 3185
        Invalid WS-I rule id in the list.
    """
    pass


class NSNitroNserrAsObjectnameTooBig(NSNitroAsErrors):
    """
        Nitro error code 3186
        Object too big.
    """
    pass


class NSNitroNserrAsObjectNoExist(NSNitroAsErrors):
    """
        Nitro error code 3187
        Imported file does not exist [Please import the file before
        use]. See /var/log/ns.log for more details.
    """
    pass


class NSNitroNserrAsServerNameTooBig(NSNitroAsErrors):
    """
        Nitro error code 3188
        Server name too big.
    """
    pass


class NSNitroNserrAsObjectNotReadable(NSNitroAsErrors):
    """
        Nitro error code 3189
        Object not readable [Please make sure it exists].
    """
    pass


class NSNitroNserrAsNoprofile(NSNitroAsErrors):
    """
        Nitro error code 3190
        No such profile.
    """
    pass


class NSNitroNserrAsBadActionXmlAttachment(NSNitroAsErrors):
    """
        Nitro error code 3191
        Invalid XML - Attachment Action
    """
    pass


class NSNitroNserrAsBadActionMsgval(NSNitroAsErrors):
    """
        Nitro error code 3192
        Invalid XML Message Validation Action.
    """
    pass


class NSNitroNserrAsExistXmlMsgvalUrl(NSNitroAsErrors):
    """
        Nitro error code 3193
        The XML MSGVAL URL check is already in use.
    """
    pass


class NSNitroNserrAsNoMsgvalUrl(NSNitroAsErrors):
    """
        Nitro error code 3194
        No such URL exist for MSGVAL check.
    """
    pass


class NSNitroNserrAsInvalidXmlMsgvalConf(NSNitroAsErrors):
    """
        Nitro error code 3195
        Invalid MsgVal configuration.
    """
    pass


class NSNitroNserrAsBindXmlMsgvalConf(NSNitroAsErrors):
    """
        Nitro error code 3196
        Error in message validation binding. For More details see log
        messages.
    """
    pass


class NSNitroNserrAsImportFailed(NSNitroAsErrors):
    """
        Nitro error code 3197
        Importing the resource failed
    """
    pass


class NSNitroNserrAsObjectExist(NSNitroAsErrors):
    """
        Nitro error code 3198
        Object already exists
    """
    pass


class NSNitroNserrAsInvalidOption(NSNitroAsErrors):
    """
        Nitro error code 3199
        Invalid option
    """
    pass


class NSNitroNserrAsRemoveFailed(NSNitroAsErrors):
    """
        Nitro error code 3200
        Problem in removing resource
    """
    pass


class NSNitroNserrAsNoResource(NSNitroAsErrors):
    """
        Nitro error code 3201
        No such resource. Object your are trying to update or remove
        does not exist.
    """
    pass


class NSNitroNserrAsShowFailed(NSNitroAsErrors):
    """
        Nitro error code 3202
        Problem in showing object
    """
    pass


class NSNitroNserrAsDependencyFailed(NSNitroAsErrors):
    """
        Nitro error code 3203
        Problem in downloading dependencies
    """
    pass


class NSNitroNserrAsCompilationFailed(NSNitroAsErrors):
    """
        Nitro error code 3204
        Problem compiling object. For more details see /var/log/ns.log
        file
    """
    pass


class NSNitroNserrInvalidObjectName(NSNitroAsErrors):
    """
        Nitro error code 3205
        Invalid name; names must begin with an alphanumeric character or
        underscore and must contain only alphanumerics,  '_',  '#',
        '.',  ' ',  ':',  '@',  '=' or '-'
    """
    pass


class NSNitroNserrAsImportDownloadFailed(NSNitroAsErrors):
    """
        Nitro error code 3206
        Problem in importing the object. Please check the DNS
        NameServer/Route settings and try again. For more details see
        /var/log/ns.log file
    """
    pass


class NSNitroNserrAsResourceInuse(NSNitroAsErrors):
    """
        Nitro error code 3207
        Can not remove resource. Resource is in use
    """
    pass


class NSNitroNserrAsBadMappingData(NSNitroAsErrors):
    """
        Nitro error code 3208
        Mapping Data Corrupted
    """
    pass


class NSNitroNserrAsProfileChangeHtml(NSNitroAsErrors):
    """
        Nitro error code 3209
        HTML checks will not be applicable when profile type is XML
    """
    pass


class NSNitroNserrAsProfileChangeXml(NSNitroAsErrors):
    """
        Nitro error code 3210
        XML checks will not be applicable when profile type is HTML
    """
    pass


class NSNitroNserrAsImportAlreadyInprocess(NSNitroAsErrors):
    """
        Nitro error code 3211
        Import failed. Another resource with the same name being
        processed
    """
    pass


class NSNitroNserrAsInvalidXmlErrorObject(NSNitroAsErrors):
    """
        Nitro error code 3212
        Invalid XML error object
    """
    pass


class NSNitroNserrAsXmlWellformednessDisabled(NSNitroAsErrors):
    """
        Nitro error code 3213
        XML Security checks can not be performed,  once an XML message
        is found not wellformed.
    """
    pass


class NSNitroNserrAsIndividualImportLimitExceeded(NSNitroAsErrors):
    """
        Nitro error code 3214
        Import failed - importing file size greater than configured size
        limit
    """
    pass


class NSNitroNserrAsTotalImportLimitExceeded(NSNitroAsErrors):
    """
        Nitro error code 3215
        Import failed - exceeding the configured total size limit on the
        imported objects
    """
    pass


class NSNitroNserrAsLearningBusy(NSNitroAsErrors):
    """
        Nitro error code 3216
        Please wait for the learning database to finish updating
    """
    pass


class NSNitroNserrAsDeprecatedXmlWsiRuleR4003(NSNitroAsErrors):
    """
        Nitro error code 3217
        WS-I Rule R4003 has been deprecated,  it will be removed from
        the WS-I binding list.
    """
    pass


class NSNitroNserrAsExistXmlAttachmentUrl(NSNitroAsErrors):
    """
        Nitro error code 3218
        The XML Attachment URL check is already in use.
    """
    pass


class NSNitroNserrAsNoXmlAttachmentUrl(NSNitroAsErrors):
    """
        Nitro error code 3219
        No such URL exist for XML Attachment check.
    """
    pass


class NSNitroNserrAsBadActionSoapFault(NSNitroAsErrors):
    """
        Nitro error code 3220
        Invalid SOAP Fault Filtering Action.
    """
    pass


class NSNitroNserrAsXmlDosValueOutOfRange(NSNitroAsErrors):
    """
        Nitro error code 3221
        XML DoS check value is not within the allowed range.
    """
    pass


class NSNitroNserrAsXmlMsgvalCliError(NSNitroAsErrors):
    """
        Nitro error code 3222
        -XMLValidateResponse requires one of [-XMLValidateSOAPEnvelope,
        -XMLWSDL,  -XMLRequestSchema,  -XMLResponseSchema]
    """
    pass


class NSNitroNserrAsInvalidCustomSettingsObject(NSNitroAsErrors):
    """
        Nitro error code 3223
        Import failed. Please check syntax of custom settings object
    """
    pass


class NSNitroNserrAsSessionTimeoutLifetimeConflict(NSNitroAsErrors):
    """
        Nitro error code 3224
        The session lifetime cannot be less than the session timeout
    """
    pass


class NSNitroNserrAsClassicPolicyAlreadyBound(NSNitroAsErrors):
    """
        Nitro error code 3225
        Failed to bind advanced policy because a classic one is already
        bound globally or to a vserver. Binding classic and advanced
        policies at the same time is not allowed
    """
    pass


class NSNitroNserrAsAdvancedPolicyAlreadyBound(NSNitroAsErrors):
    """
        Nitro error code 3226
        Failed to bind classic policy because an advanced one is already
        bound globally or to a vserver. Binding classic and advanced
        policies at the same time is not allowed
    """
    pass


class NSNitroNserrAsCustomSettingsNoInjectionType(NSNitroAsErrors):
    """
        Nitro error code 3227
        Failed to set custom settings object. One of the  tags do not
        have 'type' attribute
    """
    pass


class NSNitroNserrAsNocsrfTag(NSNitroAsErrors):
    """
        Nitro error code 3228
        No such CrossSiteRequestForgery check
    """
    pass


class NSNitroNserrAsExistCsrfTag(NSNitroAsErrors):
    """
        Nitro error code 3229
        The CrossSiteRequestForgery check is already in use
    """
    pass


class NSNitroNserrAsBadActionCsrfTag(NSNitroAsErrors):
    """
        Nitro error code 3230
        Invalid CSRF Tag Action
    """
    pass


class NSNitroNserrAsTurningTaggingOffCsrfTagOn(NSNitroAsErrors):
    """
        Nitro error code 3231
        Must set CSRF tagging check to 'none' before disabling form
        tagging.
    """
    pass


class NSNitroNserrAsTurningCsrfTagOnTaggingOff(NSNitroAsErrors):
    """
        Nitro error code 3232
        Form tagging must be enabled before turning on CSRF tag checks.
    """
    pass


class NSNitroNserrAsImportLimitLessThanImportDirSize(NSNitroAsErrors):
    """
        Nitro error code 3233
        Import limit should be greater than the current total imported
        objects size.
    """
    pass


class NSNitroNserrAsUnsupportedImportProtocol(NSNitroAsErrors):
    """
        Nitro error code 3234
        Unsupported import source protocol. Supported protocols are http
        and https
    """
    pass


class NSNitroNserrAsUnsupportedExportProtocol(NSNitroAsErrors):
    """
        Nitro error code 3235
        Unsupported export target protocol. Supported protocols are http
        and  https
    """
    pass


class NSNitroNserrAsExportFailed(NSNitroAsErrors):
    """
        Nitro error code 3236
        Export failed. Check /var/log/ns.log for details.
    """
    pass


class NSNitroNserrAsBadLocalFile(NSNitroAsErrors):
    """
        Nitro error code 3237
        Local file cannot use .. to backtrack up a directory.
    """
    pass


class NSNitroNserrAsInvalidRegexCustomObject(NSNitroAsErrors):
    """
        Nitro error code 3238
        Invalid regular expression in custom object. Reverting to
        default settings.
    """
    pass


class NSNitroNserrAsBuiltinInvalidOp(NSNitroAsErrors):
    """
        Nitro error code 3239
        Invalid operation for built-in profile
    """
    pass


class NSNitroNserrAsInvalidAdvPolicyState(NSNitroAsErrors):
    """
        Nitro error code 3240
        Cannot bind advanced policy with state set to DISABLED
    """
    pass


class NSNitroNserrAsBuiltinNamesInConf(NSNitroAsErrors):
    """
        Nitro error code 3241
        Entities with names reserved for built-in profiles have been
        discarded
    """
    pass


class NSNitroNserrAsDefaultProfileIsBypass(NSNitroAsErrors):
    """
        Nitro error code 3242
        The default profile is set to bypass traffic. It can be set
        using the 'set appfw settings' command.
    """
    pass


class NSNitroNserrAsNoLearnDenyurl(NSNitroAsErrors):
    """
        Nitro error code 3243
        Learn is not supported as a denyURLAction.
    """
    pass


class NSNitroNserrAsNoLearnCsrfTag(NSNitroAsErrors):
    """
        Nitro error code 3244
        Learn is not supported as a CSRFtagAction.
    """
    pass


class NSNitroNserrAsNoLearnCcard(NSNitroAsErrors):
    """
        Nitro error code 3245
        Learn is not supported as a creditCardAction.
    """
    pass


class NSNitroNserrAsNoLearnBufferoverflow(NSNitroAsErrors):
    """
        Nitro error code 3246
        Learn is not supported as a bufferOvewflowAction.
    """
    pass


class NSNitroNserrAsNoLearnXmlFormat(NSNitroAsErrors):
    """
        Nitro error code 3247
        Learn is not supported as an XMLFormatAction.
    """
    pass


class NSNitroNserrAsNoLearnXmlSqlinjection(NSNitroAsErrors):
    """
        Nitro error code 3251
        Learn is not supported as an XMLSQLInjectionAction.
    """
    pass


class NSNitroNserrAsNoLearnXmlXss(NSNitroAsErrors):
    """
        Nitro error code 3252
        Learn is not supported as an XMLXSSAction.
    """
    pass


class NSNitroNserrAsNoLearnXmlMsgval(NSNitroAsErrors):
    """
        Nitro error code 3253
        Learn is not supported as an XMLValidationAction.
    """
    pass


class NSNitroNserrAsNoLearnXmlSoapFault(NSNitroAsErrors):
    """
        Nitro error code 3254
        Learn is not supported as an XMLSOAPFaultAction.
    """
    pass


class NSNitroNserrAsImportInternalError(NSNitroAsErrors):
    """
        Nitro error code 3255
        Internal error while importing resource.
    """
    pass


class NSNitroNserrAsNetsvcConnFailed(NSNitroAsErrors):
    """
        Nitro error code 3256
        Critical internal error. please retry after some time.
    """
    pass


class NSNitroNserrAsValidationFailed(NSNitroAsErrors):
    """
        Nitro error code 3257
        Problem validating WSDL against WSDL specification. For more
        details see /var/log/ns.log file.
    """
    pass


class NSNitroNserrAsCkiTransformDisabled(NSNitroAsErrors):
    """
        Nitro error code 3258
        This setting will not take effect until cookieTransforms is
        turned ON.
    """
    pass


class NSNitroNserrAsNoxmlxss(NSNitroAsErrors):
    """
        Nitro error code 3259
        No such XMLXSS check
    """
    pass


class NSNitroNserrAsExistXmlxss(NSNitroAsErrors):
    """
        Nitro error code 3260
        The XMLXSS check is already in use
    """
    pass


class NSNitroNserrAsNoxmlsql(NSNitroAsErrors):
    """
        Nitro error code 3261
        No such XMLSQLInjection check
    """
    pass


class NSNitroNserrAsExistXmlsql(NSNitroAsErrors):
    """
        Nitro error code 3262
        The XMLSQLInjection check is already in use
    """
    pass


class NSNitroNserrAsNoEndtag(NSNitroAsErrors):
    """
        Nitro error code 3263
        Missing end tag in the imported custom settings file.
    """
    pass


class NSNitroNserrAsSigInvalidRuleid(NSNitroAsErrors):
    """
        Nitro error code 3264
        Invalid rule id in imported signature.
    """
    pass


class NSNitroNserrAsSigInvalidRuleVersion(NSNitroAsErrors):
    """
        Nitro error code 3265
        Invalid version in imported signature.
    """
    pass


class NSNitroNserrAsSigParseError(NSNitroAsErrors):
    """
        Nitro error code 3266
        Error parsing imported signatures.
    """
    pass


class NSNitroNserrAsSigInvalidAttribute(NSNitroAsErrors):
    """
        Nitro error code 3267
        Imported signatures have invalid attributes
    """
    pass


class NSNitroNserrAsSigMultipleLocations(NSNitroAsErrors):
    """
        Nitro error code 3268
        Imported signature patterns has multiple locations
    """
    pass


class NSNitroNserrAsSigInvalidState(NSNitroAsErrors):
    """
        Nitro error code 3269
        Error parsing imported signatures. Invalid parse state.
    """
    pass


class NSNitroNserrAsCkiEncryptMethodIsNone(NSNitroAsErrors):
    """
        Nitro error code 3270
        For security purposes,  please set the NS encryptions parameter
        using the \"set ns encryptionParams\" command.
    """
    pass


class NSNitroNserrAsUpdateFailed(NSNitroAsErrors):
    """
        Nitro error code 3271
        Updating the resource failed
    """
    pass


class NSNitroNserrAsObjectNotUsed(NSNitroAsErrors):
    """
        Nitro error code 3272
        The specified object is not used
    """
    pass


class NSNitroNserrAsSigMultipleUrls(NSNitroAsErrors):
    """
        Nitro error code 3273
        Imported signature pattern location has multiple URLs
    """
    pass


class NSNitroNserrAsSigMultipleFieldNames(NSNitroAsErrors):
    """
        Nitro error code 3274
        Imported signature pattern location has multiple field names
    """
    pass


class NSNitroNserrAsSqlinjectionKeywordInvalidAttribute(NSNitroAsErrors):
    """
        Nitro error code 3284
        Imported signatures has invalid SQL injection attributes.
    """
    pass


class NSNitroNserrAsSplstringInvalidAttribute(NSNitroAsErrors):
    """
        Nitro error code 3285
        Imported signatures has invalid special string attributes.
    """
    pass


class NSNitroNserrAsSqlinjectionKeywordLiteralExceedMaxlen(NSNitroAsErrors):
    """
        Nitro error code 3286
        Maximum allowed length for type \"LITERAL\" for keyword is 255.
    """
    pass


class NSNitroNserrAsSplstringLiteralExceedMaxlen(NSNitroAsErrors):
    """
        Nitro error code 3287
        Maximum allowed length for type \"LITERAL\" for special string
        is 255.
    """
    pass


class NSNitroNserrAsXssDeniedPatternInvalidAttribute(NSNitroAsErrors):
    """
        Nitro error code 3294
        Imported signatures has invalid denied pattern attribute.
    """
    pass


class NSNitroNserrAsXssDeniedPatternExceedMaxlen(NSNitroAsErrors):
    """
        Nitro error code 3295
        Maximum allowed length for type \"LITERAL\" for denied pattern
        is 255.
    """
    pass


class NSNitroNserrAsXssAllowedPatternInvalidAttribute(NSNitroAsErrors):
    """
        Nitro error code 3296
        Imported signatures has invalid allowed pattern attribute.
    """
    pass


class NSNitroNserrAsXssAllowedPatternExceedMaxlen(NSNitroAsErrors):
    """
        Nitro error code 3297
        Maximum allowed length for type \"LITERAL\" for allowed pattern
        is 255.
    """
    pass


class NSNitroNserrAsSigInternalError(NSNitroAsErrors):
    """
        Nitro error code 3299
        Internal error when configuring signatures.
    """
    pass


class NSNitroNserrAsSigNonLiteralFastmatch(NSNitroAsErrors):
    """
        Nitro error code 3305
        Signature file has \"fastmatch\" on a non-literal match.
    """
    pass


class NSNitroNserrAsSigNegatedLiteralFastmatch(NSNitroAsErrors):
    """
        Nitro error code 3306
        Signature file has \"fastmatch\" on a negated literal match.
    """
    pass


class NSNitroNserrAsSigMemAllocFailed(NSNitroAsErrors):
    """
        Nitro error code 3307
        Memory allocation failed while loading signatures.
    """
    pass


class NSNitroNserrAsSigTooManyPatterns(NSNitroAsErrors):
    """
        Nitro error code 3308
        Signature file has a rule with too many patterns.
    """
    pass


class NSNitroNserrAsSigLiteralHexParseError(NSNitroAsErrors):
    """
        Nitro error code 3309
        Signature file has a pattern with hex byte syntax error.
    """
    pass


class NSNitroNserrAsSigPcreCompileError(NSNitroAsErrors):
    """
        Nitro error code 3310
        Signature file has an invalid PCRE.
    """
    pass


class NSNitroNserrAsSigInvalidFileVersion(NSNitroAsErrors):
    """
        Nitro error code 3314
        Signature file has an invalid SignaturesFile 'version' value.
    """
    pass


class NSNitroCvpnErrors(NSNitroError):
    """
        Base exception class NSNitroCvpnErrors
    """
    pass


class NSNitroNserrNoSuchProfile(NSNitroCvpnErrors):
    """
        Nitro error code 3248
        Profile does not exist
    """
    pass


class NSNitroNserrProfileInUse(NSNitroCvpnErrors):
    """
        Nitro error code 3249
        Profile in use
    """
    pass


class NSNitroVmacErrors(NSNitroError):
    """
        Base exception class NSNitroVmacErrors
    """
    pass


class NSNitroNserrInterfaceBound(NSNitroVmacErrors):
    """
        Nitro error code 3329
        Interface already bound
    """
    pass


class NSNitroNserrVridInterfaceNotBound(NSNitroVmacErrors):
    """
        Nitro error code 3330
        Interface not bound
    """
    pass


class NSNitroNserrNoSuchInterface(NSNitroVmacErrors):
    """
        Nitro error code 3331
        No such interface
    """
    pass


class NSNitroSnmpErrors(NSNitroError):
    """
        Base exception class NSNitroSnmpErrors
    """
    pass


class NSNitroNserrInvalthreshold(NSNitroSnmpErrors):
    """
        Nitro error code 3457
        Threshold value for this alarm is a percentage (1 - 100)
    """
    pass


class NSNitroNserrWrongthresholds(NSNitroSnmpErrors):
    """
        Nitro error code 3458
        Normal threshold must be lower than alarm threshold
    """
    pass


class NSNitroNserrInvalidSrcip(NSNitroSnmpErrors):
    """
        Nitro error code 3459
        Source IP of SNMP trap should be NetScaler IP,  subnet IP or
        mapped IP
    """
    pass


class NSNitroNserrThresholdUnsettable(NSNitroSnmpErrors):
    """
        Nitro error code 3460
        Threshold value cannot be set/unset for this alarm
    """
    pass


class NSNitroNserrTimeUnsettable(NSNitroSnmpErrors):
    """
        Nitro error code 3461
        Time interval cannot be set/unset for this alarm
    """
    pass


class NSNitroNserrWrongLowThresholds(NSNitroSnmpErrors):
    """
        Nitro error code 3462
        Normal threshold must be higher than alarm threshold
    """
    pass


class NSNitroHtmlInjectionErrors(NSNitroError):
    """
        Base exception class NSNitroHtmlInjectionErrors
    """
    pass


class NSNitroInatErrors(NSNitroError):
    """
        Base exception class NSNitroInatErrors
    """
    pass


class NSNitroNserrPublicip(NSNitroInatErrors):
    """
        Nitro error code 3888
        Invalid Public IP address
    """
    pass


class NSNitroNserrPrivateip(NSNitroInatErrors):
    """
        Nitro error code 3889
        Invalid Private IP address
    """
    pass


class NSNitroNserrProxyip(NSNitroInatErrors):
    """
        Nitro error code 3890
        Invalid Proxy IP address
    """
    pass


class NSNitroNserrWildcardtcpvip(NSNitroInatErrors):
    """
        Nitro error code 3891
        TCPPROXY enabled when wildcard TCP Vserver already present
    """
    pass


class NSNitroNserrWildcardanyvip(NSNitroInatErrors):
    """
        Nitro error code 3892
        INAT rule with wildcard ANY vserver,  not allowed
    """
    pass


class NSNitroNserrFtpvippresent(NSNitroInatErrors):
    """
        Nitro error code 3893
        FTP enabled when FTP vserver already present
    """
    pass


class NSNitroNserrV46Usip(NSNitroInatErrors):
    """
        Nitro error code 3894
        USIP is not allowed in mixed topology
    """
    pass


class NSNitroNserrIncompatibleIp(NSNitroInatErrors):
    """
        Nitro error code 3895
        Private and Proxy IP should share the same IP Type
    """
    pass


class NSNitroNetbridgeErrors(NSNitroError):
    """
        Base exception class NSNitroNetbridgeErrors
    """
    pass


class NSNitroNserrTnlNetbridged(NSNitroNetbridgeErrors):
    """
        Nitro error code 3920
        Tunnel bound to netbridge
    """
    pass


class NSNitroNserrTnlGre(NSNitroNetbridgeErrors):
    """
        Nitro error code 3921
        Tunnel protocol is not GRE
    """
    pass


class NSNitroNserrTnlRipmask(NSNitroNetbridgeErrors):
    """
        Nitro error code 3922
        Remote IP mask of the tunnel should be 255.255.255.255
    """
    pass


class NSNitroNserrVlanNetbridged(NSNitroNetbridgeErrors):
    """
        Nitro error code 3923
        Vlan already bound to some netbridge
    """
    pass


class NSNitroNserrMaxNetbridgeTunnel(NSNitroNetbridgeErrors):
    """
        Nitro error code 3924
        reached maximum netbridge tunnel bindings
    """
    pass


class NSNitroNserrTunBound(NSNitroNetbridgeErrors):
    """
        Nitro error code 3925
        Tunnel already bound to this netbridge
    """
    pass


class NSNitroNserrSubnetBound(NSNitroNetbridgeErrors):
    """
        Nitro error code 3926
        Subnet already bound to this netbridge
    """
    pass


class NSNitroAppflowErrors(NSNitroError):
    """
        Base exception class NSNitroAppflowErrors
    """
    pass


class NSNitroNserrAppflowInvalidport(NSNitroAppflowErrors):
    """
        Nitro error code 3936
        Invalid collector port
    """
    pass


class NSNitroNserrIpfixMaxCollectors(NSNitroAppflowErrors):
    """
        Nitro error code 3937
        Exceeded maximum collectors limit
    """
    pass


class NSNitroNserrNoSuchCollector(NSNitroAppflowErrors):
    """
        Nitro error code 3938
        No matching collector
    """
    pass


class NSNitroNserrAppflowNcoreOnly(NSNitroAppflowErrors):
    """
        Nitro error code 3939
        The AppFlow feature is available only on Citrix NetScaler nCore.
    """
    pass


class NSNitroNserrAppflowNonzeroActionRefcount(NSNitroAppflowErrors):
    """
        Nitro error code 3940
        The specified AppFlow collector is being used in an AppFlow
        action.
    """
    pass


class NSNitroNserrAppflowCollectorNameInuse(NSNitroAppflowErrors):
    """
        Nitro error code 3941
        AppFlow collector name already in use.
    """
    pass


class NSNitroNserrAppflowActInval(NSNitroAppflowErrors):
    """
        Nitro error code 3942
        No such AppFlow action exists.
    """
    pass


class NSNitroIntfErrors(NSNitroError):
    """
        Base exception class NSNitroIntfErrors
    """
    pass


class NSNitroNserr1gsfpspeedlimit(NSNitroIntfErrors):
    """
        Nitro error code 3968
        1G SFP's are restricted to speed 1000 or AUTO only
    """
    pass


class NSNitroNserr1gsfpduplexlimit(NSNitroIntfErrors):
    """
        Nitro error code 3969
        1G SFP's are restricted to duplex FULL or AUTO only
    """
    pass


class NSNitroNserr1gspeedlimit(NSNitroIntfErrors):
    """
        Nitro error code 3970
        1G port can not be configured as 10G speed
    """
    pass


class NSNitroNserr1gduplexlimit(NSNitroIntfErrors):
    """
        Nitro error code 3971
        1G port can not be configured as HALF duplex
    """
    pass


class NSNitroNserr10gspeedlimit(NSNitroIntfErrors):
    """
        Nitro error code 3972
        10G ports on this platform can only be configured as speed 1G,
        10G or AUTO only
    """
    pass


class NSNitroNserr10gduplexlimit(NSNitroIntfErrors):
    """
        Nitro error code 3973
        10G ports on this platform can only be configured as duplex FULL
        or AUTO only
    """
    pass


class NSNitroNserr10gautoneglimit(NSNitroIntfErrors):
    """
        Nitro error code 3974
        10G ports on this platform don't support AUTONEG
    """
    pass


class NSNitroNserr10gspeedonly(NSNitroIntfErrors):
    """
        Nitro error code 3975
        10G ports on this platform are restricted to speed 10000 or AUTO
        only
    """
    pass


class NSNitroNserrFullduplexonly(NSNitroIntfErrors):
    """
        Nitro error code 3976
        These ports don't support HALF duplex mode
    """
    pass


class NSNitroWarningErrors(NSNitroError):
    """
        Base exception class NSNitroWarningErrors
    """
    pass


NSNitroExceptionClassMap = defaultdict(lambda: NSNitroError)
NSNitroExceptions = {
    256: NSNitroNserrNotrunning,
    257: NSNitroNserrPerm,
    258: NSNitroNserrNoent,
    259: NSNitroNserrSrch,
    260: NSNitroNserrIntr,
    261: NSNitroNserrIo,
    262: NSNitroNserrNxio,
    263: NSNitroNserr2big,
    264: NSNitroNserrNoexec,
    265: NSNitroNserrBadf,
    266: NSNitroNserrChild,
    267: NSNitroNserrDeadlk,
    268: NSNitroNserrNomem,
    269: NSNitroNserrAcces,
    270: NSNitroNserrFault,
    271: NSNitroNserrNotblk,
    272: NSNitroNserrBusy,
    273: NSNitroNserrExist,
    274: NSNitroNserrXdev,
    275: NSNitroNserrNodev,
    276: NSNitroNserrNotdir,
    277: NSNitroNserrIsdir,
    278: NSNitroNserrInval,
    279: NSNitroNserrNfile,
    280: NSNitroNserrMfile,
    281: NSNitroNserrNotty,
    282: NSNitroNserrTxtbsy,
    283: NSNitroNserrFbig,
    284: NSNitroNserrNospace,
    285: NSNitroNserrSpipe,
    286: NSNitroNserrRofs,
    287: NSNitroNserrMlink,
    288: NSNitroNserrPipe,
    289: NSNitroNserrDom,
    290: NSNitroNserrRange,
    291: NSNitroNserrAgain,
    292: NSNitroNserrInprogress,
    293: NSNitroNserrAlready,
    294: NSNitroNserrNotsock,
    295: NSNitroNserrDestaddrreq,
    296: NSNitroNserrMsgsize,
    297: NSNitroNserrPrototype,
    298: NSNitroNserrNoprotoopt,
    299: NSNitroNserrProtonosupport,
    300: NSNitroNserrSocktnosupport,
    301: NSNitroNserrOpnotsupp,
    302: NSNitroNserrPfnosupport,
    303: NSNitroNserrAfnosupport,
    304: NSNitroNserrAddrinuse,
    305: NSNitroNserrAddrnotavail,
    306: NSNitroNserrNetdown,
    307: NSNitroNserrNetunreach,
    308: NSNitroNserrNetreset,
    309: NSNitroNserrConnaborted,
    310: NSNitroNserrConnreset,
    311: NSNitroNserrNobufs,
    312: NSNitroNserrIsconn,
    313: NSNitroNserrNotconn,
    314: NSNitroNserrShutdown,
    315: NSNitroNserrToomanyrefs,
    316: NSNitroNserrTimedout,
    317: NSNitroNserrConnrefused,
    318: NSNitroNserrLoop,
    319: NSNitroNserrNametoolong,
    320: NSNitroNserrHostdown,
    321: NSNitroNserrHostunreach,
    322: NSNitroNserrNotempty,
    323: NSNitroNserrProclim,
    324: NSNitroNserrUsers,
    325: NSNitroNserrDquot,
    326: NSNitroNserrStale,
    327: NSNitroNserrRemote,
    328: NSNitroNserrBadrpc,
    329: NSNitroNserrRpcmismatch,
    330: NSNitroNserrProgunavail,
    331: NSNitroNserrProgmismatch,
    332: NSNitroNserrProcunavail,
    333: NSNitroNserrNolck,
    334: NSNitroNserrNosys,
    335: NSNitroNserrFtype,
    336: NSNitroNserrAuth,
    337: NSNitroNserrNeedauth,
    338: NSNitroNserrWouldblock,
    339: NSNitroNserrNocode,
    340: NSNitroNserrNotsuser,
    341: NSNitroNserrBigdata,
    342: NSNitroNserrSmalldata,
    343: NSNitroNserrNomorent,
    344: NSNitroNserrNoservice,
    345: NSNitroNserrOserror,
    346: NSNitroNserrNonexpcmd,
    347: NSNitroNserrCmdpropfail,
    348: NSNitroNserrToomanynodes,
    349: NSNitroNserrSecondaryfail,
    350: NSNitroNserrInvalbackup,
    351: NSNitroNserrNoserver,
    352: NSNitroNserrLoginreqd,
    353: NSNitroNserrRpcinval,
    354: NSNitroNserrNouser,
    355: NSNitroNserrInvalpasswd,
    356: NSNitroNserrLicense,
    357: NSNitroNserrDeferred,
    358: NSNitroNserrPropauthfail,
    359: NSNitroNserrNodelsuser,
    360: NSNitroNserrNomodsuser,
    362: NSNitroNserrInvalnodeid,
    363: NSNitroNserrNotopha,
    364: NSNitroNserrNooppeerbad,
    365: NSNitroNserrNoopbad,
    366: NSNitroNserrNopnow,
    367: NSNitroNserrNooppri,
    368: NSNitroNserrNoopsec,
    369: NSNitroNserrRedirect,
    370: NSNitroNserrBufoverflow,
    371: NSNitroNserrNouserpolicy,
    372: NSNitroNserrNosysgroup,
    373: NSNitroNserrNosyscmdpol,
    374: NSNitroNserrHaipv6pt,
    375: NSNitroNserrHansipv6,
    376: NSNitroNserrNsipv6active,
    377: NSNitroNserrRtmonStandalone,
    378: NSNitroNserrIpv6featDisabled,
    394: NSNitroNserrIprangenotallowd,
    395: NSNitroNserrIvalidiprange,
    396: NSNitroNserrIprangemaxlimit,
    397: NSNitroNserrIpNotExist,
    398: NSNitroNserrToomanyrules,
    399: NSNitroNserrPasswdLenMin8,
    410: NSNitroNserrSyncDisabled,
    411: NSNitroNserrNodeDisabled,
    412: NSNitroNserrSyncProgress,
    413: NSNitroNserrAdnsPerm,
    414: NSNitroNserrNoincIpsamesubnet,
    415: NSNitroNserrInvalidPeerip,
    416: NSNitroNserrRedirect307,
    417: NSNitroNserrInvalhostname,
    418: NSNitroNserrRewriteNotSupported,
    419: NSNitroNserrIpchgDeny,
    420: NSNitroNserrIpchgGslb,
    421: NSNitroNserrGslbIpchg,
    422: NSNitroNserrNoauditsrvc,
    423: NSNitroNserrLacpkeyNotset,
    424: NSNitroNserrChannelInusebylacp,
    425: NSNitroNserrLacpenabled,
    426: NSNitroNserrIfacemanuallybound,
    427: NSNitroNserrIntrecinuse,
    428: NSNitroNserrIpportVipConflict,
    429: NSNitroNserrIpportVipBound,
    430: NSNitroNserrNoBackupVip,
    431: NSNitroNserrReqSetArgs,
    432: NSNitroNserrSvcgrpMemberNameconflict,
    433: NSNitroNserrServerNameExist,
    434: NSNitroNserrMaxServiceBindingOnVserver,
    435: NSNitroNserrMaxSvcEntityBindingOnSvcgroup,
    436: NSNitroNserrFsmall,
    437: NSNitroNserrIntoflow,
    438: NSNitroNserrAsyncBlocked,
    439: NSNitroNserrSaclClearpending,
    440: NSNitroNserrSaclNameExists,
    441: NSNitroNserrSaclSupersetExists,
    442: NSNitroNserrSaclSubsetExists,
    443: NSNitroNserrNoincRoutemonitor,
    444: NSNitroNserrSessionExpired,
    445: NSNitroNserrSessionExceeded,
    446: NSNitroNserrCfeConnExceeded,
    447: NSNitroNserrCfeConnPerSessExceeded,
    449: NSNitroNserrCfeKillself,
    450: NSNitroNserrCfeIncompletesession,
    451: NSNitroNserrCfeInvalidsession,
    452: NSNitroNserrCfeSessionNoexist,
    453: NSNitroNserrSysgroupUserExists,
    454: NSNitroNserrSysgroupPolicyExists,
    455: NSNitroNserrSleep,
    456: NSNitroNserrPpedie,
    457: NSNitroNserrNoconnCmdpropfail,
    458: NSNitroNserrTimeoutSecondary,
    459: NSNitroNserrRpcTimeout,
    460: NSNitroNserrNotSupported,
    461: NSNitroNserrNoentVserver,
    462: NSNitroNserrNoentSvc,
    463: NSNitroNserrNoentSvcSvcgrp,
    464: NSNitroNserrHaNov4Netmask,
    465: NSNitroNserrMaxVsevrverBindingsToService,
    466: NSNitroNserrSacl6Clearpending,
    467: NSNitroNserrSacl6NameExists,
    468: NSNitroNserrSacl6SupersetExists,
    469: NSNitroNserrSacl6SubsetExists,
    470: NSNitroNserrNoBackupVipBound,
    471: NSNitroNserrVserverTypeMismatch,
    472: NSNitroNserrSessionExpiredRedirect,
    480: NSNitroNserrCaconfCnflHeurexpRelexp,
    481: NSNitroNserrCaconfCnflHeurexpRelexpmili,
    482: NSNitroNserrCaconfCnflRelexpRelexpmili,
    483: NSNitroNserrCaconfCnflAbsexpHeurexp,
    484: NSNitroNserrCaconfCnflAbsexpRelexpmili,
    485: NSNitroNserrCaconfCnflAbsexpgmtHeruexp,
    486: NSNitroNserrCaconfCnflAbsexpAbsexpgmt,
    487: NSNitroNserrCaconfCnflAbsexpgmtRelexpmili,
    488: NSNitroNserrCaconfCnflHitparamsHitslctr,
    489: NSNitroNserrCaconfCnflInvalparamsHitslctr,
    490: NSNitroNserrCaconfCnflHitparamsInvlslctr,
    491: NSNitroNserrCaconfCnflInvalparamsInvlslctr,
    492: NSNitroNserrCaconfCnflHitslctrMatchcooky,
    493: NSNitroNserrCaconfCnflHitslctrInvalrest2host,
    494: NSNitroNserrCaconfCnflHitslctrIgnrparamvalcase,
    495: NSNitroNserrCaconfCnflInvalslctrMatchcooky,
    496: NSNitroNserrCaconfCnflInvalslctrInvalrest2host,
    497: NSNitroNserrCaconfCnflInvalslctrIgnrparamvalcase,
    498: NSNitroNserrCaconfCnflPosrelexpRelexp,
    499: NSNitroNserrCaconfCnflPosrelexpRelexpmili,
    500: NSNitroNserrCaconfCnflAbsexpPosrelexp,
    501: NSNitroNserrCaconfCnflAbsexpgmtPosrelexp,
    502: NSNitroNserrCaconfCnflIgnrparamvalcaseHitparams,
    503: NSNitroNserrCaconfCnflHitInvalparamsMatchcuky,
    504: NSNitroNserrCaconfCnflInvalrest2hostInvalparam,
    505: NSNitroNserrCaconfCnflPrefetchPrefetchsec,
    506: NSNitroNserrCaconfCnflPrefetchPrefetchmili,
    507: NSNitroNserrCaconfCnflPrefetchmiliPrefetchsec,
    508: NSNitroNserrCaconfArgLeMinVal,
    509: NSNitroNserrCaconfArgGeMaxVal,
    512: NSNitroNserrPxyCacheHmg,
    513: NSNitroNserrPxyRmLastMemt,
    514: NSNitroNserrCswInsInvalPfx,
    515: NSNitroNserrPengExprIvalName,
    516: NSNitroNserrCswBigUrl,
    517: NSNitroNserrCswBigPfx,
    518: NSNitroNserrCswBigSfx,
    519: NSNitroNserrCswInvalSfx,
    520: NSNitroNserrExprNomethod,
    521: NSNitroNserrExprNourltokens,
    522: NSNitroNserrExprNoversion,
    523: NSNitroNserrExprNohdr,
    524: NSNitroNserrExprNocacntl,
    525: NSNitroNserrExprNoprag,
    526: NSNitroNserrExprNoquery,
    527: NSNitroNserrExprNoqual,
    528: NSNitroNserrActionInuse,
    529: NSNitroNserrActionHdrInval,
    530: NSNitroNserrUrlqInval,
    531: NSNitroNserrUndefAction,
    532: NSNitroNserrCpeInuse,
    533: NSNitroNserrCpeReqactInval,
    534: NSNitroNserrCpeRspactInval,
    535: NSNitroNserrCpeReqruleInval,
    536: NSNitroNserrCpeRspruleInval,
    537: NSNitroNserrActionDefinval,
    538: NSNitroNserrActionNotpresent,
    539: NSNitroNserrPxyInvalServicetype,
    540: NSNitroNserrCachepolicyInuse,
    543: NSNitroNserrCachegroupInternal,
    544: NSNitroNserrCpeInval,
    545: NSNitroNserrExprNolen,
    546: NSNitroNserrDnswait,
    547: NSNitroNserrGwTimeout,
    548: NSNitroNserrCswdmnInuse,
    549: NSNitroNserrCswdmnPlcyExist,
    550: NSNitroNserrActionNomodHdr,
    551: NSNitroNserrExprInvalOperator,
    552: NSNitroNserrExprDefRemInval,
    553: NSNitroNserrExprToomany,
    554: NSNitroNserrActionToomany,
    555: NSNitroNserrCswpolicyToomany,
    556: NSNitroNserrCrdpolicyToomany,
    557: NSNitroNserrMappolicyToomany,
    558: NSNitroNserrFiltpolicyToomany,
    559: NSNitroNserrCachepolicyToomany,
    560: NSNitroNserrCachegroupToomany,
    561: NSNitroNserrCacheparamMemallocFailed,
    562: NSNitroNserrCachegroupInuse,
    563: NSNitroNserrCachegroupExpconflict,
    564: NSNitroNserrCacheparamInval,
    565: NSNitroNserrCachegroupParamInval,
    566: NSNitroNserrCachegroupQueryInval,
    567: NSNitroNserrActionInval,
    568: NSNitroNserrExprDefSetInval,
    569: NSNitroNserrCachegroupResszMinGtMax,
    570: NSNitroNserrFiltacionInvalrespcode,
    576: NSNitroNserrCachegroupHostReq,
    577: NSNitroNserrCachegroupHostNreq,
    578: NSNitroNserrCachegroupDyngrpNexp,
    579: NSNitroNserrCachegroupOneGrpReq,
    580: NSNitroNserrCachegroupOneAllReq,
    581: NSNitroNserrCachegroupMatchParamInval,
    582: NSNitroNserrCachegroupDynResCache,
    583: NSNitroNserrExprInvalValue,
    584: NSNitroNserrCachegroupPrefetchConflict,
    585: NSNitroNserrCachegroupPrefetchEnable,
    586: NSNitroNserrCachegroupCchUnknown,
    587: NSNitroNserrCachegroupRelexpX10ms,
    588: NSNitroNserrCachegroupPrefetchX10ms,
    589: NSNitroNserrCachegroupStaticToDynamic,
    591: NSNitroNserrPlcyDefRemInval,
    592: NSNitroNserrCachegroupPrefetchRelNreq,
    593: NSNitroNserrExprSetInvalFlowtype,
    594: NSNitroNserrExprTooBig,
    595: NSNitroNserrCpeInvalidIdrange,
    596: NSNitroNserrExprTooBigExt,
    597: NSNitroNserrCachegroupMatchcookieDynReq,
    598: NSNitroNserrCachegroupMatchcookieNreq,
    599: NSNitroNserrCachefwpxyPresent,
    600: NSNitroNserrCachePrefetchReevalNreq,
    601: NSNitroNserrCachefwpxyToomany,
    602: NSNitroNserrCachePetFcNreq,
    603: NSNitroNserrSaveconfigInProgress,
    604: NSNitroNserrGwsubnetNotExist,
    605: NSNitroNserrGwReqSubnet,
    606: NSNitroNserrUrlpolNoPri,
    607: NSNitroNserrBadCrAttribs,
    608: NSNitroNserrMacNotSupported,
    609: NSNitroNserrPolicyNotSupported,
    610: NSNitroNserrCacheabilityNotSupported,
    611: NSNitroNserrHostRtNotAllowed,
    612: NSNitroNserrRoutingNotAllowed,
    613: NSNitroNserrConfigNotsaved,
    624: NSNitroNserrExprmismatch,
    627: NSNitroNserrNoHost,
    628: NSNitroNserrNoDflt,
    629: NSNitroNserrDfltdmnFirst,
    630: NSNitroNserrPxyConfLoop,
    632: NSNitroNserrPxyMeDup,
    633: NSNitroNserrPxyIvalTgt,
    634: NSNitroNserrConnected,
    635: NSNitroNserrAuthenticate,
    636: NSNitroNserrLargeDomain,
    640: NSNitroNserrPxyIvalUrl,
    641: NSNitroNserrPxyMeUse,
    642: NSNitroNserrPxyMtType,
    643: NSNitroNserrPxyMtUse,
    644: NSNitroNserrPxyMbInval,
    645: NSNitroNserrPxyMbUse,
    646: NSNitroNserrPxySetdcdn,
    647: NSNitroNserrPxySetdflt,
    648: NSNitroNserrPxyDfltNotset,
    649: NSNitroNserrPxyFwdIval,
    656: NSNitroNserrPxyMtxProt,
    657: NSNitroNserrPxyMtxTra,
    658: NSNitroNserrPxyMtxFwd,
    659: NSNitroNserrPxyMtxRev,
    660: NSNitroNserrPxyAddTraNonhttp,
    661: NSNitroNserrPxyAddTraOther,
    662: NSNitroNserrPxyOptInval,
    663: NSNitroNserrPxyAddSvrOther,
    664: NSNitroNserrPxyMbDup,
    665: NSNitroNserrPxyDfltDup,
    672: NSNitroNserrSelInuse,
    673: NSNitroNserrSelParseFailed,
    674: NSNitroNserrNoselector,
    675: NSNitroNserrSelToomany,
    677: NSNitroNserrCachegroupNoselparam,
    678: NSNitroNserrNocachegroup,
    679: NSNitroNserrNonreqSel,
    680: NSNitroNserrInvalarg,
    681: NSNitroNserrNowildAllowed,
    682: NSNitroNserrDateIncompat,
    683: NSNitroNserrTimedateInvalid,
    684: NSNitroNserrContentgroupCookieReqParam,
    685: NSNitroNserrContentgroupIgnorecaseReqHitparam,
    686: NSNitroNserrContentgroupInvalparamReq,
    687: NSNitroNserrClisecExpTooLong,
    688: NSNitroNserrNonhttpCswBindHttpSslPolicy,
    689: NSNitroNserrNonhttpCswBindDomainPolicy,
    690: NSNitroNserrNonhttpCswBindUrlPolicy,
    691: NSNitroNserrPolboundtoTooManyVsvrs,
    692: NSNitroNserrPiCswUrlDomain,
    693: NSNitroNserrPiToPeCsw,
    694: NSNitroNserrPeToPiCsw,
    695: NSNitroNserrPriorityCompPiCsw,
    696: NSNitroNserrPiTcpcsw,
    697: NSNitroNserrPeGoto,
    698: NSNitroNserrPiToPePolCsw,
    699: NSNitroNserrCacheobjectEvict,
    700: NSNitroNserrDnsfail,
    701: NSNitroNserrHcRetTypeChange,
    702: NSNitroNserrHcNotHttpVs,
    703: NSNitroNserrHcReqConfigXor,
    704: NSNitroNserrHcServiceConfigXor,
    705: NSNitroNserrHcRetTypeReqd,
    706: NSNitroNserrRtspCswBindIpPolicy,
    707: NSNitroNserrCswBindIncompatTgt,
    708: NSNitroNserrAsBadXmlnamespacePrefix,
    709: NSNitroNserrInvalidSipExpr,
    710: NSNitroNserrNoBackendvserver,
    711: NSNitroNserrContentGroupToomany,
    712: NSNitroNserrCacheMemSizeChanged,
    713: NSNitroNserrCacheMemSizeZero,
    714: NSNitroNserrL2connNotAllowed,
    715: NSNitroNserrSqlNotAllowed,
    716: NSNitroNserrIpsecNotAllowed,
    717: NSNitroNserrCswBindIncompatBkup,
    769: NSNitroNserrRnatInv,
    770: NSNitroNserrInvalidIf,
    771: NSNitroNserrMgrlimitReached,
    772: NSNitroNserrSpInvaldTable,
    773: NSNitroNserrRnatNatipExists,
    774: NSNitroNserrRnatExists,
    775: NSNitroNserrRnatNotExists,
    776: NSNitroNserrRnatNatipNotExists,
    777: NSNitroNserrRnatInvalidNatip,
    784: NSNitroNserrArpDisabled,
    785: NSNitroNserrArpSecNotOwnedip,
    786: NSNitroNserrCpeRuleInval,
    787: NSNitroNserrInvalFlowtype,
    788: NSNitroNserrInvalPolicyType,
    789: NSNitroNserrCpeRuleActionInval,
    790: NSNitroNserrCpeDefSetInval,
    791: NSNitroNserrInvalForcecleanup,
    792: NSNitroNserrInvalAaaGroup,
    793: NSNitroNserrInvalProxy,
    800: NSNitroNserrInvalHtttpproxy,
    801: NSNitroNserrInvalFtpproxy,
    802: NSNitroNserrInvalSockproxy,
    803: NSNitroNserrInvalGopherproxy,
    804: NSNitroNserrInvalSslproxy,
    805: NSNitroNserrInvalAaagrpMax,
    806: NSNitroNserrInvalMaxPortNum,
    807: NSNitroNserrInvalHttpport,
    808: NSNitroNserrInvalVpnvsererPoltype,
    809: NSNitroNserrInvalVpnglobalPoltype,
    810: NSNitroNserrCpeRemInuse,
    811: NSNitroNserrProxyConflict,
    812: NSNitroNserrProxyInval,
    813: NSNitroNserrPxyexcptInval,
    814: NSNitroNserrCpePoltypeNoCse,
    815: NSNitroNserrSessactCseIncompatible,
    816: NSNitroNserrNomemCse,
    817: NSNitroNserrIncompatFsRule,
    818: NSNitroNserrIncompatFsMix,
    819: NSNitroNserrDrEnable,
    820: NSNitroNserrMaxDistance,
    821: NSNitroNserrNullRouteDistance,
    822: NSNitroNserrBadActionTcpProfileType,
    823: NSNitroNserrBadActionHttpProfileType,
    824: NSNitroNserrSpInvalidThreshold,
    825: NSNitroNserrVipRouteExists,
    864: NSNitroNserrAclNotExists,
    865: NSNitroNserrAclExists,
    866: NSNitroNserrAclpipWosrcdst,
    867: NSNitroNserrAclSameipPip,
    868: NSNitroNserrAclInvalPeerip,
    869: NSNitroNserrAclIppipExists,
    870: NSNitroNserrXacldelerror,
    871: NSNitroNserrXacladderror,
    872: NSNitroNserrXaclPriorityExists,
    873: NSNitroNserrXaclIcmpReqd,
    874: NSNitroNserrNoloopback,
    875: NSNitroNserrInvicmptype,
    876: NSNitroNserrInvicmpcode,
    877: NSNitroNserrXaclrnatdel,
    880: NSNitroNserrXaclmodcfginfo,
    896: NSNitroNserrAcl6IppipExists,
    897: NSNitroNserrAcl6Delerror,
    898: NSNitroNserrAcl6Adderror,
    899: NSNitroNserrAcl6PriorityExists,
    900: NSNitroNserrAcl6IcmpReqd,
    901: NSNitroNserrAcl6Unspecaddr,
    902: NSNitroNserrAcl6Modcfginfo,
    903: NSNitroNserrAcl6Prefixlen,
    912: NSNitroNserrPbrNexthopNotdirect,
    913: NSNitroNserrPbrNoloopback,
    914: NSNitroNserrPbrdelerror,
    915: NSNitroNserrPbrIppipExists,
    916: NSNitroNserrPbrPriorityExists,
    918: NSNitroNserrPbrmodcfginfo,
    919: NSNitroNserrPbrNexthopReqd,
    920: NSNitroNserrPbrL2ConfigInfo,
    921: NSNitroNserrPbrmodcfgL2Info,
    922: NSNitroNserrPbrNoMonitorGateway,
    923: NSNitroNserrPbrInvalidIporgateway,
    924: NSNitroNserrPbrMaxRuleExceeded,
    1024: NSNitroNserrTcpconnfail,
    1025: NSNitroNserrLoginfail,
    1026: NSNitroNserrNologin,
    1027: NSNitroNserrAuthtimeout,
    1028: NSNitroNserrNotPrimary,
    1029: NSNitroNserrRemoteop,
    1030: NSNitroNserrConnlost,
    1031: NSNitroNserrRpcdatamismatch,
    1032: NSNitroNserrRpcbadreply,
    1033: NSNitroNserrUnabletoprompt,
    1040: NSNitroNserrUserabort,
    1041: NSNitroNserrEof,
    1042: NSNitroNserrInterrupt,
    1043: NSNitroNserrInternal,
    1048: NSNitroNserrStrmaxlen255,
    1049: NSNitroNserrStrmaxlen32,
    1056: NSNitroNserrNoresponse,
    1057: NSNitroNserrIoerror,
    1058: NSNitroNserrEnv,
    1059: NSNitroNserrCmdsfailed,
    1060: NSNitroNserrAllcmdsfailed,
    1061: NSNitroNserrInvalidTcpOptionType,
    1066: NSNitroNserrLicexpired,
    1067: NSNitroNserrFeatdisabled,
    1072: NSNitroNserrMaxlimit,
    1073: NSNitroNserrSetNosupport,
    1074: NSNitroNserrInvalidvalue,
    1075: NSNitroNserrInvalidname,
    1088: NSNitroNserrNosuchcmd,
    1089: NSNitroNserrCmdambiguous,
    1090: NSNitroNserrNosucharg,
    1091: NSNitroNserrArgvalmissing,
    1092: NSNitroNserrArgsmutex,
    1093: NSNitroNserrArgprereq,
    1094: NSNitroNserrArgstoofew,
    1095: NSNitroNserrArgmissing,
    1096: NSNitroNserrArgorder,
    1097: NSNitroNserrArgvalbad,
    1098: NSNitroNserrArgvalseq,
    1099: NSNitroNserrArgambiguous,
    1100: NSNitroNserrSyncgslbconfig,
    1101: NSNitroNserrSyncgslbconfigWarn,
    1104: NSNitroNserrArgvalsneq,
    1105: NSNitroNserrArgvalambiguous,
    1106: NSNitroNserrStrmaxlen,
    1107: NSNitroNserrStrminlen,
    1108: NSNitroNserrIntmaxval,
    1109: NSNitroNserrIntminval,
    1110: NSNitroNserrInvalidip,
    1111: NSNitroNserrInvalidnetmask,
    1112: NSNitroNserrToomanyvals,
    1113: NSNitroNserrBadrange,
    1114: NSNitroNserrExprquotes,
    1115: NSNitroNserrBadquotes,
    1116: NSNitroNserrInvalidrange,
    1117: NSNitroNserrMismatchranges,
    1118: NSNitroNserrMultiranges,
    1119: NSNitroNserrNomatchchar,
    1120: NSNitroNserrNeedreboot,
    1121: NSNitroNsqSaveconfig,
    1122: NSNitroNserrNotsaved,
    1123: NSNitroNserrCmdexec,
    1124: NSNitroNsqReboot,
    1125: NSNitroNserrNoreboot,
    1126: NSNitroNserrPgmfailed,
    1127: NSNitroNserrCtxmode,
    1128: NSNitroNserrCmdincomplete,
    1129: NSNitroNserrCmdoutofctx,
    1130: NSNitroNserrConfigsaved,
    1131: NSNitroNserrConfigcleared,
    1132: NSNitroNserrRebooting,
    1133: NSNitroNserrNoconfigsave,
    1135: NSNitroNserrRegexnoanchor,
    1136: NSNitroNserrRegexnomatch,
    1137: NSNitroNserrRegexinvalid,
    1138: NSNitroNserrRegexnotallowed,
    1139: NSNitroNserrRegexnocmd,
    1140: NSNitroNserrInvalidipv6Format,
    1141: NSNitroNserrInvalidipv6TwoDoubecolon,
    1142: NSNitroNserrInvalidipv6NoprefixLength,
    1143: NSNitroNserrInvalidipv6PrefixValue,
    1144: NSNitroNserrTermnameinvalid,
    1145: NSNitroNserrTerminvalid,
    1146: NSNitroNserrForcefailover,
    1147: NSNitroNserrForcefailHealthWarn,
    1148: NSNitroNserrHellotimeMultiple,
    1149: NSNitroNserrForcesyncsave,
    1150: NSNitroNserrErroutfilename,
    1151: NSNitroNserrRnatipdel,
    1152: NSNitroNserrInvalidalias,
    1153: NSNitroNserrNosuchalias,
    1154: NSNitroNserrAliasexists,
    1155: NSNitroNserrNosuchfile,
    1156: NSNitroNserrNotregfile,
    1157: NSNitroNserrDeprcmd,
    1158: NSNitroNserrDeprarg,
    1159: NSNitroNserrNotlogfile,
    1160: NSNitroNserrNoplenforipv6range,
    1161: NSNitroNserrInvalidint,
    1162: NSNitroNserrCmdambiguousUsecompletionsoptions,
    1163: NSNitroNserrMetadataInvalEntitytype,
    1164: NSNitroNserrSetnotexist,
    1165: NSNitroNserrSetargnotexist,
    1166: NSNitroNserrInvalidDs,
    1167: NSNitroNserrNosuchcounter,
    1168: NSNitroNserrInvalidipmask,
    1169: NSNitroNserrInvalidippat,
    1170: NSNitroNserrBadrc,
    1171: NSNitroNserrInvalidrangetype,
    1172: NSNitroNserrInvalidrangeval,
    1173: NSNitroNserrInvalidipv6PrefixLength,
    1174: NSNitroNserrEntitydeleteFail,
    1181: NSNitroNserrIncompatibleip,
    1182: NSNitroNserrTranscrIp,
    1183: NSNitroNserrPasswordMismatch,
    1184: NSNitroNserrNosuchioctl,
    1185: NSNitroNserrNotargets,
    1186: NSNitroNserrCantrecover,
    1187: NSNitroNserrIgnoredioctl,
    1188: NSNitroNserrRemoteclose,
    1189: NSNitroNserrInvalidTarget,
    1190: NSNitroNserrFileError,
    1191: NSNitroNserrCommentDropped,
    1192: NSNitroNserrAggreqTimeout,
    1193: NSNitroNserrAggread,
    1194: NSNitroNserrRpcCmdDup,
    1195: NSNitroNserrRpcCmdNondup,
    1196: NSNitroNserrCfePeComm,
    1197: NSNitroNserrAggConfail,
    1198: NSNitroNserrCfePeTimout,
    1199: NSNitroNserrAggInvalidresponse,
    1200: NSNitroNserrNontpsvr,
    1201: NSNitroNserrAggSendfail,
    1202: NSNitroNserrCfeAslearnComm,
    1232: NSNitroNserrNitroInvalidObjectname,
    1233: NSNitroNserrNitroInvalidJsonInput,
    1234: NSNitroNserrNitroInvalidJsonDatatype,
    1235: NSNitroNserrNitroInvalidXmlInput,
    1236: NSNitroNserrNitroInvalidDatatype,
    1237: NSNitroNserrNitroInvalidMethod,
    1238: NSNitroNserrNitroParseError,
    1239: NSNitroNserrNitroCmdexecFailed,
    1240: NSNitroNserrNitroInvalidAction,
    1248: NSNitroNserrNsappTemplateExists,
    1249: NSNitroNserrNsappInvalidTemplate,
    1250: NSNitroNserrNsappDirError,
    1251: NSNitroNserrNsappFileError,
    1252: NSNitroNserrNsappInvalidAppInput,
    1253: NSNitroNserrNsappExceededFilelength,
    1254: NSNitroNserrNsappEndpointInuse,
    1255: NSNitroNserrNsappProtocolMismatch,
    1256: NSNitroNserrNsappInvalidVarname,
    1257: NSNitroNserrNsappZipFile,
    1258: NSNitroNserrNsappMaxepReached,
    1259: NSNitroNserrNsappNotExist,
    1260: NSNitroNserrNsappInvalidServicetype,
    1261: NSNitroNserrNsappTemplateFormatError,
    1262: NSNitroNserrNsappAppWithoutAppunits,
    1263: NSNitroNserrNsappServicrgroupExists,
    1280: NSNitroNserrSlesslbLbmethodNotsupported,
    1281: NSNitroNserrSlesslbPersistNotsupported,
    1282: NSNitroNserrSlesslbTypeNotsupported,
    1283: NSNitroNserrSlesslbModeNotsupported,
    1284: NSNitroNserrSlesslbSvcUsipnotset,
    1286: NSNitroNserrWildcardvipLbmethodInval,
    1287: NSNitroNserrWildcardvipPersistInval,
    1288: NSNitroNserrLbSoThreshold,
    1289: NSNitroNserrConnfailoverUsip,
    1290: NSNitroNserrConnfailoverService,
    1291: NSNitroNserrLbSoDynamicconThreshold,
    1292: NSNitroNserrLbSoAddrvip,
    1293: NSNitroNserrConnfailoverNotforSless,
    1296: NSNitroNserrSipNocallid,
    1297: NSNitroNserrSipNovia,
    1298: NSNitroNserrSipNocseq,
    1299: NSNitroNserrSipNoto,
    1300: NSNitroNserrSipNofrom,
    1301: NSNitroNserrSipNomaxForwards,
    1302: NSNitroNserrSipServiceUnavailable,
    1303: NSNitroNserrSvcNotBound,
    1304: NSNitroNserrSvctypeMismatch,
    1305: NSNitroNserrChConNotAllowed,
    1312: NSNitroNserrChIncompleteHdr,
    1313: NSNitroNserrSpilloverdisabled,
    1314: NSNitroNserrMaxtimeexceeded,
    1315: NSNitroNserrScinvalproto,
    1316: NSNitroNserrRootrec,
    1317: NSNitroNserrRootGluerec,
    1356: NSNitroNserrVipinsertNotSupported,
    1318: NSNitroNserrVsvrAlrdyBound,
    1319: NSNitroNserrInvalidWlmBinding,
    1320: NSNitroNserrVsvrNotBound,
    1321: NSNitroNserrWlmExists,
    1322: NSNitroNserrInvalidTimeout,
    1323: NSNitroNserrConnfailoverIncmode,
    1324: NSNitroNserrConnfailoverTcpb,
    1326: NSNitroNserrConnfailoverTcpbSvcBind,
    1327: NSNitroNserrConnfailoverTcpbSvcParam,
    1328: NSNitroNserrConnfailoverServiceStatefull,
    1329: NSNitroNserrConnfailoverSslSvcBind,
    1330: NSNitroNserrConnfailoverHaIncNode,
    1331: NSNitroNserrConnfailoverSslSvc,
    1332: NSNitroNserrInvalidPersistence,
    1333: NSNitroNserrRtspsessionInvalid,
    1334: NSNitroNserrLbMethodSameasBackupMethod,
    1335: NSNitroNserrServerExist,
    1336: NSNitroNserrLbSoHealth,
    1337: NSNitroNserrReqRuleMissing,
    1338: NSNitroNserrConnfailoverBindlo,
    1339: NSNitroNserrConnfailoverSetwithlo,
    1340: NSNitroNserrRedirectUrlNotApplicable,
    1341: NSNitroNserrStatefulConnfailoverIpv6,
    1342: NSNitroNserrConnfailoverNotSupported,
    1343: NSNitroNserrNobindOnpush,
    1344: NSNitroNserrPushVsvr,
    1345: NSNitroNserrOnlyHttpssl,
    1346: NSNitroNserrPushBindExists,
    1347: NSNitroNserrSetPushvsOnly,
    1348: NSNitroNserrSlessNoSupport,
    1349: NSNitroNserrConnfailoverV6service,
    1350: NSNitroNserrConnfailoverVserver,
    1352: NSNitroNserrNoListenPolicyForDummyvs,
    1355: NSNitroNserrNormalVsNoneListenpol,
    1357: NSNitroNserrNoLispriForNoneLispol,
    1358: NSNitroNserrInvalidPolicyString,
    1359: NSNitroNserrNodatalenoffforvs,
    1285: NSNitroNserrLbgrppersiswithrdp,
    1360: NSNitroNserrPqBindvip,
    1361: NSNitroNserrPqInvalprio,
    1362: NSNitroNserrPq2bigrule,
    1363: NSNitroNserrPqInvalwt,
    1364: NSNitroNserrPqPolexist,
    1365: NSNitroNserrPqNopol,
    1366: NSNitroNserrPq2manyref,
    1367: NSNitroNserrPqNolbvip,
    1368: NSNitroNserrPqPhsconfig,
    1369: NSNitroNserrPqNobind,
    1536: NSNitroNserrSslCert,
    1537: NSNitroNserrSslPkey,
    1538: NSNitroNserrSslNomatch,
    1539: NSNitroNserrSslCerttype,
    1540: NSNitroNserrSslNocert,
    1541: NSNitroNserrSslRefext,
    1542: NSNitroNserrSslBind,
    1543: NSNitroNserrSslLink,
    1544: NSNitroNserrSslNeedSslproto,
    1545: NSNitroNserrSslNolink,
    1546: NSNitroNserrSslBindor,
    1547: NSNitroNserrSslNosvrcert,
    1548: NSNitroNserrSslIssubmis,
    1549: NSNitroNserrSslCrl,
    1550: NSNitroNserrSslNocrl,
    1551: NSNitroNserrSslDhcount,
    1552: NSNitroNserrSslSessto,
    1553: NSNitroNserrSslErsacount,
    1554: NSNitroNserrSslDhSize,
    1555: NSNitroNserrDhpath,
    1556: NSNitroNserrCertheader,
    1557: NSNitroNserrSessheader,
    1558: NSNitroNserrCipherPerm,
    1559: NSNitroNserrSslErsadisabled,
    1560: NSNitroNserrSslDhdisabled,
    1561: NSNitroNserrSslSessdisabled,
    1562: NSNitroNserrSslPkeySize,
    1563: NSNitroNserrSslNotApplicable,
    1567: NSNitroNserrSslInternalerr,
    1568: NSNitroNserrSslNocacert,
    1569: NSNitroNserrSslRefreshdis,
    1570: NSNitroNserrSslSvrportneeded,
    1571: NSNitroNserrSslBaseobjneeded,
    1572: NSNitroNserrSslCipherRedirect,
    1573: NSNitroNserrSslNodsa,
    1574: NSNitroNserrSslFipsrefext,
    1575: NSNitroNserrSslNofipskey,
    1576: NSNitroNserrNofipscard,
    1577: NSNitroNserrFipscardnotconf,
    1578: NSNitroNserrSslSslv2Redirect,
    1579: NSNitroNserrSslModsize64,
    1580: NSNitroNserrSslNonfipskey,
    1581: NSNitroNserrNfipsFipsUpd,
    1582: NSNitroNserrFipsNfipsUpd,
    1583: NSNitroNserrSslIssuerNotinGlbcertlist,
    1584: NSNitroNserrSslCrlsigcheckFail,
    1585: NSNitroNserrSslPortrewrite,
    1586: NSNitroNserrSslSslv2RenegClientCert,
    1587: NSNitroNserrSslBrklink,
    1588: NSNitroNserrSslCertNotYetValid,
    1589: NSNitroNserrSslCertExpired,
    1590: NSNitroNserrSslExpiredBrklink,
    1591: NSNitroNserrSslNyvalidBrklink,
    1592: NSNitroNserrSslOcspRespcert,
    1593: NSNitroNserrSslOcspSigncert,
    1600: NSNitroNserrSslOcspAia,
    3584: NSNitroNserrSslFipscardlocked,
    3585: NSNitroNserrSslDomincompat,
    3586: NSNitroNserrSslNomthdchange,
    3587: NSNitroNserrSslUrlsrvrneeded,
    3588: NSNitroNserrSslInvalidUrl,
    3589: NSNitroNserrSslMixparams,
    3590: NSNitroNserrSslPkeyMinsize,
    3591: NSNitroNserrSslSyncinprogress,
    3592: NSNitroNserrSslSyncfailed,
    3593: NSNitroNserrSslCiphgrpRefcnt,
    3594: NSNitroNserrSslCvmNodsa,
    3595: NSNitroNserrCerthashheader,
    3596: NSNitroNserrSslCrlinrefresh,
    3597: NSNitroNserrSslCrlmemExceeds,
    3598: NSNitroNserrSslCrlindeletion,
    3599: NSNitroNserrSslIndeleteNorefresh,
    3600: NSNitroNserrSslInrefreshNodelete,
    3601: NSNitroNserrNomix,
    3602: NSNitroNserrNopolicyNontrsvc,
    3603: NSNitroNserrSslSslpolBindConst,
    3604: NSNitroNserrSslNoUsableCiphers,
    3605: NSNitroNserrSslCertNotCa,
    3606: NSNitroNserrSslCacertNoCrlsign,
    3607: NSNitroNserrSslCrlExpired,
    3608: NSNitroNserrSslCrlNotyetValid,
    3609: NSNitroNserrSslParsingDeltaCrlExtn,
    3610: NSNitroNserrSslDeltaCrlMissingBaseCrl,
    3611: NSNitroNserrNofipscipher,
    3612: NSNitroNserrNofipsciphergrp,
    3613: NSNitroNserrNonfipsciphertogrp,
    3614: NSNitroNserrNonfipsaliastogrp,
    3615: NSNitroNserrNonfipsgrouptogrp,
    3616: NSNitroNserrSslImportFipskeyNameMismatch,
    3617: NSNitroNserrSslPkeySizeCa,
    3618: NSNitroNserrSslCrlPortMismatch,
    3619: NSNitroNserrSslPkeySizeVpx,
    3620: NSNitroNserrSslDhSizeVpx,
    3621: NSNitroNserrNoentCipher,
    3622: NSNitroNserrFipsfwwrongmajor,
    3623: NSNitroNserrFipsfwwrongminor,
    3624: NSNitroNserrFipsfwupdated,
    3625: NSNitroNserrSslPendingCmds,
    3626: NSNitroNserrFipsfwupdatedoreboot,
    3627: NSNitroNserrSslSniNotenable,
    3628: NSNitroNserrSslNoCn,
    3629: NSNitroNserrSslDupSnicert,
    3630: NSNitroNserrSslSniNotvalidServ,
    3632: NSNitroNserrOcspReferences,
    3633: NSNitroNserrOcspSignerNokey,
    3634: NSNitroNserrSslNotSupported,
    3635: NSNitroNserrOcspTooManyResponders,
    3636: NSNitroNserrOcspNoDnsServerConfigured,
    3637: NSNitroNserrSslDupSnicertBrklink,
    3638: NSNitroNserrSslNoCnBrllink,
    3639: NSNitroNserrNgfipsresetreboot,
    3640: NSNitroNserrNgfipsinitreboot,
    3641: NSNitroNserrFipscmdtimeout,
    3642: NSNitroNserrSslSimtimeout,
    3643: NSNitroNserrSslNgfipsQfull,
    3644: NSNitroNserrSslNomemVsvrsrvlistnode,
    3645: NSNitroNserrSslCertkeySize64,
    3646: NSNitroNserrSniAtk,
    3647: NSNitroNserrSniNohosthdr,
    3648: NSNitroNserrCrlShmemAllocFail,
    3655: NSNitroNserrSslCertMissingParam,
    3656: NSNitroNserrSslNomemCertkeyOcsprespListnode,
    3657: NSNitroNserrSslBundleIcFileExists,
    3658: NSNitroNserrSslBundleScertMissing,
    3659: NSNitroNserrSslBundleCertMissing,
    3660: NSNitroNserrSslBundleFailed,
    3661: NSNitroNserrSslBundleParseErr,
    3662: NSNitroNserrSslBundleMaxCert,
    3663: NSNitroNserrSslBundleMaxKey,
    3664: NSNitroNserrSslBundleIcFileCreateFailed,
    3668: NSNitroNserrSslIssuerMismatch,
    1601: NSNitroNserrSslConffile,
    1602: NSNitroNserrSslNoconffile,
    1603: NSNitroNserrSslSigfail,
    1604: NSNitroNserrSslInvalformat,
    1605: NSNitroNserrSslOutfile,
    1606: NSNitroNserrSslVerifyFail,
    1607: NSNitroNserrSslFilecreate,
    1608: NSNitroNserrSslMinkeysize,
    1609: NSNitroNserrSslInvalidReq,
    1610: NSNitroNserrSslGentool,
    1611: NSNitroNserrSslPemOnly,
    1612: NSNitroNserrSslPassmismatch,
    1613: NSNitroNserrSslPassreq,
    1614: NSNitroNserrSslInvalpass,
    1615: NSNitroNserrSslMaxkeysize,
    1616: NSNitroNserrSslGntoolargMissing,
    1617: NSNitroNserrSslInvalPubexp,
    1618: NSNitroNserrSslInvalidValue,
    1619: NSNitroNserrSslMissingKval,
    1620: NSNitroNserrSslInvalDhgen,
    1621: NSNitroNserrSslNofileCertreq,
    1622: NSNitroNserrSslReqNomatch,
    1623: NSNitroNserrSslPkcs12,
    1624: NSNitroNserrSslNofileCapvtkey,
    1625: NSNitroNserrSslNofileCacert,
    1626: NSNitroNserrSslNofileSerial,
    1627: NSNitroNserrSslNofilePkcs12,
    1628: NSNitroNserrSslReadCacert,
    1629: NSNitroNserrReadCert,
    1630: NSNitroNserrImpExpNotTogether,
    1631: NSNitroNserrNofileCert,
    1632: NSNitroNserrNofileKey,
    1633: NSNitroNserrCacertpkeyMismatch,
    1634: NSNitroNserrWrongRevEntry,
    1635: NSNitroNserrWrongRevDate,
    1636: NSNitroNserrWrongSerialNo,
    1637: NSNitroNserrCreateDatabaseEntry,
    1638: NSNitroNserrAlreadyRevkd,
    1639: NSNitroNserrLoadPkey,
    1640: NSNitroNserrCertpkeyNeeded,
    1641: NSNitroNserrPkcs12Needed,
    1642: NSNitroNserrErrFileexists,
    1643: NSNitroNserrFipskeyKeyfileOption,
    1644: NSNitroNserrOutfilelenbig,
    1645: NSNitroNserrSslDefpath,
    1646: NSNitroNserrSslCrlDefpath,
    1647: NSNitroNserrSslDeflocation,
    1791: NSNitroNserrDhreqd,
    1650: NSNitroNserrSslCrlDeflocation,
    1651: NSNitroNserrSslNofipsKey,
    1652: NSNitroNserrSslImproperSerialfile,
    1653: NSNitroNserrSslSerialNumRevoked,
    1654: NSNitroNserrSslMaxrsakeysize,
    1655: NSNitroNserrSslMustbepem,
    1656: NSNitroNserrSslCantbepem,
    1657: NSNitroNserrSslBadLabel,
    1792: NSNitroNserrBadDnsOption,
    1793: NSNitroNserrDnsBadCachetype,
    1794: NSNitroNserrDnsNotavail,
    1795: NSNitroNserrDnsBadVstype,
    1796: NSNitroNserrGslbSitelkupFailed,
    1801: NSNitroNserrNoarec,
    1806: NSNitroNserrInvalttl,
    1807: NSNitroNserrCnameexists,
    1808: NSNitroNserrInvalSvcoption,
    1809: NSNitroNserrGslbbindExists,
    1810: NSNitroNserrNotLocalremote,
    1811: NSNitroNserrCountMismatch,
    1812: NSNitroNserrIpMismatch,
    1813: NSNitroNserrSvcipRepeat,
    1814: NSNitroNserrNotRemote,
    1815: NSNitroNserrNotLocal,
    1816: NSNitroNserrProxyRec,
    1817: NSNitroNserrNoproxyArec,
    1819: NSNitroNserrSvcGslbbindExists,
    1820: NSNitroNserrSvctypemismatch,
    1822: NSNitroNserrInvalidPubipOption,
    1823: NSNitroNserrInvalNameSyntax,
    1824: NSNitroNserrGslbBackup,
    1825: NSNitroNserrIsBackup,
    1826: NSNitroNserrGslbHasBackup,
    1827: NSNitroNserrGslbRequiresIndependentBackup,
    1828: NSNitroNserrGslbNoqualifier,
    1829: NSNitroNserrGslbNoname,
    1830: NSNitroNserrGslbCustomNospace,
    1836: NSNitroNserrGslbStaticNospace,
    1831: NSNitroNserrGslbsitenameExists,
    1832: NSNitroNserrGslbsiteipExists,
    1833: NSNitroNserrNoGslbsite,
    1834: NSNitroNserrLocalExists,
    1835: NSNitroNserrNoGslbsvc,
    1837: NSNitroNserrNoGslbvip,
    1839: NSNitroNserrNoDmn,
    1840: NSNitroNserrDmnNotbound,
    1842: NSNitroNserrGslbdomainBound,
    1844: NSNitroNserrNotGslbent,
    1845: NSNitroNserrGslbdomainPerm,
    1846: NSNitroNserrGslbMaxqual,
    1847: NSNitroNserrGslbMaxloclength,
    1848: NSNitroNserrGslbvipPerm,
    1849: NSNitroNserrGslbsvcPerm,
    1850: NSNitroNserrGslbMaxsites,
    1851: NSNitroNserrGslbQualtoolong,
    1852: NSNitroNserrGslbPersistidexists,
    1854: NSNitroNserrGslbInvldLdnstoIntvl,
    1856: NSNitroNserrVipBackupIsgslb,
    1857: NSNitroNserrGslbPubipPubportExists,
    1858: NSNitroNserrGslblocalsvcEnadisNotallowed,
    1859: NSNitroNserrGslblocalsvrEnadisNotallowed,
    1860: NSNitroNserrInvalidPersistid,
    1861: NSNitroNserrPermPersistid,
    1862: NSNitroNserrInvalidLocalsiteip,
    1863: NSNitroNserrInvalidRemotesiteip,
    1864: NSNitroNserrInvalidSitetype,
    1865: NSNitroNserrInvalidBackupip,
    1866: NSNitroNserrGslbvipMaxsvc,
    1867: NSNitroNserrInvalidJitter,
    1868: NSNitroNserrGslblocsvcDisNotallowd,
    1869: NSNitroNserrDummybkupNotallowd,
    1870: NSNitroNserrGslbsvcBindNotallowd,
    1871: NSNitroNserrNsmapVersion,
    1872: NSNitroNserrNsmapFormat,
    1873: NSNitroNserrNsmapEof,
    1874: NSNitroNserrNsmapParse,
    1875: NSNitroNserrNsmapRead,
    1876: NSNitroNserrNsmapWrite,
    1877: NSNitroNserrNsmapIoctl,
    1878: NSNitroNserrNsmapOutputfile,
    1879: NSNitroNserrNsmapInputfile,
    1880: NSNitroNserrNsmapRequiredField,
    1881: NSNitroNserrNsmapDbfile,
    1882: NSNitroNserrNsmapDbinsert,
    1883: NSNitroNserrNsmapDbsearch,
    1884: NSNitroNserrGslbproxmLicenceAbsent,
    1885: NSNitroNserrGslbSitepersistenceHttponly,
    1886: NSNitroNserrGslbNositepfx,
    1888: NSNitroNserrGslbSiteprefixSize,
    1889: NSNitroNserrGslbSitedomainSize,
    1890: NSNitroNserrGslbSitedomainSyntax,
    1891: NSNitroNserrGslbSitedomainRefers,
    1892: NSNitroNserrGslbdomainRefers,
    1893: NSNitroNserrGslbArecordExists,
    1894: NSNitroNserrGslbSitecookieTimeoutRange,
    1895: NSNitroNserrGslbdomainSyntax,
    1896: NSNitroNserrGslbSoPerm,
    1897: NSNitroNserrGslbDeprcookietout,
    1898: NSNitroNserrDnsNamesvrSyntax,
    1899: NSNitroNserrDnsOrigsvrSyntax,
    1900: NSNitroNserrDnsContactSyntax,
    1901: NSNitroNserrDnsMxSyntax,
    1902: NSNitroNserrDnsCnameSyntax,
    1904: NSNitroNserrDnsAliasSyntax,
    1905: NSNitroNserrGslbNolocalvip,
    1906: NSNitroNserrGslbLocalsvcexists,
    1907: NSNitroNserrGslblocalsvcPerm,
    1908: NSNitroNserrDnsInvalRevdomnameSyntax,
    1909: NSNitroNserrDnsAliasrec,
    1910: NSNitroNserrGslblocsvcDelayedcleanNotallowd,
    1911: NSNitroNserrNoBkpVip,
    1912: NSNitroNserrGslbNosuchLdnsentry,
    1913: NSNitroNserrMaxDnsView,
    1914: NSNitroNserrGslbSiteIpExists,
    1915: NSNitroNserrGslbLastMip,
    1916: NSNitroNserrRmGslbSite,
    1917: NSNitroNserrGslbIprmLastMip,
    1918: NSNitroNserrGslbSvcPubPortErr,
    1919: NSNitroNserrRecHasRef,
    1920: NSNitroNserrDnsViewRef,
    1921: NSNitroNserrGslbSitePersistenceMatch,
    1922: NSNitroNserrGslbSitePersistenceConflicts,
    1923: NSNitroNserrDnsPolicyInval,
    1924: NSNitroNserrGslbvipCnameMismatch,
    1925: NSNitroNserrGslbvipCnameUnsupportedLbmethods,
    1926: NSNitroNserrGslbServiceMonNoipport,
    1927: NSNitroNserrGslbServiceMonSetNoipport,
    1928: NSNitroNserrGslbCnameServiceSet,
    1929: NSNitroNserrGslbCnameVserverSet,
    1930: NSNitroNserrGslbvipCnameUnsupportedBkupLbmethods,
    1931: NSNitroNserrGslbvipCnameUnsupportedEdr,
    1932: NSNitroNserrGslbvipCnameUnsupportedMir,
    1933: NSNitroNserrGslbsvcViewNexist,
    1934: NSNitroNserrDnsTtlMoreThanMaxAllowed,
    1935: NSNitroNserrGslbLbMaxsites,
    1936: NSNitroNserrGslbHaschildren,
    1937: NSNitroNserrGslbParentischild,
    1938: NSNitroNserrMaxRltSelectors,
    1939: NSNitroNserrMaxRltIdentifers,
    1940: NSNitroNserrNoSuchSelector,
    1941: NSNitroNserrNoSuchIdentifier,
    1942: NSNitroNserrRltTimesliceInvalidVal,
    1943: NSNitroNserrIllegalSubnetMask,
    1944: NSNitroNserrRltSelectorInuse,
    1945: NSNitroNserrRltIdentifierInuse,
    1946: NSNitroNserrRltSelectorCannotChangeAttribType,
    1947: NSNitroNserrGslbIgnTrigmon,
    1948: NSNitroNserrRltSelectorNotMoreThan2Ipv6Exp,
    1949: NSNitroNserrRepeatedMonitors,
    1950: NSNitroNserrAllMonitorsDisabled,
    1951: NSNitroNserrGslbAaaarecordExists,
    1952: NSNitroNserrGslbvipHeterogeneousServiceIpversion,
    1953: NSNitroNserrViewipIpv6,
    1954: NSNitroNserrBackupipIpv6,
    1955: NSNitroNserrBackupVipMismatch,
    1956: NSNitroNserrGslbDomainConversion,
    1957: NSNitroNserrGslbIpv4Backupip,
    1958: NSNitroNserrRltCannotAddSelector,
    1959: NSNitroNserrRltSelConflictingAttributes,
    1960: NSNitroNserrGslbvipCnameBackupip,
    1961: NSNitroNserrGslbHeterogeneousSiteip,
    1962: NSNitroNserrGslbUnused1,
    1963: NSNitroNserrGslbUnused2,
    1964: NSNitroNserrAaaaRecordExists,
    1965: NSNitroNserrGslbRectypeService,
    1966: NSNitroNserrGslbRectypeDomain,
    1967: NSNitroNserrGslbRectypeBackupVip,
    1968: NSNitroNserrGslbBkpvipRectype,
    1969: NSNitroNserrGslbUnused3,
    1970: NSNitroNserrBackupipIpv4,
    1971: NSNitroNserrGslbIpv6Backupip,
    1972: NSNitroNserrGslbDbReqTooBig,
    1973: NSNitroNserrGslbDbQueueMaxed,
    1974: NSNitroNserrGslbDbServer,
    1975: NSNitroNserrGslbDbTimeout,
    1976: NSNitroNserrGslbDbClosed,
    1977: NSNitroNserrGslbCoordinates,
    1978: NSNitroNserrInvalidIpv6Prefixlen,
    1979: NSNitroNserrGslbdomainCanmeRecordExists,
    1980: NSNitroNserrGslbdomainAaaaCnameExists,
    1981: NSNitroNserrGslbNonParentRemotesite,
    1982: NSNitroNserrZoneExists,
    1983: NSNitroNserrInvalKeyflags,
    1984: NSNitroNserrDnskeyNonexists,
    1985: NSNitroNserrNorecsInZone,
    1986: NSNitroNserrSignfailed,
    1987: NSNitroNserrDigestinitFailed,
    1988: NSNitroNserrDigestupdateFailed,
    1989: NSNitroNserrKeyexists,
    1990: NSNitroNserrNopasvkeys,
    1991: NSNitroNserrDnsMaxkeysize,
    1992: NSNitroNserrNodataToSign,
    1993: NSNitroNserrCnameSiteNotexists,
    1994: NSNitroNserrDnsNosoaNons,
    1995: NSNitroNserrDnsProxyZone,
    1996: NSNitroNserrNoactvkeys,
    1997: NSNitroNserrNotifyperiod,
    1998: NSNitroNserrLoadPubkey,
    1999: NSNitroNserrDnskeygenUnsupportedAlgo,
    2000: NSNitroNserrDnskeygenErrPubfileOpen,
    2001: NSNitroNserrDnskeygenErrPrivfileOpen,
    2002: NSNitroNserrDnskeygenErrDsfileOpen,
    2003: NSNitroNserrGslbOptNotsupported,
    2004: NSNitroNserrGslbGfsNotSupported,
    2005: NSNitroNserrNsmapImportfile,
    2006: NSNitroNserrDnsCnameloop,
    2049: NSNitroNscfgInfo,
    2050: NSNitroNscsInfo,
    2051: NSNitroNscsprobeInfo,
    2052: NSNitroNsappprobeInfo,
    2112: NSNitroNscfgMpInfo,
    2113: NSNitroNserrNointranetip,
    2114: NSNitroNserrAlreadylogedin,
    2115: NSNitroNserrUrlinuse,
    2116: NSNitroNserrVpnappinuse,
    2117: NSNitroNserrNotsuppTransIntercpt,
    2118: NSNitroNserrNotsuppProtUdp,
    2119: NSNitroNserrDefaultcmdplcy,
    2120: NSNitroNserrClntCertReqd,
    2121: NSNitroNserrInvalCertfield,
    2064: NSNitroNserrVpnappProxyIprange,
    2065: NSNitroNserrVpnappProxyNetmask,
    2066: NSNitroNserrVpnappProxyDstportRange,
    2067: NSNitroNserrVpnappProxyProtocol,
    2068: NSNitroNserrVpnappProxyHostname,
    2069: NSNitroNserrVpnappTransSrcip,
    2070: NSNitroNserrVpnappTransSrcport,
    2071: NSNitroNserrVpnappNoInterceptionType,
    2072: NSNitroNserrVpnappCliappPort,
    2073: NSNitroNserrVpnappCliappProto,
    2074: NSNitroNserrVpnappProxyCliapp,
    2075: NSNitroNserrVpnappMissingProto,
    2076: NSNitroNserrVpnappMissingArg,
    2077: NSNitroNserrVpnappTooManyArg,
    2078: NSNitroNserrFsAuthfail,
    2079: NSNitroNserrNsipv6notpresent,
    2096: NSNitroNserrRemoveSession,
    3250: NSNitroNserrStawiExist,
    2099: NSNitroNserrInvalidSsoAction,
    2100: NSNitroNserrInvalidTmtrafficAction,
    2101: NSNitroNserrInvalfsso,
    2102: NSNitroNserrInvalidurl,
    2053: NSNitroNserrInvalidpol,
    2054: NSNitroNserrNopol,
    2055: NSNitroNserrRuleurl,
    2056: NSNitroNserrDelmc,
    2057: NSNitroNserrAcp,
    2058: NSNitroNserrAcs,
    2059: NSNitroNserrNosetCexp,
    2060: NSNitroNserrCexpDepth,
    2061: NSNitroNserrNovpnapp,
    2062: NSNitroNserrNosetCse,
    2063: NSNitroNserrInvalPolname,
    2097: NSNitroNserrUnbindInvalidpol,
    2098: NSNitroNserrExceedMaxPolLimit,
    2103: NSNitroNserrInternalPiError,
    2080: NSNitroNserrInterfacebound,
    2081: NSNitroNserrIfaceNoUnbind,
    2082: NSNitroNserrIfaceMaxVlans,
    2128: NSNitroNserrMonitorInterval,
    2129: NSNitroNserrMonitorDestip,
    2130: NSNitroNserrMonitorCodes,
    2131: NSNitroNserrMonitorRef,
    2132: NSNitroNserrMonitorBuiltin,
    2133: NSNitroNserrMonitorBound,
    2134: NSNitroNserrMonitorType,
    2135: NSNitroNserrMonitorLocal,
    2136: NSNitroNserrTimeoutRange,
    2137: NSNitroNserrInvalidhashlen,
    2138: NSNitroNserrNotauthorized,
    2139: NSNitroNserrMonitorDefault,
    2140: NSNitroNserrMonitorLdnsAddPerm,
    2141: NSNitroNserrMonitorLdnsBindPerm,
    2144: NSNitroNserrBackupLoop,
    2154: NSNitroNserrSecureUdp,
    2155: NSNitroNserrMonitorWrongType,
    2156: NSNitroNserrLrtmPerm,
    2157: NSNitroNserrMonitorScriptname,
    2159: NSNitroNserrMonitorDispatcherip,
    2160: NSNitroNserrMonitorUserperm,
    2161: NSNitroNserrMonitorNocodes,
    2162: NSNitroNserrInvalMon,
    2163: NSNitroNserrTypeExists,
    2164: NSNitroNserrMonitorUnbindDefault,
    2165: NSNitroNserrMonitorBindDefault,
    2166: NSNitroNserrMonitorDisableDefault,
    2167: NSNitroNserrDrtmPerm,
    2168: NSNitroNserrMonDtrmDeviation,
    2169: NSNitroNserrMonitorInvalidValue,
    2170: NSNitroNserrMonitorNotBound,
    2171: NSNitroNserrInvalidMonitor,
    2172: NSNitroNserrMonitorNoSuchipaddr,
    2173: NSNitroNserrMonitorScriptArgSize,
    2174: NSNitroNserrMetrictableNoent,
    2175: NSNitroNserrMetrictableExist,
    2176: NSNitroNserrDelMetrictablePermanent,
    2177: NSNitroNserrMaxMetricBinding,
    2178: NSNitroNserrMetricNoent,
    2179: NSNitroNserrMetricExists,
    2180: NSNitroNserrOidExist,
    2181: NSNitroNserrSnmpOidInval,
    2182: NSNitroNserrMetrictableRdonly,
    2183: NSNitroNserrThresholdZero,
    2184: NSNitroNserrLdapMonitorIncomplete,
    2185: NSNitroNserrMysqlMonitorIncomplete,
    2186: NSNitroNserrPop3MonitorIncomplete,
    2187: NSNitroNserrNntpMonitorIncomplete,
    2188: NSNitroNserrFtpextendedMonitorIncomplete,
    2189: NSNitroNserrSnmpMonitorIncomplete,
    2190: NSNitroNserrCitrixXmlService,
    2191: NSNitroNserrCitrixWebInterface,
    2192: NSNitroNserrLdnsMonCantDisable,
    2193: NSNitroNserrResRetryOnIpSvr,
    2194: NSNitroNserrIpOnDbsSvr,
    2195: NSNitroNserrMonitorAlertretries,
    2196: NSNitroNserrMonitorFailureretries,
    2197: NSNitroNserrMonitorAlertfailureretries,
    2198: NSNitroNserrMonitorIp,
    2199: NSNitroNserrMonitorSubnet,
    2200: NSNitroNserrMonitorStatic,
    2201: NSNitroNserrTosidNotSet,
    2202: NSNitroNserrFailureretriesNotSupported,
    2203: NSNitroNserrSuccessretriesNotSupported,
    2204: NSNitroNserrSetvsInvalMysqlparams,
    2205: NSNitroNserrSetvsInvalProtocolParams,
    2206: NSNitroNserrSetvsInvalProtocolsParams,
    2207: NSNitroNserrDdcValidateCredRequired,
    2208: NSNitroNserrCitrixWiExtendedMonitorIncomplete,
    2305: NSNitroNserrSvcporttype,
    2306: NSNitroNserrVipInGroup,
    2307: NSNitroNserrUnsupportedBkp,
    2308: NSNitroNserrNonhttpsslVipingrp,
    2309: NSNitroNserrNonhttpVipingrp,
    2310: NSNitroNserrUseProperRmCmd,
    2321: NSNitroNserrLbmethodNotSupported,
    2322: NSNitroNserrPersistenceNotSupported,
    2323: NSNitroNserrVserverParameters,
    2324: NSNitroNserrServiceParameters,
    2325: NSNitroNserrLbvipDelete,
    2326: NSNitroNserrCachepolicyRespactionInval,
    2327: NSNitroNserrCachelicenseFailed,
    2328: NSNitroNserrLbvipMultiroutes,
    2329: NSNitroNserrLbmacInval,
    2336: NSNitroNserrCachestatsObjNotpresent,
    2337: NSNitroNserrCachepolicyNotactive,
    2338: NSNitroNserrCacheBuiltinsNotSourced,
    2339: NSNitroNserrCachepolicyPriorityInval,
    2340: NSNitroNserrRoute6DefaultOnly,
    2341: NSNitroNserrRoute6DefaultExists,
    2342: NSNitroNserrRoute6InvalidGateway,
    2343: NSNitroNserrRoute6Max,
    2344: NSNitroNserrRoute6NotExist,
    2345: NSNitroNserrIpv6InvalidAddr,
    2352: NSNitroNserrLbvipIpv6tov4,
    2353: NSNitroNserrIpv6Nsiptovip,
    2354: NSNitroNserrIpv6Viptonsip,
    2355: NSNitroNserrIpv6Scope,
    2356: NSNitroNserrLbvipIpv4tov6,
    2357: NSNitroNserrIpv6Linklocaltovip,
    2358: NSNitroNserrIpv6Mapiponnsip,
    2359: NSNitroNserrSecureipportaddrinuse,
    2360: NSNitroNserrIpv6InvalidPrefix,
    2361: NSNitroNserrNd6LinklocalVlan,
    2368: NSNitroNserrNd6VlanIntf,
    2369: NSNitroNserrPersistTimeoutToDefault,
    2370: NSNitroNserrLbGroupNotExist,
    2371: NSNitroNserrLbVserverAlreadyBound,
    2561: NSNitroNserrNameSvrExists,
    2562: NSNitroNserrNameSvrIdnsNempty,
    2563: NSNitroNserrNameSvrIvalpolicy,
    2564: NSNitroNserrNameSvrIvalproto,
    2565: NSNitroNserrNameSvrAddNexistVip,
    2566: NSNitroNserrNameSvrNexist,
    2567: NSNitroNserrNameSvrIdnsPerm,
    2568: NSNitroNserrNameSvrIpExists,
    2624: NSNitroNserrErrAaaLicense,
    2625: NSNitroNserrUsrNointraip,
    2626: NSNitroNserrUsrNotconfigured,
    2627: NSNitroNserrInvalAaaGrp,
    2628: NSNitroNserrInvalCombnation,
    2629: NSNitroNserrInvalMipIip,
    2630: NSNitroNserrInvalMipoffIipoff,
    2631: NSNitroNserrUserexist,
    2632: NSNitroNserrGroupexist,
    2633: NSNitroNserrUseralreadybound,
    2640: NSNitroNserrUsernotbound,
    2641: NSNitroNserrEntitynotbound,
    2642: NSNitroNserrGroupnotexist,
    2643: NSNitroNserrInvalidloglevel,
    2644: NSNitroNserrDhMisconfig,
    2645: NSNitroNserrDhIpport,
    2646: NSNitroNserrDhinuse,
    2647: NSNitroNserrInvalAaaglobalPoltype,
    2648: NSNitroNserrNoIp,
    2649: NSNitroNserrAaatmLic,
    2650: NSNitroNserrAaatmDisabled,
    2651: NSNitroNserrNoAuthHost,
    2652: NSNitroNserrAuthOn,
    2653: NSNitroNserrKillpending,
    2654: NSNitroNserrAaatmNoAuthVs,
    2655: NSNitroNserrAaatm401authOn,
    2656: NSNitroNserrUnauthrzed,
    2657: NSNitroNserrKillInprogress,
    2658: NSNitroNserrWiFrmNotexist,
    2659: NSNitroNserrWiFrmLast,
    2660: NSNitroNserrWiNotinst,
    2661: NSNitroNserrWiGenfailed,
    2662: NSNitroNserrWiSiteExist,
    2663: NSNitroNserrWiSiteNotexist,
    2664: NSNitroNserrWiSiteInvalAgurl,
    2665: NSNitroNserrWiSiteInvalStaurl,
    2666: NSNitroNserrWiSiteOnlyMpx,
    2667: NSNitroNserrWiInstfailed,
    2668: NSNitroNserrWiMaxsiteExcd,
    2669: NSNitroNserrWiStawithoutagurl,
    2670: NSNitroNserrWiAgurlwithoutsta,
    2671: NSNitroNserrWiRelwithoutagurl,
    2672: NSNitroNserrWiAuthwithoutagurl,
    2673: NSNitroNserrWiTwotktwithoutrel,
    2674: NSNitroNserrWiTwotktwithoutsecsta,
    2675: NSNitroNserrWiSecstasame,
    2676: NSNitroNserrWiLicense,
    2677: NSNitroNserrWiSecstawithoutsta,
    2678: NSNitroNserrAuthNegotiate,
    2679: NSNitroNserrWiInstsitesreduced,
    2680: NSNitroNserrWiIncompatibleauthpoint,
    2681: NSNitroNserrWiSiteWithinSite,
    2686: NSNitroNserrTmInvalidPersConfig,
    2817: NSNitroNserrRwActInval,
    2818: NSNitroNserrRwUndefactInval,
    2819: NSNitroNserrActflowmismatch,
    2820: NSNitroNserrRonlyTarExpr,
    2821: NSNitroNserrPatsetBindfail,
    2822: NSNitroNserrPatsetUnbindfail,
    2823: NSNitroNserrPatsetNotpresent,
    2824: NSNitroNserrRspActInval,
    2825: NSNitroNserrRspPolicyFlowtypeReq,
    2826: NSNitroNserrTarFlowtypeNres,
    2827: NSNitroNserrRspConfigLock,
    2828: NSNitroNserrRspActMustBeNoop,
    2829: NSNitroNserrPatsetInvalidRegex,
    2830: NSNitroNserrPatsetBindfailDupIndex,
    2831: NSNitroNserrPatsetBindfailIndexNotGiven,
    2832: NSNitroNserrPatsetBindfailIndexNotRequired,
    2833: NSNitroNserrPatsetBindfailPatlenLtWuMinlen,
    2834: NSNitroNserrTargetNotAllowedInRule,
    2835: NSNitroNserrRwTargetNotAllowedInStrbuilder,
    2836: NSNitroNserrPitInval,
    2837: NSNitroNserrInvalInvokepoint,
    2838: NSNitroNserrPitMaxPacket,
    2839: NSNitroNserrRefineSearchInvalid,
    2840: NSNitroNserrExtendInvalid,
    2841: NSNitroNserrNonExtendExpr,
    2842: NSNitroNserrExtendInvalPirl,
    2843: NSNitroNserrInvalTarExpr,
    2844: NSNitroNserrInvalPatternSearchSet,
    2845: NSNitroNserrInvalSearchArgs,
    2846: NSNitroNserrRspActMustBeResetDrop,
    2847: NSNitroNserrInvalSearchSyntax,
    2848: NSNitroNserrInvalSearchXpathSyntax,
    2849: NSNitroNserrInvalSearchPatsetSyntax,
    2850: NSNitroNserrInvalSearchRegexSyntax,
    2851: NSNitroNserrRwReqBodyNotAllowed,
    2852: NSNitroNserrRenameNotsupported,
    2853: NSNitroNserrEntityRemovalNotallowed,
    2854: NSNitroNserrPiEntityExists,
    2855: NSNitroNserrIncompatibleCalloutChange,
    2856: NSNitroNserrStringmapNotpresent,
    2960: NSNitroNserrUrltransMaxEntities,
    2962: NSNitroNserrUrltransInvalProfile,
    2963: NSNitroNserrUrltransActionInuse,
    2964: NSNitroNserrUrltransPriorityExists,
    2965: NSNitroNserrUrltransReqPcreErr,
    2966: NSNitroNserrUrltransRespPcreErr,
    2967: NSNitroNserrUrltransReqIntoErr,
    2968: NSNitroNserrUrltransRespIntoErr,
    2969: NSNitroNserrUrltransCookieIntoErr,
    2970: NSNitroNserrUrltransCookiePcreErr,
    2971: NSNitroNserrUrltransTooManyBackrefs,
    2972: NSNitroNserrUrltransMissingFrom,
    3040: NSNitroNserrPiLongvsvrname,
    3041: NSNitroNserrPiPriorityExists,
    3073: NSNitroNserrInvalpiexpr,
    3074: NSNitroNserrInvalintop,
    3075: NSNitroNserrInvalcompare,
    3076: NSNitroNserrInvalboolop,
    3077: NSNitroNserrArgneg,
    3078: NSNitroNserrArgexceed,
    3079: NSNitroNserrArgzero,
    3080: NSNitroNserrMaxheader,
    3081: NSNitroNserrInvalpicexpr,
    3082: NSNitroNserrCexprlimit,
    3083: NSNitroNserrExprlimit,
    3084: NSNitroNserrSexprlimit,
    3085: NSNitroNserrInvalpisexpr,
    3086: NSNitroNserrNobidi,
    3087: NSNitroNserrNolab,
    3088: NSNitroNserrInternalLabelRm,
    3089: NSNitroNserrPolicyFlowtypeNone,
    3090: NSNitroNserrInvalPriority,
    3091: NSNitroNserrNumericexpr,
    3092: NSNitroNserrBoolexpr,
    3093: NSNitroNserrNotbound,
    3094: NSNitroNserrPolicyInuse,
    3095: NSNitroNserrPolicySetNotallowed,
    3096: NSNitroNserrInvalidBind,
    3097: NSNitroNserrUseInvokeResult,
    3104: NSNitroNserrInvalUnbind,
    3105: NSNitroNserrRegexInvalid,
    3106: NSNitroNserrRegexBackref,
    3107: NSNitroNserrRegexRecursive,
    3108: NSNitroNserrPixlExprUnsafe,
    3109: NSNitroNserrPiActionMaxRefReached,
    3110: NSNitroNserrPiInvalidUnset,
    3111: NSNitroNserrEmptyString,
    3112: NSNitroNserrInvalBtwArgs,
    3113: NSNitroNserrInvalArgSpecified,
    3854: NSNitroNserrInvalArgCspl,
    3114: NSNitroNserrFlowtypeNotApplicable,
    3115: NSNitroNserrInvalArgSpecifiedCs,
    3116: NSNitroNserrInvalGotoexprCs,
    3117: NSNitroNserrRebindFailed,
    3118: NSNitroNserrSecondBind,
    3119: NSNitroNserrNonhttpVs,
    3858: NSNitroNserrInvalXpathExpr,
    3859: NSNitroNserrXpathExprNotSupported,
    3860: NSNitroNserrTargetInval,
    3861: NSNitroNserrNonRespHttpVsList,
    3862: NSNitroNserrInvalVserverBind,
    3863: NSNitroNserrAppFreedNsb,
    3864: NSNitroNserrMultBindInval,
    3905: NSNitroNserrInvalidKeyvalue,
    3120: NSNitroNserrAsNostarturl,
    3121: NSNitroNserrAsExistStarturl,
    3122: NSNitroNserrAsNodenyurl,
    3123: NSNitroNserrAsExistDenyurl,
    3124: NSNitroNserrAsNocookieconsistency,
    3125: NSNitroNserrAsExistCookieconsistency,
    3126: NSNitroNserrAsNofieldconsistency,
    3127: NSNitroNserrAsExistFieldconsistency,
    3128: NSNitroNserrAsNoxss,
    3129: NSNitroNserrAsExistXss,
    3130: NSNitroNserrAsNosql,
    3131: NSNitroNserrAsExistSql,
    3132: NSNitroNserrAsNofieldformat,
    3133: NSNitroNserrAsExistFieldformat,
    3134: NSNitroNserrAsNoobjectexpression,
    3135: NSNitroNserrAsExistObjectexpression,
    3136: NSNitroNserrAsNofieldtype,
    3138: NSNitroNserrAsBadActionStarturl,
    3139: NSNitroNserrAsBadActionDenyurl,
    3140: NSNitroNserrAsBadActionCookieconsistency,
    3141: NSNitroNserrAsBadActionFieldconsistency,
    3142: NSNitroNserrAsBadActionXss,
    3143: NSNitroNserrAsBadActionSql,
    3144: NSNitroNserrAsBadActionFieldformat,
    3145: NSNitroNserrAsBadActionObjectexpression,
    3146: NSNitroNserrAsBadActionBufferoverflow,
    3147: NSNitroNserrAsBadActionCcard,
    3148: NSNitroNserrAsFieldformatMinGtMax,
    3149: NSNitroNserrAsFieldtypeBadNameLen,
    3150: NSNitroNserrAsBadCommentLen,
    3151: NSNitroNserrAsFieldtypeBadRegexLen,
    3152: NSNitroNserrAsSecurityCheckRequired,
    3153: NSNitroNserrAsFieldtypeBuiltin,
    3154: NSNitroNserrAsMaxEntities,
    3155: NSNitroNserrAsBadDefaultCharset,
    3156: NSNitroNserrAsBadCookieconsistencyName,
    3157: NSNitroNserrAsBadErrorurl,
    3158: NSNitroNserrAsBadEncodingUrl,
    3159: NSNitroNserrAsBadEncodingFieldname,
    3160: NSNitroNserrAsBadEncodingCookiename,
    3161: NSNitroNserrAsBadEncodingObjectexpressionName,
    3162: NSNitroNserrAsBadEncodingExpression,
    3163: NSNitroNserrAsBadEncodingRegex,
    3164: NSNitroNserrAsModifiedUrl,
    3165: NSNitroNserrAsModifiedObjectexpression,
    3166: NSNitroNserrAsCffieldBadFieldnameLen,
    3167: NSNitroNserrAsCffieldBadUrlLen,
    3168: NSNitroNserrAsNocffield,
    3169: NSNitroNserrAsBadCffName,
    3170: NSNitroNserrAsBadCffUrl,
    3171: NSNitroNserrAsCffDup,
    3172: NSNitroNserrAsBadActionXdos,
    3173: NSNitroNserrAsExistXmlDosUrl,
    3174: NSNitroNserrXmlUrlNotSupported,
    3175: NSNitroNserrAsNoXdosUrl,
    3176: NSNitroNserrAsInvalidXmlDosConf,
    3177: NSNitroNserrAsBadActionXmlSqlinjection,
    3178: NSNitroNserrAsBadActionXmlXss,
    3179: NSNitroNserrAsBadActionXmlWellformedness,
    3180: NSNitroNserrAsBadActionProfileType,
    3181: NSNitroNserrAsModifiedFieldname,
    3182: NSNitroNserrAsBadActionWsi,
    3183: NSNitroNserrAsExistXmlWsiUrl,
    3184: NSNitroNserrAsNoWsiUrl,
    3185: NSNitroNserrAsInvalidXmlWsiConf,
    3186: NSNitroNserrAsObjectnameTooBig,
    3187: NSNitroNserrAsObjectNoExist,
    3188: NSNitroNserrAsServerNameTooBig,
    3189: NSNitroNserrAsObjectNotReadable,
    3190: NSNitroNserrAsNoprofile,
    3191: NSNitroNserrAsBadActionXmlAttachment,
    3192: NSNitroNserrAsBadActionMsgval,
    3193: NSNitroNserrAsExistXmlMsgvalUrl,
    3194: NSNitroNserrAsNoMsgvalUrl,
    3195: NSNitroNserrAsInvalidXmlMsgvalConf,
    3196: NSNitroNserrAsBindXmlMsgvalConf,
    3197: NSNitroNserrAsImportFailed,
    3198: NSNitroNserrAsObjectExist,
    3199: NSNitroNserrAsInvalidOption,
    3200: NSNitroNserrAsRemoveFailed,
    3201: NSNitroNserrAsNoResource,
    3202: NSNitroNserrAsShowFailed,
    3203: NSNitroNserrAsDependencyFailed,
    3204: NSNitroNserrAsCompilationFailed,
    3205: NSNitroNserrInvalidObjectName,
    3206: NSNitroNserrAsImportDownloadFailed,
    3207: NSNitroNserrAsResourceInuse,
    3208: NSNitroNserrAsBadMappingData,
    3209: NSNitroNserrAsProfileChangeHtml,
    3210: NSNitroNserrAsProfileChangeXml,
    3211: NSNitroNserrAsImportAlreadyInprocess,
    3212: NSNitroNserrAsInvalidXmlErrorObject,
    3213: NSNitroNserrAsXmlWellformednessDisabled,
    3214: NSNitroNserrAsIndividualImportLimitExceeded,
    3215: NSNitroNserrAsTotalImportLimitExceeded,
    3216: NSNitroNserrAsLearningBusy,
    3217: NSNitroNserrAsDeprecatedXmlWsiRuleR4003,
    3218: NSNitroNserrAsExistXmlAttachmentUrl,
    3219: NSNitroNserrAsNoXmlAttachmentUrl,
    3220: NSNitroNserrAsBadActionSoapFault,
    3221: NSNitroNserrAsXmlDosValueOutOfRange,
    3222: NSNitroNserrAsXmlMsgvalCliError,
    3223: NSNitroNserrAsInvalidCustomSettingsObject,
    3224: NSNitroNserrAsSessionTimeoutLifetimeConflict,
    3225: NSNitroNserrAsClassicPolicyAlreadyBound,
    3226: NSNitroNserrAsAdvancedPolicyAlreadyBound,
    3227: NSNitroNserrAsCustomSettingsNoInjectionType,
    3228: NSNitroNserrAsNocsrfTag,
    3229: NSNitroNserrAsExistCsrfTag,
    3230: NSNitroNserrAsBadActionCsrfTag,
    3231: NSNitroNserrAsTurningTaggingOffCsrfTagOn,
    3232: NSNitroNserrAsTurningCsrfTagOnTaggingOff,
    3233: NSNitroNserrAsImportLimitLessThanImportDirSize,
    3234: NSNitroNserrAsUnsupportedImportProtocol,
    3235: NSNitroNserrAsUnsupportedExportProtocol,
    3236: NSNitroNserrAsExportFailed,
    3237: NSNitroNserrAsBadLocalFile,
    3238: NSNitroNserrAsInvalidRegexCustomObject,
    3239: NSNitroNserrAsBuiltinInvalidOp,
    3240: NSNitroNserrAsInvalidAdvPolicyState,
    3241: NSNitroNserrAsBuiltinNamesInConf,
    3242: NSNitroNserrAsDefaultProfileIsBypass,
    3243: NSNitroNserrAsNoLearnDenyurl,
    3244: NSNitroNserrAsNoLearnCsrfTag,
    3245: NSNitroNserrAsNoLearnCcard,
    3246: NSNitroNserrAsNoLearnBufferoverflow,
    3247: NSNitroNserrAsNoLearnXmlFormat,
    3251: NSNitroNserrAsNoLearnXmlSqlinjection,
    3252: NSNitroNserrAsNoLearnXmlXss,
    3253: NSNitroNserrAsNoLearnXmlMsgval,
    3254: NSNitroNserrAsNoLearnXmlSoapFault,
    3255: NSNitroNserrAsImportInternalError,
    3256: NSNitroNserrAsNetsvcConnFailed,
    3257: NSNitroNserrAsValidationFailed,
    3258: NSNitroNserrAsCkiTransformDisabled,
    3259: NSNitroNserrAsNoxmlxss,
    3260: NSNitroNserrAsExistXmlxss,
    3261: NSNitroNserrAsNoxmlsql,
    3262: NSNitroNserrAsExistXmlsql,
    3263: NSNitroNserrAsNoEndtag,
    3264: NSNitroNserrAsSigInvalidRuleid,
    3265: NSNitroNserrAsSigInvalidRuleVersion,
    3266: NSNitroNserrAsSigParseError,
    3267: NSNitroNserrAsSigInvalidAttribute,
    3268: NSNitroNserrAsSigMultipleLocations,
    3269: NSNitroNserrAsSigInvalidState,
    3270: NSNitroNserrAsCkiEncryptMethodIsNone,
    3271: NSNitroNserrAsUpdateFailed,
    3272: NSNitroNserrAsObjectNotUsed,
    3273: NSNitroNserrAsSigMultipleUrls,
    3274: NSNitroNserrAsSigMultipleFieldNames,
    3284: NSNitroNserrAsSqlinjectionKeywordInvalidAttribute,
    3285: NSNitroNserrAsSplstringInvalidAttribute,
    3286: NSNitroNserrAsSqlinjectionKeywordLiteralExceedMaxlen,
    3287: NSNitroNserrAsSplstringLiteralExceedMaxlen,
    3294: NSNitroNserrAsXssDeniedPatternInvalidAttribute,
    3295: NSNitroNserrAsXssDeniedPatternExceedMaxlen,
    3296: NSNitroNserrAsXssAllowedPatternInvalidAttribute,
    3297: NSNitroNserrAsXssAllowedPatternExceedMaxlen,
    3299: NSNitroNserrAsSigInternalError,
    3305: NSNitroNserrAsSigNonLiteralFastmatch,
    3306: NSNitroNserrAsSigNegatedLiteralFastmatch,
    3307: NSNitroNserrAsSigMemAllocFailed,
    3308: NSNitroNserrAsSigTooManyPatterns,
    3309: NSNitroNserrAsSigLiteralHexParseError,
    3310: NSNitroNserrAsSigPcreCompileError,
    3314: NSNitroNserrAsSigInvalidFileVersion,
    3248: NSNitroNserrNoSuchProfile,
    3249: NSNitroNserrProfileInUse,
    3329: NSNitroNserrInterfaceBound,
    3330: NSNitroNserrVridInterfaceNotBound,
    3331: NSNitroNserrNoSuchInterface,
    3457: NSNitroNserrInvalthreshold,
    3458: NSNitroNserrWrongthresholds,
    3459: NSNitroNserrInvalidSrcip,
    3460: NSNitroNserrThresholdUnsettable,
    3461: NSNitroNserrTimeUnsettable,
    3462: NSNitroNserrWrongLowThresholds,
    3888: NSNitroNserrPublicip,
    3889: NSNitroNserrPrivateip,
    3890: NSNitroNserrProxyip,
    3891: NSNitroNserrWildcardtcpvip,
    3892: NSNitroNserrWildcardanyvip,
    3893: NSNitroNserrFtpvippresent,
    3894: NSNitroNserrV46Usip,
    3895: NSNitroNserrIncompatibleIp,
    3920: NSNitroNserrTnlNetbridged,
    3921: NSNitroNserrTnlGre,
    3922: NSNitroNserrTnlRipmask,
    3923: NSNitroNserrVlanNetbridged,
    3924: NSNitroNserrMaxNetbridgeTunnel,
    3925: NSNitroNserrTunBound,
    3926: NSNitroNserrSubnetBound,
    3936: NSNitroNserrAppflowInvalidport,
    3937: NSNitroNserrIpfixMaxCollectors,
    3938: NSNitroNserrNoSuchCollector,
    3939: NSNitroNserrAppflowNcoreOnly,
    3940: NSNitroNserrAppflowNonzeroActionRefcount,
    3941: NSNitroNserrAppflowCollectorNameInuse,
    3942: NSNitroNserrAppflowActInval,
    3968: NSNitroNserr1gsfpspeedlimit,
    3969: NSNitroNserr1gsfpduplexlimit,
    3970: NSNitroNserr1gspeedlimit,
    3971: NSNitroNserr1gduplexlimit,
    3972: NSNitroNserr10gspeedlimit,
    3973: NSNitroNserr10gduplexlimit,
    3974: NSNitroNserr10gautoneglimit,
    3975: NSNitroNserr10gspeedonly,
    3976: NSNitroNserrFullduplexonly,
}
NSNitroExceptionClassMap.update(NSNitroExceptions)
