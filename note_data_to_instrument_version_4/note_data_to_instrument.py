from time import sleep
import time
import glob, os

# Copy of GNU Public License Version 3
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
# 
#  Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
# 
#                             Preamble
# 
#   The GNU General Public License is a free, copyleft license for
# software and other kinds of works.
# 
#   The licenses for most software and other practical works are designed
# to take away your freedom to share and change the works.  By contrast,
# the GNU General Public License is intended to guarantee your freedom to
# share and change all versions of a program--to make sure it remains free
# software for all its users.  We, the Free Software Foundation, use the
# GNU General Public License for most of our software; it applies also to
# any other work released this way by its authors.  You can apply it to
# your programs, too.
# 
#   When we speak of free software, we are referring to freedom, not
# price.  Our General Public Licenses are designed to make sure that you
# have the freedom to distribute copies of free software (and charge for
# them if you wish), that you receive source code or can get it if you
# want it, that you can change the software or use pieces of it in new
# free programs, and that you know you can do these things.
# 
#   To protect your rights, we need to prevent others from denying you
# these rights or asking you to surrender the rights.  Therefore, you have
# certain responsibilities if you distribute copies of the software, or if
# you modify it: responsibilities to respect the freedom of others.
# 
#   For example, if you distribute copies of such a program, whether
# gratis or for a fee, you must pass on to the recipients the same
# freedoms that you received.  You must make sure that they, too, receive
# or can get the source code.  And you must show them these terms so they
# know their rights.
# 
#   Developers that use the GNU GPL protect your rights with two steps:
# (1) assert copyright on the software, and (2) offer you this License
# giving you legal permission to copy, distribute and/or modify it.
# 
#   For the developers' and authors' protection, the GPL clearly explains
# that there is no warranty for this free software.  For both users' and
# authors' sake, the GPL requires that modified versions be marked as
# changed, so that their problems will not be attributed erroneously to
# authors of previous versions.
# 
#   Some devices are designed to deny users access to install or run
# modified versions of the software inside them, although the manufacturer
# can do so.  This is fundamentally incompatible with the aim of
# protecting users' freedom to change the software.  The systematic
# pattern of such abuse occurs in the area of products for individuals to
# use, which is precisely where it is most unacceptable.  Therefore, we
# have designed this version of the GPL to prohibit the practice for those
# products.  If such problems arise substantially in other domains, we
# stand ready to extend this provision to those domains in future versions
# of the GPL, as needed to protect the freedom of users.
# 
#   Finally, every program is threatened constantly by software patents.
# States should not allow patents to restrict development and use of
# software on general-purpose computers, but in those that do, we wish to
# avoid the special danger that patents applied to a free program could
# make it effectively proprietary.  To prevent this, the GPL assures that
# patents cannot be used to render the program non-free.
# 
#   The precise terms and conditions for copying, distribution and
# modification follow.
# 
#                        TERMS AND CONDITIONS
# 
#   0. Definitions.
# 
#   "This License" refers to version 3 of the GNU General Public License.
# 
#   "Copyright" also means copyright-like laws that apply to other kinds of
# works, such as semiconductor masks.
# 
#   "The Program" refers to any copyrightable work licensed under this
# License.  Each licensee is addressed as "you".  "Licensees" and
# "recipients" may be individuals or organizations.
# 
#   To "modify" a work means to copy from or adapt all or part of the work
# in a fashion requiring copyright permission, other than the making of an
# exact copy.  The resulting work is called a "modified version" of the
# earlier work or a work "based on" the earlier work.
# 
#   A "covered work" means either the unmodified Program or a work based
# on the Program.
# 
#   To "propagate" a work means to do anything with it that, without
# permission, would make you directly or secondarily liable for
# infringement under applicable copyright law, except executing it on a
# computer or modifying a private copy.  Propagation includes copying,
# distribution (with or without modification), making available to the
# public, and in some countries other activities as well.
# 
#   To "convey" a work means any kind of propagation that enables other
# parties to make or receive copies.  Mere interaction with a user through
# a computer network, with no transfer of a copy, is not conveying.
# 
#   An interactive user interface displays "Appropriate Legal Notices"
# to the extent that it includes a convenient and prominently visible
# feature that (1) displays an appropriate copyright notice, and (2)
# tells the user that there is no warranty for the work (except to the
# extent that warranties are provided), that licensees may convey the
# work under this License, and how to view a copy of this License.  If
# the interface presents a list of user commands or options, such as a
# menu, a prominent item in the list meets this criterion.
# 
#   1. Source Code.
# 
#   The "source code" for a work means the preferred form of the work
# for making modifications to it.  "Object code" means any non-source
# form of a work.
# 
#   A "Standard Interface" means an interface that either is an official
# standard defined by a recognized standards body, or, in the case of
# interfaces specified for a particular programming language, one that
# is widely used among developers working in that language.
# 
#   The "System Libraries" of an executable work include anything, other
# than the work as a whole, that (a) is included in the normal form of
# packaging a Major Component, but which is not part of that Major
# Component, and (b) serves only to enable use of the work with that
# Major Component, or to implement a Standard Interface for which an
# implementation is available to the public in source code form.  A
# "Major Component", in this context, means a major essential component
# (kernel, window system, and so on) of the specific operating system
# (if any) on which the executable work runs, or a compiler used to
# produce the work, or an object code interpreter used to run it.
# 
#   The "Corresponding Source" for a work in object code form means all
# the source code needed to generate, install, and (for an executable
# work) run the object code and to modify the work, including scripts to
# control those activities.  However, it does not include the work's
# System Libraries, or general-purpose tools or generally available free
# programs which are used unmodified in performing those activities but
# which are not part of the work.  For example, Corresponding Source
# includes interface definition files associated with source files for
# the work, and the source code for shared libraries and dynamically
# linked subprograms that the work is specifically designed to require,
# such as by intimate data communication or control flow between those
# subprograms and other parts of the work.
# 
#   The Corresponding Source need not include anything that users
# can regenerate automatically from other parts of the Corresponding
# Source.
# 
#   The Corresponding Source for a work in source code form is that
# same work.
# 
#   2. Basic Permissions.
# 
#   All rights granted under this License are granted for the term of
# copyright on the Program, and are irrevocable provided the stated
# conditions are met.  This License explicitly affirms your unlimited
# permission to run the unmodified Program.  The output from running a
# covered work is covered by this License only if the output, given its
# content, constitutes a covered work.  This License acknowledges your
# rights of fair use or other equivalent, as provided by copyright law.
# 
#   You may make, run and propagate covered works that you do not
# convey, without conditions so long as your license otherwise remains
# in force.  You may convey covered works to others for the sole purpose
# of having them make modifications exclusively for you, or provide you
# with facilities for running those works, provided that you comply with
# the terms of this License in conveying all material for which you do
# not control copyright.  Those thus making or running the covered works
# for you must do so exclusively on your behalf, under your direction
# and control, on terms that prohibit them from making any copies of
# your copyrighted material outside their relationship with you.
# 
#   Conveying under any other circumstances is permitted solely under
# the conditions stated below.  Sublicensing is not allowed; section 10
# makes it unnecessary.
# 
#   3. Protecting Users' Legal Rights From Anti-Circumvention Law.
# 
#   No covered work shall be deemed part of an effective technological
# measure under any applicable law fulfilling obligations under article
# 11 of the WIPO copyright treaty adopted on 20 December 1996, or
# similar laws prohibiting or restricting circumvention of such
# measures.
# 
#   When you convey a covered work, you waive any legal power to forbid
# circumvention of technological measures to the extent such circumvention
# is effected by exercising rights under this License with respect to
# the covered work, and you disclaim any intention to limit operation or
# modification of the work as a means of enforcing, against the work's
# users, your or third parties' legal rights to forbid circumvention of
# technological measures.
# 
#   4. Conveying Verbatim Copies.
# 
#   You may convey verbatim copies of the Program's source code as you
# receive it, in any medium, provided that you conspicuously and
# appropriately publish on each copy an appropriate copyright notice;
# keep intact all notices stating that this License and any
# non-permissive terms added in accord with section 7 apply to the code;
# keep intact all notices of the absence of any warranty; and give all
# recipients a copy of this License along with the Program.
# 
#   You may charge any price or no price for each copy that you convey,
# and you may offer support or warranty protection for a fee.
# 
#   5. Conveying Modified Source Versions.
# 
#   You may convey a work based on the Program, or the modifications to
# produce it from the Program, in the form of source code under the
# terms of section 4, provided that you also meet all of these conditions:
# 
#     a) The work must carry prominent notices stating that you modified
#     it, and giving a relevant date.
# 
#     b) The work must carry prominent notices stating that it is
#     released under this License and any conditions added under section
#     7.  This requirement modifies the requirement in section 4 to
#     "keep intact all notices".
# 
#     c) You must license the entire work, as a whole, under this
#     License to anyone who comes into possession of a copy.  This
#     License will therefore apply, along with any applicable section 7
#     additional terms, to the whole of the work, and all its parts,
#     regardless of how they are packaged.  This License gives no
#     permission to license the work in any other way, but it does not
#     invalidate such permission if you have separately received it.
# 
#     d) If the work has interactive user interfaces, each must display
#     Appropriate Legal Notices; however, if the Program has interactive
#     interfaces that do not display Appropriate Legal Notices, your
#     work need not make them do so.
# 
#   A compilation of a covered work with other separate and independent
# works, which are not by their nature extensions of the covered work,
# and which are not combined with it such as to form a larger program,
# in or on a volume of a storage or distribution medium, is called an
# "aggregate" if the compilation and its resulting copyright are not
# used to limit the access or legal rights of the compilation's users
# beyond what the individual works permit.  Inclusion of a covered work
# in an aggregate does not cause this License to apply to the other
# parts of the aggregate.
# 
#   6. Conveying Non-Source Forms.
# 
#   You may convey a covered work in object code form under the terms
# of sections 4 and 5, provided that you also convey the
# machine-readable Corresponding Source under the terms of this License,
# in one of these ways:
# 
#     a) Convey the object code in, or embodied in, a physical product
#     (including a physical distribution medium), accompanied by the
#     Corresponding Source fixed on a durable physical medium
#     customarily used for software interchange.
# 
#     b) Convey the object code in, or embodied in, a physical product
#     (including a physical distribution medium), accompanied by a
#     written offer, valid for at least three years and valid for as
#     long as you offer spare parts or customer support for that product
#     model, to give anyone who possesses the object code either (1) a
#     copy of the Corresponding Source for all the software in the
#     product that is covered by this License, on a durable physical
#     medium customarily used for software interchange, for a price no
#     more than your reasonable cost of physically performing this
#     conveying of source, or (2) access to copy the
#     Corresponding Source from a network server at no charge.
# 
#     c) Convey individual copies of the object code with a copy of the
#     written offer to provide the Corresponding Source.  This
#     alternative is allowed only occasionally and noncommercially, and
#     only if you received the object code with such an offer, in accord
#     with subsection 6b.
# 
#     d) Convey the object code by offering access from a designated
#     place (gratis or for a charge), and offer equivalent access to the
#     Corresponding Source in the same way through the same place at no
#     further charge.  You need not require recipients to copy the
#     Corresponding Source along with the object code.  If the place to
#     copy the object code is a network server, the Corresponding Source
#     may be on a different server (operated by you or a third party)
#     that supports equivalent copying facilities, provided you maintain
#     clear directions next to the object code saying where to find the
#     Corresponding Source.  Regardless of what server hosts the
#     Corresponding Source, you remain obligated to ensure that it is
#     available for as long as needed to satisfy these requirements.
# 
#     e) Convey the object code using peer-to-peer transmission, provided
#     you inform other peers where the object code and Corresponding
#     Source of the work are being offered to the general public at no
#     charge under subsection 6d.
# 
#   A separable portion of the object code, whose source code is excluded
# from the Corresponding Source as a System Library, need not be
# included in conveying the object code work.
# 
#   A "User Product" is either (1) a "consumer product", which means any
# tangible personal property which is normally used for personal, family,
# or household purposes, or (2) anything designed or sold for incorporation
# into a dwelling.  In determining whether a product is a consumer product,
# doubtful cases shall be resolved in favor of coverage.  For a particular
# product received by a particular user, "normally used" refers to a
# typical or common use of that class of product, regardless of the status
# of the particular user or of the way in which the particular user
# actually uses, or expects or is expected to use, the product.  A product
# is a consumer product regardless of whether the product has substantial
# commercial, industrial or non-consumer uses, unless such uses represent
# the only significant mode of use of the product.
# 
#   "Installation Information" for a User Product means any methods,
# procedures, authorization keys, or other information required to install
# and execute modified versions of a covered work in that User Product from
# a modified version of its Corresponding Source.  The information must
# suffice to ensure that the continued functioning of the modified object
# code is in no case prevented or interfered with solely because
# modification has been made.
# 
#   If you convey an object code work under this section in, or with, or
# specifically for use in, a User Product, and the conveying occurs as
# part of a transaction in which the right of possession and use of the
# User Product is transferred to the recipient in perpetuity or for a
# fixed term (regardless of how the transaction is characterized), the
# Corresponding Source conveyed under this section must be accompanied
# by the Installation Information.  But this requirement does not apply
# if neither you nor any third party retains the ability to install
# modified object code on the User Product (for example, the work has
# been installed in ROM).
# 
#   The requirement to provide Installation Information does not include a
# requirement to continue to provide support service, warranty, or updates
# for a work that has been modified or installed by the recipient, or for
# the User Product in which it has been modified or installed.  Access to a
# network may be denied when the modification itself materially and
# adversely affects the operation of the network or violates the rules and
# protocols for communication across the network.
# 
#   Corresponding Source conveyed, and Installation Information provided,
# in accord with this section must be in a format that is publicly
# documented (and with an implementation available to the public in
# source code form), and must require no special password or key for
# unpacking, reading or copying.
# 
#   7. Additional Terms.
# 
#   "Additional permissions" are terms that supplement the terms of this
# License by making exceptions from one or more of its conditions.
# Additional permissions that are applicable to the entire Program shall
# be treated as though they were included in this License, to the extent
# that they are valid under applicable law.  If additional permissions
# apply only to part of the Program, that part may be used separately
# under those permissions, but the entire Program remains governed by
# this License without regard to the additional permissions.
# 
#   When you convey a copy of a covered work, you may at your option
# remove any additional permissions from that copy, or from any part of
# it.  (Additional permissions may be written to require their own
# removal in certain cases when you modify the work.)  You may place
# additional permissions on material, added by you to a covered work,
# for which you have or can give appropriate copyright permission.
# 
#   Notwithstanding any other provision of this License, for material you
# add to a covered work, you may (if authorized by the copyright holders of
# that material) supplement the terms of this License with terms:
# 
#     a) Disclaiming warranty or limiting liability differently from the
#     terms of sections 15 and 16 of this License; or
# 
#     b) Requiring preservation of specified reasonable legal notices or
#     author attributions in that material or in the Appropriate Legal
#     Notices displayed by works containing it; or
# 
#     c) Prohibiting misrepresentation of the origin of that material, or
#     requiring that modified versions of such material be marked in
#     reasonable ways as different from the original version; or
# 
#     d) Limiting the use for publicity purposes of names of licensors or
#     authors of the material; or
# 
#     e) Declining to grant rights under trademark law for use of some
#     trade names, trademarks, or service marks; or
# 
#     f) Requiring indemnification of licensors and authors of that
#     material by anyone who conveys the material (or modified versions of
#     it) with contractual assumptions of liability to the recipient, for
#     any liability that these contractual assumptions directly impose on
#     those licensors and authors.
# 
#   All other non-permissive additional terms are considered "further
# restrictions" within the meaning of section 10.  If the Program as you
# received it, or any part of it, contains a notice stating that it is
# governed by this License along with a term that is a further
# restriction, you may remove that term.  If a license document contains
# a further restriction but permits relicensing or conveying under this
# License, you may add to a covered work material governed by the terms
# of that license document, provided that the further restriction does
# not survive such relicensing or conveying.
# 
#   If you add terms to a covered work in accord with this section, you
# must place, in the relevant source files, a statement of the
# additional terms that apply to those files, or a notice indicating
# where to find the applicable terms.
# 
#   Additional terms, permissive or non-permissive, may be stated in the
# form of a separately written license, or stated as exceptions;
# the above requirements apply either way.
# 
#   8. Termination.
# 
#   You may not propagate or modify a covered work except as expressly
# provided under this License.  Any attempt otherwise to propagate or
# modify it is void, and will automatically terminate your rights under
# this License (including any patent licenses granted under the third
# paragraph of section 11).
# 
#   However, if you cease all violation of this License, then your
# license from a particular copyright holder is reinstated (a)
# provisionally, unless and until the copyright holder explicitly and
# finally terminates your license, and (b) permanently, if the copyright
# holder fails to notify you of the violation by some reasonable means
# prior to 60 days after the cessation.
# 
#   Moreover, your license from a particular copyright holder is
# reinstated permanently if the copyright holder notifies you of the
# violation by some reasonable means, this is the first time you have
# received notice of violation of this License (for any work) from that
# copyright holder, and you cure the violation prior to 30 days after
# your receipt of the notice.
# 
#   Termination of your rights under this section does not terminate the
# licenses of parties who have received copies or rights from you under
# this License.  If your rights have been terminated and not permanently
# reinstated, you do not qualify to receive new licenses for the same
# material under section 10.
# 
#   9. Acceptance Not Required for Having Copies.
# 
#   You are not required to accept this License in order to receive or
# run a copy of the Program.  Ancillary propagation of a covered work
# occurring solely as a consequence of using peer-to-peer transmission
# to receive a copy likewise does not require acceptance.  However,
# nothing other than this License grants you permission to propagate or
# modify any covered work.  These actions infringe copyright if you do
# not accept this License.  Therefore, by modifying or propagating a
# covered work, you indicate your acceptance of this License to do so.
# 
#   10. Automatic Licensing of Downstream Recipients.
# 
#   Each time you convey a covered work, the recipient automatically
# receives a license from the original licensors, to run, modify and
# propagate that work, subject to this License.  You are not responsible
# for enforcing compliance by third parties with this License.
# 
#   An "entity transaction" is a transaction transferring control of an
# organization, or substantially all assets of one, or subdividing an
# organization, or merging organizations.  If propagation of a covered
# work results from an entity transaction, each party to that
# transaction who receives a copy of the work also receives whatever
# licenses to the work the party's predecessor in interest had or could
# give under the previous paragraph, plus a right to possession of the
# Corresponding Source of the work from the predecessor in interest, if
# the predecessor has it or can get it with reasonable efforts.
# 
#   You may not impose any further restrictions on the exercise of the
# rights granted or affirmed under this License.  For example, you may
# not impose a license fee, royalty, or other charge for exercise of
# rights granted under this License, and you may not initiate litigation
# (including a cross-claim or counterclaim in a lawsuit) alleging that
# any patent claim is infringed by making, using, selling, offering for
# sale, or importing the Program or any portion of it.
# 
#   11. Patents.
# 
#   A "contributor" is a copyright holder who authorizes use under this
# License of the Program or a work on which the Program is based.  The
# work thus licensed is called the contributor's "contributor version".
# 
#   A contributor's "essential patent claims" are all patent claims
# owned or controlled by the contributor, whether already acquired or
# hereafter acquired, that would be infringed by some manner, permitted
# by this License, of making, using, or selling its contributor version,
# but do not include claims that would be infringed only as a
# consequence of further modification of the contributor version.  For
# purposes of this definition, "control" includes the right to grant
# patent sublicenses in a manner consistent with the requirements of
# this License.
# 
#   Each contributor grants you a non-exclusive, worldwide, royalty-free
# patent license under the contributor's essential patent claims, to
# make, use, sell, offer for sale, import and otherwise run, modify and
# propagate the contents of its contributor version.
# 
#   In the following three paragraphs, a "patent license" is any express
# agreement or commitment, however denominated, not to enforce a patent
# (such as an express permission to practice a patent or covenant not to
# sue for patent infringement).  To "grant" such a patent license to a
# party means to make such an agreement or commitment not to enforce a
# patent against the party.
# 
#   If you convey a covered work, knowingly relying on a patent license,
# and the Corresponding Source of the work is not available for anyone
# to copy, free of charge and under the terms of this License, through a
# publicly available network server or other readily accessible means,
# then you must either (1) cause the Corresponding Source to be so
# available, or (2) arrange to deprive yourself of the benefit of the
# patent license for this particular work, or (3) arrange, in a manner
# consistent with the requirements of this License, to extend the patent
# license to downstream recipients.  "Knowingly relying" means you have
# actual knowledge that, but for the patent license, your conveying the
# covered work in a country, or your recipient's use of the covered work
# in a country, would infringe one or more identifiable patents in that
# country that you have reason to believe are valid.
# 
#   If, pursuant to or in connection with a single transaction or
# arrangement, you convey, or propagate by procuring conveyance of, a
# covered work, and grant a patent license to some of the parties
# receiving the covered work authorizing them to use, propagate, modify
# or convey a specific copy of the covered work, then the patent license
# you grant is automatically extended to all recipients of the covered
# work and works based on it.
# 
#   A patent license is "discriminatory" if it does not include within
# the scope of its coverage, prohibits the exercise of, or is
# conditioned on the non-exercise of one or more of the rights that are
# specifically granted under this License.  You may not convey a covered
# work if you are a party to an arrangement with a third party that is
# in the business of distributing software, under which you make payment
# to the third party based on the extent of your activity of conveying
# the work, and under which the third party grants, to any of the
# parties who would receive the covered work from you, a discriminatory
# patent license (a) in connection with copies of the covered work
# conveyed by you (or copies made from those copies), or (b) primarily
# for and in connection with specific products or compilations that
# contain the covered work, unless you entered into that arrangement,
# or that patent license was granted, prior to 28 March 2007.
# 
#   Nothing in this License shall be construed as excluding or limiting
# any implied license or other defenses to infringement that may
# otherwise be available to you under applicable patent law.
# 
#   12. No Surrender of Others' Freedom.
# 
#   If conditions are imposed on you (whether by court order, agreement or
# otherwise) that contradict the conditions of this License, they do not
# excuse you from the conditions of this License.  If you cannot convey a
# covered work so as to satisfy simultaneously your obligations under this
# License and any other pertinent obligations, then as a consequence you may
# not convey it at all.  For example, if you agree to terms that obligate you
# to collect a royalty for further conveying from those to whom you convey
# the Program, the only way you could satisfy both those terms and this
# License would be to refrain entirely from conveying the Program.
# 
#   13. Use with the GNU Affero General Public License.
# 
#   Notwithstanding any other provision of this License, you have
# permission to link or combine any covered work with a work licensed
# under version 3 of the GNU Affero General Public License into a single
# combined work, and to convey the resulting work.  The terms of this
# License will continue to apply to the part which is the covered work,
# but the special requirements of the GNU Affero General Public License,
# section 13, concerning interaction through a network will apply to the
# combination as such.
# 
#   14. Revised Versions of this License.
# 
#   The Free Software Foundation may publish revised and/or new versions of
# the GNU General Public License from time to time.  Such new versions will
# be similar in spirit to the present version, but may differ in detail to
# address new problems or concerns.
# 
#   Each version is given a distinguishing version number.  If the
# Program specifies that a certain numbered version of the GNU General
# Public License "or any later version" applies to it, you have the
# option of following the terms and conditions either of that numbered
# version or of any later version published by the Free Software
# Foundation.  If the Program does not specify a version number of the
# GNU General Public License, you may choose any version ever published
# by the Free Software Foundation.
# 
#   If the Program specifies that a proxy can decide which future
# versions of the GNU General Public License can be used, that proxy's
# public statement of acceptance of a version permanently authorizes you
# to choose that version for the Program.
# 
#   Later license versions may give you additional or different
# permissions.  However, no additional obligations are imposed on any
# author or copyright holder as a result of your choosing to follow a
# later version.
# 
#   15. Disclaimer of Warranty.
# 
#   THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
# APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
# HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
# OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
# IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
# ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
# 
#   16. Limitation of Liability.
# 
#   IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
# WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
# THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
# GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
# USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
# DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
# PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
# EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGES.
# 
#   17. Interpretation of Sections 15 and 16.
# 
#   If the disclaimer of warranty and limitation of liability provided
# above cannot be given local legal effect according to their terms,
# reviewing courts shall apply local law that most closely approximates
# an absolute waiver of all civil liability in connection with the
# Program, unless a warranty or assumption of liability accompanies a
# copy of the Program in return for a fee.
# 
#                      END OF TERMS AND CONDITIONS
# 
#             How to Apply These Terms to Your New Programs
# 
#   If you develop a new program, and you want it to be of the greatest
# possible use to the public, the best way to achieve this is to make it
# free software which everyone can redistribute and change under these terms.
# 
#   To do so, attach the following notices to the program.  It is safest
# to attach them to the start of each source file to most effectively
# state the exclusion of warranty; and each file should have at least
# the "copyright" line and a pointer to where the full notice is found.
# 
#     <one line to give the program's name and a brief idea of what it does.>
#     Copyright (C) <year>  <name of author>
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 
# Also add information on how to contact you by electronic and paper mail.
# 
#   If the program does terminal interaction, make it output a short
# notice like this when it starts in an interactive mode:
# 
#     <program>  Copyright (C) <year>  <name of author>
#     This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#     This is free software, and you are welcome to redistribute it
#     under certain conditions; type `show c' for details.
# 
# The hypothetical commands `show w' and `show c' should show the appropriate
# parts of the General Public License.  Of course, your program's commands
# might be different; for a GUI interface, you would use an "about box".
# 
#   You should also get your employer (if you work as a programmer) or school,
# if any, to sign a "copyright disclaimer" for the program, if necessary.
# For more information on this, and how to apply and follow the GNU GPL, see
# <https://www.gnu.org/licenses/>.
# 
#   The GNU General Public License does not permit incorporating your program
# into proprietary programs.  If your program is a subroutine library, you
# may consider it more useful to permit linking proprietary applications with
# the library.  If this is what you want to do, use the GNU Lesser General
# Public License instead of this License.  But first, please read
# <https://www.gnu.org/licenses/why-not-lgpl.html>.

def menu():
    # new line to seperate instances
    # Copyright and license notice
    print("\n");
    print("Copyright (C) 2022-2023 Daniel Hanrahan");
    print("\n");
    print("This program is free software: you can redistribute it and/or modify it under the terms of the GNU");
    print("General Public License as published by the Free Software Foundation, either version 3 of the License, or");
    print("(at your option) any later version.");
    print("\n");
    print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without");
    print("even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.");
    print("See the GNU General Public License for more details.");
    print("\n");
    print("You should have received a copy of the GNU General Public License along with this program. If not, see");
    print("<https://www.gnu.org/licenses/>.");
    print("\n");
    # type in for what device you want to use and notice for exiting
    strDevice = input("What device do you want to use Raspberry Pi(1), Arduino(2) or exit out of the app(exit): ")
    print("\n");
    # type in for what device you want to use and notice for exiting
    strModPrompt = input("What device do you want to use No Mods(1) or Mods(2): ")
    print("\n");
    
    # when you exit out of app
    if strDevice == "exit":
        # calls exit function
        Exit()
    
    # when you select raspberry pi
    if strDevice == "1":
        # when you select No Mods
        if strModPrompt == "1":
            # calls Raspberry Pi No Mod function
            RaspberryPiNoMod()
        # when you select Mods
        if strModPrompt == "2":
            # calls Raspberry Pi Mod function
            RaspberryPiMod()
        
    # when you select Arduino
    if strDevice == "2":
        # when you select No Mods
        if strModPrompt == "1":
            # calls Arduino No Mod Function
            ArduinoNoMod()
        # when you select Mods
        if strModPrompt == "2":
            # calls Arduino Mod Function
            ArduinoMod()
# exit function
def Exit():
    print("Good Bye");
    exit()

# Raspberry Pi No Mod function
def RaspberryPiNoMod():
    
    import RPi.GPIO as GPIO
    
    # set up the pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)

    pwm = GPIO.PWM(3, 50)
    pwm.start(0)
    
    # notice about files
    print("this can only read .mid files right now, if you can add the ability to read .mxl(sheet music file type), .mod, .xm, .s3m and .it files please add it in here because I cannot find good documentation on reading those files.\n");
    # type in for what directory you want to use
    strDirectory = input("What Directory would you like to use (case sensitive): ")
    
    os.chdir(strDirectory)
    print("\n");
    for file in glob.glob("*.mid"):
        print(file)
    
    # selections
    strSongName = input("Enter Name of the song file exactly as typed on the list: ")

    from mido import MidiFile
    mid = MidiFile(strSongName, clip=True)
    midimsgs = []

    # stores note data in array for chords
    intNote=[]

    # Put all note on/off in midinote as dictionary
    # midi reads in delta time as in time for a note appears before data for the note and if delta time = 0 for 1 note it is playing at the same time as the note before it
    # reads 1 line at a time
    # needs a loop for multiple notes playing quickly back and forth to have it sound like multiple notes are playing at the same time
    for i in mid:
        
        # timing for the song
        start_time = time.time()
        sngTime=0
        sngTime = i.time
        
        # note loop and it allows the app to play chords
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
                
            # note c octave -1
            if 0 in intNote:
                pwm.ChangeDutyCycle(0.78125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave -1
            if 1 in intNote:
                pwm.ChangeDutyCycle(1.5625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave -1
            if 2 in intNote:
                pwm.ChangeDutyCycle(2.34375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave -1
            if 3 in intNote:
                pwm.ChangeDutyCycle(3.125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave -1
            if 4 in intNote:
                pwm.ChangeDutyCycle(3.90625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave -1
            if 5 in intNote:
                pwm.ChangeDutyCycle(4.6875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave -1
            if 6 in intNote:
                pwm.ChangeDutyCycle(5.46875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave -1
            if 7 in intNote:
                pwm.ChangeDutyCycle(6.25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave -1
            if 8 in intNote:
                pwm.ChangeDutyCycle(7.03125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave -1
            if 9 in intNote:
                pwm.ChangeDutyCycle(7.8125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave -1
            if 10 in intNote:
                pwm.ChangeDutyCycle(8.59375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave -1
            if 11 in intNote:
                pwm.ChangeDutyCycle(9.375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 0
            if 12 in intNote:
                pwm.ChangeDutyCycle(10.15625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 0
            if 13 in intNote:
                pwm.ChangeDutyCycle(10.9375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 0
            if 14 in intNote:
                pwm.ChangeDutyCycle(11.71875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 0
            if 15 in intNote:
                pwm.ChangeDutyCycle(12.5)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 0
            if 16 in intNote:
                pwm.ChangeDutyCycle(13.28125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 0
            if 17 in intNote:
                pwm.ChangeDutyCycle(14.0625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 0
            if 18 in intNote:
                pwm.ChangeDutyCycle(14.84375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 0
            if 19 in intNote:
                pwm.ChangeDutyCycle(15.625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 0
            if 20 in intNote:
                pwm.ChangeDutyCycle(16.40625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
            
            # note a octave 0
            if 21 in intNote:
                pwm.ChangeDutyCycle(17.1875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 0
            if 22 in intNote:
                pwm.ChangeDutyCycle(17.96875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 0
            if 23 in intNote:
                pwm.ChangeDutyCycle(18.75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 1
            if 24 in intNote:
                pwm.ChangeDutyCycle(19.53125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 1
            if 25 in intNote:
                pwm.ChangeDutyCycle(20.3125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 1
            if 26 in intNote:
                pwm.ChangeDutyCycle(21.09375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 1
            if 27 in intNote:
                pwm.ChangeDutyCycle(21.875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 1
            if 28 in intNote:
                pwm.ChangeDutyCycle(22.65625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 1
            if 29 in intNote:
                pwm.ChangeDutyCycle(23.4375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 1
            if 30 in intNote:
                pwm.ChangeDutyCycle(24.21875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0) 
                
            # note g octave 1
            if 31 in intNote:
                pwm.ChangeDutyCycle(25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 1
            if 32 in intNote:
                pwm.ChangeDutyCycle(25.78125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 1
            if 33 in intNote:
                pwm.ChangeDutyCycle(26.5625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 1
            if 34 in intNote:
                pwm.ChangeDutyCycle(27.34375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 1
            if 35 in intNote:
                pwm.ChangeDutyCycle(28.125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 2
            if 36 in intNote:
                pwm.ChangeDutyCycle(28.90625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 2
            if 37 in intNote:
                pwm.ChangeDutyCycle(29.6875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 2
            if 38 in intNote:
                pwm.ChangeDutyCycle(30.46875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 2
            if 39 in intNote:
                pwm.ChangeDutyCycle(31.25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 2
            if 40 in intNote:
                pwm.ChangeDutyCycle(32.03125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 2
            if 41 in intNote:
                pwm.ChangeDutyCycle(32.8125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 2
            if 42 in intNote:
                pwm.ChangeDutyCycle(33.59375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 2
            if 43 in intNote:
                pwm.ChangeDutyCycle(34.375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 2
            if 44 in intNote:
                pwm.ChangeDutyCycle(35.15625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 2
            if 45 in intNote:
                pwm.ChangeDutyCycle(35.9375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 2
            if 46 in intNote:
                pwm.ChangeDutyCycle(36.71875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 2
            if 47 in intNote:
                pwm.ChangeDutyCycle(37.5)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 3
            if 48 in intNote:
                pwm.ChangeDutyCycle(38.28125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 3
            if 49 in intNote:
                pwm.ChangeDutyCycle(39.0625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 3
            if 50 in intNote:
                pwm.ChangeDutyCycle(39.84375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 3
            if 51 in intNote:
                pwm.ChangeDutyCycle(40.625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 3
            if 52 in intNote:
                pwm.ChangeDutyCycle(41.40625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 3
            if 53 in intNote:
                pwm.ChangeDutyCycle(42.1875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 3
            if 54 in intNote:
                pwm.ChangeDutyCycle(42.96875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 3
            if 55 in intNote:
                pwm.ChangeDutyCycle(43.75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 3
            if 56 in intNote:
                pwm.ChangeDutyCycle(44.53125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 3
            if 57 in intNote:
                pwm.ChangeDutyCycle(45.3125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 3
            if 58 in intNote:
                pwm.ChangeDutyCycle(46.09375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 3
            if 59 in intNote:
                pwm.ChangeDutyCycle(46.875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 4
            if 60 in intNote:
                pwm.ChangeDutyCycle(47.65625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 4
            if 61 in intNote:
                pwm.ChangeDutyCycle(48.4375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 4
            if 62 in intNote:
                pwm.ChangeDutyCycle(49.21875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 4
            if 63 in intNote:
                pwm.ChangeDutyCycle(50)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 4
            if 64 in intNote:
                pwm.ChangeDutyCycle(50.78125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 4
            if 65 in intNote:
                pwm.ChangeDutyCycle(51.5625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 4
            if 66 in intNote:
                pwm.ChangeDutyCycle(52.34375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 4
            if 67 in intNote:
                pwm.ChangeDutyCycle(53.125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 4
            if 68 in intNote:
                pwm.ChangeDutyCycle(53.90625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 4
            if 69 in intNote:
                pwm.ChangeDutyCycle(54.6875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 4
            if 70 in intNote:
                pwm.ChangeDutyCycle(55.46875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 4
            if 71 in intNote:
                pwm.ChangeDutyCycle(56.25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 5
            if 72 in intNote:
                pwm.ChangeDutyCycle(57.03125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 5
            if 73 in intNote:
                pwm.ChangeDutyCycle(57.8125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 5
            if 74 in intNote:
                pwm.ChangeDutyCycle(58.59375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 5
            if 75 in intNote:
                pwm.ChangeDutyCycle(59.375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 5
            if 76 in intNote:
                pwm.ChangeDutyCycle(60.15625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 5
            if 77 in intNote:
                pwm.ChangeDutyCycle(60.9375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 5
            if 78 in intNote:
                pwm.ChangeDutyCycle(61.71875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 5
            if 79 in intNote:
                pwm.ChangeDutyCycle(62.5)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 5
            if 80 in intNote:
                pwm.ChangeDutyCycle(63.28125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
            
            # note a octave 5
            if 81 in intNote:
                pwm.ChangeDutyCycle(64.0625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 5
            if 82 in intNote:
                pwm.ChangeDutyCycle(64.84375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 5
            if 83 in intNote:
                pwm.ChangeDutyCycle(65.625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 6
            if 84 in intNote:
                pwm.ChangeDutyCycle(66.40625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 6
            if 85 in intNote:
                pwm.ChangeDutyCycle(67.1875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 6
            if 86 in intNote:
                pwm.ChangeDutyCycle(67.96875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 6
            if 87 in intNote:
                pwm.ChangeDutyCycle(68.75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 6
            if 88 in intNote:
                pwm.ChangeDutyCycle(69.53125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 6
            if 89 in intNote:
                pwm.ChangeDutyCycle(70.3125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 6
            if 90 in intNote:
                pwm.ChangeDutyCycle(71.09375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 6
            if 91 in intNote:
                pwm.ChangeDutyCycle(71.875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 6
            if 92 in intNote:
                pwm.ChangeDutyCycle(72.65625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 6
            if 93 in intNote:
                pwm.ChangeDutyCycle(73.4375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 6
            if 94 in intNote:
                pwm.ChangeDutyCycle(74.21875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 6
            if 95 in intNote:
                pwm.ChangeDutyCycle(75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 7
            if 96 in intNote:
                pwm.ChangeDutyCycle(75.78125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 7
            if 97 in intNote:
                pwm.ChangeDutyCycle(76.5625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 7
            if 98 in intNote:
                pwm.ChangeDutyCycle(77.34375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 7
            if 99 in intNote:
                pwm.ChangeDutyCycle(78.125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 7
            if 100 in intNote:
                pwm.ChangeDutyCycle(78.90625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 7
            if 101 in intNote:
                pwm.ChangeDutyCycle(79.6875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 7
            if 102 in intNote:
                pwm.ChangeDutyCycle(80.46875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 7
            if 103 in intNote:
                pwm.ChangeDutyCycle(81.25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 7
            if 104 in intNote:
                pwm.ChangeDutyCycle(82.03125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 7
            if 105 in intNote:
                pwm.ChangeDutyCycle(82.8125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 7
            if 106 in intNote:
                pwm.ChangeDutyCycle(83.59375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 7
            if 107 in intNote:
                pwm.ChangeDutyCycle(84.375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 8
            if 108 in intNote:
                pwm.ChangeDutyCycle(85.15625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 8
            if 109 in intNote:
                pwm.ChangeDutyCycle(85.9375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 8
            if 110 in intNote:
                pwm.ChangeDutyCycle(86.71875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 8
            if 111 in intNote:
                pwm.ChangeDutyCycle(87.5)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 8
            if 112 in intNote:
                pwm.ChangeDutyCycle(88.28125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 8
            if 113 in intNote:
                pwm.ChangeDutyCycle(89.0625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 8
            if 114 in intNote:
                pwm.ChangeDutyCycle(89.84375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 8
            if 115 in intNote:
                pwm.ChangeDutyCycle(90.625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 8
            if 116 in intNote:
                pwm.ChangeDutyCycle(91.40625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 8
            if 117 in intNote:
                pwm.ChangeDutyCycle(92.1875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 8
            if 118 in intNote:
                pwm.ChangeDutyCycle(92.96875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 8
            if 119 in intNote:
                pwm.ChangeDutyCycle(93.75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 9
            if 120 in intNote:
                pwm.ChangeDutyCycle(94.53125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 9
            if 121 in intNote:
                pwm.ChangeDutyCycle(95.3125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 9
            if 122 in intNote:
                pwm.ChangeDutyCycle(96.09375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 9
            if 123 in intNote:
                pwm.ChangeDutyCycle(96.875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 9
            if 124 in intNote:
                pwm.ChangeDutyCycle(97.65625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 9
            if 125 in intNote:
                pwm.ChangeDutyCycle(98.4375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 9
            if 126 in intNote:
                pwm.ChangeDutyCycle(99.21875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 9
            if 127 in intNote:
                pwm.ChangeDutyCycle(100)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
            
            if elapsed_time > sngTime:
                pwm.ChangeDutyCycle(0)
                break

        # makes sure nothing is in time
        if sngTime!=0:
            intNote.clear()
        
        # gets data for the note loop
        if i.type == 'note_on':
            
            # note c octave -1
            if i.note == 0:
                intNote.append(0)
                
            # note c#/d| octave -1
            if i.note == 1:
                intNote.append(1)
                
            # note d octave -1
            if i.note == 2:
                intNote.append(2)
                
            # note d#/e| octave -1
            if i.note == 3:
                intNote.append(3)
                
            # note e octave -1
            if i.note == 4:
                intNote.append(4)
                
            # note f octave -1
            if i.note == 5:
                intNote.append(5)
                
            # note f#/g| octave -1
            if i.note == 6:
                intNote.append(6)
                
            # note g octave -1
            if i.note == 7:
                intNote.append(7)
                
            # note g#/a| octave -1
            if i.note == 8:
                intNote.append(8)
                
            # note a octave -1
            if i.note == 9:
                intNote.append(9)
                
            # note a#/b| octave -1
            if i.note == 10:
                intNote.append(10)
                
            # note b octave -1
            if i.note == 11:
                intNote.append(11)
                
            # note c octave 0
            if i.note == 12:
                intNote.append(12)
                
            # note c#/d| octave 0
            if i.note == 13:
                intNote.append(13)
                
            # note d octave 0
            if i.note == 14:
                intNote.append(14)
                
            # note d#/e| octave 0
            if i.note == 15:
                intNote.append(15)
                
            # note e octave 0
            if i.note == 16:
                intNote.append(16)
                
            # note f octave 0
            if i.note == 17:
                intNote.append(17)
                
            # note f#/g| octave 0
            if i.note == 18:
                intNote.append(18)
                
            # note g octave 0
            if i.note == 19:
                intNote.append(19)
                
            # note g#a| octave 0
            if i.note == 20:
                intNote.append(20)
            
            # note a octave 0
            if i.note == 21:
                intNote.append(21)
                
            # note a#/b| octave 0
            if i.note == 22:
                intNote.append(22)
                
            # note b octave 0
            if i.note == 23:
                intNote.append(23)
                
            # note c octave 1
            if i.note == 24:
                intNote.append(24)
                
            # note c#/d| octave 1
            if i.note == 25:
                intNote.append(25)
                
            # note d octave 1
            if i.note == 26:
                intNote.append(26)
                
            # note d#/e| octave 1
            if i.note == 27:
                intNote.append(27)
                
            # note e octave 1
            if i.note == 28:
                intNote.append(28)
                
            # note f octave 1
            if i.note == 29:
                pintNote.append(29)
                
            # note f#/g| octave 1
            if i.note == 30:
                intNote.append(30)
                
            # note g octave 1
            if i.note == 31:
                intNote.append(31)
                
            # note g#/a| octave 1
            if i.note == 32:
                intNote.append(32)
                
            # note a octave 1
            if i.note == 33:
                intNote.append(33)
                
            # note a#/b| octave 1
            if i.note == 34:
                intNote.append(34)
                
            # note b octave 1
            if i.note == 35:
                intNote.append(35)
                
            # note c octave 2
            if i.note == 36:
                intNote.append(36)
                
            # note c#/d| octave 2
            if i.note == 37:
                intNote.append(37)
                
            # note d octave 2
            if i.note == 38:
                intNote.append(38)
                
            # note d#/e| octave 2
            if i.note == 39:
                intNote.append(39)
                
            # note e octave 2
            if i.note == 40:
                intNote.append(40)
                
            # note f octave 2
            if i.note == 41:
                intNote.append(41)
                
            # note f#/g| octave 2
            if i.note == 42:
                intNote.append(42)
                
            # note g octave 2
            if i.note == 43:
                intNote.append(43)
                
            # note g#/a| octave 2
            if i.note == 44:
                intNote.append(44)
                
            # note a octave 2
            if i.note == 45:
                intNote.append(45)
                
            # note a#/b| octave 2
            if i.note == 46:
                intNote.append(46)
                
            # note b octave 2
            if i.note == 47:
                intNote.append(47)
                
            # note c octave 3
            if i.note == 48:
                intNote.append(48)
                
            # note c#/d| octave 3
            if i.note == 49:
                intNote.append(49)
                
            # note d octave 3
            if i.note == 50:
                intNote.append(50)
                
            # note d#/e| octave 3
            if i.note == 51:
                intNote.append(51)
                
            # note e octave 3
            if i.note == 52:
                intNote.append(52)
                
            # note f octave 3
            if i.note == 53:
                intNote.append(53)
                
            # note f#/g| octave 3
            if i.note == 54:
                intNote.append(54)
                
            # note g octave 3
            if i.note == 55:
                intNote.append(55)
                
            # note g#/a| octave 3
            if i.note == 56:
                intNote.append(56)
                
            # note a octave 3
            if i.note == 57:
                intNote.append(57)
                
            # note a#/b| octave 3
            if i.note == 58:
                intNote.append(58)
                
            # note b octave 3
            if i.note == 59:
                intNote.append(59)
                
            # note c octave 4
            if i.note == 60:
                intNote.append(60)
                
            # note c#/d| octave 4
            if i.note == 61:
                intNote.append(61)
                
            # note d octave 4
            if i.note == 62:
                intNote.append(62)
                
            # note d#/e| octave 4
            if i.note == 63:
                intNote.append(63)
                
            # note e octave 4
            if i.note == 64:
                intNote.append(64)
                
            # note f octave 4
            if i.note == 65:
                intNote.append(65)
                
            # note f#/g| octave 4
            if i.note == 66:
                intNote.append(66)
                
            # note g octave 4
            if i.note == 67:
                intNote.append(67)
                
            # note g#/a| octave 4
            if i.note == 68:
                intNote.append(68)
                
            # note a octave 4
            if i.note == 69:
                intNote.append(69)
                
            # note a#/b| octave 4
            if i.note == 70:
                intNote.append(70)
                
            # note b octave 4
            if i.note == 71:
                intNote.append(71)
                
            # note c octave 5
            if i.note == 72:
                intNote.append(72)
                
            # note c#/d| octave 5
            if i.note == 73:
                intNote.append(73)
                
            # note d octave 5
            if i.note == 74:
                intNote.append(74)
                
            # note d#/e| octave 5
            if i.note == 75:
                intNote.append(75)
                
            # note e octave 5
            if i.note == 76:
                intNote.append(76)
                
            # note f octave 5
            if i.note == 77:
                intNote.append(77)
                
            # note f#/g| octave 5
            if i.note == 78:
                intNote.append(78)
                
            # note g octave 5
            if i.note == 79:
                intNote.append(79)
                
            # note g#/a| octave 5
            if i.note == 80:
                intNote.append(80)
            
            # note a octave 5
            if i.note == 81:
                intNote.append(81)
                
            # note a#/b| octave 5
            if i.note == 82:
                intNote.append(82)
                
            # note b octave 5
            if i.note == 83:
                intNote.append(83)
                
            # note c octave 6
            if i.note == 84:
                intNote.append(84)
                
            # note c#/d| octave 6
            if i.note == 85:
                intNote.append(85)
                
            # note d octave 6
            if i.note == 86:
                intNote.append(86)
                
            # note d#/e| octave 6
            if i.note == 87:
                intNote.append(87)
                
            # note e octave 6
            if i.note == 88:
                intNote.append(88)
                
            # note f octave 6
            if i.note == 89:
                intNote.append(89)
                
            # note f#/g| octave 6
            if i.note == 90:
                intNote.append(90)
                
            # note g octave 6
            if i.note == 91:
                intNote.append(91)
                
            # note g#/a| octave 6
            if i.note == 92:
                intNote.append(92)
                
            # note a octave 6
            if i.note == 93:
                intNote.append(93)
                
            # note a#/b| octave 6
            if i.note == 94:
                intNote.append(94)
                
            # note b octave 6
            if i.note == 95:
                intNote.append(95)
                
            # note c octave 7
            if i.note == 96:
                intNote.append(96)
                
            # note c#/d| octave 7
            if i.note == 97:
                intNote.append(97)
                
            # note d octave 7
            if i.note == 98:
                intNote.append(98)
                
            # note d#/e| octave 7
            if i.note == 99:
                intNote.append(99)
                
            # note e octave 7
            if i.note == 100:
                intNote.append(100)
                
            # note f octave 7
            if i.note == 101:
                intNote.append(101)
                
            # note f#/g| octave 7
            if i.note == 102:
                intNote.append(102)
                
            # note g octave 7
            if i.note == 103:
                intNote.append(103)
                
            # note g#/a| octave 7
            if i.note == 104:
                intNote.append(104)
                
            # note a octave 7
            if i.note == 105:
                intNote.append(105)
                
            # note a#/b| octave 7
            if i.note == 106:
                intNote.append(106)
                
            # note b octave 7
            if i.note == 107:
                intNote.append(107)
                
            # note c octave 8
            if i.note == 108:
                intNote.append(108)
                
            # note c#/d| octave 8
            if i.note == 109:
                intNote.append(109)
                
            # note d octave 8
            if i.note == 110:
                intNote.append(110)
                
            # note d#/e| octave 8
            if i.note == 111:
                intNote.append(111)
                
            # note e octave 8
            if i.note == 112:
                intNote.append(112)
                
            # note f octave 8
            if i.note == 113:
                intNote.append(113)
                
            # note f#/g| octave 8
            if i.note == 114:
                intNote.append(114)
                
            # note g octave 8
            if i.note == 115:
                intNote.append(115)
                
            # note g#/a| octave 8
            if i.note == 116:
                intNote.append(116)
            
            # note a octave 8
            if i.note == 117:
                intNote.append(117)
                
            # note a#/b| octave 8
            if i.note == 118:
                intNote.append(118)
                
            # note b octave 8
            if i.note == 119:
                intNote.append(119)
                
            # note c octave 9
            if i.note == 120:
                intNote.append(120)
                
            # note c#/d| octave 9
            if i.note == 121:
                intNote.append(121)
                
            # note d octave 9
            if i.note == 122:
                intNote.append(122)
                
            # note d#/e| octave 9
            if i.note == 123:
                intNote.append(123)
                
            # note e octave 9
            if i.note == 124:
                intNote.append(124)
                
            # note f octave 9
            if i.note == 125:
                intNote.append(125)
                
            # note f#/g| octave 9
            if i.note == 126:
                intNote.append(126)
                
            # note g octave 9
            if i.note == 127:
                intNote.append(127)
            
        elif i.type == 'end_of_track':
            print("Good Bye");
            exit() # exits after song is done
    
# Arduino No Mod function
def ArduinoNoMod():

    import serial

    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");

    # calls the Arduino druver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600)
    
    # notice about files
    print("this can only read .mid files right now, if you can add the ability to read .mxl(sheet music file type), .mod, .xm, .s3m and .it files please add it in here because I cannot find good documentation on reading those files.\n");
    # type in for what directory you want to use
    strDirectory = input("What Directory would you like to use (case sensitive): ")
    
    os.chdir(strDirectory)
    print("\n");
    for file in glob.glob("*.mid"):
        print(file)
    
    # selections
    strSongName = input("Enter Name of the song file exactly as typed on the list: ")

    from mido import MidiFile
    mid = MidiFile(strSongName, clip=True)
    midimsgs = []

    # stores note data in array for chords
    intNote=[]

    # Put all note on/off in midinote as dictionary
    # midi reads in delta time as in time for a note appears before data for the note and if delta time = 0 for 1 note it is playing at the same time as the note before it
    # reads 1 line at a time
    # needs a loop for multiple notes playing quickly back and forth to have it sound like multiple notes are playing at the same time
    for i in mid:
        
        # timing for the song
        start_time = time.time()
        sngTime=0
        sngTime = i.time
        
        # note loop and it allows the app to play chords
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
                
            # note c octave -1
            if 0 in intNote:
                arduinoDriver.write("1".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave -1
            if 1 in intNote:
                arduinoDriver.write("2".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave -1
            if 2 in intNote:
                arduinoDriver.write("3".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave -1
            if 3 in intNote:
                arduinoDriver.write("4".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave -1
            if 4 in intNote:
                arduinoDriver.write("5".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave -1
            if 5 in intNote:
                arduinoDriver.write("6".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave -1
            if 6 in intNote:
                arduinoDriver.write("7".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave -1
            if 7 in intNote:
                arduinoDriver.write("8".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave -1
            if 8 in intNote:
                arduinoDriver.write("9".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave -1
            if 9 in intNote:
                arduinoDriver.write("10".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave -1
            if 10 in intNote:
                arduinoDriver.write("11".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave -1
            if 11 in intNote:
                arduinoDriver.write("12".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 0
            if 12 in intNote:
                arduinoDriver.write("13".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 0
            if 13 in intNote:
                arduinoDriver.write("14".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 0
            if 14 in intNote:
                arduinoDriver.write("15".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 0
            if 15 in intNote:
                arduinoDriver.write("16".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 0
            if 16 in intNote:
                arduinoDriver.write("17".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 0
            if 17 in intNote:
                arduinoDriver.write("18".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 0
            if 18 in intNote:
                arduinoDriver.write("19".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 0
            if 19 in intNote:
                arduinoDriver.write("20".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 0
            if 20 in intNote:
                arduinoDriver.write("21".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
            
            # note a octave 0
            if 21 in intNote:
                arduinoDriver.write("22".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 0
            if 22 in intNote:
                arduinoDriver.write("23".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 0
            if 23 in intNote:
                arduinoDriver.write("24".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 1
            if 24 in intNote:
                arduinoDriver.write("25".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 1
            if 25 in intNote:
                arduinoDriver.write("26".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 1
            if 26 in intNote:
                arduinoDriver.write("27".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 1
            if 27 in intNote:
                arduinoDriver.write("28".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 1
            if 28 in intNote:
                arduinoDriver.write("29".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 1
            if 29 in intNote:
                arduinoDriver.write("30".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 1
            if 30 in intNote:
                arduinoDriver.write("31".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 1
            if 31 in intNote:
                arduinoDriver.write("32".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 1
            if 32 in intNote:
                arduinoDriver.write("33".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 1
            if 33 in intNote:
                arduinoDriver.write("34".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 1
            if 34 in intNote:
                arduinoDriver.write("35".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 1
            if 35 in intNote:
                arduinoDriver.write("36".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 2
            if 36 in intNote:
                arduinoDriver.write("37".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 2
            if 37 in intNote:
                arduinoDriver.write("38".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 2
            if 38 in intNote:
                arduinoDriver.write("39".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 2
            if 39 in intNote:
                arduinoDriver.write("40".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 2
            if 40 in intNote:
                arduinoDriver.write("41".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 2
            if 41 in intNote:
                arduinoDriver.write("42".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 2
            if 42 in intNote:
                arduinoDriver.write("43".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 2
            if 43 in intNote:
                arduinoDriver.write("44".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 2
            if 44 in intNote:
                arduinoDriver.write("45".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 2
            if 45 in intNote:
                arduinoDriver.write("46".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 2
            if 46 in intNote:
                arduinoDriver.write("47".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 2
            if 47 in intNote:
                arduinoDriver.write("48".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 3
            if 48 in intNote:
                arduinoDriver.write("49".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 3
            if 49 in intNote:
                arduinoDriver.write("50".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 3
            if 50 in intNote:
                arduinoDriver.write("51".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 3
            if 51 in intNote:
                arduinoDriver.write("52".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 3
            if 52 in intNote:
                arduinoDriver.write("53".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 3
            if 53 in intNote:
                arduinoDriver.write("54".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 3
            if 54 in intNote:
                arduinoDriver.write("55".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 3
            if 55 in intNote:
                arduinoDriver.write("56".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 3
            if 56 in intNote:
                arduinoDriver.write("57".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 3
            if 57 in intNote:
                arduinoDriver.write("58".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 3
            if 58 in intNote:
                arduinoDriver.write("59".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 3
            if 59 in intNote:
                arduinoDriver.write("60".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 4
            if 60 in intNote:
                arduinoDriver.write("61".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 4
            if 61 in intNote:
                arduinoDriver.write("62".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 4
            if 62 in intNote:
                arduinoDriver.write("63".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 4
            if 63 in intNote:
                arduinoDriver.write("64".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 4
            if 64 in intNote:
                arduinoDriver.write("65".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 4
            if 65 in intNote:
                arduinoDriver.write("66".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 4
            if 66 in intNote:
                arduinoDriver.write("67".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 4
            if 67 in intNote:
                arduinoDriver.write("68".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 4
            if 68 in intNote:
                arduinoDriver.write("69".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 4
            if 69 in intNote:
                arduinoDriver.write("70".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 4
            if 70 in intNote:
                arduinoDriver.write("71".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 4
            if 71 in intNote:
                arduinoDriver.write("72".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 5
            if 72 in intNote:
                arduinoDriver.write("73".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 5
            if 73 in intNote:
                arduinoDriver.write("74".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 5
            if 74 in intNote:
                arduinoDriver.write("75".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 5
            if 75 in intNote:
                arduinoDriver.write("76".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 5
            if 76 in intNote:
                arduinoDriver.write("77".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 5
            if 77 in intNote:
                arduinoDriver.write("78".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 5
            if 78 in intNote:
                arduinoDriver.write("79".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 5
            if 79 in intNote:
                arduinoDriver.write("80".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 5
            if 80 in intNote:
                arduinoDriver.write("81".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
            
            # note a octave 5
            if 81 in intNote:
                arduinoDriver.write("82".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 5
            if 82 in intNote:
                arduinoDriver.write("83".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 5
            if 83 in intNote:
                arduinoDriver.write("84".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 6
            if 84 in intNote:
                arduinoDriver.write("85".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 6
            if 85 in intNote:
                arduinoDriver.write("86".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 6
            if 86 in intNote:
                arduinoDriver.write("87".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 6
            if 87 in intNote:
                arduinoDriver.write("88".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 6
            if 88 in intNote:
                arduinoDriver.write("89".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 6
            if 89 in intNote:
                arduinoDriver.write("90".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 6
            if 90 in intNote:
                arduinoDriver.write("91".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 6
            if 91 in intNote:
                arduinoDriver.write("92".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 6
            if 92 in intNote:
                arduinoDriver.write("93".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 6
            if 93 in intNote:
                arduinoDriver.write("94".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 6
            if 94 in intNote:
                arduinoDriver.write("95".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 6
            if 95 in intNote:
                arduinoDriver.write("96".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 7
            if 96 in intNote:
                arduinoDriver.write("97".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 7
            if 97 in intNote:
                arduinoDriver.write("98".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 7
            if 98 in intNote:
                arduinoDriver.write("99".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 7
            if 99 in intNote:
                arduinoDriver.write("100".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 7
            if 100 in intNote:
                arduinoDriver.write("101".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 7
            if 101 in intNote:
                arduinoDriver.write("102".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 7
            if 102 in intNote:
                arduinoDriver.write("103".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 7
            if 103 in intNote:
                arduinoDriver.write("104".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 7
            if 104 in intNote:
                arduinoDriver.write("105".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 7
            if 105 in intNote:
                arduinoDriver.write("106".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 7
            if 106 in intNote:
                arduinoDriver.write("107".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 7
            if 107 in intNote:
                arduinoDriver.write("108".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 8
            if 108 in intNote:
                arduinoDriver.write("109".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 8
            if 109 in intNote:
                arduinoDriver.write("110".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 8
            if 110 in intNote:
                arduinoDriver.write("111".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 8
            if 111 in intNote:
                arduinoDriver.write("112".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 8
            if 112 in intNote:
                arduinoDriver.write("113".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 8
            if 113 in intNote:
                arduinoDriver.write("114".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 8
            if 114 in intNote:
                arduinoDriver.write("115".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 8
            if 115 in intNote:
                arduinoDriver.write("116".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 8
            if 116 in intNote:
                arduinoDriver.write("117".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 8
            if 117 in intNote:
                arduinoDriver.write("118".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 8
            if 118 in intNote:
                arduinoDriver.write("119".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 8
            if 119 in intNote:
                arduinoDriver.write("120".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 9
            if 120 in intNote:
                arduinoDriver.write("121".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 9
            if 121 in intNote:
                arduinoDriver.write("122".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 9
            if 122 in intNote:
                arduinoDriver.write("123".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 9
            if 123 in intNote:
                arduinoDriver.write("124".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 9
            if 124 in intNote:
                arduinoDriver.write("125".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 9
            if 125 in intNote:
                arduinoDriver.write("126".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 9
            if 126 in intNote:
                arduinoDriver.write("127".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 9
            if 127 in intNote:
                arduinoDriver.write("128".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
            
            if elapsed_time > sngTime:
                arduinoDriver.write("0".encode())
                break

        # makes sure nothing is in time
        if sngTime!=0:
            intNote.clear()
        
        # gets data for the note loop
        if i.type == 'note_on':
            
            # note c octave -1
            if i.note == 0:
                intNote.append(0)
                
            # note c#/d| octave -1
            if i.note == 1:
                intNote.append(1)
                
            # note d octave -1
            if i.note == 2:
                intNote.append(2)
                
            # note d#/e| octave -1
            if i.note == 3:
                intNote.append(3)
                
            # note e octave -1
            if i.note == 4:
                intNote.append(4)
                
            # note f octave -1
            if i.note == 5:
                intNote.append(5)
                
            # note f#/g| octave -1
            if i.note == 6:
                intNote.append(6)
                
            # note g octave -1
            if i.note == 7:
                intNote.append(7)
                
            # note g#/a| octave -1
            if i.note == 8:
                intNote.append(8)
                
            # note a octave -1
            if i.note == 9:
                intNote.append(9)
                
            # note a#/b| octave -1
            if i.note == 10:
                intNote.append(10)
                
            # note b octave -1
            if i.note == 11:
                intNote.append(11)
                
            # note c octave 0
            if i.note == 12:
                intNote.append(12)
                
            # note c#/d| octave 0
            if i.note == 13:
                intNote.append(13)
                
            # note d octave 0
            if i.note == 14:
                intNote.append(14)
                
            # note d#/e| octave 0
            if i.note == 15:
                intNote.append(15)
                
            # note e octave 0
            if i.note == 16:
                intNote.append(16)
                
            # note f octave 0
            if i.note == 17:
                intNote.append(17)
                
            # note f#/g| octave 0
            if i.note == 18:
                intNote.append(18)
                
            # note g octave 0
            if i.note == 19:
                intNote.append(19)
                
            # note g#a| octave 0
            if i.note == 20:
                intNote.append(20)
            
            # note a octave 0
            if i.note == 21:
                intNote.append(21)
                
            # note a#/b| octave 0
            if i.note == 22:
                intNote.append(22)
                
            # note b octave 0
            if i.note == 23:
                intNote.append(23)
                
            # note c octave 1
            if i.note == 24:
                intNote.append(24)
                
            # note c#/d| octave 1
            if i.note == 25:
                intNote.append(25)
                
            # note d octave 1
            if i.note == 26:
                intNote.append(26)
                
            # note d#/e| octave 1
            if i.note == 27:
                intNote.append(27)
                
            # note e octave 1
            if i.note == 28:
                intNote.append(28)
                
            # note f octave 1
            if i.note == 29:
                pintNote.append(29)
                
            # note f#/g| octave 1
            if i.note == 30:
                intNote.append(30)
                
            # note g octave 1
            if i.note == 31:
                intNote.append(31)
                
            # note g#/a| octave 1
            if i.note == 32:
                intNote.append(32)
                
            # note a octave 1
            if i.note == 33:
                intNote.append(33)
                
            # note a#/b| octave 1
            if i.note == 34:
                intNote.append(34)
                
            # note b octave 1
            if i.note == 35:
                intNote.append(35)
                
            # note c octave 2
            if i.note == 36:
                intNote.append(36)
                
            # note c#/d| octave 2
            if i.note == 37:
                intNote.append(37)
                
            # note d octave 2
            if i.note == 38:
                intNote.append(38)
                
            # note d#/e| octave 2
            if i.note == 39:
                intNote.append(39)
                
            # note e octave 2
            if i.note == 40:
                intNote.append(40)
                
            # note f octave 2
            if i.note == 41:
                intNote.append(41)
                
            # note f#/g| octave 2
            if i.note == 42:
                intNote.append(42)
                
            # note g octave 2
            if i.note == 43:
                intNote.append(43)
                
            # note g#/a| octave 2
            if i.note == 44:
                intNote.append(44)
                
            # note a octave 2
            if i.note == 45:
                intNote.append(45)
                
            # note a#/b| octave 2
            if i.note == 46:
                intNote.append(46)
                
            # note b octave 2
            if i.note == 47:
                intNote.append(47)
                
            # note c octave 3
            if i.note == 48:
                intNote.append(48)
                
            # note c#/d| octave 3
            if i.note == 49:
                intNote.append(49)
                
            # note d octave 3
            if i.note == 50:
                intNote.append(50)
                
            # note d#/e| octave 3
            if i.note == 51:
                intNote.append(51)
                
            # note e octave 3
            if i.note == 52:
                intNote.append(52)
                
            # note f octave 3
            if i.note == 53:
                intNote.append(53)
                
            # note f#/g| octave 3
            if i.note == 54:
                intNote.append(54)
                
            # note g octave 3
            if i.note == 55:
                intNote.append(55)
                
            # note g#/a| octave 3
            if i.note == 56:
                intNote.append(56)
                
            # note a octave 3
            if i.note == 57:
                intNote.append(57)
                
            # note a#/b| octave 3
            if i.note == 58:
                intNote.append(58)
                
            # note b octave 3
            if i.note == 59:
                intNote.append(59)
                
            # note c octave 4
            if i.note == 60:
                intNote.append(60)
                
            # note c#/d| octave 4
            if i.note == 61:
                intNote.append(61)
                
            # note d octave 4
            if i.note == 62:
                intNote.append(62)
                
            # note d#/e| octave 4
            if i.note == 63:
                intNote.append(63)
                
            # note e octave 4
            if i.note == 64:
                intNote.append(64)
                
            # note f octave 4
            if i.note == 65:
                intNote.append(65)
                
            # note f#/g| octave 4
            if i.note == 66:
                intNote.append(66)
                
            # note g octave 4
            if i.note == 67:
                intNote.append(67)
                
            # note g#/a| octave 4
            if i.note == 68:
                intNote.append(68)
                
            # note a octave 4
            if i.note == 69:
                intNote.append(69)
                
            # note a#/b| octave 4
            if i.note == 70:
                intNote.append(70)
                
            # note b octave 4
            if i.note == 71:
                intNote.append(71)
                
            # note c octave 5
            if i.note == 72:
                intNote.append(72)
                
            # note c#/d| octave 5
            if i.note == 73:
                intNote.append(73)
                
            # note d octave 5
            if i.note == 74:
                intNote.append(74)
                
            # note d#/e| octave 5
            if i.note == 75:
                intNote.append(75)
                
            # note e octave 5
            if i.note == 76:
                intNote.append(76)
                
            # note f octave 5
            if i.note == 77:
                intNote.append(77)
                
            # note f#/g| octave 5
            if i.note == 78:
                intNote.append(78)
                
            # note g octave 5
            if i.note == 79:
                intNote.append(79)
                
            # note g#/a| octave 5
            if i.note == 80:
                intNote.append(80)
            
            # note a octave 5
            if i.note == 81:
                intNote.append(81)
                
            # note a#/b| octave 5
            if i.note == 82:
                intNote.append(82)
                
            # note b octave 5
            if i.note == 83:
                intNote.append(83)
                
            # note c octave 6
            if i.note == 84:
                intNote.append(84)
                
            # note c#/d| octave 6
            if i.note == 85:
                intNote.append(85)
                
            # note d octave 6
            if i.note == 86:
                intNote.append(86)
                
            # note d#/e| octave 6
            if i.note == 87:
                intNote.append(87)
                
            # note e octave 6
            if i.note == 88:
                intNote.append(88)
                
            # note f octave 6
            if i.note == 89:
                intNote.append(89)
                
            # note f#/g| octave 6
            if i.note == 90:
                intNote.append(90)
                
            # note g octave 6
            if i.note == 91:
                intNote.append(91)
                
            # note g#/a| octave 6
            if i.note == 92:
                intNote.append(92)
                
            # note a octave 6
            if i.note == 93:
                intNote.append(93)
                
            # note a#/b| octave 6
            if i.note == 94:
                intNote.append(94)
                
            # note b octave 6
            if i.note == 95:
                intNote.append(95)
                
            # note c octave 7
            if i.note == 96:
                intNote.append(96)
                
            # note c#/d| octave 7
            if i.note == 97:
                intNote.append(97)
                
            # note d octave 7
            if i.note == 98:
                intNote.append(98)
                
            # note d#/e| octave 7
            if i.note == 99:
                intNote.append(99)
                
            # note e octave 7
            if i.note == 100:
                intNote.append(100)
                
            # note f octave 7
            if i.note == 101:
                intNote.append(101)
                
            # note f#/g| octave 7
            if i.note == 102:
                intNote.append(102)
                
            # note g octave 7
            if i.note == 103:
                intNote.append(103)
                
            # note g#/a| octave 7
            if i.note == 104:
                intNote.append(104)
                
            # note a octave 7
            if i.note == 105:
                intNote.append(105)
                
            # note a#/b| octave 7
            if i.note == 106:
                intNote.append(106)
                
            # note b octave 7
            if i.note == 107:
                intNote.append(107)
                
            # note c octave 8
            if i.note == 108:
                intNote.append(108)
                
            # note c#/d| octave 8
            if i.note == 109:
                intNote.append(109)
                
            # note d octave 8
            if i.note == 110:
                intNote.append(110)
                
            # note d#/e| octave 8
            if i.note == 111:
                intNote.append(111)
                
            # note e octave 8
            if i.note == 112:
                intNote.append(112)
                
            # note f octave 8
            if i.note == 113:
                intNote.append(113)
                
            # note f#/g| octave 8
            if i.note == 114:
                intNote.append(114)
                
            # note g octave 8
            if i.note == 115:
                intNote.append(115)
                
            # note g#/a| octave 8
            if i.note == 116:
                intNote.append(116)
            
            # note a octave 8
            if i.note == 117:
                intNote.append(117)
                
            # note a#/b| octave 8
            if i.note == 118:
                intNote.append(118)
                
            # note b octave 8
            if i.note == 119:
                intNote.append(119)
                
            # note c octave 9
            if i.note == 120:
                intNote.append(120)
                
            # note c#/d| octave 9
            if i.note == 121:
                intNote.append(121)
                
            # note d octave 9
            if i.note == 122:
                intNote.append(122)
                
            # note d#/e| octave 9
            if i.note == 123:
                intNote.append(123)
                
            # note e octave 9
            if i.note == 124:
                intNote.append(124)
                
            # note f octave 9
            if i.note == 125:
                intNote.append(125)
                
            # note f#/g| octave 9
            if i.note == 126:
                intNote.append(126)
                
            # note g octave 9
            if i.note == 127:
                intNote.append(127)
            
        elif i.type == 'end_of_track':
            print("Good Bye");
            arduinoDriver.write("0".encode())
            exit() # exits after song is done

# Raspberry Pi Mod function
def RaspberryPiMod():
    
    import RPi.GPIO as GPIO
    
    # set up the pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)

    pwm = GPIO.PWM(3, 50)
    pwm.start(0)
    
    # library for mods and process vm call needed for mods
    from lupa import LuaRuntime
    lua = LuaRuntime()

    # The mod file must be in your home directory and must be called note_data_to_instrument_mod.lua
    lua.execute(r'''dofile("note_data_to_instrument_mod.lua")''')
    
    # get the mod global envirorment
    globals = lua.globals()
    
    # Mod Notice and Name
    strModNoticeAndName = lua.globals().strNoticeAndName
    print(strModNoticeAndName)
    
    # results from each mod function
    resultNote0 = globals.Note0()
    resultNote1 = globals.Note1()
    resultNote2 = globals.Note2()
    resultNote3 = globals.Note3()
    resultNote4 = globals.Note4()
    resultNote5 = globals.Note5()
    resultNote6 = globals.Note6()
    resultNote7 = globals.Note7()
    resultNote8 = globals.Note8()
    resultNote9 = globals.Note9()
    resultNote10 = globals.Note10()
    resultNote11 = globals.Note11()
    resultNote12 = globals.Note12()
    resultNote13 = globals.Note13()
    resultNote14 = globals.Note14()
    resultNote15 = globals.Note15()
    resultNote16 = globals.Note16()
    resultNote17 = globals.Note17()
    resultNote18 = globals.Note18()
    resultNote19 = globals.Note19()
    resultNote20 = globals.Note20()
    resultNote21 = globals.Note21()
    resultNote22 = globals.Note22()
    resultNote23 = globals.Note23()
    resultNote24 = globals.Note24()
    resultNote25 = globals.Note25()
    resultNote26 = globals.Note26()
    resultNote27 = globals.Note27()
    resultNote28 = globals.Note28()
    resultNote29 = globals.Note29()
    resultNote30 = globals.Note30()
    resultNote31 = globals.Note31()
    resultNote32 = globals.Note32()
    resultNote33 = globals.Note33()
    resultNote34 = globals.Note34()
    resultNote35 = globals.Note35()
    resultNote36 = globals.Note36()
    resultNote37 = globals.Note37()
    resultNote38 = globals.Note38()
    resultNote39 = globals.Note39()
    resultNote40 = globals.Note40()
    resultNote41 = globals.Note41()
    resultNote42 = globals.Note42()
    resultNote43 = globals.Note43()
    resultNote44 = globals.Note44()
    resultNote45 = globals.Note45()
    resultNote46 = globals.Note46()
    resultNote47 = globals.Note47()
    resultNote48 = globals.Note48()
    resultNote49 = globals.Note49()
    resultNote50 = globals.Note50()
    resultNote51 = globals.Note51()
    resultNote52 = globals.Note52()
    resultNote53 = globals.Note53()
    resultNote54 = globals.Note54()
    resultNote55 = globals.Note55()
    resultNote56 = globals.Note56()
    resultNote57 = globals.Note57()
    resultNote58 = globals.Note58()
    resultNote59 = globals.Note59()
    resultNote60 = globals.Note60()
    resultNote61 = globals.Note61()
    resultNote62 = globals.Note62()
    resultNote63 = globals.Note63()
    resultNote64 = globals.Note64()
    resultNote65 = globals.Note65()
    resultNote66 = globals.Note66()
    resultNote67 = globals.Note67()
    resultNote68 = globals.Note68()
    resultNote69 = globals.Note69()
    resultNote70 = globals.Note70()
    resultNote71 = globals.Note71()
    resultNote72 = globals.Note72()
    resultNote73 = globals.Note73()
    resultNote74 = globals.Note74()
    resultNote75 = globals.Note75()
    resultNote76 = globals.Note76()
    resultNote77 = globals.Note77()
    resultNote78 = globals.Note78()
    resultNote79 = globals.Note79()
    resultNote80 = globals.Note80()
    resultNote81 = globals.Note81()
    resultNote82 = globals.Note82()
    resultNote83 = globals.Note83()
    resultNote84 = globals.Note84()
    resultNote85 = globals.Note85()
    resultNote86 = globals.Note86()
    resultNote87 = globals.Note87()
    resultNote88 = globals.Note88()
    resultNote89 = globals.Note89()
    resultNote90 = globals.Note90()
    resultNote91 = globals.Note91()
    resultNote92 = globals.Note92()
    resultNote93 = globals.Note93()
    resultNote94 = globals.Note94()
    resultNote95 = globals.Note95()
    resultNote96 = globals.Note96()
    resultNote97 = globals.Note97()
    resultNote98 = globals.Note98()
    resultNote99 = globals.Note99()
    resultNote100 = globals.Note100()
    resultNote101 = globals.Note101()
    resultNote102 = globals.Note102()
    resultNote103 = globals.Note103()
    resultNote104 = globals.Note104()
    resultNote105 = globals.Note105()
    resultNote106 = globals.Note106()
    resultNote107 = globals.Note107()
    resultNote108 = globals.Note108()
    resultNote109 = globals.Note109()
    resultNote110 = globals.Note110()
    resultNote111 = globals.Note111()
    resultNote112 = globals.Note112()
    resultNote113 = globals.Note113()
    resultNote114 = globals.Note114()
    resultNote115 = globals.Note115()
    resultNote116 = globals.Note116()
    resultNote117 = globals.Note117()
    resultNote118 = globals.Note118()
    resultNote119 = globals.Note119()
    resultNote120 = globals.Note120()
    resultNote121 = globals.Note121()
    resultNote122 = globals.Note122()
    resultNote123 = globals.Note123()
    resultNote124 = globals.Note124()
    resultNote125 = globals.Note125()
    resultNote126 = globals.Note126()
    resultNote127 = globals.Note127()
    
    # notice about files
    print("this can only read .mid files right now for songs, if you can add the ability to read .mxl(sheet music file type), .mod, .xm, .s3m and .it files please add it in here because I cannot find good documentation on reading those files.\n");
    # type in for what directory you want to use
    strDirectory = input("What Directory would you like to use for songs(case sensitive): ")
    
    os.chdir(strDirectory)
    print("\n");
    for file in glob.glob("*.mid"):
        print(file)
    
    # selections for songs
    strSongName = input("Enter Name of the song file exactly as typed on the list: ")

    from mido import MidiFile
    mid = MidiFile(strSongName, clip=True)
    midimsgs = []

    # stores note data in array for chords
    intNote=[]

    # Put all note on/off in midinote as dictionary
    # midi reads in delta time as in time for a note appears before data for the note and if delta time = 0 for 1 note it is playing at the same time as the note before it
    # reads 1 line at a time
    # needs a loop for multiple notes playing quickly back and forth to have it sound like multiple notes are playing at the same time
    for i in mid:
        
        # timing for the song
        start_time = time.time()
        sngTime=0
        sngTime = i.time
        
        # note loop and it allows the app to play chords
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
                
            # note c octave -1
            if 0 in intNote:
                print(resultNote0);
                pwm.ChangeDutyCycle(0.78125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave -1
            if 1 in intNote:
                print(resultNote1);
                pwm.ChangeDutyCycle(1.5625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave -1
            if 2 in intNote:
                print(resultNote2);
                pwm.ChangeDutyCycle(2.34375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave -1
            if 3 in intNote:
                print(resultNote3);
                pwm.ChangeDutyCycle(3.125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave -1
            if 4 in intNote:
                print(resultNote4);
                pwm.ChangeDutyCycle(3.90625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave -1
            if 5 in intNote:
                print(resultNote5);
                pwm.ChangeDutyCycle(4.6875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave -1
            if 6 in intNote:
                print(resultNote6);
                pwm.ChangeDutyCycle(5.46875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave -1
            if 7 in intNote:
                print(resultNote7);
                pwm.ChangeDutyCycle(6.25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave -1
            if 8 in intNote:
                print(resultNote8);
                pwm.ChangeDutyCycle(7.03125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave -1
            if 9 in intNote:
                print(resultNote9);
                pwm.ChangeDutyCycle(7.8125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave -1
            if 10 in intNote:
                print(resultNote10);
                pwm.ChangeDutyCycle(8.59375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave -1
            if 11 in intNote:
                print(resultNote11);
                pwm.ChangeDutyCycle(9.375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 0
            if 12 in intNote:
                print(resultNote12);
                pwm.ChangeDutyCycle(10.15625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 0
            if 13 in intNote:
                print(resultNote13);
                pwm.ChangeDutyCycle(10.9375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 0
            if 14 in intNote:
                print(resultNote14);
                pwm.ChangeDutyCycle(11.71875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 0
            if 15 in intNote:
                print(resultNote15);
                pwm.ChangeDutyCycle(12.5)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 0
            if 16 in intNote:
                print(resultNote16);
                pwm.ChangeDutyCycle(13.28125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 0
            if 17 in intNote:
                print(resultNote17);
                pwm.ChangeDutyCycle(14.0625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 0
            if 18 in intNote:
                print(resultNote18);
                pwm.ChangeDutyCycle(14.84375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 0
            if 19 in intNote:
                print(resultNote19);
                pwm.ChangeDutyCycle(15.625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 0
            if 20 in intNote:
                print(resultNote20);
                pwm.ChangeDutyCycle(16.40625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
            
            # note a octave 0
            if 21 in intNote:
                print(resultNote21);
                pwm.ChangeDutyCycle(17.1875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 0
            if 22 in intNote:
                print(resultNote22);
                pwm.ChangeDutyCycle(17.96875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 0
            if 23 in intNote:
                print(resultNote23);
                pwm.ChangeDutyCycle(18.75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 1
            if 24 in intNote:
                print(resultNote24);
                pwm.ChangeDutyCycle(19.53125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 1
            if 25 in intNote:
                print(resultNote25);
                pwm.ChangeDutyCycle(20.3125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 1
            if 26 in intNote:
                print(resultNote26);
                pwm.ChangeDutyCycle(21.09375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 1
            if 27 in intNote:
                print(resultNote27);
                pwm.ChangeDutyCycle(21.875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 1
            if 28 in intNote:
                print(resultNote28);
                pwm.ChangeDutyCycle(22.65625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 1
            if 29 in intNote:
                print(resultNote29);
                pwm.ChangeDutyCycle(23.4375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 1
            if 30 in intNote:
                print(resultNote30);
                pwm.ChangeDutyCycle(24.21875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0) 
                
            # note g octave 1
            if 31 in intNote:
                print(resultNote31);
                pwm.ChangeDutyCycle(25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 1
            if 32 in intNote:
                print(resultNote32);
                pwm.ChangeDutyCycle(25.78125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 1
            if 33 in intNote:
                print(resultNote33);
                pwm.ChangeDutyCycle(26.5625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 1
            if 34 in intNote:
                print(resultNote34);
                pwm.ChangeDutyCycle(27.34375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 1
            if 35 in intNote:
                print(resultNote35);
                pwm.ChangeDutyCycle(28.125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 2
            if 36 in intNote:
                print(resultNote36);
                pwm.ChangeDutyCycle(28.90625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 2
            if 37 in intNote:
                print(resultNote37);
                pwm.ChangeDutyCycle(29.6875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 2
            if 38 in intNote:
                print(resultNote38);
                pwm.ChangeDutyCycle(30.46875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 2
            if 39 in intNote:
                print(resultNote39);
                pwm.ChangeDutyCycle(31.25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 2
            if 40 in intNote:
                print(resultNote40);
                pwm.ChangeDutyCycle(32.03125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 2
            if 41 in intNote:
                print(resultNote41);
                pwm.ChangeDutyCycle(32.8125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 2
            if 42 in intNote:
                print(resultNote42);
                pwm.ChangeDutyCycle(33.59375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 2
            if 43 in intNote:
                print(resultNote43);
                pwm.ChangeDutyCycle(34.375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 2
            if 44 in intNote:
                print(resultNote44);
                pwm.ChangeDutyCycle(35.15625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 2
            if 45 in intNote:
                print(resultNote45);
                pwm.ChangeDutyCycle(35.9375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 2
            if 46 in intNote:
                print(resultNote46);
                pwm.ChangeDutyCycle(36.71875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 2
            if 47 in intNote:
                print(resultNote47);
                pwm.ChangeDutyCycle(37.5)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 3
            if 48 in intNote:
                print(resultNote48);
                pwm.ChangeDutyCycle(38.28125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 3
            if 49 in intNote:
                print(resultNote49);
                pwm.ChangeDutyCycle(39.0625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 3
            if 50 in intNote:
                print(resultNote50);
                pwm.ChangeDutyCycle(39.84375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 3
            if 51 in intNote:
                print(resultNote51);
                pwm.ChangeDutyCycle(40.625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 3
            if 52 in intNote:
                print(resultNote52);
                pwm.ChangeDutyCycle(41.40625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 3
            if 53 in intNote:
                print(resultNote53);
                pwm.ChangeDutyCycle(42.1875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 3
            if 54 in intNote:
                print(resultNote54);
                pwm.ChangeDutyCycle(42.96875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 3
            if 55 in intNote:
                print(resultNote55);
                pwm.ChangeDutyCycle(43.75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 3
            if 56 in intNote:
                print(resultNote56);
                pwm.ChangeDutyCycle(44.53125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 3
            if 57 in intNote:
                print(resultNote57);
                pwm.ChangeDutyCycle(45.3125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 3
            if 58 in intNote:
                print(resultNote58);
                pwm.ChangeDutyCycle(46.09375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 3
            if 59 in intNote:
                print(resultNote59);
                pwm.ChangeDutyCycle(46.875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 4
            if 60 in intNote:
                print(resultNote60);
                pwm.ChangeDutyCycle(47.65625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 4
            if 61 in intNote:
                print(resultNote61);
                pwm.ChangeDutyCycle(48.4375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 4
            if 62 in intNote:
                print(resultNote62);
                pwm.ChangeDutyCycle(49.21875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 4
            if 63 in intNote:
                print(resultNote63);
                pwm.ChangeDutyCycle(50)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 4
            if 64 in intNote:
                print(resultNote64);
                pwm.ChangeDutyCycle(50.78125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 4
            if 65 in intNote:
                print(resultNote65);
                pwm.ChangeDutyCycle(51.5625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 4
            if 66 in intNote:
                print(resultNote66);
                pwm.ChangeDutyCycle(52.34375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 4
            if 67 in intNote:
                print(resultNote67);
                pwm.ChangeDutyCycle(53.125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 4
            if 68 in intNote:
                print(resultNote68);
                pwm.ChangeDutyCycle(53.90625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 4
            if 69 in intNote:
                print(resultNote69);
                pwm.ChangeDutyCycle(54.6875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 4
            if 70 in intNote:
                print(resultNote70);
                pwm.ChangeDutyCycle(55.46875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 4
            if 71 in intNote:
                print(resultNote71);
                pwm.ChangeDutyCycle(56.25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 5
            if 72 in intNote:
                print(resultNote72);
                pwm.ChangeDutyCycle(57.03125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 5
            if 73 in intNote:
                print(resultNote73);
                pwm.ChangeDutyCycle(57.8125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 5
            if 74 in intNote:
                print(resultNote74);
                pwm.ChangeDutyCycle(58.59375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 5
            if 75 in intNote:
                print(resultNote75);
                pwm.ChangeDutyCycle(59.375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 5
            if 76 in intNote:
                print(resultNote76);
                pwm.ChangeDutyCycle(60.15625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 5
            if 77 in intNote:
                print(resultNote77);
                pwm.ChangeDutyCycle(60.9375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 5
            if 78 in intNote:
                print(resultNote78);
                pwm.ChangeDutyCycle(61.71875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 5
            if 79 in intNote:
                print(resultNote79);
                pwm.ChangeDutyCycle(62.5)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 5
            if 80 in intNote:
                print(resultNote80);
                pwm.ChangeDutyCycle(63.28125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
            
            # note a octave 5
            if 81 in intNote:
                print(resultNote81);
                pwm.ChangeDutyCycle(64.0625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 5
            if 82 in intNote:
                print(resultNote82);
                pwm.ChangeDutyCycle(64.84375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 5
            if 83 in intNote:
                print(resultNote83);
                pwm.ChangeDutyCycle(65.625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 6
            if 84 in intNote:
                print(resultNote84);
                pwm.ChangeDutyCycle(66.40625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 6
            if 85 in intNote:
                print(resultNote85);
                pwm.ChangeDutyCycle(67.1875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 6
            if 86 in intNote:
                print(resultNote86);
                pwm.ChangeDutyCycle(67.96875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 6
            if 87 in intNote:
                print(resultNote87);
                pwm.ChangeDutyCycle(68.75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 6
            if 88 in intNote:
                print(resultNote88);
                pwm.ChangeDutyCycle(69.53125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 6
            if 89 in intNote:
                print(resultNote89);
                pwm.ChangeDutyCycle(70.3125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 6
            if 90 in intNote:
                print(resultNote90);
                pwm.ChangeDutyCycle(71.09375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 6
            if 91 in intNote:
                print(resultNote91);
                pwm.ChangeDutyCycle(71.875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 6
            if 92 in intNote:
                print(resultNote92);
                pwm.ChangeDutyCycle(72.65625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 6
            if 93 in intNote:
                print(resultNote93);
                pwm.ChangeDutyCycle(73.4375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 6
            if 94 in intNote:
                print(resultNote94);
                pwm.ChangeDutyCycle(74.21875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 6
            if 95 in intNote:
                print(resultNote95);
                pwm.ChangeDutyCycle(75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 7
            if 96 in intNote:
                print(resultNote96);
                pwm.ChangeDutyCycle(75.78125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 7
            if 97 in intNote:
                print(resultNote97);
                pwm.ChangeDutyCycle(76.5625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 7
            if 98 in intNote:
                print(resultNote98);
                pwm.ChangeDutyCycle(77.34375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 7
            if 99 in intNote:
                print(resultNote99);
                pwm.ChangeDutyCycle(78.125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 7
            if 100 in intNote:
                print(resultNote100);
                pwm.ChangeDutyCycle(78.90625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 7
            if 101 in intNote:
                print(resultNote101);
                pwm.ChangeDutyCycle(79.6875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 7
            if 102 in intNote:
                print(resultNote102);
                pwm.ChangeDutyCycle(80.46875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 7
            if 103 in intNote:
                print(resultNote103);
                pwm.ChangeDutyCycle(81.25)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 7
            if 104 in intNote:
                print(resultNote104);
                pwm.ChangeDutyCycle(82.03125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 7
            if 105 in intNote:
                print(resultNote105);
                pwm.ChangeDutyCycle(82.8125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 7
            if 106 in intNote:
                print(resultNote106);
                pwm.ChangeDutyCycle(83.59375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 7
            if 107 in intNote:
                print(resultNote107);
                pwm.ChangeDutyCycle(84.375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 8
            if 108 in intNote:
                print(resultNote108);
                pwm.ChangeDutyCycle(85.15625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 8
            if 109 in intNote:
                print(resultNote109);
                pwm.ChangeDutyCycle(85.9375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 8
            if 110 in intNote:
                print(resultNote110);
                pwm.ChangeDutyCycle(86.71875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 8
            if 111 in intNote:
                print(resultNote111);
                pwm.ChangeDutyCycle(87.5)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 8
            if 112 in intNote:
                print(resultNote112);
                pwm.ChangeDutyCycle(88.28125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 8
            if 113 in intNote:
                print(resultNote113);
                pwm.ChangeDutyCycle(89.0625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 8
            if 114 in intNote:
                print(resultNote114);
                pwm.ChangeDutyCycle(89.84375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 8
            if 115 in intNote:
                print(resultNote115);
                pwm.ChangeDutyCycle(90.625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g#/a| octave 8
            if 116 in intNote:
                print(resultNote116);
                pwm.ChangeDutyCycle(91.40625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a octave 8
            if 117 in intNote:
                print(resultNote117);
                pwm.ChangeDutyCycle(92.1875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note a#/b| octave 8
            if 118 in intNote:
                print(resultNote118);
                pwm.ChangeDutyCycle(92.96875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note b octave 8
            if 119 in intNote:
                print(resultNote119);
                pwm.ChangeDutyCycle(93.75)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c octave 9
            if 120 in intNote:
                print(resultNote120);
                pwm.ChangeDutyCycle(94.53125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note c#/d| octave 9
            if 121 in intNote:
                print(resultNote121);
                pwm.ChangeDutyCycle(95.3125)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d octave 9
            if 122 in intNote:
                print(resultNote122);
                pwm.ChangeDutyCycle(96.09375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note d#/e| octave 9
            if 123 in intNote:
                print(resultNote123);
                pwm.ChangeDutyCycle(96.875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note e octave 9
            if 124 in intNote:
                print(resultNote124);
                pwm.ChangeDutyCycle(97.65625)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f octave 9
            if 125 in intNote:
                print(resultNote125);
                pwm.ChangeDutyCycle(98.4375)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note f#/g| octave 9
            if 126 in intNote:
                print(resultNote126);
                pwm.ChangeDutyCycle(99.21875)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
                
            # note g octave 9
            if 127 in intNote:
                print(resultNote127);
                pwm.ChangeDutyCycle(100)
                sleep(0.0000000001)
                pwm.ChangeDutyCycle(0)
            
            if elapsed_time > sngTime:
                pwm.ChangeDutyCycle(0)
                break

        # makes sure nothing is in time
        if sngTime!=0:
            intNote.clear()
        
        # gets data for the note loop
        if i.type == 'note_on':
            
            # note c octave -1
            if i.note == 0:
                intNote.append(0)
                
            # note c#/d| octave -1
            if i.note == 1:
                intNote.append(1)
                
            # note d octave -1
            if i.note == 2:
                intNote.append(2)
                
            # note d#/e| octave -1
            if i.note == 3:
                intNote.append(3)
                
            # note e octave -1
            if i.note == 4:
                intNote.append(4)
                
            # note f octave -1
            if i.note == 5:
                intNote.append(5)
                
            # note f#/g| octave -1
            if i.note == 6:
                intNote.append(6)
                
            # note g octave -1
            if i.note == 7:
                intNote.append(7)
                
            # note g#/a| octave -1
            if i.note == 8:
                intNote.append(8)
                
            # note a octave -1
            if i.note == 9:
                intNote.append(9)
                
            # note a#/b| octave -1
            if i.note == 10:
                intNote.append(10)
                
            # note b octave -1
            if i.note == 11:
                intNote.append(11)
                
            # note c octave 0
            if i.note == 12:
                intNote.append(12)
                
            # note c#/d| octave 0
            if i.note == 13:
                intNote.append(13)
                
            # note d octave 0
            if i.note == 14:
                intNote.append(14)
                
            # note d#/e| octave 0
            if i.note == 15:
                intNote.append(15)
                
            # note e octave 0
            if i.note == 16:
                intNote.append(16)
                
            # note f octave 0
            if i.note == 17:
                intNote.append(17)
                
            # note f#/g| octave 0
            if i.note == 18:
                intNote.append(18)
                
            # note g octave 0
            if i.note == 19:
                intNote.append(19)
                
            # note g#a| octave 0
            if i.note == 20:
                intNote.append(20)
            
            # note a octave 0
            if i.note == 21:
                intNote.append(21)
                
            # note a#/b| octave 0
            if i.note == 22:
                intNote.append(22)
                
            # note b octave 0
            if i.note == 23:
                intNote.append(23)
                
            # note c octave 1
            if i.note == 24:
                intNote.append(24)
                
            # note c#/d| octave 1
            if i.note == 25:
                intNote.append(25)
                
            # note d octave 1
            if i.note == 26:
                intNote.append(26)
                
            # note d#/e| octave 1
            if i.note == 27:
                intNote.append(27)
                
            # note e octave 1
            if i.note == 28:
                intNote.append(28)
                
            # note f octave 1
            if i.note == 29:
                pintNote.append(29)
                
            # note f#/g| octave 1
            if i.note == 30:
                intNote.append(30)
                
            # note g octave 1
            if i.note == 31:
                intNote.append(31)
                
            # note g#/a| octave 1
            if i.note == 32:
                intNote.append(32)
                
            # note a octave 1
            if i.note == 33:
                intNote.append(33)
                
            # note a#/b| octave 1
            if i.note == 34:
                intNote.append(34)
                
            # note b octave 1
            if i.note == 35:
                intNote.append(35)
                
            # note c octave 2
            if i.note == 36:
                intNote.append(36)
                
            # note c#/d| octave 2
            if i.note == 37:
                intNote.append(37)
                
            # note d octave 2
            if i.note == 38:
                intNote.append(38)
                
            # note d#/e| octave 2
            if i.note == 39:
                intNote.append(39)
                
            # note e octave 2
            if i.note == 40:
                intNote.append(40)
                
            # note f octave 2
            if i.note == 41:
                intNote.append(41)
                
            # note f#/g| octave 2
            if i.note == 42:
                intNote.append(42)
                
            # note g octave 2
            if i.note == 43:
                intNote.append(43)
                
            # note g#/a| octave 2
            if i.note == 44:
                intNote.append(44)
                
            # note a octave 2
            if i.note == 45:
                intNote.append(45)
                
            # note a#/b| octave 2
            if i.note == 46:
                intNote.append(46)
                
            # note b octave 2
            if i.note == 47:
                intNote.append(47)
                
            # note c octave 3
            if i.note == 48:
                intNote.append(48)
                
            # note c#/d| octave 3
            if i.note == 49:
                intNote.append(49)
                
            # note d octave 3
            if i.note == 50:
                intNote.append(50)
                
            # note d#/e| octave 3
            if i.note == 51:
                intNote.append(51)
                
            # note e octave 3
            if i.note == 52:
                intNote.append(52)
                
            # note f octave 3
            if i.note == 53:
                intNote.append(53)
                
            # note f#/g| octave 3
            if i.note == 54:
                intNote.append(54)
                
            # note g octave 3
            if i.note == 55:
                intNote.append(55)
                
            # note g#/a| octave 3
            if i.note == 56:
                intNote.append(56)
                
            # note a octave 3
            if i.note == 57:
                intNote.append(57)
                
            # note a#/b| octave 3
            if i.note == 58:
                intNote.append(58)
                
            # note b octave 3
            if i.note == 59:
                intNote.append(59)
                
            # note c octave 4
            if i.note == 60:
                intNote.append(60)
                
            # note c#/d| octave 4
            if i.note == 61:
                intNote.append(61)
                
            # note d octave 4
            if i.note == 62:
                intNote.append(62)
                
            # note d#/e| octave 4
            if i.note == 63:
                intNote.append(63)
                
            # note e octave 4
            if i.note == 64:
                intNote.append(64)
                
            # note f octave 4
            if i.note == 65:
                intNote.append(65)
                
            # note f#/g| octave 4
            if i.note == 66:
                intNote.append(66)
                
            # note g octave 4
            if i.note == 67:
                intNote.append(67)
                
            # note g#/a| octave 4
            if i.note == 68:
                intNote.append(68)
                
            # note a octave 4
            if i.note == 69:
                intNote.append(69)
                
            # note a#/b| octave 4
            if i.note == 70:
                intNote.append(70)
                
            # note b octave 4
            if i.note == 71:
                intNote.append(71)
                
            # note c octave 5
            if i.note == 72:
                intNote.append(72)
                
            # note c#/d| octave 5
            if i.note == 73:
                intNote.append(73)
                
            # note d octave 5
            if i.note == 74:
                intNote.append(74)
                
            # note d#/e| octave 5
            if i.note == 75:
                intNote.append(75)
                
            # note e octave 5
            if i.note == 76:
                intNote.append(76)
                
            # note f octave 5
            if i.note == 77:
                intNote.append(77)
                
            # note f#/g| octave 5
            if i.note == 78:
                intNote.append(78)
                
            # note g octave 5
            if i.note == 79:
                intNote.append(79)
                
            # note g#/a| octave 5
            if i.note == 80:
                intNote.append(80)
            
            # note a octave 5
            if i.note == 81:
                intNote.append(81)
                
            # note a#/b| octave 5
            if i.note == 82:
                intNote.append(82)
                
            # note b octave 5
            if i.note == 83:
                intNote.append(83)
                
            # note c octave 6
            if i.note == 84:
                intNote.append(84)
                
            # note c#/d| octave 6
            if i.note == 85:
                intNote.append(85)
                
            # note d octave 6
            if i.note == 86:
                intNote.append(86)
                
            # note d#/e| octave 6
            if i.note == 87:
                intNote.append(87)
                
            # note e octave 6
            if i.note == 88:
                intNote.append(88)
                
            # note f octave 6
            if i.note == 89:
                intNote.append(89)
                
            # note f#/g| octave 6
            if i.note == 90:
                intNote.append(90)
                
            # note g octave 6
            if i.note == 91:
                intNote.append(91)
                
            # note g#/a| octave 6
            if i.note == 92:
                intNote.append(92)
                
            # note a octave 6
            if i.note == 93:
                intNote.append(93)
                
            # note a#/b| octave 6
            if i.note == 94:
                intNote.append(94)
                
            # note b octave 6
            if i.note == 95:
                intNote.append(95)
                
            # note c octave 7
            if i.note == 96:
                intNote.append(96)
                
            # note c#/d| octave 7
            if i.note == 97:
                intNote.append(97)
                
            # note d octave 7
            if i.note == 98:
                intNote.append(98)
                
            # note d#/e| octave 7
            if i.note == 99:
                intNote.append(99)
                
            # note e octave 7
            if i.note == 100:
                intNote.append(100)
                
            # note f octave 7
            if i.note == 101:
                intNote.append(101)
                
            # note f#/g| octave 7
            if i.note == 102:
                intNote.append(102)
                
            # note g octave 7
            if i.note == 103:
                intNote.append(103)
                
            # note g#/a| octave 7
            if i.note == 104:
                intNote.append(104)
                
            # note a octave 7
            if i.note == 105:
                intNote.append(105)
                
            # note a#/b| octave 7
            if i.note == 106:
                intNote.append(106)
                
            # note b octave 7
            if i.note == 107:
                intNote.append(107)
                
            # note c octave 8
            if i.note == 108:
                intNote.append(108)
                
            # note c#/d| octave 8
            if i.note == 109:
                intNote.append(109)
                
            # note d octave 8
            if i.note == 110:
                intNote.append(110)
                
            # note d#/e| octave 8
            if i.note == 111:
                intNote.append(111)
                
            # note e octave 8
            if i.note == 112:
                intNote.append(112)
                
            # note f octave 8
            if i.note == 113:
                intNote.append(113)
                
            # note f#/g| octave 8
            if i.note == 114:
                intNote.append(114)
                
            # note g octave 8
            if i.note == 115:
                intNote.append(115)
                
            # note g#/a| octave 8
            if i.note == 116:
                intNote.append(116)
            
            # note a octave 8
            if i.note == 117:
                intNote.append(117)
                
            # note a#/b| octave 8
            if i.note == 118:
                intNote.append(118)
                
            # note b octave 8
            if i.note == 119:
                intNote.append(119)
                
            # note c octave 9
            if i.note == 120:
                intNote.append(120)
                
            # note c#/d| octave 9
            if i.note == 121:
                intNote.append(121)
                
            # note d octave 9
            if i.note == 122:
                intNote.append(122)
                
            # note d#/e| octave 9
            if i.note == 123:
                intNote.append(123)
                
            # note e octave 9
            if i.note == 124:
                intNote.append(124)
                
            # note f octave 9
            if i.note == 125:
                intNote.append(125)
                
            # note f#/g| octave 9
            if i.note == 126:
                intNote.append(126)
                
            # note g octave 9
            if i.note == 127:
                intNote.append(127)
            
        elif i.type == 'end_of_track':
            print("Good Bye");
            exit() # exits after song is done
    
# Arduino Mod function
def ArduinoMod():

    import serial

    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");

    # calls the Arduino druver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600)
    
    # library for mods and process vm call needed for mods
    from lupa import LuaRuntime
    lua = LuaRuntime()

    # The mod file must be in your home directory and must be called note_data_to_instrument_mod.lua
    lua.execute(r'''dofile("note_data_to_instrument_mod.lua")''')
    
    # get the mod global envirorment
    globals = lua.globals()
    
    # Mod Notice and Name
    strModNoticeAndName = lua.globals().strNoticeAndName
    print(strModNoticeAndName)
    
    # results from each mod function
    resultNote0 = globals.Note0()
    resultNote1 = globals.Note1()
    resultNote2 = globals.Note2()
    resultNote3 = globals.Note3()
    resultNote4 = globals.Note4()
    resultNote5 = globals.Note5()
    resultNote6 = globals.Note6()
    resultNote7 = globals.Note7()
    resultNote8 = globals.Note8()
    resultNote9 = globals.Note9()
    resultNote10 = globals.Note10()
    resultNote11 = globals.Note11()
    resultNote12 = globals.Note12()
    resultNote13 = globals.Note13()
    resultNote14 = globals.Note14()
    resultNote15 = globals.Note15()
    resultNote16 = globals.Note16()
    resultNote17 = globals.Note17()
    resultNote18 = globals.Note18()
    resultNote19 = globals.Note19()
    resultNote20 = globals.Note20()
    resultNote21 = globals.Note21()
    resultNote22 = globals.Note22()
    resultNote23 = globals.Note23()
    resultNote24 = globals.Note24()
    resultNote25 = globals.Note25()
    resultNote26 = globals.Note26()
    resultNote27 = globals.Note27()
    resultNote28 = globals.Note28()
    resultNote29 = globals.Note29()
    resultNote30 = globals.Note30()
    resultNote31 = globals.Note31()
    resultNote32 = globals.Note32()
    resultNote33 = globals.Note33()
    resultNote34 = globals.Note34()
    resultNote35 = globals.Note35()
    resultNote36 = globals.Note36()
    resultNote37 = globals.Note37()
    resultNote38 = globals.Note38()
    resultNote39 = globals.Note39()
    resultNote40 = globals.Note40()
    resultNote41 = globals.Note41()
    resultNote42 = globals.Note42()
    resultNote43 = globals.Note43()
    resultNote44 = globals.Note44()
    resultNote45 = globals.Note45()
    resultNote46 = globals.Note46()
    resultNote47 = globals.Note47()
    resultNote48 = globals.Note48()
    resultNote49 = globals.Note49()
    resultNote50 = globals.Note50()
    resultNote51 = globals.Note51()
    resultNote52 = globals.Note52()
    resultNote53 = globals.Note53()
    resultNote54 = globals.Note54()
    resultNote55 = globals.Note55()
    resultNote56 = globals.Note56()
    resultNote57 = globals.Note57()
    resultNote58 = globals.Note58()
    resultNote59 = globals.Note59()
    resultNote60 = globals.Note60()
    resultNote61 = globals.Note61()
    resultNote62 = globals.Note62()
    resultNote63 = globals.Note63()
    resultNote64 = globals.Note64()
    resultNote65 = globals.Note65()
    resultNote66 = globals.Note66()
    resultNote67 = globals.Note67()
    resultNote68 = globals.Note68()
    resultNote69 = globals.Note69()
    resultNote70 = globals.Note70()
    resultNote71 = globals.Note71()
    resultNote72 = globals.Note72()
    resultNote73 = globals.Note73()
    resultNote74 = globals.Note74()
    resultNote75 = globals.Note75()
    resultNote76 = globals.Note76()
    resultNote77 = globals.Note77()
    resultNote78 = globals.Note78()
    resultNote79 = globals.Note79()
    resultNote80 = globals.Note80()
    resultNote81 = globals.Note81()
    resultNote82 = globals.Note82()
    resultNote83 = globals.Note83()
    resultNote84 = globals.Note84()
    resultNote85 = globals.Note85()
    resultNote86 = globals.Note86()
    resultNote87 = globals.Note87()
    resultNote88 = globals.Note88()
    resultNote89 = globals.Note89()
    resultNote90 = globals.Note90()
    resultNote91 = globals.Note91()
    resultNote92 = globals.Note92()
    resultNote93 = globals.Note93()
    resultNote94 = globals.Note94()
    resultNote95 = globals.Note95()
    resultNote96 = globals.Note96()
    resultNote97 = globals.Note97()
    resultNote98 = globals.Note98()
    resultNote99 = globals.Note99()
    resultNote100 = globals.Note100()
    resultNote101 = globals.Note101()
    resultNote102 = globals.Note102()
    resultNote103 = globals.Note103()
    resultNote104 = globals.Note104()
    resultNote105 = globals.Note105()
    resultNote106 = globals.Note106()
    resultNote107 = globals.Note107()
    resultNote108 = globals.Note108()
    resultNote109 = globals.Note109()
    resultNote110 = globals.Note110()
    resultNote111 = globals.Note111()
    resultNote112 = globals.Note112()
    resultNote113 = globals.Note113()
    resultNote114 = globals.Note114()
    resultNote115 = globals.Note115()
    resultNote116 = globals.Note116()
    resultNote117 = globals.Note117()
    resultNote118 = globals.Note118()
    resultNote119 = globals.Note119()
    resultNote120 = globals.Note120()
    resultNote121 = globals.Note121()
    resultNote122 = globals.Note122()
    resultNote123 = globals.Note123()
    resultNote124 = globals.Note124()
    resultNote125 = globals.Note125()
    resultNote126 = globals.Note126()
    resultNote127 = globals.Note127()
    
    # notice about files
    print("this can only read .mid files right now, if you can add the ability to read .mxl(sheet music file type), .mod, .xm, .s3m and .it files please add it in here because I cannot find good documentation on reading those files.\n");
    # type in for what directory you want to use
    strDirectory = input("What Directory would you like to use (case sensitive): ")
    
    os.chdir(strDirectory)
    print("\n");
    for file in glob.glob("*.mid"):
        print(file)
    
    # selections
    strSongName = input("Enter Name of the song file exactly as typed on the list: ")

    from mido import MidiFile
    mid = MidiFile(strSongName, clip=True)
    midimsgs = []

    # stores note data in array for chords
    intNote=[]

    # Put all note on/off in midinote as dictionary
    # midi reads in delta time as in time for a note appears before data for the note and if delta time = 0 for 1 note it is playing at the same time as the note before it
    # reads 1 line at a time
    # needs a loop for multiple notes playing quickly back and forth to have it sound like multiple notes are playing at the same time
    for i in mid:
        
        # timing for the song
        start_time = time.time()
        sngTime=0
        sngTime = i.time
        
        # note loop and it allows the app to play chords
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
                
            # note c octave -1
            if 0 in intNote:
                print(resultNote0);
                arduinoDriver.write("1".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave -1
            if 1 in intNote:
                print(resultNote1);
                arduinoDriver.write("2".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave -1
            if 2 in intNote:
                print(resultNote2);
                arduinoDriver.write("3".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave -1
            if 3 in intNote:
                print(resultNote3);
                arduinoDriver.write("4".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave -1
            if 4 in intNote:
                print(resultNote4);
                arduinoDriver.write("5".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave -1
            if 5 in intNote:
                print(resultNote5);
                arduinoDriver.write("6".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave -1
            if 6 in intNote:
                print(resultNote6);
                arduinoDriver.write("7".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave -1
            if 7 in intNote:
                print(resultNote7);
                arduinoDriver.write("8".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave -1
            if 8 in intNote:
                print(resultNote8);
                arduinoDriver.write("9".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave -1
            if 9 in intNote:
                print(resultNote9);
                arduinoDriver.write("10".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave -1
            if 10 in intNote:
                print(resultNote10);
                arduinoDriver.write("11".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave -1
            if 11 in intNote:
                print(resultNote11);
                arduinoDriver.write("12".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 0
            if 12 in intNote:
                print(resultNote12);
                arduinoDriver.write("13".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 0
            if 13 in intNote:
                print(resultNote13);
                arduinoDriver.write("14".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 0
            if 14 in intNote:
                print(resultNote14);
                arduinoDriver.write("15".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 0
            if 15 in intNote:
                print(resultNote15);
                arduinoDriver.write("16".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 0
            if 16 in intNote:
                print(resultNote16);
                arduinoDriver.write("17".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 0
            if 17 in intNote:
                print(resultNote17);
                arduinoDriver.write("18".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 0
            if 18 in intNote:
                print(resultNote18);
                arduinoDriver.write("19".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 0
            if 19 in intNote:
                print(resultNote19);
                arduinoDriver.write("20".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 0
            if 20 in intNote:
                print(resultNote20);
                arduinoDriver.write("21".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
            
            # note a octave 0
            if 21 in intNote:
                print(resultNote21);
                arduinoDriver.write("22".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 0
            if 22 in intNote:
                print(resultNote22);
                arduinoDriver.write("23".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 0
            if 23 in intNote:
                print(resultNote23);
                arduinoDriver.write("24".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 1
            if 24 in intNote:
                print(resultNote24);
                arduinoDriver.write("25".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 1
            if 25 in intNote:
                print(resultNote25);
                arduinoDriver.write("26".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 1
            if 26 in intNote:
                print(resultNote26);
                arduinoDriver.write("27".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 1
            if 27 in intNote:
                print(resultNote27);
                arduinoDriver.write("28".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 1
            if 28 in intNote:
                print(resultNote28);
                arduinoDriver.write("29".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 1
            if 29 in intNote:
                print(resultNote29);
                arduinoDriver.write("30".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 1
            if 30 in intNote:
                print(resultNote30);
                arduinoDriver.write("31".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 1
            if 31 in intNote:
                print(resultNote31);
                arduinoDriver.write("32".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 1
            if 32 in intNote:
                print(resultNote32);
                arduinoDriver.write("33".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 1
            if 33 in intNote:
                print(resultNote33);
                arduinoDriver.write("34".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 1
            if 34 in intNote:
                print(resultNote34);
                arduinoDriver.write("35".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 1
            if 35 in intNote:
                print(resultNote35);
                arduinoDriver.write("36".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 2
            if 36 in intNote:
                print(resultNote36);
                arduinoDriver.write("37".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 2
            if 37 in intNote:
                print(resultNote37);
                arduinoDriver.write("38".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 2
            if 38 in intNote:
                print(resultNote38);
                arduinoDriver.write("39".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 2
            if 39 in intNote:
                print(resultNote39);
                arduinoDriver.write("40".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 2
            if 40 in intNote:
                print(resultNote40);
                arduinoDriver.write("41".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 2
            if 41 in intNote:
                print(resultNote41);
                arduinoDriver.write("42".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 2
            if 42 in intNote:
                print(resultNote42);
                arduinoDriver.write("43".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 2
            if 43 in intNote:
                print(resultNote43);
                arduinoDriver.write("44".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 2
            if 44 in intNote:
                print(resultNote44);
                arduinoDriver.write("45".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 2
            if 45 in intNote:
                print(resultNote45);
                arduinoDriver.write("46".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 2
            if 46 in intNote:
                print(resultNote46);
                arduinoDriver.write("47".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 2
            if 47 in intNote:
                print(resultNote47);
                arduinoDriver.write("48".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 3
            if 48 in intNote:
                print(resultNote48);
                arduinoDriver.write("49".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 3
            if 49 in intNote:
                print(resultNote49);
                arduinoDriver.write("50".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 3
            if 50 in intNote:
                print(resultNote50);
                arduinoDriver.write("51".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 3
            if 51 in intNote:
                print(resultNote51);
                arduinoDriver.write("52".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 3
            if 52 in intNote:
                print(resultNote52);
                arduinoDriver.write("53".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 3
            if 53 in intNote:
                print(resultNote53);
                arduinoDriver.write("54".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 3
            if 54 in intNote:
                print(resultNote54);
                arduinoDriver.write("55".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 3
            if 55 in intNote:
                print(resultNote55);
                arduinoDriver.write("56".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 3
            if 56 in intNote:
                print(resultNote56);
                arduinoDriver.write("57".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 3
            if 57 in intNote:
                print(resultNote57);
                arduinoDriver.write("58".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 3
            if 58 in intNote:
                print(resultNote58);
                arduinoDriver.write("59".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 3
            if 59 in intNote:
                print(resultNote59);
                arduinoDriver.write("60".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 4
            if 60 in intNote:
                print(resultNote60);
                arduinoDriver.write("61".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 4
            if 61 in intNote:
                print(resultNote61);
                arduinoDriver.write("62".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 4
            if 62 in intNote:
                print(resultNote62);
                arduinoDriver.write("63".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 4
            if 63 in intNote:
                print(resultNote63);
                arduinoDriver.write("64".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 4
            if 64 in intNote:
                print(resultNote64);
                arduinoDriver.write("65".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 4
            if 65 in intNote:
                print(resultNote65);
                arduinoDriver.write("66".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 4
            if 66 in intNote:
                print(resultNote66);
                arduinoDriver.write("67".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 4
            if 67 in intNote:
                print(resultNote67);
                arduinoDriver.write("68".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 4
            if 68 in intNote:
                print(resultNote68);
                arduinoDriver.write("69".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 4
            if 69 in intNote:
                print(resultNote69);
                arduinoDriver.write("70".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 4
            if 70 in intNote:
                print(resultNote70);
                arduinoDriver.write("71".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 4
            if 71 in intNote:
                print(resultNote71);
                arduinoDriver.write("72".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 5
            if 72 in intNote:
                print(resultNote72);
                arduinoDriver.write("73".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 5
            if 73 in intNote:
                print(resultNote73);
                arduinoDriver.write("74".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 5
            if 74 in intNote:
                print(resultNote74);
                arduinoDriver.write("75".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 5
            if 75 in intNote:
                print(resultNote75);
                arduinoDriver.write("76".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 5
            if 76 in intNote:
                print(resultNote76);
                arduinoDriver.write("77".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 5
            if 77 in intNote:
                print(resultNote77);
                arduinoDriver.write("78".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 5
            if 78 in intNote:
                print(resultNote78);
                arduinoDriver.write("79".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 5
            if 79 in intNote:
                print(resultNote79);
                arduinoDriver.write("80".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 5
            if 80 in intNote:
                print(resultNote80);
                arduinoDriver.write("81".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
            
            # note a octave 5
            if 81 in intNote:
                print(resultNote81);
                arduinoDriver.write("82".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 5
            if 82 in intNote:
                print(resultNote82);
                arduinoDriver.write("83".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 5
            if 83 in intNote:
                print(resultNote83);
                arduinoDriver.write("84".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 6
            if 84 in intNote:
                print(resultNote84);
                arduinoDriver.write("85".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 6
            if 85 in intNote:
                print(resultNote85);
                arduinoDriver.write("86".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 6
            if 86 in intNote:
                print(resultNote86);
                arduinoDriver.write("87".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 6
            if 87 in intNote:
                print(resultNote87);
                arduinoDriver.write("88".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 6
            if 88 in intNote:
                print(resultNote88);
                arduinoDriver.write("89".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 6
            if 89 in intNote:
                print(resultNote89);
                arduinoDriver.write("90".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 6
            if 90 in intNote:
                print(resultNote90);
                arduinoDriver.write("91".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 6
            if 91 in intNote:
                print(resultNote91);
                arduinoDriver.write("92".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 6
            if 92 in intNote:
                print(resultNote92);
                arduinoDriver.write("93".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 6
            if 93 in intNote:
                print(resultNote93);
                arduinoDriver.write("94".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 6
            if 94 in intNote:
                print(resultNote94);
                arduinoDriver.write("95".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 6
            if 95 in intNote:
                print(resultNote95);
                arduinoDriver.write("96".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 7
            if 96 in intNote:
                print(resultNote96);
                arduinoDriver.write("97".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 7
            if 97 in intNote:
                print(resultNote97);
                arduinoDriver.write("98".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 7
            if 98 in intNote:
                print(resultNote98);
                arduinoDriver.write("99".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 7
            if 99 in intNote:
                print(resultNote99);
                arduinoDriver.write("100".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 7
            if 100 in intNote:
                print(resultNote100);
                arduinoDriver.write("101".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 7
            if 101 in intNote:
                print(resultNote101);
                arduinoDriver.write("102".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 7
            if 102 in intNote:
                print(resultNote102);
                arduinoDriver.write("103".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 7
            if 103 in intNote:
                print(resultNote103);
                arduinoDriver.write("104".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 7
            if 104 in intNote:
                print(resultNote104);
                arduinoDriver.write("105".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 7
            if 105 in intNote:
                print(resultNote105);
                arduinoDriver.write("106".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 7
            if 106 in intNote:
                print(resultNote106);
                arduinoDriver.write("107".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 7
            if 107 in intNote:
                print(resultNote107);
                arduinoDriver.write("108".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 8
            if 108 in intNote:
                print(resultNote108);
                arduinoDriver.write("109".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 8
            if 109 in intNote:
                print(resultNote109);
                arduinoDriver.write("110".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 8
            if 110 in intNote:
                print(resultNote110);
                arduinoDriver.write("111".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 8
            if 111 in intNote:
                print(resultNote111);
                arduinoDriver.write("112".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 8
            if 112 in intNote:
                print(resultNote112);
                arduinoDriver.write("113".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 8
            if 113 in intNote:
                print(resultNote113);
                arduinoDriver.write("114".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 8
            if 114 in intNote:
                print(resultNote114);
                arduinoDriver.write("115".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 8
            if 115 in intNote:
                print(resultNote115);
                arduinoDriver.write("116".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g#/a| octave 8
            if 116 in intNote:
                print(resultNote116);
                arduinoDriver.write("117".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a octave 8
            if 117 in intNote:
                print(resultNote117);
                arduinoDriver.write("118".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note a#/b| octave 8
            if 118 in intNote:
                print(resultNote118);
                arduinoDriver.write("119".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note b octave 8
            if 119 in intNote:
                print(resultNote119);
                arduinoDriver.write("120".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c octave 9
            if 120 in intNote:
                print(resultNote120);
                arduinoDriver.write("121".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note c#/d| octave 9
            if 121 in intNote:
                print(resultNote121);
                arduinoDriver.write("122".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d octave 9
            if 122 in intNote:
                print(resultNote122);
                arduinoDriver.write("123".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note d#/e| octave 9
            if 123 in intNote:
                print(resultNote123);
                arduinoDriver.write("124".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note e octave 9
            if 124 in intNote:
                print(resultNote124);
                arduinoDriver.write("125".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f octave 9
            if 125 in intNote:
                print(resultNote125);
                arduinoDriver.write("126".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note f#/g| octave 9
            if 126 in intNote:
                print(resultNote126);
                arduinoDriver.write("127".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
                
            # note g octave 9
            if 127 in intNote:
                print(resultNote127);
                arduinoDriver.write("128".encode())
                sleep(0.0000000001)
                arduinoDriver.write("0".encode())
            
            if elapsed_time > sngTime:
                arduinoDriver.write("0".encode())
                break

        # makes sure nothing is in time
        if sngTime!=0:
            intNote.clear()
        
        # gets data for the note loop
        if i.type == 'note_on':
            
            # note c octave -1
            if i.note == 0:
                intNote.append(0)
                
            # note c#/d| octave -1
            if i.note == 1:
                intNote.append(1)
                
            # note d octave -1
            if i.note == 2:
                intNote.append(2)
                
            # note d#/e| octave -1
            if i.note == 3:
                intNote.append(3)
                
            # note e octave -1
            if i.note == 4:
                intNote.append(4)
                
            # note f octave -1
            if i.note == 5:
                intNote.append(5)
                
            # note f#/g| octave -1
            if i.note == 6:
                intNote.append(6)
                
            # note g octave -1
            if i.note == 7:
                intNote.append(7)
                
            # note g#/a| octave -1
            if i.note == 8:
                intNote.append(8)
                
            # note a octave -1
            if i.note == 9:
                intNote.append(9)
                
            # note a#/b| octave -1
            if i.note == 10:
                intNote.append(10)
                
            # note b octave -1
            if i.note == 11:
                intNote.append(11)
                
            # note c octave 0
            if i.note == 12:
                intNote.append(12)
                
            # note c#/d| octave 0
            if i.note == 13:
                intNote.append(13)
                
            # note d octave 0
            if i.note == 14:
                intNote.append(14)
                
            # note d#/e| octave 0
            if i.note == 15:
                intNote.append(15)
                
            # note e octave 0
            if i.note == 16:
                intNote.append(16)
                
            # note f octave 0
            if i.note == 17:
                intNote.append(17)
                
            # note f#/g| octave 0
            if i.note == 18:
                intNote.append(18)
                
            # note g octave 0
            if i.note == 19:
                intNote.append(19)
                
            # note g#a| octave 0
            if i.note == 20:
                intNote.append(20)
            
            # note a octave 0
            if i.note == 21:
                intNote.append(21)
                
            # note a#/b| octave 0
            if i.note == 22:
                intNote.append(22)
                
            # note b octave 0
            if i.note == 23:
                intNote.append(23)
                
            # note c octave 1
            if i.note == 24:
                intNote.append(24)
                
            # note c#/d| octave 1
            if i.note == 25:
                intNote.append(25)
                
            # note d octave 1
            if i.note == 26:
                intNote.append(26)
                
            # note d#/e| octave 1
            if i.note == 27:
                intNote.append(27)
                
            # note e octave 1
            if i.note == 28:
                intNote.append(28)
                
            # note f octave 1
            if i.note == 29:
                pintNote.append(29)
                
            # note f#/g| octave 1
            if i.note == 30:
                intNote.append(30)
                
            # note g octave 1
            if i.note == 31:
                intNote.append(31)
                
            # note g#/a| octave 1
            if i.note == 32:
                intNote.append(32)
                
            # note a octave 1
            if i.note == 33:
                intNote.append(33)
                
            # note a#/b| octave 1
            if i.note == 34:
                intNote.append(34)
                
            # note b octave 1
            if i.note == 35:
                intNote.append(35)
                
            # note c octave 2
            if i.note == 36:
                intNote.append(36)
                
            # note c#/d| octave 2
            if i.note == 37:
                intNote.append(37)
                
            # note d octave 2
            if i.note == 38:
                intNote.append(38)
                
            # note d#/e| octave 2
            if i.note == 39:
                intNote.append(39)
                
            # note e octave 2
            if i.note == 40:
                intNote.append(40)
                
            # note f octave 2
            if i.note == 41:
                intNote.append(41)
                
            # note f#/g| octave 2
            if i.note == 42:
                intNote.append(42)
                
            # note g octave 2
            if i.note == 43:
                intNote.append(43)
                
            # note g#/a| octave 2
            if i.note == 44:
                intNote.append(44)
                
            # note a octave 2
            if i.note == 45:
                intNote.append(45)
                
            # note a#/b| octave 2
            if i.note == 46:
                intNote.append(46)
                
            # note b octave 2
            if i.note == 47:
                intNote.append(47)
                
            # note c octave 3
            if i.note == 48:
                intNote.append(48)
                
            # note c#/d| octave 3
            if i.note == 49:
                intNote.append(49)
                
            # note d octave 3
            if i.note == 50:
                intNote.append(50)
                
            # note d#/e| octave 3
            if i.note == 51:
                intNote.append(51)
                
            # note e octave 3
            if i.note == 52:
                intNote.append(52)
                
            # note f octave 3
            if i.note == 53:
                intNote.append(53)
                
            # note f#/g| octave 3
            if i.note == 54:
                intNote.append(54)
                
            # note g octave 3
            if i.note == 55:
                intNote.append(55)
                
            # note g#/a| octave 3
            if i.note == 56:
                intNote.append(56)
                
            # note a octave 3
            if i.note == 57:
                intNote.append(57)
                
            # note a#/b| octave 3
            if i.note == 58:
                intNote.append(58)
                
            # note b octave 3
            if i.note == 59:
                intNote.append(59)
                
            # note c octave 4
            if i.note == 60:
                intNote.append(60)
                
            # note c#/d| octave 4
            if i.note == 61:
                intNote.append(61)
                
            # note d octave 4
            if i.note == 62:
                intNote.append(62)
                
            # note d#/e| octave 4
            if i.note == 63:
                intNote.append(63)
                
            # note e octave 4
            if i.note == 64:
                intNote.append(64)
                
            # note f octave 4
            if i.note == 65:
                intNote.append(65)
                
            # note f#/g| octave 4
            if i.note == 66:
                intNote.append(66)
                
            # note g octave 4
            if i.note == 67:
                intNote.append(67)
                
            # note g#/a| octave 4
            if i.note == 68:
                intNote.append(68)
                
            # note a octave 4
            if i.note == 69:
                intNote.append(69)
                
            # note a#/b| octave 4
            if i.note == 70:
                intNote.append(70)
                
            # note b octave 4
            if i.note == 71:
                intNote.append(71)
                
            # note c octave 5
            if i.note == 72:
                intNote.append(72)
                
            # note c#/d| octave 5
            if i.note == 73:
                intNote.append(73)
                
            # note d octave 5
            if i.note == 74:
                intNote.append(74)
                
            # note d#/e| octave 5
            if i.note == 75:
                intNote.append(75)
                
            # note e octave 5
            if i.note == 76:
                intNote.append(76)
                
            # note f octave 5
            if i.note == 77:
                intNote.append(77)
                
            # note f#/g| octave 5
            if i.note == 78:
                intNote.append(78)
                
            # note g octave 5
            if i.note == 79:
                intNote.append(79)
                
            # note g#/a| octave 5
            if i.note == 80:
                intNote.append(80)
            
            # note a octave 5
            if i.note == 81:
                intNote.append(81)
                
            # note a#/b| octave 5
            if i.note == 82:
                intNote.append(82)
                
            # note b octave 5
            if i.note == 83:
                intNote.append(83)
                
            # note c octave 6
            if i.note == 84:
                intNote.append(84)
                
            # note c#/d| octave 6
            if i.note == 85:
                intNote.append(85)
                
            # note d octave 6
            if i.note == 86:
                intNote.append(86)
                
            # note d#/e| octave 6
            if i.note == 87:
                intNote.append(87)
                
            # note e octave 6
            if i.note == 88:
                intNote.append(88)
                
            # note f octave 6
            if i.note == 89:
                intNote.append(89)
                
            # note f#/g| octave 6
            if i.note == 90:
                intNote.append(90)
                
            # note g octave 6
            if i.note == 91:
                intNote.append(91)
                
            # note g#/a| octave 6
            if i.note == 92:
                intNote.append(92)
                
            # note a octave 6
            if i.note == 93:
                intNote.append(93)
                
            # note a#/b| octave 6
            if i.note == 94:
                intNote.append(94)
                
            # note b octave 6
            if i.note == 95:
                intNote.append(95)
                
            # note c octave 7
            if i.note == 96:
                intNote.append(96)
                
            # note c#/d| octave 7
            if i.note == 97:
                intNote.append(97)
                
            # note d octave 7
            if i.note == 98:
                intNote.append(98)
                
            # note d#/e| octave 7
            if i.note == 99:
                intNote.append(99)
                
            # note e octave 7
            if i.note == 100:
                intNote.append(100)
                
            # note f octave 7
            if i.note == 101:
                intNote.append(101)
                
            # note f#/g| octave 7
            if i.note == 102:
                intNote.append(102)
                
            # note g octave 7
            if i.note == 103:
                intNote.append(103)
                
            # note g#/a| octave 7
            if i.note == 104:
                intNote.append(104)
                
            # note a octave 7
            if i.note == 105:
                intNote.append(105)
                
            # note a#/b| octave 7
            if i.note == 106:
                intNote.append(106)
                
            # note b octave 7
            if i.note == 107:
                intNote.append(107)
                
            # note c octave 8
            if i.note == 108:
                intNote.append(108)
                
            # note c#/d| octave 8
            if i.note == 109:
                intNote.append(109)
                
            # note d octave 8
            if i.note == 110:
                intNote.append(110)
                
            # note d#/e| octave 8
            if i.note == 111:
                intNote.append(111)
                
            # note e octave 8
            if i.note == 112:
                intNote.append(112)
                
            # note f octave 8
            if i.note == 113:
                intNote.append(113)
                
            # note f#/g| octave 8
            if i.note == 114:
                intNote.append(114)
                
            # note g octave 8
            if i.note == 115:
                intNote.append(115)
                
            # note g#/a| octave 8
            if i.note == 116:
                intNote.append(116)
            
            # note a octave 8
            if i.note == 117:
                intNote.append(117)
                
            # note a#/b| octave 8
            if i.note == 118:
                intNote.append(118)
                
            # note b octave 8
            if i.note == 119:
                intNote.append(119)
                
            # note c octave 9
            if i.note == 120:
                intNote.append(120)
                
            # note c#/d| octave 9
            if i.note == 121:
                intNote.append(121)
                
            # note d octave 9
            if i.note == 122:
                intNote.append(122)
                
            # note d#/e| octave 9
            if i.note == 123:
                intNote.append(123)
                
            # note e octave 9
            if i.note == 124:
                intNote.append(124)
                
            # note f octave 9
            if i.note == 125:
                intNote.append(125)
                
            # note f#/g| octave 9
            if i.note == 126:
                intNote.append(126)
                
            # note g octave 9
            if i.note == 127:
                intNote.append(127)
            
        elif i.type == 'end_of_track':
            print("Good Bye");
            arduinoDriver.write("0".encode())
            exit() # exits after song is done



menu()
