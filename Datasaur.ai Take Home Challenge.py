Feature: Link a device

  Scenario Outline: As a user, i can link a device

    Given I am on the WhatsApp Settings
    When I Link a Device
    And I Unlock my phone
    Then I Point your phone at the screen of the device you want to link to scan the QR code

Feature: Reply a message

  Scenario Outline: As a user, i can reply a message

    Given I am on the WhatsApp messages
    When I Hover over the message
    And I click icon arrow
    And I click reply
    Then I Enter my response and click Send

Feature: Make a voice call

  Scenario Outline: As a user, i can make a voice call

    Given I am on the WhatsApp messages
    When I open the individual chat with the contact i like to call
    And I click the Voice call icon
    Then I can talk to my friend

Feature: Switch between voice and video calls

  Scenario Outline: As a user, i can switch between voice and video calls

    Given I am a whatsapp voice call user
    When I on the call
    And I hover over the Camera icon during the call
    And I click the Camera icon
    Then the voice call will switch to a video call if your contact accepts the switch

Feature: Make a video call

  Scenario Outline: As a user, i can make a video call

    Given I am on the WhatsApp messages
    When I open the individual chat with the contact i like to call
    And I click the video call icon
    Then I can talk to my friend

Feature: Send photos, videos, documents, stickers or contacts

  Scenario Outline: As a user, i can send photos, videos, documents, stickers or contacts

    Given I am on the WhatsApp messages
    When I open an individual or group chat
    And I click attach
    And I click photos & videos or camera or document or contact
    Then I click send

Feature: Send a voice message

  Scenario Outline: As a user, i can send a voice message

    Given I am on the WhatsApp messages
    When I Open an individual or group chat
    And I click the microphone
    And I start speaking into your computer's microphone
    Then I click send

Feature: Save a photo or video to your computer

  Scenario Outline: As a user, i can save a photo or video to your computer

    Given I am on the WhatsApp messages
    When I Open an individual or group chat
    And I click the photo or video i want to save
    And I click download
    Then I click save

Feature: Mute group notifications

  Scenario Outline: As a user, i can mute group notifications

    Given I am on the WhatsApp
    When I Open the group chat
    And I click the group subject
    And I Select the length of time you'd like to mute notifications for
    Then I click MUTE NOTIFICATIONS

Feature: Unmute group notifications

  Scenario Outline: As a user, i can unmute group notifications

    Given I am on the WhatsApp
    When I Open the group chat
    And I click the group subject
    And I Uncheck the Muted box
    Then I click UNMUTE

