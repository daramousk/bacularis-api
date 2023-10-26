# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobid** | **int** | Job identifier | [optional] 
**job** | **str** | Job name with date and time | [optional] 
**name** | **str** | Job name | [optional] 
**type** | **str** | Job type | [optional] 
**level** | **str** | Job level | [optional] 
**clientid** | **int** | Client identifier | [optional] 
**jobstatus** | **str** | Job status. Note, some statuses can be not visible outside (used internally by Bacula) | [optional] 
**schedtime** | **str** | Scheduled time (YYY-MM-DD HH:MM:SS) | [optional] 
**schedtime_epoch** | **int** | Scheduled time in Unix timestamp form | [optional] 
**starttime** | **str** | Start time (YYYY-MM-DD HH:M:SS) | [optional] 
**starttime_epoch** | **int** | Start time in Unix timestamp form | [optional] 
**endtime** | **str** | End time (YYYY-MM-DD HH:M:SS) | [optional] 
**endtime_epoch** | **int** | End time in Unix timestamp form | [optional] 
**realendtime** | **str** | Real end time (YYYY-MM-DD HH:M:SS) | [optional] 
**realendtime_epoch** | **int** | Real end time in Unix timestamp form | [optional] 
**jobtdate** | **int** | Backup time/date in Unix timestamp form | [optional] 
**volsessionid** | **int** | Volume session identifier | [optional] 
**volsessiontime** | **int** | Volume session time | [optional] 
**jobfiles** | **int** | Job file count | [optional] 
**jobbytes** | **int** | Job size in bytes | [optional] 
**readbytes** | **int** | Read bytes | [optional] 
**joberrors** | **int** | Job error count | [optional] 
**jobmissingfiles** | **int** | Job missing file count | [optional] 
**poolid** | **int** | Pool identifier | [optional] 
**filesetid** | **int** | FileSet identifier | [optional] 
**priorjobid** | **int** | JobId of migrated (prior) job | [optional] 
**purgedfiles** | **int** | Purged file count | [optional] 
**hasbase** | **int** | Has base jobs, 1 if job uses base job, otherwise 0 | [optional] 
**hascache** | **int** | Has Bvfs cache, 1 if job has Bvfs cache, otherwise 0 | [optional] 
**reviewed** | **int** | Reviewed | [optional] 
**comment** | **str** | Job comment | [optional] 
**filetable** | **str** | File table | [optional] 
**client** | **str** | Client name | [optional] 
**pool** | **str** | Pool name | [optional] 
**fileset** | **str** | FileSet name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

