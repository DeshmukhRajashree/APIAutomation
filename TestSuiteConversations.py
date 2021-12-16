#include required libraries
import http
import pytest
import requests
import json

#inculde the file containing all functions related to Conversation API
import ApplicationKeywords

#######################################################################################################

#Test case no: TC_01
#Title : GetConversations

def TC_01():
        # get all conversations
        response = ApplicationKeywords.getConversations()
        # Test cases passes if the status code returned by the response object is 200
        print('TC_01 Message code')
        print(response.status_code)
        assert response.status_code == http.HTTPStatus.OK,'fail'+str(response.status_code)
#######################################################################################################
#Test case no: TC_02
#Title : Create Conversations
def TC_02():
    # create a conversation
    response = ApplicationKeywords.createconversation()
    # Test cases passes if the status code returned by the response object is 200
    print('TC_02 Message code')
    print(response.status_code)
    assert response.status_code == http.HTTPStatus.OK,'fail'+str(response.status_code)
#######################################################################################################
# Test case no: TC_04
# Title : Get Conversation by Id (provide invalid id, expected status is 404 , sample negative test case)
def TC_04_02() :
    # get all conversations
    response = ApplicationKeywords.getConversation("1")
    # Test cases passes if the status code returned by the response object is 200
    print('TC_00_02 Message code')
    print(response.status_code)
    assert response.status_code == http.HTTPStatus.NOT_FOUND, 'fail' + str(response.status_code)
#######################################################################################################
#Test case no: TC_05
#Title - Delete conversation
def TC_05():
    # Prerequisite -create a conversation
    # Delete  conversation
    response = ApplicationKeywords.createconversation()
    print('TC_05 Message code')
    print(response.status_code)
    respBody = json.loads(response.text)
    if response.status_code == http.HTTPStatus.OK:
        # get Conversatio Id and Url of newly created convesration
        conId = respBody['id']
        url = respBody['href']
        responseDel = ApplicationKeywords.deleteconversation(conId)
        #Expected status is 200 on successful delete
        print(responseDel.status_code)
        assert responseDel.status_code == http.HTTPStatus.OK,'fail' + str(responseDel.status_code)
    else:assert False
