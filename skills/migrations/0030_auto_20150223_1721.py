# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0029_auto_20141210_1950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditoptions',
            options={'verbose_name_plural': 'Credit Options'},
        ),
        migrations.AlterField(
            model_name='creditoptions',
            name='crew_position',
            field=models.IntegerField(default=0, null=True, choices=[(0, b'--- Please select ---'), (1, b'Accounting - 1st Assistant Accountant'), (2, b'Accounting - 1st Assistant Accountant - Payroll'), (3, b'Accounting - 2nd Assistant Accountant'), (4, b'Accounting - Production Accountant'), (128, b'Accounting - Post-Production Accountant'), (129, b'Accounting - Post-Production Assistant Accountant'), (5, b'Accounting - Trainee Assistant Accountant'), (6, b'Accounting - 3rd Assistant Accountant'), (7, b'Art Department - 1st Assistant Art Director'), (8, b'Art Department - 2nd Assistant Art Director'), (9, b'Art Department - 3rd Assistant Art Director'), (10, b'Art Department - Art Department Coordinator'), (11, b'Art Department - Art Director'), (12, b'Art Department - Graphic Artist  GRAPHIC'), (13, b'Art Department - Production Designer PD'), (14, b'Art Department - Trainee Assistant Art Director'), (15, b'Art Department - Storyboard Artist'), (16, b'Assistant Directors - 1st Assistant Director'), (17, b'Assistant Directors - Medic  / Set Medic'), (18, b'Assistant Directors - Set Production Assistant'), (19, b'Assistant Directors - Trainee Assistant Director/4th Assistant'), (20, b'Assistant Directors - 2nd Assistant Director'), (21, b'Assistant Directors - 2nd Unit Director'), (22, b'Assistant Directors - 3rd Assistant Director'), (23, b'Casting - Background Performer'), (24, b'Casting - Stand In'), (25, b'Camera - 1st Assistant Camera'), (26, b'Camera - Camera Operator'), (27, b'Camera - Camera Trainee'), (28, b'Camera - Data Imaging Technician'), (29, b'Camera - Data Management Technician'), (30, b'Camera - Director of Photography/Cinematographer'), (31, b'Camera - Stand In'), (32, b'Camera - 2nd Assistant Camera'), (33, b'Casting - Casting Director'), (34, b'Casting - Extras Casting'), (35, b'Catering & Craft - Catering'), (36, b'Catering & Craft - Craft Service'), (37, b'Construction - Carpenter'), (38, b'Construction - Scenic Artist/Painter'), (39, b'Continuity - Script Supervisor'), (40, b'Electric / Lighting - Best Boy Electric'), (41, b'Electric / Lighting - Electric'), (42, b'Electric / Lighting - Gaffer'), (43, b'Electric / Lighting - Genny Op'), (44, b'Grip - Best Boy Grip'), (45, b'Grip - Dolly Grip'), (46, b'Grip - Grip'), (47, b'Grip - Key Grip'), (48, b'Hair & Make Up - Assistant Hair'), (49, b'Hair & Make Up - Assistant Make Up'), (50, b'Hair & Make Up - Hair'), (51, b'Hair & Make Up - Make Up'), (52, b'Hair & Make Up - SPFX Make Up'), (53, b'Locations - Assistant Location Manager'), (130, b'Locations - Key Locations Support (Security)'), (54, b'Locations - Location Manager'), (55, b'Locations - Location Production Assistant'), (56, b'Locations - Location Scout'), (57, b'Locations - Location Support Personnel/Security'), (58, b'Locations - Trainee Location Manager'), (59, b'Post-Production - 1st Assistant Picture Editor'), (131, b'Post-Production - Accountant'), (132, b'Post-Production - Assistant Accountant'), (60, b'Post-Production - Composer'), (70, b'Post-Production - Dialogue Editor'), (71, b'Post-Production - Music Editor'), (72, b'Post-Production - Picture Editor'), (73, b'Post-Production - Post Production Assistant'), (74, b'Post-Production - Post Production Supervisor'), (75, b'Post-Production - Sound Editor'), (76, b'Post-Production - Trainee Assistant Editor'), (77, b'Post-Production - 1st Assistant Sound Editor'), (78, b'Post-Production - 2nd Assistant Picture Editor'), (79, b'Post-Production - 2nd Assistant Sound Editor'), (80, b'Production - Assistant Production Coordinator'), (81, b'Production - Assistant Production Manager'), (82, b'Production - Associate Producer'), (83, b'Production - Director'), (84, b'Production - Directors Assistant'), (85, b'Production - Executive Producer'), (86, b'Production - Line Producer'), (87, b'Production - Producer'), (88, b'Production - Producers Assistant'), (89, b'Production - Production Coordinator'), (90, b'Production - Production Manager'), (91, b'Production - Production Secretary'), (92, b'Production - Researcher'), (93, b'Production - Tutor/Set Teacher'), (94, b'Production - Unit Manager'), (95, b'Production - Unit Production Manager'), (96, b'Production - Co-Producer'), (97, b'Production - Office Production Assistant'), (126, b'Production - Production Associate'), (127, b'Production - Production Liason'), (98, b'Props - Assistant Props Master'), (99, b'Props - Props Buyer'), (100, b'Props - Props Master'), (101, b'Props - Armourer'), (102, b'Publicity - EPK/Behind the Scenes Videographer'), (103, b'Publicity - Stills Photographer'), (104, b'Set Decoration - Assistant Set Decorator'), (105, b'Set Decoration - Set Dec Buyer'), (106, b'Set Decoration - Set Decorator'), (107, b'Set Decoration - Set Dresser'), (108, b'Sound - Boom Op'), (109, b'Sound - Cable Puller'), (110, b'Sound - Sound Mixer'), (111, b'Special FX - Effects Editor'), (112, b'Special FX - SPFX Coordinator'), (113, b'Special FX - SPFX Technician'), (114, b'Stunts - Stunt Coordinator'), (115, b'Stunts - Stunt Performer'), (133, b'Transport - Cast Driver'), (116, b'Transport - Driver'), (134, b'Transport - Picture Car Driver'), (117, b'Transport - Picture Cars Captain'), (118, b'Transport - Transport Captain'), (119, b'Transport - Transport Coordinator'), (135, b'Transport - Unit Driver'), (120, b'Wardrobe & Costumes - Costume Buyer'), (121, b'Wardrobe & Costumes - Costume Designer'), (122, b'Wardrobe & Costumes - Assistant Costume Designer (& Set Jobs)'), (123, b'Writers - Writer'), (124, b'Animals - Animal Wrangler'), (125, b'Other - Other')]),
        ),
    ]